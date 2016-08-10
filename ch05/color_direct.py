# Implementation of the Color class permitting direct access to the class
# properties, as is typical in Python.

class Color:
    """
    Implementation of a Color class allowing direct access to properties, as
    is common in Python.
    """
    def __init__(self, rgb_value, name):
        self.rgb_value = rgb_value
        self.name = name


# Demonstration of class API
def main():
    c = Color('#ff0000', 'bright red')
    print("Name: %s" % c.name)
    c.name = 'red'
    print("Name: %s" % c.name)


# Import guard
if __name__ == '__main__':
    main()
