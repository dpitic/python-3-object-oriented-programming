import sys

"""
Demonstration of using generator expressions to create an output warnings file
by stripping the 'WARNING' column from the input log file.

The generator expression creates a generator object.
"""

inname, outname = sys.argv[1:3]

# Use generator expression to remove 'WARNING' column from log file.
with open(inname) as infile:
    with open(outname, "w") as outfile:
        warnings = (l.replace('\tWARNING', '')
                    for l in infile if 'WARNING' in l)
        for l in warnings:
            outfile.write(l)
outfile.close()

# Display the contents of the processed warning log file.
with open(outname) as file:
    lines = (l for l in file)
    for l in lines:
        print(l, end='')
