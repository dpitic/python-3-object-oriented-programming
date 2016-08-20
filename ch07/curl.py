import sys
from urllib.request import urlopen

# Transfer the contents of the specified URL to stdout.

url = sys.argv[1]

with urlopen(url) as obj:
    for line in obj:
        str_line = str(line).lstrip("b'").rstrip("\\r\\n'")
        print(str_line)
