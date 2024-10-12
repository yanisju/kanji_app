from PyQt6.QtGui import QStandardItemModel, QStandardItem
from ...str_utils import *

import PyQt6.QtCore

class KanjiDataModel(QStandardItemModel):
    """Model containg kanjis, theirs readings and theirs meanings for TableView.
    self.kanji_data is a dictionnary containing in real time the data about kanjis: theirs readings / meanings / positions in view.
    """

    def __init__(self):
        super().__init__(0, 3)
        self.modified_rows = dict()

        self._configure()
        

    def _configure(self):
        self.setHeaderData(0, PyQt6.QtCore.Qt.Orientation.Horizontal, "Kanji")
        self.setHeaderData(1, PyQt6.QtCore.Qt.Orientation.Horizontal, "Reading")
        self.setHeaderData(2, PyQt6.QtCore.Qt.Orientation.Horizontal, "Meanings")

    def add_row(self, kanji, reading, meaning):
        self.appendRow([QStandardItem(kanji), QStandardItem(reading), QStandardItem(meaning)])

    def modify_reading_meaning(self, row, reading, meaning):
        kanji = self.item(row, 0).text()
        data = [QStandardItem(kanji), QStandardItem(reading), QStandardItem(meaning)]
        for i in range(3):
            self.setItem(row, i, data[i])

    def get_a_copy(self):
        new_model = KanjiDataModel()
        for row_index in range(self.rowCount()):
            row = [self.item(row_index,c).clone() for c in range(self.columnCount())]
            new_model.appendRow(row)
        return new_model

    def get_all_rows(self):
        l = []
        for row_index in range(self.rowCount()):
            l.append([self.item(row_index,c).text() for c in range(self.columnCount())])
        return l
    
    def remove(self, row):
        self.removeRow(row)

    
    # def refresh(self, kanji_data: dict, sentence: str):
    #     """Refresh model with a new dictionnary containing kanjis data."""
    #     if self.kanji_data != None:  # If model is not empty
    #         self.removeRows(0, self.rowCount())
    #     self.kanji_data = dict(sorted(kanji_data.items(), key=lambda item: item[1][2]))

    #     for kanji in self.kanji_data.keys():
    #         reading, meaning, _ = kanji_data[kanji]
    #         self.appendRow(
                
    #         )

    #     self.sentence = sentence

    #     self.position_kanji_sentence = get_position_kanji_sentence(self.sentence, self.kanji_data.keys())
 

    def set_position_kanji_sentence(self, sentence, kanjis):
        """Modify dictionnary containing positions in sentence as keys, and kanjis as values."""
        kanjis_sorted = sorted(kanjis, key=len, reverse=True)

        self.position_kanji_sentence.clear()
        for word in kanjis_sorted:
            while(sentence.find(word) != -1):
                for i in range(sentence.find(word), sentence.find(word) + len(word)):
                    self.position_kanji_sentence[i] = word
                
                replacement = "_" * len(word)
                sentence = sentence.replace(word, replacement, 1)
