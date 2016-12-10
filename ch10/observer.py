# Demonstration of the observer pattern. The core object is an Inventory and
# the observer is a ConsoleObserver.
#
# The observer pattern decouples the code being observed from the code doing the
# observing.


class Inventory:
    """
    Core object. This inventory keeps track of a product and quantity. It also
    supports attachment of observer objects to be notified when the core object
    state changes.
    """

    def __init__(self):
        self._product = None
        self._quantity = 0
        # List of observers to be notified of state changes
        self.observers = []

    def attach(self, observer):
        """
        Attach an observer to this object.
        :param observer: observer object to attach to this object
        :return: None
        """
        self.observers.append(observer)

    @property
    def product(self):
        """
        Accessor for the inventory product.
        :return: product value
        """
        return self._product

    @product.setter
    def product(self, value):
        """
        Set the inventory product and notify the observers.
        :param value: product value.
        :return: None
        """
        self._product = value
        # Notify observers that the product value has changed
        self._update_observers()

    @property
    def quantity(self):
        """
        Accessor for the inventory quantity.
        :return: quantity value.
        """
        return self._quantity

    @quantity.setter
    def quantity(self, value):
        """
        Set the inventory quantity and notify the observers.
        :param value: quantity value.
        :return: None
        """
        self._quantity = value
        # Notify observers that the quantity has changed
        self._update_observers()

    def _update_observers(self):
        """
        Notify the observers that state has changed in this object. The
        observers are called directly, so they must implement the __call__()
        method, which is useful shortcut in Python.
        :return: None
        """
        for observer in self.observers:
            observer()


class ConsoleObserver:
    """
    Implementation of the observer. This class simply prints the inventory
    product and quantity.
    """

    def __init__(self, inventory):
        """
        Enable the inventory to be accessed by this observer, so it has access
        to the inventory object state.
        :param inventory: object this observer is observing.
        """
        self.inventory = inventory

    def __call__(self, *args, **kwargs):
        """
        Enable the inventory object to call the observer directly. This simply
        prints the inventory product and quantity.
        :param args:
        :param kwargs:
        :return: None
        """
        print(self.inventory.product)
        print(self.inventory.quantity)


# API demonstration code.
def main():
    # Create an Inventory object to which the observers will be attached.
    i = Inventory()
    # Create and attach 2 observers to this inventory object.
    c1 = ConsoleObserver(i)
    c2 = ConsoleObserver(i)
    i.attach(c1)
    i.attach(c2)
    # Update the inventory product; both observers should print the inventory
    # state.
    i.product = 'Gadget'


if __name__ == '__main__':
    main()
