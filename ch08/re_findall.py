import re

# Example of re.findall() method

print(re.findall("a.", "abacadefagah"))
print(re.findall("a(.)", "abacadefagah"))
print(re.findall("(a)(.)", "abacadefagah"))
print(re.findall("((a)(.))", "abacadefagah"))
