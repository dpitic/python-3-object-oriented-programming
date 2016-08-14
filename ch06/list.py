import string

# A complicated implementation of the letter frequency function using lists.

# Define the list of possible characters in the sentence.
CHARACTERS = list(string.ascii_letters) + [" "] + ["."]

def letter_frequency(sentence):
    """
    Return a list of tuples containing the letters and frequencies in the given
    sentence. This is a complicated implementation using lists. The simpler
    implementation uses dictionary and Counter.
    """
    # Convert the permissible characters into a frequency list of tuples using
    # list comprehension.
    frequencies = [(c, 0) for c in CHARACTERS]
    for letter in sentence:
        index = CHARACTERS.index(letter)
        frequencies[index] = (letter, frequencies[index][1]+1)
    return frequencies

sentence = "The quick brown fox jumped over the lazy dog."
print("Frequencies = %s" % str(letter_frequency(sentence)))
