import sys

# Demonstration of the with statement which automatically calls the __exit__()
# method on a file object to close the file, even if an exception is raised.
# The script displays the contents of a file to stdout.

filename = sys.argv[1]

with open(filename) as file:
    for line in file:
        print(line, end='')
