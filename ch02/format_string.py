def format_string(string, formatter=None):
    '''
    Format a string using the formatter object, which is expected to have a
    format() method that accepts a string. This is a demonstration of defining
    a class inside a function.
    '''
    class DefaultFormatter(object):
        """
        Format a string in title case. This class cannot be accessed outside
        of this function scope.
        """
        def format(self, string):
            return str(string).title()

    # If a formatter object has not been provided in the function call, create
    # a new DefaultFormatter object to use as the formatter.
    if not formatter:
        formatter = DefaultFormatter()

    return formatter.format(string)

# Test the module.
def main():
    # Define the non-title case string to operate on.
    hello_string = "hello world, how are you today?"
    print(" input: " + hello_string)
    print("output: " + format_string(hello_string))

if __name__ == '__main__':
    main()
