import unittest
import sys

"""
Demonstration of skipping unit tests.
"""

class SkipTests(unittest.TestCase):
    @unittest.expectedFailure
    def test_fails(self):
        """
        Expect a failure, so ensure the test runner doesn't record this test as
        a failure when it fails.
        :return: None
        """
        self.assertEqual(False, True)

    @unittest.skip('This test is skipped deliberately.')
    def test_skip(self):
        self.assertEqual(False, True)

    @unittest.skipIf(sys.version_info.minor == 4,
                     'Skip test for Python 3.4')
    def test_skipif(self):
        self.assertEqual(False, True)

    @unittest.skipUnless(sys.platform.startswith('linux'),
                         'Only run this test on Linux')
    def test_skipunless(self):
        self.assertEqual(False, True)


if __name__ == '__main__':
    unittest.main()
