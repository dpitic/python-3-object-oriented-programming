import sys

# Demonstration of enumerate(). Used to return a sequence of tuples where
# the first object in each tuple is the index and the second is the original
# item.

filename = sys.argv[1]

with open(filename) as file:
    for index, line in enumerate(file):
        print("{0}: {1}".format(index + 1, line), end='')
