import datetime

# Two types of tuple literals
stock = "FB", 75.00, 75.03, 74.90
stock2 = ("FB", 75.00, 75.03, 74.90)

def middle(stock, date):
    symbol, current, high, low = stock
    return (((high + low) / 2), date)

# Using a tuple in a function call as an argument
# Tuple unpacking in the function return
mid_value, date = middle(("FB", 75.00, 75.03, 74.90),
                        datetime.date(2014, 10, 31))
print("Mid value = %f" % mid_value)
print("date = %s" % date)
print()

print("stock[2] = %f" % stock[2])
print("stock[1:3] = %s" % str(stock[1:3]))
