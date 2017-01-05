from stats import StatsList

"""
Demonstration of using the py.test funcargs feature to set up variables.
"""


def pytest_funcarg__valid_stats(request):
    """
    Global test configuration. This function can also be placed in conftest.py
    which is parsed by py.test. Funcargs must be named according to the
    convention pytest_funcarg__<identifier>, where <identifier> is a valid
    variable name that can be used as a parameter in a test function.
    :param request:
    :return: object to be passed as an argument into the individual test
    functions.
    """
    return StatsList([1, 2, 2, 3, 3, 4])


def test_mean(valid_stats):
    assert valid_stats.mean() == 2.5


def test_median(valid_stats):
    assert valid_stats.median() == 2.5
    valid_stats.append(4)
    assert valid_stats.median() == 3


def test_mode(valid_stats):
    assert valid_stats.mode() == [2, 3]
    valid_stats.remove(2)
    assert valid_stats.mode() == [3]
