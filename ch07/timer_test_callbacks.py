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


# Set of callbacks used to test the timer
def one(timer):
    format_time("{now}: Called One")


def two(timer):
    format_time("{now}: Called Two")


def three(timer):
    format_time("{now}: Called Three")


class Repeater:
    """
    Class used to demonstrate that methods can be used as callbacks.
    """

    def __init__(self):
        self.count = 0

    def repeater(self, timer):
        """
        Add this method as a callback with a delay of 5 seconds timer.
        :param timer: object used to execute this callback method.
        :return: None
        """
        format_time("{now}: repeat {0}", self.count)
        self.count += 1
        timer.call_after(5, self.repeater)


# Demonstration and sample code
timer = Timer()
timer.call_after(1, one)
timer.call_after(2, one)
timer.call_after(2, two)
timer.call_after(4, two)
timer.call_after(3, three)
timer.call_after(6, three)
repeater = Repeater()
timer.call_after(5, repeater.repeater)
format_time("{now}: Starting")
timer.run()
