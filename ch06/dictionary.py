from collections import defaultdict
from collections import Counter

# Demonstration of using dictionary
stocks = {"GOOG": (613.30, 625.86, 610.50),
          "MSFT": (30.25, 30.70, 30.19)}
print("stocks['GOOG'] = %s" % str(stocks["GOOG"]))
# Exception raised if the key is not in the dictionary
try:
    print("stocks['RIM'] = %s" % str(stocks["RIM"]))
except KeyError as e:
    print("Key 'RIM' not in dictionary")

print("stocks.get('RIM') = %s" % str(stocks.get('RIM')))
print("stocks.get('RIM', 'NOT FOUND') = %s" % str(
        stocks.get('RIM', 'NOT FOUND')))

# setdefault()
# Sets a value in the dictionary only if that value has not previously been set,
# then returns the value.
print("stocks.setdefault('GOOG', 'INVALID') = %s" % str(
        stocks.setdefault('GOOG', 'INVALID')))
print("stocks.setdefault('BBRY', (10.50, 10.62, 10.39)) = %s" % str(
        stocks.setdefault('BBRY', (10.50, 10.62, 10.39))))
print("stocks['BBRY'] = %s" % str(stocks["BBRY"]))

# keys(), values() and items()
print("stocks.keys() = %s" % str(stocks.keys()))
print("stocks.values() = %s" % str(stocks.values()))
for stock, values in stocks.items():
    print("{} current value is {}".format(stock, values[0]))

# Setting dictionary values
stocks["GOOG"] = (597.63, 610.00, 596.28)
print("stocks['GOOG'] = %s" % str(stocks['GOOG']))

# Keys are not limited to strings, and different types of keys can be used in
# a single dictionary.
random_keys = {}
random_keys["astring"] = "something"
random_keys[5] = "aninteger"
random_keys[25.2] = "floats work too"
random_keys[("abc", 123)] = "so do tuples"

class AnObject:
    """docstring for AnObject."""
    def __init__(self, avalue):
        self.avalue = avalue

my_object = AnObject(14)
random_keys[my_object] = "We can even store objects"
my_object.avalue = 12
print("my_object.avalue = %d" % my_object.avalue)
try:
    random_keys[[1,2,3]] = "we can't store lists though"
except Exception as e:
    print("unable to store lists\n")
for key, value in random_keys.items():
    print("{} has value {}".format(key, value))

# Demonstration of using defaultdict() as an alternative to setdefault()
def letter_frequency(sentence):
    """
    Returns a dictionary of letter frequencies for the given sentence. The
    implementation uses the build-in Python dictionary and sets the default
    frequency value for a letter to zero initially and then increments it.
    """
    frequencies = {}
    for letter in sentence:
        frequency = frequencies.setdefault(letter, 0)
        frequencies[letter] = frequency + 1
    return frequencies

sentence = "The quick brown fox jumped over the lazy dog."
print("Letter frequency =\n%s" % str(letter_frequency(sentence)))

def letter_frequency(sentence):
    """
    Returns a dictionary of letter frequencies for the given sentence. The
    implementation uses the Python standard library defaultdict() object
    initialised to integer values.
    """
    frequencies = defaultdict(int)
    for letter in sentence:
        frequencies[letter] += 1
    return frequencies

print("Letter frequency =\n%s" % str(letter_frequency(sentence)))

# implementation of the letter frequency counter using the standard library
# Counter class. This is used to count specific instances in an iterable.
def letter_frequency(sentence):
    return Counter(sentence)

freq = letter_frequency(sentence)
print("Letter frequency =\n%s" % str(freq))
print("All most common = %s" % freq.most_common())
print("2 most common = %s" % freq.most_common(2))

responses = [
    "vanilla",
    "chocolate",
    "vanilla",
    "vanilla",
    "caramel",
    "strawberry",
    "vanilla"
]

print("The children voted for {} ice cream".format(
    Counter(responses).most_common(1)[0][0]))
flavour, freq = Counter(responses).most_common(1)[0]
print("The children voted for {} ice cream {} times".format(flavour, freq))
