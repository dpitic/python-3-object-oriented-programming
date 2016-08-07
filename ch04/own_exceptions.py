class InvalidWithdrawal(Exception):
    """Example of defining exceptions."""
    pass


class InvalidWithdrawal2(Exception):
    """
    Example of overriding the Exception.__init__(). This is not necessary as
    the initialier accepts any arguments and stores them in an attribute called
    args.
    """

    def __init__(self, balance, amount):
        super(InvalidWithdrawal2, self).__init__(
            "acount doesn't have ${}".format(amount))
        self.amount = amount
        self.balance = balance

    def overage(self):
        return self.amount - self.balance


def divide_with_exception(number, divisor):
    """Example of using exceptions to control program flow."""
    try:
        print("{} / {} = {}".format(number, divisor, number / divisor * 1.0))
    except ZeroDivisionError as e:
        print("You can't divide by zero")


def divide_with_if(number, divisor):
    """Implementation of divide_with_exception() using if...else"""
    if divisor == 0:
        print("You can't divide by zero")
    else:
        print("{} / {} = {}".format(number, divisor, number / divisor * 1.0))


def main():
    # InvalidWithdrawal
    try:
        # Example of how to raise a user defined exception.
        raise InvalidWithdrawal("You don't have $50 in your account")
    except InvalidWithdrawal as e:
        print("InvalidWithdrawal caught: %s" % e)
    print()

    # InvalidWithdrawal2
    try:
        # Example of raising a user defined exception with arguments
        raise InvalidWithdrawal2(25, 50)
    except InvalidWithdrawal2 as e:
        print("I'm sorry, but your withdrawal is more than your balance by ${}"
            .format(e.overage()))
    print()

    # Using exceptions to control program flow
    divide_with_exception(5, 0)
    # Using if...else to control exceptional program flow
    divide_with_if(5, 0)


if __name__ == '__main__':
    main()
