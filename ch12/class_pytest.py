"""
Demonstration of testing a class using the py.test framework.

Classes are useful for grouping related tests together or for tests that need to
access related attributes or methods on the class. This script shows an extended
class with a passing and a failing test. The output is more comprehensive than
that provided by the standard library unittest module.

The py.test framework will also execute unittest TestCase unit tests.
"""


class TestNumbers:
    """
    py.test unit test don't have to subclass anything.
    """
    def test_int_float(self):
        """
        The py.test framework suppresses output from the print() statement if
        the test is successful.
        :return:
        """
        print('This print() statement is suppressed.')
        assert 1 == 1.0

    def test_int_str(self):
        print('Failing tests do not suppress the print() statement.')
        assert 1 == "1"
