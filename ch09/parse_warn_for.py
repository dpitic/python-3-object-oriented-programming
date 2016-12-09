import sys

"""
Alternative implementation of warning log file parser using a for loop. Compared
to the implementation using generator expressions, this implementation has many
levels of indent making it more difficult to read and maintain.
"""

inname, outname = sys.argv[1:3]

# Process log file to remove 'WARNING' column.
with open(inname) as infile:
    with open(outname, "w") as outfile:
        for l in infile:
            if 'WARNING' in l:
                outfile.write(l.replace('\tWARNING', ''))
outfile.close()

# Display the processed log file.
with open(outname) as file:
    lines = (l for l in file)
    for l in lines:
        print(l, end='')
