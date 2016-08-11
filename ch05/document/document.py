# Case study for the development of a simple Document class that could be used
# in a text editor or word processor.


class Document:
    """
    Document class used to represent simple documents in a text editor or word
    processor.
    """

    def __init__(self):
        self.characters = []
        self.cursor = Cursor(self)
        self.filename = ''

    def insert(self, character):
        """
        Insert a character at the current cursor position and advance the
        cursor by one character.
        """
        if not hasattr(character, 'character'):
            character = Character(character)
        self.characters.insert(self.cursor.position, character)
        self.cursor.forward()

    def delete(self):
        """
        Delete the character at the current cursor position. Leave the cursor
        in its current position.
        :return: None
        """
        del self.characters[self.cursor.position]

    def save(self):
        """
        Save this Document to disk.
        :return: None
        """
        f = open(self.filename, 'w')
        f.write(''.join(self.characters))
        f.close()

    def forward(self):
        """Advance the cursor 1 character forward in the Document."""
        self.cursor.forward()

    def back(self):
        """Move the cursor back 1 character in the Document."""
        self.cursor.back()

    @property
    def string(self):
        """
        Return the Document as a string of characters.
        :return: Document as a string of characters.
        """
        return "".join((str(c) for c in self.characters))


class Cursor:
    """Cursor represents the position of the cursor in a document."""

    def __init__(self, document):
        self.document = document
        self.position = 0

    def forward(self):
        """Move the cursor forward 1 character in the document."""
        self.position += 1

    def back(self):
        """Move the cursor back 1 character in the document."""
        self.position -= 1

    def home(self):
        """Move the cursor to the start of the line."""
        while self.document.characters[self.position-1].character != '\n':
            self.position -= 1
            if self.position == 0:
                # Got to beginning of file before newline
                break

    def end(self):
        """Move to the end of the line."""
        while self.position < len(self.document.characters
                                  ) and self.document.characters[
                                  self.position].character != '\n':
            self.position += 1


class Character:
    """Represents a character with formatting information."""

    def __init__(self, character, bold=False, italic=False, underline=False):
        """
        Initialise a character with formatting.
        :param character: The character this class represents.
        :param bold: True for bold character.
        :param italic: True for italic character.
        :param underline: True for underline character.
        """
        assert len(character) == 1
        self.character = character
        self.bold = bold
        self.italic = italic
        self.underline = underline

    def __str__(self):
        """
        String representation of this character with formatting.
        :return: String representation of this character with formatting.
        """
        bold = "*" if self.bold else ''
        italic = "/" if self.italic else ''
        underline = "_" if self.underline else ''
        return bold + italic + underline + self.character


# Demonstration of class API
def main():
    doc = Document()
    doc.filename = 'test_document'
    # Document without formatted characters
    for ch in 'hello':
        doc.insert(ch)
    print("Document = \n%s" % doc.string)
    doc.back()
    doc.delete()
    doc.insert('p')
    print("Document = \n%s" % doc.string)
    print()

    for ch in '\nworld':
        doc.insert(ch)
    doc.cursor.home()
    doc.insert('*')
    print("Document = \n%s" % doc.string)
    print()

    # Document with formatted characters
    doc = Document()
    doc.insert('h')
    doc.insert('e')
    doc.insert(Character('l', bold=True))
    doc.insert(Character('l', bold=True))
    doc.insert('o')
    doc.insert('\n')
    doc.insert(Character('w', italic=True))
    doc.insert(Character('o', italic=True))
    doc.insert(Character('r', underline=True))
    doc.insert('l')
    doc.insert('d')
    print("Document = \n%s" % doc.string)
    doc.cursor.home()
    doc.delete()
    doc.insert('W')
    print("Document = \n%s" % doc.string)
    doc.characters[0].underline = True
    print("Document = \n%s" % doc.string)
    print()


# Import guard
if __name__ == '__main__':
    main()
