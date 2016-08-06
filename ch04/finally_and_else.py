# This demonstrates how to execute code regardless of whether or not an
# exception has occurred. It also demonstrates code that should only be
# executed if an exception does not occur.
import random

some_exceptions = [ValueError, TypeError, IndexError, None]

try:
    choice = random.choice(some_exceptions)
    print("Raising {}".format(choice))
    if choice:
        raise choice("An error")
except ValueError:
    print("Caught a ValueError")
except TypeError:
    print("Caught a TypeError")
except Exception as e:
    print("Caught some other error: %s" % (e.__class__.__name__))
else:
    # Only executed if there is no exception raised.
    print("This code is executed only if there is no exception")
finally:
    # Always executed, regardless of whether or not an exception was raised.
    # This will even be executed if there is a return statement in the try
    # clause. The finally code will be executed before the value is returned.
    print("This cleanup code is always executed, regardless of exceptions")
