from collections import namedtuple

"""
Demonstration of set comprehensions using named tuples. Set comprehensions use
similar syntax with braces to create sets and dictionaries.
"""

# Use a named tuple to model a book consisting of author, title, genre.
Book = namedtuple("Book", "author title genre")
# List of books used as input.
books = [
    Book("Pratchett", "Nightwatch", "fantasy"),
    Book("Pratchett", "Thief Of Time", "fantasy"),
    Book("Le Guin", "The Dispossessed", "scifi"),
    Book("Le Guin", "A Wizard Of Earthsea", "fantasy"),
    Book("Turner", "The Thief", "fantasy"),
    Book("Phillips", "Preston Diamond", "western"),
    Book("Phillips", "Twice Upon A Time", "scifi"),
]

# Set comprehension using braces {}. The duplicates are removed (set).
fantasy_authors = {
    b.author for b in books if b.genre == 'fantasy'
}
print('Set comprehension with duplicate authors removed:')
print(fantasy_authors)

# Use dictionary comprehension to map titles to book objects. Dictionary
# comprehension are created by using a colon : syntax. This converts a sequence
# into a dictionary using key:value pairs. In this case, the dictionary contains
# title:Book. This dictionary can be used to look up books using their title.
fantasy_titles = {
    b.title: b for b in books if b.genre == 'fantasy'
}
print('\nDictionary comprehension:')
print(fantasy_titles)
