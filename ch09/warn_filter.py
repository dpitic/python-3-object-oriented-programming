import sys

"""
This is an OO implementation of the warning log file parser. It implements an
iterator object that is used to process the log file. This implementation is
difficult to read and maintain compared to the generator expression
implementation.
"""

inname, outname = sys.argv[1:3]


class WarningFilter:
    """
    Iterator used to filter the log file to remove the 'WARNING' column.
    """
    def __init__(self, insequence):
        self.insequence = insequence

    def __iter__(self):
        """
        The iterator typically returns itself.
        :return: the iterator.
        """
        return self

    def __next__(self):
        """
        Implement the iterator protocol to return the next element in the
        sequence.
        :return: the next line in the processed log file.
        """
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


# Process the input log file and remove the 'WARNING' column.
with open(inname) as infile:
    with open(outname, "w") as outfile:
        warn_filter = WarningFilter(infile)
        for l in warn_filter:
            outfile.write(l)
outfile.close()

# Display the contents of the processed log file.
with open(outname) as file:
    lines = (l for l in file)
    for l in lines:
        print(l, end='')
