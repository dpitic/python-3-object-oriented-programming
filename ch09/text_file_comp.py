import sys

"""
Demonstration of iterating over a text file. Each call to __next__() on the
file's iterator returns one line of the file. This sample code loads a tab
delimited file, where the first line is a header row, into a dictionary using
the zip() function.
"""

filename = sys.argv[1]

with open(filename) as file:
    header = file.readline().strip().split('\t')
    contacts = [
        dict(zip(header, line.strip().split('\t'))) for line in file
    ]

for contact in contacts:
    print("email: {email} -- {last}, {first}".format(**contact))
