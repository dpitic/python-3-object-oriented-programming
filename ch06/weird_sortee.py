from functools import total_ordering
from operator import itemgetter

# Demonstration of sorting a list of user-defined class

@total_ordering
class WeirdSortee:
    """Custom class used to demonstrate list sorting using custom objects."""
    def __init__(self, string, number, sort_num):
        """
        Instantiate an object.
        :param string: string object.
        :param number: numerical object.
        :param sort_num: True to sort by number; False to sort by string.
        """
        self.string = string
        self.number = number
        self.sort_num = sort_num

    def __lt__(self, arg):
        """
        Comparable method returns True if this object < the argument.
        """
        if self.sort_num:
            return self.number < arg.number
        return self.string < arg.string

    def __eq__(self, arg):
        return all((
            self.string == arg.string,
            self.number == arg.number,
            self.sort_num == arg.sort_num
        ))

    def __repr__(self):
        return "{}:{}".format(self.string, self.number)


# Demonstration of list sorting
def main():
    a = WeirdSortee('a', 4, True)
    b = WeirdSortee('b', 3, True)
    c = WeirdSortee('c', 2, True)
    d = WeirdSortee('d', 1, True)
    l = [a, b, c, d]
    print("Original list = %s" % l)
    l.sort()
    print("Sorted by number = %s" % l)
    # Change object to sort by string
    for i in l:
        i.sort_num = False
    l.sort()
    print("Sorted by string = %s" % l)

    # Demonstration of list sorting with key
    l = ["hello", "HELP", "Helo"]
    print("Original list = %s" % l)
    # Standard list sort is case sensitive
    l.sort()
    print("l.sort() = %s" % l)
    # Case insensitive list sort
    l.sort(key=str.lower)
    print("l.sort(key=str.lower) = %s" % l)

    # Demonstration of sorting a list of tuples by the 2nd element; default is
    # the first element.
    l = [('y', 2), ('h', 4), ('o', 5), ('n', 6), ('p', 1), ('t', 3)]
    print("Original list =\n%s" % l)
    # Sort the list by the first element (by default)
    l.sort()
    print("l.sort() =\n%s" % l)
    # Sort by the 2nd element
    l.sort(key=itemgetter(1))
    print("l.sort(key=itemgetter(1)) =\n%s" % l)


# Import guard
if __name__ == '__main__':
    main()
