from PyQt6.QtGui import QStandardItem
from ..str_utils import *

class Sentence():
    def __init__(self, sentence, translation, kanji_data, word):
        self.word = word
        self.sentence = sentence
        self.translation = translation
        word1_reading, word1_meaning, word1_position = kanji_data[word]
        self.word1_data = (word, word1_reading, word1_meaning, word1_position)
        self.word2_data = None
        self.fields = (sentence, translation, self.word1_data, self.word2_data)

        self.kanji_data = kanji_data # Dict containing kanji and theirs readings.
        self.position_kanji_sentence = get_position_kanji_sentence(sentence, kanji_data.keys()) # Dict containg positions in text as keys and kanjis as values.

        self.standard_item = None # QStandardItem in order to be inserted in the model
        self.compute_standard_item()

    def compute_standard_item(self):
        """Update standard item to insert in Sentence model, based on current sentences attributes. """
        word1_kanji, word2_kanji = None, None
        if self.word1_data != None:
            word1_kanji = self.word1_data[0]
        if self.word2_data != None:
            word2_kanji = self.word2_data[0]
        self.standard_item = [QStandardItem(self.sentence), QStandardItem(self.translation), QStandardItem(word1_kanji), QStandardItem(word2_kanji)] 

    def update_attributes(self, fields: tuple, kanji_data: dict):
        """Update sentence attributes."""
        self.sentence, self.translation, self.word1_data, self.word2_data = fields
        self.fields = fields
        
        self.kanji_data = dict(kanji_data)
        self.position_kanji_sentence = get_position_kanji_sentence(self.sentence, self.kanji_data.keys())