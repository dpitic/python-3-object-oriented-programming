import sys

"""
Demonstration of generator expressions to parse log files. Rather than loading
the whole log file into memory, the generator expression yields the current
element. Generator expressions prevent us from having to create a new container
to store all of the elements we need to process.

Generator expressing use the same syntax as comprehensions, but they don't
create a container object. To create a generator expression, wrap the
comprehension in (), instead of [] or {}.
"""

inname = sys.argv[1]
outname = sys.argv[2]

with open(inname) as infile:
    with open(outname, "w") as outfile:
        # Create the generator expression to yield lines with 'WARNING' only
        warnings = (l for l in infile if 'WARNING' in l)
        for l in warnings:
            outfile.write(l)
