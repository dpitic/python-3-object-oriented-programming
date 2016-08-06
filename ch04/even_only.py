class EvenOnly(list):
    """
    Demonstration of handling exceptions. This class is designed to hold a list
    of even integers only. It raises exceptions if the object added to the list
    is not an integer and if the integer is odd.
    """

    def append(self, integer):
        if not isinstance(integer, int):
            raise TypeError("Only integers can be added")
        if integer % 2:
            raise ValueError("Only even numbers can be added")
        super().append(integer)
