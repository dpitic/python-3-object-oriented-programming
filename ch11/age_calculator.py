import datetime

"""
Demonstration of the adapter pattern.

The adapter pattern is used to allow two pre-existing objects to work together
when their interfaces are not compatible. It is designed to interact with
existing code, translating between the interfaces of the two objects.

The structure of the adapter pattern is similar to a simplified decorator
pattern. Decorators typically provide the same interface they replace, whereas
adapters map between two different interfaces.

The adapter pattern encapsulates the interface translation in one place. The
alternative would be to perform the translation in multiple places whenever the
code needed to be accessed; this would be highly error prone and difficult to
maintain.
"""


class AgeCalculator:
    """
    This class takes a string date in the format YYYY-MM-DD and calculates a
    person's age on that day. The interface is fixed, it uses a date string
    rather than the Python standard library datetime object. In order to use it
    with the Python standard library, it needs an adapter.

    This class represents some code with desired functionality and has a fixed
    interface, which is not compatible with client code. Client code that needs
    to use this functionality must do so through an adapter object.
    """

    def __init__(self, birthday):
        """
        Initialise this object with a birthday date.
        :param birthday: Birthday date string in the format YYYY-MM-DD.
        """
        self.year, self.month, self.day = (
            int(x) for x in birthday.split('-')
        )

    def calculate_age(self, date):
        """
        Calculate the age in years from the birthday to the specified date.
        :param date: date to which the age is calculated. Date string format
        YYYY-MM-DD.
        :return: age in years.
        """
        year, month, day = (
            int(x) for x in date.split('-')
        )
        age = year - self.year
        if (month, day) < (self.month, self.day):
            age -= 1
        return age


class DateAgeAdapter:
    """
    Implementation of the adapter pattern. This class maps between the Python
    standard library datetime and the AgeCalculator date format (string).
    Client code that needs to use AgeCalculator functionality can do so through
    this class.
    """

    def __init__(self, birthday):
        """
        Initialise this adapter object with an AgeCalculator object using the
        specified birthday.
        :param birthday: using Python datetime.date object.
        """
        birthday_str = self._str_date(birthday)
        self.age_calculator = AgeCalculator(birthday_str)

    def get_age(self, date):
        """
        Calculate the age to the given date, using the AgeCalculator object.
        :param date: datetime.date object to which the age should be calculated.
        :return: age in years
        """
        date_str = self._str_date(date)
        return self.age_calculator.calculate_age(date_str)

    def _str_date(self, date):
        """
        Map between the given Python datetime.date object and the date string
        used by the AgeCalculator.
        :param date: datetime.date object to convert to AgeCalculator date
        string
        :return: date string representation in YYYY-MM-DD format.
        """
        return date.strftime('%Y-%m-%d')


# Demonstration of API
def main():
    # Create the adapter object with the birthday datetime.date object
    date_age_adapter = DateAgeAdapter(datetime.date(1980, 1, 1))
    # Calculate the age in years
    age = date_age_adapter.get_age(datetime.date.today())
    print('Age = {} years'.format(age))


# Import guard
if __name__ == '__main__':
    main()
