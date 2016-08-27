from m_list.send_email import send_email
from collections import defaultdict


class MailingList:
    """Manage groups of email addresses for sending emails."""

    def __init__(self, data_file):
        self.data_file = data_file
        self.email_map = defaultdict(set)

    def add_to_group(self, email, group):
        """
        Add email address to group.
        :param email: email address.
        :param group: email group.
        :return: None
        """
        self.email_map[email].add(group)

    def emails_in_groups(self, *groups):
        """
        Collect all the email addresses in one or more groups by converting the
        list of groups to a set.
        :param groups: email groups
        :return: set of email address groups.
        """
        groups = set(groups)
        emails = set()
        for e, g in self.email_map.items():
            if g & groups:
                emails.add(e)
        return emails

    def send_mailing(self, subject, message, from_addr, *groups, headers=None):
        """
        Send an email message to the specified email groups.
        :param subject: email subject.
        :param message: email message to send.
        :param from_addr: sender's email address.
        :param groups: destination email group.
        :param headers: dictionary of email headers.
        :return: None.
        """
        emails = self.emails_in_groups(*groups)
        send_email(subject, message, from_addr, *emails, headers=headers)

    def save(self):
        """
        Save email mailing list.

        Saves the email mailing list in a text file using the format:
        <email address> <group1>,<group2>,<groupn>
        :return: None
        """
        with open(self.data_file, 'w') as file:
            for email, groups in self.email_map.items():
                file.write('{} {}\n'.format(email, ','.join(groups)))

    def load(self):
        """
        Load email mailing list from text file. The format is:
        <email address> <group1>,<group2>,<groupn>
        :return: None
        """
        self.email_map = defaultdict(set)
        try:
            with open(self.data_file) as file:
                for line in file:
                    email, groups = line.strip().split(' ')
                    groups = set(groups.split(','))
                    self.email_map[email] = groups
        except IOError:
            pass

    def __enter__(self):
        self.load()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.save()


# Demonstration of class API
def main():
    m = MailingList('addresses.db')
    m.add_to_group("friend1@example.com", "friends")
    m.add_to_group("friend2@example.com", "friends")
    m.add_to_group("family1@example.com", "family")
    m.add_to_group("pro1@example.com", "professional")
    m.save()
    # Send email message to friends and family group
    m.send_mailing("A Party", "Friends and family only: a party",
                   "me@example.com", "friends", "family",
                   headers={"Reply-To": "me2@example.com"})
    # Use context manager methods
    with MailingList('addresses.db') as ml:
        ml.add_to_group('friend3@example.com', 'friends')
        ml.send_mailing("What's up", "hey friends, how's it going",
                        "me@example.com", 'friends')
    # Load mailing list and send to professional group
    with MailingList('addresses.db') as ml:
        ml.send_mailing("Professional Subject", "Professional message",
                        "me@example.com", "professional")


# Import guard
if __name__ == '__main__':
    main()
