# Comprehensions provide simple but powerful syntax that enable iterable objects
# to be transformed or filtered in one line of code. The resulting object can be
# any sequence such as a list, set or dictionary, or it can be a generator
# expression that can be efficiently consumed in one go.
#
# Comprehensions provide an optimised syntax for creating a list, set or
# dictionary from an existing sequence (iterable).
#
# Demonstration of list comprehensions. Convert a list of strings to list of
# integers. The list comprehension syntax uses a for statement inside [] to
# generate a new list object containing the transformed or filtered sequence
# elements provided as input. Any iterable can be used as input to a list
# comprehension.

input_strings = ['1', '5', '28', '131', '3']
print('Input list of strings:')
print(input_strings)

# Implementation without using comprehensions
output_integers = []
for num in input_strings:
    output_integers.append(int(num))
print('\nOutput implemented without using comprehensions:')
print(output_integers)

# Implementation using comprehensions. This is faster and more readable than
# looping using the for loop.
out_integers = [int(num) for num in input_strings]
print('\nOutput implementation using comprehensions:')
print(out_integers)

# Excluding certain values using an if statement.
output_ints = [int(n) for n in input_strings if len(n) < 3]
print('\nOutput demonstrating exclusion of values using "if" statement:')
print(output_ints)
