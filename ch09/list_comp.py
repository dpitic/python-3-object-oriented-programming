# Demonstration of list comprehensions. Convert a list of strings to list of
# integers.

input_strings = ['1', '5', '28', '131', '3']
print(input_strings)

# Implementation without using comprehensions
output_integers = []
for num in input_strings:
    output_integers.append(int(num))
print(output_integers)
print()

# Implementation using comprehensions. This is faster and more readable than
# looping using the for loop.
out_integers = [int(num) for num in input_strings]
print(out_integers)
print()

# Excluding certain values using an if statement.
output_ints = [int(n) for n in input_strings if len(n) < 3]
print(output_ints)
