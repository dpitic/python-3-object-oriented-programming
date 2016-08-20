# Demonstration of the reversed() built-in function.

normal_list = [1, 2, 3, 4, 5]

class CustomSequence():
    """
    Custom sequence class used to demonstrate the effects of overriding
    sequence methods.

    NOTE: __iter__() is not defined, therefore forward iterations are infinite
    loops.
    """

    def __len__(self):
        return 5

    def __getitem__(self, index):
        return "x{0}".format(index)

class FunkyBackwards():
    """
    Demonstration of overriding the __reversed__() method.

    NOTE: __iter__() is not defined, therefore forward iterations are infinite
    loops.
    """

    def __reversed__(self):
        return "BACKWARDS!"


# Demonstration of class API
def main():
    for seq in normal_list, CustomSequence(), FunkyBackwards():
        print("\n{}: ".format(seq.__class__.__name__), end="")
        for item in reversed(seq):
            print(item, end=", ")


# Import guard
if __name__ == '__main__':
    main()
