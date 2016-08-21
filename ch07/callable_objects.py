from timer import Timer
import datetime


def format_time(message, *args):
    """
    Display a formatted time message with the current time followed by optional
    positional arguments corresponding to replacement fields delimited by {} in
    the message.
    :param message: string containing replacement fields consisting of {now} for
    the current time and additional optional replacement fields.
    :param args: optional positional arguments corresponding to additional
    replacement fields.
    :return: None
    """
    now = datetime.datetime.now().strftime("%I:%M:%S")
    print(message.format(*args, now=now))


class Repeater:
    """
    Class used to demonstrate that it is possible to create an object that can
    be called as though it were a function.
    """

    def __init__(self):
        self.count = 0

    def __call__(self, timer):
        """
        Add this object as a callback with a delay of 5 seconds to timer.
        :param timer: object used to execute this object after 5 seconds.
        :return: None
        """
        format_time("{now}: repeat {0}", self.count)
        self.count += 1
        timer.call_after(5, self)


# Demonstration and sample code
timer = Timer()
timer.call_after(5, Repeater())
format_time("{now}: Starting")
timer.run()
