import sys

"""
Demonstration of using generators to create an output warnings file by stripping
the 'WARNING' column from the input log file.
"""

inname, outname = sys.argv[1:3]

with open(inname) as infile:
    with open(outname, "w") as outfile:
        warnings = (l.replace('\tWARNING', '')
                    for l in infile if 'WARNING' in l)
        for l in warnings:
            outfile.write(l)
