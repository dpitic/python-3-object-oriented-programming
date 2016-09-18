import sys
import re

"""
Generic regex pattern matcher that accepts a pattern and search string on the
command line and returns whether the pattern matches.
"""

pattern = sys.argv[1]
search_string = sys.argv[2]
match = re.match(pattern, search_string)

if match:
    template = "'{}' matches pattern '{}'"
else:
    template = "'{}' does not match pattern '{}'"

print(template.format(search_string, pattern))
