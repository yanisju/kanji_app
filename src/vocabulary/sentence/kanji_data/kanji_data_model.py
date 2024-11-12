from PyQt6.QtGui import QStandardItemModel, QStandardItem
from ...str_utils import *

import PyQt6.QtCore

class KanjiDataModel(QStandardItemModel):
    """Model containg kanjis, theirs readings and theirs meanings for TableView.
    self.kanji_data is a dictionnary containing in real time the data about kanjis: theirs readings / meanings / positions in view.
    """

    def __init__(self, kanji_data):
        super().__init__(0, 3)
        self.kanji_data = kanji_data
        self.modified_rows = dict()
        self._configure()
        

    def _configure(self):
        self.setColumnCount(3)
        self.setHeaderData(0, PyQt6.QtCore.Qt.Orientation.Horizontal, "Kanji")
        self.setHeaderData(1, PyQt6.QtCore.Qt.Orientation.Horizontal, "Reading")
        self.setHeaderData(2, PyQt6.QtCore.Qt.Orientation.Horizontal, "Meanings")

    def add_row(self, kanji):
        self.appendRow(kanji.get_item())

    def modify_row(self, row, kanji):
        item = kanji.get_item()
        for i in range(len(item)):
            self.setItem(row, i, item[i])

    def modify_reading_meaning(self, row, reading, meaning):
        kanji = self.item(row, 0).text()
        data = [QStandardItem(kanji), QStandardItem(reading), QStandardItem(meaning)]
        for i in range(3):
            self.setItem(row, i, data[i])

    def get_a_copy(self, kanji_data):
        new_model = KanjiDataModel(kanji_data)
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
    
    def clear(self):
        super().clear()
        self._configure()

    def set_position_kanji_sentence(self, sentence, kanjis):
        kanjis_sorted = sorted(kanjis, key=len, reverse=True)

        self.position_kanji_sentence.clear()
        for word in kanjis_sorted:
            while(sentence.find(word) != -1):
                for i in range(sentence.find(word), sentence.find(word) + len(word)):
                    self.position_kanji_sentence[i] = word
                
                replacement = "_" * len(word)
                sentence = sentence.replace(word, replacement, 1)
