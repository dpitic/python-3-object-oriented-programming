import unittest

"""
Demonstration of the Python standard library unittest module for writing unit
tests.


Test cases are written in classes that subclass unittest.TestCase. The unit test
methods must begin with 'test' prefix. Each unit test method should be
completely independent of other tests. Results or calculations from a previous
test should have no impact on any other test.

The general format of a test case is to set certain variables to know values,
run one or more functions, methods or processes, and then validate the results
returned or calculated by using the TestCase assertion methods.
"""


class CheckNumbers(unittest.TestCase):
    """
    Test case class defines the unit test cases. Test case classes must subclass
    unittest.TestCase.
    """
    def test_int_float(self):
        """
        Unit test case methods have to be prefixed with 'test'.
        :return: None
        """
        self.assertEqual(1, 1.0, msg='Test failure message')

    @unittest.expectedFailure
    def test_str_float(self):
        """
        Demonstration of a failing test. The unittest.expectedFailure decorator
        marks this test as pass, because the test was expected to fail.
        :return: None
        """
        self.assertEqual(1, '1', 'Comparing integer and string')


if __name__ == '__main__':
    unittest.main()             # Execute test cases
