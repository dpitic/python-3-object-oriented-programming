from collections import namedtuple

# Demonstration of using named tuples
# namedtuple() constructor used to define the class
Stock = namedtuple("Stock", "symbol current high low")
stock = Stock("FB", 75.00, high=75.03, low=74.90)

print("stock = %s" % str(stock))
print("stock.high = %f" % stock.high)
# Unpacking
symbol, current, high, low = stock
print("Unpacked current = %f" % current)
