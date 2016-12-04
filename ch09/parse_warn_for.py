import sys

"""
Alternative implementation of warning log file parser using a for loop. Compared
to the implementation using a generator, this implementation has many levels of
indent.
"""

inname, outname = sys.argv[1:3]

with open(inname) as infile:
    with open(outname, "w") as outfile:
        for l in infile:
            if 'WARNING' in l:
                outfile.write(l.replace('\tWARNING', ''))
