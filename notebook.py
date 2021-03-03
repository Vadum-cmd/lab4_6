"""
This module contains classes Note and Notebook.
"""
import datetime

# Store the next available id for all new notes
last_id = 0

class Note:
    def __init__(self, memo, tags=''):
        '''
        Create a note with memo and optional
        space-separated tags. Automatically set the note's
        creation date and a unique id.S
        '''
        self.memo = memo
        self.tags = tags
        self.creation_date = datetime.date.today()
        global last_id
        last_id += 1
        self.id = last_id


    def match(self, filter):
        '''
        Determine if this note matches the filter
        text. Return True if it matches, False otherwise.
        Search is case sensitive and matches both text and
        tags.
        >>> note = Note('hello world', 'hi there')
        >>> note.match('hi')
        True
        >>> note.match('world')
        True
        >>> note.match('bye')
        False
        '''
        return filter in self.memo or filter in self.tags


class Notebook:
    def __init__(self):
        '''
        Create a notebook with an empty list.
        '''
        self.notes = []


    def new_note(self, memo, tags=''):
        '''
        Create a new note and add it to the list.
        >>> notebook = Notebook()
        >>> notebook.notes
        []
        >>> notebook.new_note('hello world', 'hi there')
        >>> len(notebook.notes)
        1
        '''
        self.notes.append(Note(memo, tags))


    def _find_note(self, note_id):
        '''
        Locate the note with the given id.
        >>> notebook = Notebook()
        >>> notebook._find_note(1)
        >>> notebook.new_note('hello world', 'hi there')
        >>> notebook._find_note(2) != None
        True
        '''
        for note in self.notes:
            if str(note.id) == str(note_id):
                return note
        return None


    def modify_memo(self, note_id, memo):
        '''
        Find the note with the given id and change its
        memo to the given value.
        >>> notebook = Notebook()
        >>> notebook.new_note('hello world', 'hi there')
        >>> notebook.modify_memo(3, 'hi world')
        True
        >>> notebook.notes[0].memo
        'hi world'
        '''
        note = self._find_note(note_id)
        if note:
            note.memo = memo
            return True
        return False


    def modify_tags(self, note_id, tags):
        '''
        Find the note with the given id and change its
        tags to the given value.
        >>> notebook = Notebook()
        >>> notebook.new_note('hello world', 'hi there')
        >>> notebook.modify_tags(4, 'hi world')
        True
        >>> notebook.notes[0].tags
        'hi world'
        '''
        note = self._find_note(note_id)
        if note:
            note.tags = tags
            return True
        return False


    def search(self, filter):
        '''
        Find all notes that match the given filter
        string.
        >>> notebook = Notebook()
        >>> notebook.new_note('hello world1', 'hi there1')
        >>> notebook.new_note('hello world2', 'hi there2')
        >>> notebook.new_note('hello world3', 'hi there3')
        >>> len(notebook.search('hello'))
        3
        '''
        return [note for note in self.notes if
                note.match(filter)]


if __name__ == "__main__":
    import doctest
    doctest.testmod()
