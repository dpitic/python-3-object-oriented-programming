class CapitalIterable:
    """
    Iterate over each word in a string and output them with the first letter
    capitalised. Most of the work is delegated to the CapitalIterator class.
    """

    def __init__(self, string):
        self.string = string

    def __iter__(self):
        return CapitalIterator(self.string)


class CapitalIterator:
    """
    Implementation of the capital iterator. This represents a specific location
    in the iterable.
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
        return self


def main():
    # Construct the iterable string
    iterable = CapitalIterable('the quick brown fox jumps over the lazy dog')
    # Obtain the iterator for the iterable
    iterator = iter(iterable)
    # Traverse the iterable using the iterator
    while True:
        try:
            print(next(iterator))
        except StopIteration:
            break

    print()
    # Traverse the iterable using for statement
    for i in iterable:
        print(i)


if __name__ == '__main__':
    main()
