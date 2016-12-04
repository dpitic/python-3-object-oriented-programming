import sys

"""
This is an OO implementation of the warning log file parser. This implementation
is difficult to read and maintain compared to the generator implementation.
"""

inname, outname = sys.argv[1:3]

class WarningFilter:
    def __init__(self, insequence):
        self.insequence = insequence

    def __iter__(self):
        return self

    def __next__(self):
        # Read a line from the file
        l = self.insequence.readline()
        # Discard the line if it is not a 'WARNING'
        while l and 'WARNING' not in l:
            l = self.insequence.readline()
        # Stop iterating when EOF is reached
        if not l:
            raise StopIteration
        # Return only the filtered lines with 'WARNING'
        return l.replace('\tWARNING', '')

with open(inname) as infile:
    with open(outname, "w") as outfile:
        warn_filter = WarningFilter(infile)
        for l in warn_filter:
            outfile.write(l)
