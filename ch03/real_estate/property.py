# Constant declarations
COLS = 80       # Maximum number of text display columns


class Property:
    """
    Superclass representing the entities managed by the real estate program.
    This is the superclass from which Apartment and House directly subclass.
    """

    def __init__(self, square_feet='', beds='', baths='', **kwargs):
        super(Property, self).__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        print("PROPERTY DETAILS")
        print("=" * COLS)
        print("square footage: {}".format(self.square_feet))
        print("bedrooms:       {}".format(self.num_bedrooms))
        print("bathrooms:      {}".format(self.num_baths))
        print()

    def prompt_init():
        """
        Static method to obtain input from the user to initialise the object.
        The return type is a dictionary for object initialisation.
        """
        return dict(square_feet=input("Enter the square feet: "),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))
        prompt_init = staticmethod(prompt_init)


def get_valid_input(input_string, valid_options):
    """
    Obtain and validate input from the user.
    :param input_string: Prompt string.
    :param valid_options: Tuple of valid input option strings.
    :return: A valid input option string.
    """
    input_string += " ({}) ".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Apartment(Property):
    """Property subclass representing an apartment."""
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        super(Apartment, self).__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        super(Apartment, self).display()
        print("APARTMENT DETAILS")
        print("=" * COLS)
        print("laundry:     %s" % self.laundry)
        print("has balcony: %s" % self.balcony)
        print()

    def prompt_init():
        parent_init = Property.prompt_init()
        laundry = get_valid_input(
            "What laundry facilities does "
            "the property have? ", Apartment.valid_laundries)
        balcony = get_valid_input(
            "Does the property have a balcony? ",
            Apartment.valid_balconies)
        parent_init.update({
            "laundry": laundry,
            "balcony": balcony
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class House(Property):
    """Property subclass representing a house."""
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        super(House, self).__init__(**kwargs)
        self.num_stories = num_stories
        self.garage = garage
        self.fenced = fenced

    def display(self):
        super(House, self).display()
        print("HOUSE DETAILS")
        print("=" * COLS)
        print("# of stories: {}".format(self.num_stories))
        print("garage:       {}".format(self.garage))
        print("fenced yard:  {}".format(self.fenced))
        print()

    def prompt_init():
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ", House.valid_fenced)
        garage = get_valid_input("Is there a garage? ", House.valid_garage)
        num_stories = input("How many stories? ")
        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init

    prompt_init = staticmethod(prompt_init)


class Purchase:
    """Class used to mark a property for purchase."""

    def __init__(self, price='', taxes='', **kwargs):
        super(Purchase, self).__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        super(Purchase, self).display()
        print("PURCHASE DETAILS")
        print("=" * COLS)
        print("selling price:   {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))
        print()

    def prompt_init():
        return dict(
            price=input("What is the selling price? "),
            taxes=input("What are the estimated taxes? "))

    prompt_init = staticmethod(prompt_init)


class Rental:
    """Class used to mark a property for rental."""

    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super(Rental, self).__init__(**kwargs)
        self.furnished = furnished
        self.utilities = utilities
        self.rent = rent

    def display(self):
        super(Rental, self).display()
        print("RENTAL DETAILS")
        print("=" * COLS)
        print("rent:                {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished:           {}".format(self.furnished))
        print()

    def prompt_init():
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input("What are the estimated utilities? "),
            furnished=get_valid_input("Is the property furnished? ",
                                      ("yes", "no")))

    prompt_init = staticmethod(prompt_init)


# Implementation note: The order of the inherited classes is important! If the
# class was defined as class HouseRental(House, Rental), then display() would
# not have called Rental.display().
# When display() is called on the version below, it refers to Rental.display()
# which calls super.display() to get the House.display() which again calls
# super.display() to get the Property.display(), and everything works as it
# should.
# If the subclass arguments were reversed, display() would refer to
# House.display(). When super() is called, it calls the method on the Property
# parent class, but Property.display() does not have a call to super(). This
# means Rental.display() would not be called.
# By placing the inheritance list in the order below, it ensures that Rental
# calls super() which initialises the House side of the hierarchy.
# Another way to fix this would be to make Rental and Purchase subclasses of
# Property (or modify the method resolution order dynamically).
class HouseRental(Rental, House):
    """Class used to represent a rental house."""

    def prompt_init():
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    """Class used to represent a rental apartment."""

    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    """Class used to represent an apartment for sale."""

    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    """Class used to represent a house for sale."""

    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init

    prompt_init = staticmethod(prompt_init)


class Agent:
    """
    Agent class is responsible for creating new listings and displaying
    existing ones.
    """
    # Dictionary class variable to map the property types to the subclasses. The
    # keys are tuples of 2 distinct strings representing the subclasses as the
    # values in the dictionary.
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def __init__(self):
        self.property_list = []

    def display_properties(self):
        for property in self.property_list:
            property.display()

    def add_property(self):
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")).lower()
        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")).lower()

        # Look up the class in the dictionary.
        property_class = self.type_map[(property_type, payment_type)]
        # Get the required input from the user (to create the property subclass)
        init_args = property_class.prompt_init()
        # Add the appropriate property object to the property list.
        self.property_list.append(property_class(**init_args))
