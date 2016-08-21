import datetime
import time


class TimedEvent:
    """
    Class used to wrap the callback function to be called at the specified time.
    """

    def __init__(self, endtime, callback):
        """
        Initialise the object with the time to call the callback.
        :param endtime: the time at which the callback should be executed.
        :param callback: function to be executed at the specified time. It
        accepts a single argument which is the timer doing the calling.
        """
        self.endtime = endtime
        self.callback = callback

    def ready(self):
        """
        Reports whether it is time to execute the callback.
        :return: True if it is time to execute the callback; False otherwise.
        """
        return self.endtime <= datetime.datetime.now()


class Timer:
    """
    Event-driven timer that stores a list of timed events and runs them at the
    appropriate time.
    """

    def __init__(self):
        """
        Initialise a new object with an empty list of timed events.
        """
        self.events = []

    def call_after(self, delay, callback):
        """
        Add a new timed event, consisting of a delay and a callback function.
        :param delay: delay time in seconds after which to call the callback.
        :param callback: function to call after the delay time has expired. The
        function accepts one argument, the timer doing the calling.
        :return: None
        """
        end_time = datetime.datetime.now() + datetime.timedelta(seconds=delay)
        self.events.append(TimedEvent(end_time, callback))

    def run(self):
        """
        Execute the callback functions in order at the appropriate time.
        :return: None
        """
        while True:
            ready_events = (e for e in self.events if e.ready())
            for event in ready_events:
                event.callback(self)
                self.events.remove(event)
            time.sleep(0.5)
