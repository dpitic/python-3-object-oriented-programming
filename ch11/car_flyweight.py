import weakref

"""
This script is a demonstration of the flyweight pattern.

The flyweight pattern is a memory optimisation pattern. It ensures that objects
that share a state can use the same memory for that shared state. It is normally
implemented only after a program has demonstrated memory problems.

Each Flyweight object has no specific state. Any time it needs to perform an
operation on some specific state object, that state needs to be passed into
the Flyweight by the calling code. Normally, the factory that returns a
Flyweight is a separate object; it's purpose is to return a Flyweight for a
given key identifying that Flyweight. It works similar to the Singleton pattern.
If the Flyweight exists, it is returned, otherwise a new one is created.

The script implements an inventory system for car sales. Each individual car has
specific attributes (serial number and colour), and a set of attributes that are
common to all cars of that model. The object that represents the model of the
car is the shared state which is implemented as the Flyweight object. The
Flyweight object is the shared object that maintains the list of features
associated with a particular car model, which can be referenced, along with
the serial number and colour for individual vehicles.

The Flyweight must be capable of returning the correct instance based on a key.
If this was implemented using a dictionary, the dictionary would maintain these
objects in memory, even when there are no more references to a particular model.
If a particular model was sold out, the Flyweight is no longer necessary for
that model.

This can be solved by using the weakref module. It provides a
WeakValueDictionary object which enables the memory to be reclaimed if there are
no references to a particular value being held in the weak referenced
dictionary.
"""


class CarModel:
    """
    Implementation of the car model Flyweight. This object maintains the set
    of common attributes for a particular car model.
    """
    _models = weakref.WeakValueDictionary()

    def __new__(cls, model_name, *args, **kwargs):
        """
        Factory for the car model Flyweight object. Returns a new car model
        if it doesn't already exist, or an existing car model object.
        :param model_name: car model name; used as the key.
        :param args:
        :param kwargs:
        :return: existing car model or new car model if not already existing.
        """
        model = cls._models.get(model_name)
        if not model:
            model = super().__new__(cls)
            cls._models[model_name] = model

        return model

    def __init__(self, model_name, air=False, tilt=False, cruise_control=False,
                 power_locks=False, alloy_wheels=False, usb_charger=False):
        """
        Initialise a new car model object, if one doesn't already exist. This
        ensures the factory can be called with just the car model name to return
        the same flyweight object.
        :param model_name: key used to reference particular car models
        :param air:
        :param tilt:
        :param cruise_control:
        :param power_locks:
        :param alloy_wheels:
        :param usb_charger:
        """
        if not hasattr(self, 'initialised'):
            self.model_name = model_name
            self.air = air
            self.tilt = tilt
            self.cruise_control = cruise_control
            self.power_locks = power_locks
            self.alloy_wheels = alloy_wheels
            self.usb_charger = usb_charger
            self.initialised = True

    def check_serial(self, serial_number):
        """
        Hypothetical method that checks whether a particular car has been
        involved in any accidents. It looks up a serial number which belongs to
        a specific model of vehicle (which is stored in the Flyweight object for
        that model).
        :param serial_number: vehicle serial number.
        :return: None
        """
        print('Sorry, we are unable to check the serial number {0} '
              'on the {1} at this time.'.format(serial_number, self.model_name))


class Car:
    """
    This class defines the individual vehicle details such as serial number and
    colour. It has a reference to the car model object.
    """
    def __init__(self, model, colour, serial):
        """
        Initialise a Car object of a particular model, colour and serial number.
        :param model: car model type object; common car model type attributes.
        :param colour: individual car colour.
        :param serial: individual car serial number.
        """
        self.model = model
        self.colour = colour
        self.serial = serial

    def check_serial(self):
        """
        Check whether this particular car has been involved in any accidents.
        :return: None
        """
        return self.model.check_serial(self.serial)


# Demonstration of API
def main():
    # Create some car models
    dx = CarModel('FIT DX')
    lx = CarModel('FIT LX', air=True, cruise_control=True, power_locks=True,
                  tilt=True)
    # Create some cars based on these models
    car1 = Car(dx, 'blue', '1234-5')
    print('Check serial car {0} {1}:'.format(id(car1), car1.model.model_name))
    car1.check_serial()
    car2 = Car(dx, 'black', '1234-6')
    print('Check serial car {0} {1}:'.format(id(car2), car2.model.model_name))
    car2.check_serial()
    car3 = Car(lx, 'red', '1234-7')
    print('Check serial car {0} {1}:'.format(id(car3), car3.model.model_name))
    car3.check_serial()
    print('Check CarModel factory:')
    print('id(lx) = {}'.format(id(lx)))
    lx = CarModel('FIT LX')     # return the same lx object
    print('id(lx) = {}'.format(id(lx)))


# Import guard
if __name__ == '__main__':
    main()
