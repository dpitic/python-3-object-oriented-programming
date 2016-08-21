# Demonstration that functions can be set as callable attributes on other
# objects.


class A:
    """
    Simple class with a print() attribute.
    """

    def print(self):
        """
        Print the identification of this class.
        :return: None
        """
        print("my class is A")


def fake_print():
    """
    A function that will be assigned to the print() attribute of class A in
    order to demonstrate that functions can be assigned as callable attributes
    on other objects.
    :return: None
    """
    print("my class is not A")

a = A()
a.print()               # this is the normal print() method
# Reassign the object's print() attribute with the new function
a.print = fake_print
a.print()               # calls the newly assigned function, not the method
