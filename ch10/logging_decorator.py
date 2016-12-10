import time

"""
Implementation of a logging decorator. This example demonstrates how to decorate
a function. The preferred syntax to decorate a function is to use the special
syntax @decorator on the line before the function definition. The primary
benefit of this syntax is that it clearly shows that the function has been
decorated at the time it is defined. However, this syntax can only be applied
to functions we define.

If we need to decorate functions that are part of a 3rd party library, we have
to use the function assignment decoration syntax.

Decorators can also be applied to other objects in Python.
"""


def log_calls(func):
    """
    Logging decorator that takes a function and returns a new function that logs
    the execution time.
    :param func: function to wrap with the logging decorator.
    :return: wrapper function used to execute the wrapped function.
    """

    def wrapper(*args, **kwargs):
        """
        Wrapper function used to log function call and execution time.
        :param args: optional arguments
        :param kwargs: keyword arguments
        :return: return value of the wrapped function.
        """
        now = time.time()
        print('Calling {0} with {1} and {2}'.format(
            func.__name__, args, kwargs))
        # Call the wrapped function; save the return value, if any.
        return_value = func(*args, **kwargs)
        print('Executed {0} in {1}ms'.format(func.__name__, time.time() - now))
        return return_value

    return wrapper


# Sample functions to be wrapped. The preferred way to wrap functions is to
# use the @decorator syntax.
@log_calls
def test1(a, b, c):
    print('\ttest1 called')

@log_calls
def test2(a, b):
    print('\ttest2 called')

@log_calls
def test3(a, b):
    print('\ttest3 called')
    time.sleep(1)

# Replace the original functions with the decorated functions. This has the
# same effect as decorating the original functions with the @decorator syntax.
# The @decorator syntax is preferred. Decorating a function after its definition
# has the disadvantage of not making it obvious that the function has been
# altered later in the code, when somebody reads the function definition.
# test1 = log_calls(test1)
# test2 = log_calls(test2)
# test3 = log_calls(test3)

# Call the wrapped functions.
test1(1, 2, 3)
test2(4, b=5)
test3(6, 7)
