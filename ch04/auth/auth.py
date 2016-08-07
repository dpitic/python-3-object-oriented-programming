import hashlib
# Case study for a central authentication and authorisation system.

# Constants
MIN_PW_LENGTH = 6


class User:
    """
    User class is responsible for storing the username and encrypted password.
    """

    def __init__(self, username, password):
        """
        Create a new user object. The password will be encrypted before storing.
        :param username: User's user name.
        :param password: User's password.
        """
        self.username = username
        self.password = self._encrypt_pw(password)
        self.is_logged_in = False

    def _encrypt_pw(self, password):
        """Encrypt the password with the username and return the sha digest."""
        hash_string = (self.username + password)
        hash_string = hash_string.encode("utf8")
        return hashlib.sha256(hash_string).hexdigest()

    def check_password(self, password):
        """
        Return True if the password is valid for this user, false otherwise.
        """
        encrypted = self._encrypt_pw(password)
        return encrypted == self.password


class AuthException(Exception):
    """Base class for authentication and authorisation"""

    def __init__(self, username, user=None):
        """
        Authentication and authorisation exception requires a username and has
        an optional User instance associated with that username.
        :param username: Username associated with the exception.
        :param user: Optional User object associated with the exception.
        """
        super(AuthException, self).__init__(username, user)
        self.username = username
        self.user = user


class UsernameAlreadyExists(AuthException):
    """Duplicate usernames are not allowed."""
    pass


class PasswordTooShort(AuthException):
    """Passwords have to be a certain minimum length for security."""
    pass


class InvalidUsername(AuthException):
    """The username does not exist."""
    pass


class InvalidPassword(AuthException):
    """The password does not match."""
    pass


class Authenticator:
    """
    Class used to manage users and logging in and out.
    """

    def __init__(self):
        """Construct an authenticator to manage users logging in and out."""
        # This class is responsible for maintaining a mapping of usernames to
        # user objects. This is implemented using a dictionary.
        self.users = {}

    def add_user(self, username, password):
        """Create and add a new user to the Authenticator."""
        if username in self.users:
            raise UsernameAlreadyExists(username)
        if len(password) < MIN_PW_LENGTH:
            raise PasswordTooShort(username)
        self.users[username] = User(username, password)

    def login(self, username, password):
        """
        Log in a user, if possible.
        :param username: Username of user trying to log in.
        :param password: Password of user trying to log in.
        :return: True for successful authentication; False otherwise.
        :raise: InvalidUsername if the username is unknown to this Authenticator
        :raise: InvalidPassword if the given password does not the user's
        password.
        """
        try:
            user = self.users[username]
        except KeyError:
            raise InvalidUsername(username)

        if not user.check_password(password):
            raise InvalidPassword(username, user)

        user.is_logged_in = True
        return True

    def is_logged_in(self, username):
        """True if a user is logged in, False otherwise."""
        if username in self.users:
            return self.users[username].is_logged_in
        return False


# Default authenticator instance to enable clients to access it using the
# auth.authenticator syntax.
authenticator = Authenticator()


class AuthPermissionError(Exception):
    """Authorisation permission error."""
    pass


class NotLoggedInError(AuthException):
    """User is not logged in."""
    pass


class NotPermittedError(AuthException):
    """User is not authorised or does not have permission."""
    pass


class Authorisor:
    """
    Responsible for mapping permissions to users. This class manages permissions
    and it will not permit user access to a permission if the user is not logged
    in.
    """

    def __init__(self, authenticator):
        """
        Initialise a new Authorisor object with the specified Authenticator.
        :param authenticator: Authenticator object containing User information.
        """
        self.authenticator = authenticator
        # Permissions are stored in a dictionary consisting of:
        # key   = the name of the permission.
        # value = set of usernames assigned that permission. The set ensures
        # that if a user is granted the same permission multiple times, the
        # permission set will only contain one entry for that user.
        self.permissions = {}

    def add_permission(self, perm_name):
        """
        Create a new permission for this Authorisor, unless it already exists.
        :param perm_name: Name of the new permission.
        :return: None
        :raise: AuthPermissionError if the permission already exists in this
        Authorisor.
        """
        try:
            # Check if the permission name already exists.
            perm_set = self.permissions[perm_name]
        except KeyError:
            # Permission does not already exist in this Authorisor.
            # Create the permission set to store users authorised with this
            # permission
            self.permissions[perm_name] = set()
        else:
            # Permission (names) must be unique in this Authorisor.
            raise AuthPermissionError("Permission already exists")

    def permit_user(self, perm_name, username):
        """
        Grant the given permission to the user.
        :param perm_name: Permission name to grant to the user.
        :param username: Username to which the permission should be granted.
        :return: None
        :raise: AuthPermissionError if the permission does not exist in this
        Authorisor.
        :raise: InvalidUsername if the username is not known to the
        Authenticator.
        """
        try:
            # Get a reference to the specified (named) permission set
            perm_set = self.permissions[perm_name]
        except KeyError:
            # Permission set does not exist
            raise AuthPermissionError("Permission does not exist")
        else:
            # Validate the username. The username must be known to the
            # Authenticator.
            if username not in self.authenticator.users:
                raise InvalidUsername(username)
            # Add the known user to the permission set.
            perm_set.add(username)

    def check_permission(self, perm_name, username):
        """
        Check whether a user has a specific permission. In order for them to be
        granted access, they have to be both logged into the authenticator and
        in the set of users who have been granted access to that privilege.
        :param perm_name: Permission name.
        :param username: Username to check for permission.
        :return: True if username has the permission; False otherwise.
        :raise: NotLoggedInError if the user is not logged into the
        Authenticator.
        :raise: NotPermittedError if the users doesn't have the necessary
        privileges.
        """
        # Users must be logged in to have any permissions at all
        if not self.authenticator.is_logged_in(username):
            raise NotLoggedInError(username)
        try:
            # Get the permission set for the specified permission name
            perm_set = self.permissions[perm_name]
        except KeyError:
            # Permission (name) does not exist in this Authorisor
            raise PermissionError("Permission does not exist")
        else:
            # Username must be in the permission set to be authorised
            if username not in perm_set:
                raise NotPermittedError(username)
            else:
                # User is logged in and they have the necessary privilege
                return True


# Define the default authorisor initialised with the default authenticator,
# so clients can access it using the syntax: auth.authorisor
authorisor = Authorisor(authenticator)


# Demonstration code
def main():
    authenticator.add_user("joe", "joepassword")
    authorisor.add_permission("paint")
    try:
        authorisor.check_permission("paint", "joe")
    except Exception as e:
        print("Permission exception: %s" % e.__class__.__name__)
    print("Is joe logged in? %s" % (authenticator.is_logged_in("joe")))
    print("Log in joe %s" % (authenticator.login("joe", "joepassword")))
    try:
        authorisor.check_permission("mix", "joe")
    except Exception as e:
        print("Permission exception: %s" % e)
    try:
        authorisor.permit_user("mix", "joe")
    except Exception as e:
        print("Permission exception: %s" % e)
    authorisor.permit_user("paint", "joe")
    print("Can joe paint: %s" % (authorisor.check_permission("paint", "joe")))


# Import guard
if __name__ == '__main__':
    main()
