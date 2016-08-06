def no_return():
    """
    When an exception is raised, it appears to stop the program execution
    immediately. All lines after the exception was raised are not executed
    unless the exception is handled, the program will exit with an error
    message.
    """
    print("I am about to raise an exception")
    raise Exception("This is always raised")
    print("This line will never execute")
    return "I won't be returned"


def call_exceptor():
    """
    If a function calls another function that raises an exception, nothing will
    be executed in the first function after the point where the second function
    was called. Raising an exception stops all execution right up through the
    function call stack until it is either handled or forces the interpreter
    to exit.
    """
    print("call_exceptor() starts here...")
    no_return()
    print("an exception was raised...")
    print("...so these lines don't run")


def funny_division(divider):
    """
    Demonstration of handling division by zero exception, but letting type
    errors propagate through.
    """
    try:
        return 100 / divider
    except ZeroDivisionError as e:
        return "Dividing by zero is not a good idea!"


def funny_division2(anumber):
    """
    Function used to demonstrate catching two or more differnt exceptions and
    handling them with the same code. This function will handle TypeError and
    ZeroDivisionError with the same exception handler, but it will raise a
    ValueError if the argument is 13.
    """
    try:
        if anumber == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / anumber
    except (ZeroDivisionError, TypeError):
        return "Enter a number other than zero"


def funny_division3(anumber):
    """
    Demonstration of catching different exceptions and handling them in
    different ways. Also handling an exception and allowing it to propagate to
    the calling function.
    """
    try:
        if anumber == 13:
            raise ValueError("13 is an unlucky number")
        return 100 / anumber
    except ZeroDivisionError:
        return "Enter a number other than zero"
    except TypeError:
        return "Enter a numerical value"
    except ValueError:
        print("No, No, not 13!")
        raise       # propagate ValueError exception to calling function


def main():
    """Demonstration of handling exceptions."""
    # Exceptions are handled by wrapping any code that might throw one either
    # directly itself, or from a call to any function or method that may raise
    # an exception, inside a try...except clause.
    try:
        # try wraps any code that might throw an exception
        no_return()
    except Exception as e:
        # except wraps the code used to handle the exception
        print("I caught an exception")
        print("The exception was: %s" % e)
    # Normal execution resumes after the try...except clause
    print("executed after the exception")
    print()
    # Demonstrate handling division by zero
    print(funny_division(0))
    print(funny_division(50.0))
    try:
        print(funny_division("hello"))
    except TypeError as e:
        print("Caught the TypeError: %s" % e)
    print()
    # Demonstrate handling division by zero and type errors. Value errors
    # can be raised by the function if the argument is 13.
    try:
        for val in (0, "hello", 50.0, 13):
            print("Testing {}:".format(val), end=' ')
            print(funny_division2(val))
    except ValueError as e:
        print("Caught the ValueError: %s" % e)
    print()
    # Demonstrate handling different types of exceptions in different ways, and
    # propatating ValueError to the calling function.
    try:
        for val in (0, "hello", 50.0, 13):
            print("Testing {}:".format(val), end=' ')
            print(funny_division3(val))
    except ValueError as e:
        print("Caught the ValueError: %s" % e)
    print()
    # Demonstrate catching exceptions with a reference to the exception and
    # printing the exception argument.
    try:
        raise ValueError("This is an exception argument")
    except ValueError as e:
        print("The exception arguments were", e.args)
        print("This is the exception: %s" % e)
    print()


if __name__ == '__main__':
    main()
