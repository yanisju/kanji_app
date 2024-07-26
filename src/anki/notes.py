import genanki
import re

class Notes():
    """ A class representing the Anki Deck containing single cards / note inside the deck.
    #TODO: correct """

    def __init__(self, model):
        self.model = model
        self._notes = []
        self._sort_number = 0

    def __get_item__(self, index):
        return self._notes[index]
    
    def __iter__(self):
        for note in self._notes:
            yield note
            
    def add(self, card):
        """Add a single note to the deck. """
        note_field = card
        note_field[0] = str(self._sort_number)
        note_field[1], note_field[2] = note_field[2], note_field[1]
        note_field.append('')

        note = genanki.Note(
                model=self.model,
                fields = note_field)
        
        self._notes.append(note)

    def modify(self, card, row):
        note = genanki.Note(
                model=self.model,
                fields = card)
        
        self._notes[row] = note

    def del_card(self, row):
        self._notes.pop(row)

    def clear(self):
        self._notes.clear()

    

        
    