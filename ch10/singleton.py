"""
The singleton pattern is used to ensure that only one instance of a certain
object exists. Typically this object is some type of manager class, which often
need to be referenced by a wide variety of other objects. Passing references
to this object around to the methods and constructors that need them can make
code hard to read. Instead, when a singleton is used, the client objects request
the single instance of the manager object from the class, so a reference to it
does not need to be passed around.

In most programming languages, singletons are enforced by making the constructor
private (so nobody can make additional instances of it), and providing a static
method to retrieve the single instance. This method creates a new instance the
first time it is called, and then returns the same instance each time it is
called again.

Python doesn't have private constructors, but the __new__() class method can be
used to ensure that only one instance is ever created.
"""


class OnlyOne:
    """
    Implementation of the singleton pattern.
    """
    _singleton = None  # reference to the singleton instance

    def __new__(cls, *args, **kwargs):
        """
        Override the __new__() method to ensure only 1 instance of this object
        exists and always return that object.
        :param args:
        :param kwargs:
        :return: singleton instance of this object.
        """
        if not cls._singleton:
            cls._singleton = super(OnlyOne, cls).__new__(cls, *args, **kwargs)
        return cls._singleton


def main():
    o1 = OnlyOne()
    o2 = OnlyOne()
    print('o1 == o2: {}'.format(o1 == o2))
    print('o1: {}'.format(o1))
    print('o2: {}'.format(o2))


if __name__ == '__main__':
    main()
