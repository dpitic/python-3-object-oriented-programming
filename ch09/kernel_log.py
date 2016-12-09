import re


# This is an example of kernel log parsing using coroutines. We want to obtain
# the serial number of any drives that have XFS errors on them.
#
# Coroutines is a function object that can have data passed in at one or more
# points and return data from one or more points. In Python, the point where
# data is returned is the yield statement.
#
# In general, functions and generators are special types of coroutines. They are
# subsets of coroutines, where a function is the simplest type of coroutine.
# With functions, you can pass data in at one point and return data out at
# another point when the function returns. While a function can have multiple
# return statements, only one of them can be called for any given invocation of
# the function.
#
# A generator is a type of coroutine that can have data passed in at one point,
# but can pass data out at multiple points. In Python, the data is passed out
# at a yield statement. You can't pass data back in. If you called send() on
# a generator, the data would be silently discarded.
#
# Generators have data pulled out using next(), and coroutines have data pushed
# in using send(). In a coroutine, the point where data is pushed in and out is
# where the yield statement is executed.


def match_regex(filename, regex):
    """
    Coroutine object used to match a line in a file using the regex. The lines
    in the file are read in reverse order to detect the failure first.
    :param filename: name of file containing lines to match.
    :param regex: regular expression used to match against.
    :return: coroutine object which yields the first group from the regex.
    """
    with open(filename) as file:
        lines = file.readlines()
    # Loop through the lines in reverse order to detect XFS failure and then
    # obtain the serial number of the drive.
    for line in reversed(lines):
        match = re.match(regex, line)
        if match:
            regex = yield match.groups()[0]


def get_serials(filename):
    """
    Generator used to supply the regex to the coroutine for matching.
    :param filename: name of log file.
    :return: generator object that returns the serial matched serial number.
    """
    ERROR_RE = 'XFS ERROR (\[sd[a-z]\])'
    # Initialise the coroutine object with the XFS error regex.
    matcher = match_regex(filename, ERROR_RE)
    # Advance the coroutine to the yield statement which returns the device.
    device = next(matcher)
    while True:
        # Update the coroutine regex to match the bus ID
        bus = matcher.send('(sd \S+) {}.*'.format(re.escape(device)))
        # Update the coroutine regex to match the serial number to yield
        serial = matcher.send('{} \(SERIAL=([^)]*)\)'.format(bus))
        yield serial
        # Reset the coroutine regex to match for XFS errors.
        device = matcher.send(ERROR_RE)


# Extract the serial numbers for failed buses from the log file.
for serial_number in get_serials('EXAMPLE_LOG.log'):
    print(serial_number)
