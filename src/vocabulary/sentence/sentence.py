from PyQt6.QtGui import QStandardItem
import re
from ..str_utils import *

class Sentence():
    def __init__(self, sentence, translation, transcription, word1, meaning1):
        self.update_attributes([sentence, translation, word1, meaning1])
        self.kanji_data = self._get_kanji_data(transcription) # Dictionnary containing kanji and theirs readings.
        self.position_kanji_sentence = get_position_kanji_sentence(sentence, self.kanji_data.keys()) # Dict containg positions in text as keys and kanjis as values.

        self.standard_item = None # QStandardItem in order to be inserted in the model
        self.compute_standard_item()

    def compute_standard_item(self):
        """Update standard item, based on current sentences attributes. """
        self.standard_item = [QStandardItem(field) for field in self.fields] 

    def update_attributes(self, fields: list, kanji_data: dict = None):
        """Update sentence attributes."""

        self.lang_from = fields[0]
        self.translation = fields[1]
        self.word1 = fields[2]
        self.word1_meaning = fields[3]

        match fields:
            case [lang_from, translation, word1, meaning1]:
                self.word2, self.word2_meaning = "", ""
                self.fields = [lang_from, translation, word1, meaning1, self.word2, self.word2_meaning]
            case [lang_from, translation, word1, meaning1, word2, meaning2]:
                self.word2, self.word2_meaning = word2, meaning2
                self.fields = list(fields)
            case _:
                raise Exception # TODO: Add DialogError
        
        if  kanji_data != None:
            self.kanji_data = dict(kanji_data)
            self.position_kanji_sentence = get_position_kanji_sentence(self.lang_from, self.kanji_data.keys())

    def _get_kanji_data(self, sentence): # TODO: put in sentence retriever
        """Return a dictionnary containg kanji as keys and a tuple (reading, meaning, position) as values."""
        pattern = r'\[([^\|\[\]]+)\|([^\[\]]+)\]'
        result = re.findall(pattern, sentence) 
        dict = {}
        i = 0
        for match in result:
                kanji, reading = match
                reading = reading.replace('|', '')
                if kanji == self.word1:
                    dict[kanji] = (reading, self.word1_meaning, i)
                elif kanji == self.word2:
                    dict[kanji] = (reading, self.word2_meaning, i)
                else:
                    dict[kanji] = (reading, "", i)
                i += 1
        return dict
    

# self.position_kanji_sentence = self._get_position_kanji_sentence()