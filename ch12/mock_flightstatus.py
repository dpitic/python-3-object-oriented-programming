import datetime
import redis
import pytest
from unittest.mock import Mock
from unittest.mock import patch

"""
Demonstration of mocking in unit testing using unittest.mock standard library.

The Mock() class removes the need to create stubs throughout the test suite.
After performing any action, assertions can be made about which methods or
attributes were used and the arguments they were called with.
"""


class FlightStatusTracker:
    """
    This class is responsible for tracking flight statuses in a key-value store
    so that the timestamp and the most recent status can be stored.
    """
    ALLOWED_STATUSES = {'CANCELLED', 'DELAYED', 'ON TIME', 'ARRIVED'}

    def __init__(self, redis_instance=None):
        self.redis = redis_instance if redis_instance else redis.StrictRedis()

    def change_status(self, flight, status):
        status = status.upper()
        if status not in self.ALLOWED_STATUSES:
            raise ValueError('{} is not a valid status'.format(status))

        key = 'flightno:{}'.format(flight)
        value = '{}|{}'.format(datetime.datetime.now().isoformat(), status)
        self.redis.set(key, value)      # This should be tested


@pytest.fixture
def tracker():
    return FlightStatusTracker()


def test_mock_method(tracker):
    """
    Test that the flight status is not valid and that it was not set in the
    database.
    :param tracker: FlightStatusTracker object under test.
    :return: None
    """
    tracker.redis.set = Mock()  # create mock object for the redis.set() method
    with pytest.raises(ValueError) as ex:
        tracker.change_status('AC101', 'lost')
    assert ex.value.args[0] == 'LOST is not a valid status'
    assert tracker.redis.set.call_count == 0


def test_patch(tracker):
    """
    Demonstration of the unittest.mock.patch() method used to mock the standard
    library datetime object.
    :param tracker: FlightStatusTracker object under test.
    :return: None
    """
    tracker.redis.set = Mock()
    # Create a known datetime for test purposes
    fake_now = datetime.datetime(2015, 4, 1)
    # Mock the standard library datetime to return the known test value
    with patch('datetime.datetime') as dt:
        dt.now.return_value = fake_now
        tracker.change_status('AC102', 'on time')
    dt.now.assert_called_once_with()    # Make sure the datetime.now() is called
    # Make sure the redis mock object was called with the correct parameters
    tracker.redis.set.assert_called_once_with(
        'flightno:AC102',
        '2015-04-01T00:00:00|ON TIME'
    )
