"""
Demonstration of the abstract factory pattern.

The abstract factory pattern is used when there are multiple possible
implementations of a system that depend on some configuration or platform. The
client code requests an object from the abstract factory without knowing the
specific class of object that will be returned. The implementation returned may
depend on a variety of factors, such as locale, operating system or local
configuration.

Common examples of the abstract factory pattern include code for operating
system independent toolkits, database backends and country specific formatters.

This script implements an abstract factory for a set of formatters that depend
on specific locale for formatting dates and currencies.
"""


# Formatter classes
class FranceDateFormatter:
    def format_date(self, y, m, d):
        """
        Format date in the locale for France: dd/mm/yy
        :param y: year
        :param m: month
        :param d: day
        :return: date string in French locale format dd/mm/yy
        """
        y, m, d = (str(x) for x in (y, m, d))
        y = '20' + y if len(y) == 2 else y
        m = '0' + m if len(m) == 1 else m
        d = '0' + d if len(d) == 1 else d
        return ('{0}/{1}/{2}'.format(d, m, y))


class USADateFormatter:
    def format_date(self, y, m, d):
        """
        Format date in the locale for the USA: mm-dd-yy
        :param y: year
        :param m: month
        :param d: day
        :return: date string in the USA local format mm-dd-yy
        """
        y, m, d = (str(x) for x in (y, m, d))
        y = '20' + y if len(y) == 2 else y
        m = '0' + m if len(m) == 1 else m
        d = '0' + d if len(d) == 1 else d
        return ('{0}-{1}-{2}'.format(m, d, y))


class FranceCurrencyFormatter:
    def format_currency(self, base, cents):
        """
        Format currency in the locale for France: base€cents, eg. 14 500€50
        :param base: currency base
        :param cents: currency cents
        :return: currency string in the French locale format base€cents
        """
        base, cents = (str(x) for x in (base, cents))
        if len(cents) == 0:
            cents = '00'
        elif len(cents) == 1:
            cents = '0' + cents

        digits = []
        for i, c in enumerate(reversed(base)):
            if i and not i % 3:
                digits.append(' ')
            digits.append(c)
        base = ''.join(reversed(digits))
        return '{0}€{1}'.format(base, cents)


class USACurrencyFormatter:
    def format_currency(self, base, cents):
        """
        Format currency in the locale for the USA: dollars.cents, eg. $14,500.50
        :param base: currency base
        :param cents: currency cents
        :return: currency string in the UAS locale format base.cents
        """
        base, cents = (str(x) for x in (base, cents))
        if len(cents) == 0:
            cents = '00'
        elif len(cents) == 1:
            cents = '0' + cents
        digits = []
        for i, c in enumerate(reversed(base)):
            if i and not i % 3:
                digits.append(',')
            digits.append(c)
        base = ''.join(reversed(digits))
        return '${0}.{1}'.format(base, cents)


# Formatter factory classes
class USAFormatterFactory:
    def create_date_formatter(self):
        return USADateFormatter()

    def create_currency_formatter(self):
        return USACurrencyFormatter()


class FranceFormatterFactory:
    def create_date_formatter(self):
        return FranceDateFormatter()

    def create_currency_formatter(self):
        return FranceCurrencyFormatter()

# Formatter factory
