from PyQt6.QtGui import QStandardItem
import re

class Sentence():
    def __init__(self, lang_from, translation, transcription, word1, meaning1):
        self.update_attributes([lang_from, translation, word1, meaning1])
        self.kanji_readings = self._get_kanji_readings(transcription) # Dictionnary containing kanji and theirs readings.

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
        """Return a dictionnary containg kanji and its reading in kana."""
        pattern = r'\[([^\|\[\]]+)\|([^\[\]]+)\]'
        result = re.findall(pattern, sentence) 
        dict = {}
        for match in result:
                kanji, reading = match
                reading = reading.replace('|', '')
                dict[kanji] = reading
        return dict