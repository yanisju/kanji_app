from PyQt6.QtGui import QStandardItem
from .kanji_model import KanjiModel
import re

class Sentence():
    def __init__(self, lang_from, translation, transcription, word1, meaning1):
        self.update_attributes([lang_from, translation, word1, meaning1])
        self.kanji_readings = self._get_kanji_readings(transcription) # Dictionnary containing kanji and theirs readings.
        self.position_kanji = self._get_position_kanji()
        self.kanji_model = KanjiModel(self.kanji_readings, word1, meaning1)

    def update_attributes(self, fields: list):
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
                self.fields = fields
            case _:
                raise Exception # TODO: Add DialogError
        
        self.standard_item = None # QStandardItem in order to be inserted in the model
        self.compute_standard_item()

    def compute_standard_item(self):
        """Update standard item, based on current sentences attributes. """
        self.standard_item = [QStandardItem(field) for field in self.fields] 

    def _get_kanji_readings(self, sentence):
        """Return a dictionnary containg kanji as keys and its reading in kana."""
        pattern = r'\[([^\|\[\]]+)\|([^\[\]]+)\]'
        result = re.findall(pattern, sentence) 
        dict = {}
        for match in result:
                kanji, reading = match
                reading = reading.replace('|', '')
                dict[kanji] = reading
        return dict
    
    def _get_position_kanji(self):
        """Return a dictionnary containing positions as keys, and kanjis as values."""
        kanjis = self.kanji_readings.keys()
        sentence = self.lang_from
        kanjis_sorted = sorted(kanjis, key=len, reverse=True)

        dict = {}
        for word in kanjis_sorted:
            while(sentence.find(word) != -1):
                for i in range(sentence.find(word), sentence.find(word) + len(word)):
                    dict[i] = word
                
                replacement = "_" * len(word)
                sentence = sentence.replace(word, replacement, 1)
        return dict