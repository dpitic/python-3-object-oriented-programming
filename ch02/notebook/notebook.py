import datetime

# Store the next available id for all new notes
last_id = 0

class Note:
    '''
    Represents a note in the notebook. Match against a string in searches and
    store tags for each note.
    '''

    def __init__(self, memo, tags=''):
        '''
        Initialise a note with memo and optional space-separated tags.
        Automatically set the note's creation date and a unique id.
        '''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id

    def match(self, filter):
        '''
        Determine if this note matches the filter text. Return True if it
        matches, False otherwise.

        Search is case sensitive and matches both text and tags.
        :param filter: text to match a note text (memo) or tags against
        :return: True for filter match; False otherwise
        '''
        return filter in self.memo or filter in self.tags

class Notebook:
    '''
    Represents a collection of notes that can be tagged, modified and searched.
    '''

    def __init__(self):
        '''Initialise a notebook with an empty list.'''
        self.notes = []

    def new_note(self, memo, tags=''):
        '''Create a new note and add it to the list.'''
        self.notes.append(Note(memo, tags))

    def _find_note(self, note_id):
        '''Locate the note with the given id.'''
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None

    def modify_memo(self, note_id, memo):
        '''
        Find the note with the given id and change its memo to the given value.
        '''
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False

    def modify_tags(self, note_id, tags):
        '''
        Find the note with the given id and change its tags to the given value.
        '''
        for note in self.notes:
            if note.id == note_id:
                note.tags = tags
                break

    def search(self, filter):
        '''Find all notes that match the given filter string.'''
        return [note for note in self.notes if note.match(filter)]

# Sample code to demonstrate the Notebook and Note API
def main():
    n = Notebook()
    n.new_note("hello world")
    n.new_note("hello again")
    print(n.notes)
    print(n.notes[0].id)
    print(n.notes[1].id)
    print(n.notes[0].memo)
    print(n.search("hello"))
    print(n.search("world"))
    n.modify_memo(1, "hi world")
    print(n.notes[0].memo)

# Module import guard. Execute sample code if explicitly run.
if __name__ == '__main__':
    main()