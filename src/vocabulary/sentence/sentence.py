from PyQt6.QtGui import QStandardItem
from .kanji_model import KanjiModel
import re

class Sentence():
    def __init__(self, lang_from, translation, transcription, word1, meaning1):
        self.update_attributes([lang_from, translation, word1, meaning1])
        self.kanji_data = self._get_kanji_data(transcription) # Dictionnary containing kanji and theirs readings.
        self.position_kanji_sentence = self._get_position_kanji_sentence() # Dict containg positions in text as keys and kanjis as values.
        self.kanji_model = KanjiModel(self.kanji_data)

        self.kanji_model.itemChanged.connect(self._is_sentence_model_changed)

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

    def _get_kanji_data(self, sentence):
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
    
    def _get_position_kanji_sentence(self):
        """Return a dictionnary containing positions in sentence as keys, and kanjis as values."""
        kanjis = self.kanji_data.keys()
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
    
    def _is_sentence_model_changed(self, item):
        index = self.kanji_model.indexFromItem(item)
        if index.column() != 0: # If reading or meaning is modified
            kanji = self.kanji_model.item(index.row(), 0).text()
            
            if index.column() == 1:
                self.kanji_data[kanji] = (item.text(), self.kanji_data[kanji][1],index.row())
            else: # Modify meaning / index.column == 2
                self.kanji_data[kanji] = (self.kanji_data[kanji][0], item.text(), index.row())
        else: # If kanji is modified
            kanji_to_del = [item for item, v in self.kanji_data.items() if v[2] == index.row()]
            self.kanji_data[item.text()] = self.kanji_data[kanji_to_del[0]]
            del self.kanji_data[kanji_to_del[0]]
        
        self.position_kanji_sentence = self._get_position_kanji_sentence()