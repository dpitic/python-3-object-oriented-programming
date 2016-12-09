import sys

"""
Warning filer implementation using generators. The yield statement creates a
generator object from the function. When __next__() is called, the generator
object runs the function until it reaches the yield statement. It then returns
the value from the yield statement, and the next time __next__() is called, it
picks ups from where it left off last time. The generator object raises a
StopIteration exception when there are no more elements in the sequence.

Generator objects have __iter__() and __next__() methods. They implement the
iterator protocol.

When __next__() is called the generator runs the function until it reaches the
yield statement. It returns the value from yield, and the next time __next__()
is called, it picks up from where it left off. A function can have multiple
yield statements and the generator will continue from the most recent yield and
continue to the next one.
"""

inname, outname = sys.argv[1:3]


def warnings_filter(insequence):
    """
    Generator used to remove the 'WARNING' column from the provided sequence
    (iterable).

    The yield statement creates a generator object from this function. When
    yield is executed it returns an element from the iterable (sequence). When
    the function is called again (via the next() method), it will continue from
    where it left off, on the line after the yield statement, rather that from
    the beginning of the function. In this case, there is no statement after the
    yield statement, so it jumps to the next iteration of the for loop. Since
    the yield statement is inside an if statement, it only yields lines that
    contain 'WARNING'.

    :param insequence: input iterable sequence.
    :return: the 'WARNING' elements with the 'WARNING' column removed.
    """
    for l in insequence:
        if 'WARNING' in l:
            # yield statement creates a generator object from this function.
            yield l.replace('\tWARNING', '')


# Process the log file to remove the 'WARNING' column.
with open(inname) as infile:
    with open(outname, "w") as outfile:
        # Create the generator object to process the log file.
        warn_filter = warnings_filter(infile)
        for l in warn_filter:
            outfile.write(l)
outfile.close()

# Display the processed log file with 'WARNING' column removed.
with open(outname) as file:
    lines = (l for l in file)
    for l in lines:
        print(l, end='')
