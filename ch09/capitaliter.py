# An iterator is an object with the next() and done() method. The done() method
# returns True if there are no items left in the sequence. The next() method
# returns an object from the sequence.
#
# Python has the __next__() method which can be accessed using the built-in
# next(iterator). Instead of a done() method, the iterator protocol raises a
# StopIteration exception to notify the loop that there are no more objects in
# the sequence. Python provides a more readable "for item in iterator" syntax
# for accessing items in an iterator.
#
# The abstract base class Iterator, in the collections.abc module defines the
# iterator protocol in Python. It must implement the __next__() method.
# Additionally, every iterator must also fulfill the Iterable interface, which
# implements the __iter__() method. This method must return an Iterator instance
# that will cover all of the elements in that class. Since an iterator is
# already looping over elements, its __iter__() method traditionally returns
# itself.
#
# An Iterable is an object with elements that can be looped over. An Iterator is
# an object that represents a specific location in that iterable. Multiple
# iterators can traverse and be at different locations in an iterable, but any
# one iterator can only mark one place in an iterable.


class CapitalIterable:
    """
    Iterate over each word in a string and output them with the first letter
    capitalised. Most of the work is delegated to the CapitalIterator class.

    The iterable is an object with elements that can be looped over (iterated).
    """

    def __init__(self, string):
        self.string = string

    def __iter__(self):
        """
        Implementation of the Iterable protocol.
        :return: Iterator delegated to perform the iteration.
        """
        return CapitalIterator(self.string)


class CapitalIterator:
    """
    Implementation of the capital iterator. This represents a specific location
    in the iterable. The iterator implements the __next__() method which returns
    another element from the iterable or raises a StopIteration exception when
    there are no more objects to return.

    The job of the iterator is to maintain the index of the iterable and return
    the next element if available.
    """

    def __init__(self, string):
        self.words = [w.capitalize() for w in string.split()]
        self.index = 0

    def __next__(self):
        """
        Return another string token from the iterable. The token is a word.
        :return: the next string token from the iterable.
        """
        if self.index == len(self.words):
            raise StopIteration()

        word = self.words[self.index]
        self.index += 1
        return word

    def __iter__(self):
        """
        Since an iterator is already looping over elements, its __iter__()
        method traditionally returns itself.
        :return: the iterator object.
        """
        return self


def main():
    # Construct the iterable string
    iterable = CapitalIterable('the quick brown fox jumps over the lazy dog')
    # Obtain the iterator for the iterable
    iterator = iter(iterable)
    # Traverse the iterable using the iterator; using a while loop
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

    print()
    # Traverse the iterable using for statement; for loop is iterator aware.
    for i in iterable:
        print(i)


if __name__ == '__main__':
    main()
