import unittest

"""
Demonstration of the assertRaises() method. This method tests than an exception
is raised when a callable is called with any positional or keyword arguments
that are also passed to assertRaises(). The test passes if exception is raised.
The test is an error if another exception is raised. The test fails if no
exception is raised.
"""


def average(seq):
    return sum(seq) / len(seq)


class TestAverage(unittest.TestCase):
    def test_zero(self):
        """
        The assertRaises() method can be used to ensure a specific function
        raises a specific option.
        :return: None
        """
        self.assertRaises(ZeroDivisionError, average, [])

    def test_with_zero(self):
        """
        The assertRaises() method can be used as a context manager to wrap
        inline code. The test passes if the code inside the with statement
        raises the specified exception, otherwise it fails. The context manager
        allows us to write the code as normal (by calling functions or executing
        code directly), rather than having to wrap the function call in another
        function call.
        :return:
        """
        with self.assertRaises(ZeroDivisionError):
            average([])


if __name__ == '__main__':
    unittest.main()
