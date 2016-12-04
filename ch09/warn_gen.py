import sys

"""
Warning filer implementation using generators. The yeild statement creates a
generator object from the function. When __next__() is called, the generator
object runs the function until it reaches the yield statement. It then returns
the value from the yeild statement, and the next time __next__() is called, it
picks ups from where it left off last time.
"""

inname, outname = sys.argv[1:3]


def warnings_filter(insequence):
    for l in insequence:
        if 'WARNING' in l:
            yield l.replace('\tWARNING', '')


with open(inname) as infile:
    with open(outname, "w") as outfile:
        warn_filter = warnings_filter(infile)
        for l in warn_filter:
            outfile.write(l)
