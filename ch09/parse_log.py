import sys

"""
Demonstration of generator expressions to parse log files. Rather than loading
the whole log file into memory, the generator expression yields the current
element.

Generator expressions enable sequences to be processed without creating a new
container object to store the elements. Sequences can be iterated over without
allocating memory for the entire sequence.

Generator expressions use a similar syntax to comprehensions, but they don't
create a container object. To create a generator expression, wrap the
comprehension in (), instead of [] or {}.

In general, generator expressions should be used whenever possible in preference
to comprehensions, unless the container object needs to be retained. If there is
a requirement to know the length of a list, or sort the results, remove
duplicates, or create a dictionary, then the comprehension syntax must be used.
"""

inname, outname = sys.argv[1:3]

# Process log file; create output file containing only warnings.
with open(inname) as infile:
    with open(outname, "w") as outfile:
        # Create the generator expression to yield lines with 'WARNING' only
        warnings = (l for l in infile if 'WARNING' in l)
        for l in warnings:
            outfile.write(l)

outfile.close()

# Display processed log file.
with open(outname) as file:
    # Create a generator to yield each line in the processed log file.
    lines = (l for l in file)
    for l in lines:
        # The lines all have \n at the end; no need to add new line to print.
        print(l, end='')
