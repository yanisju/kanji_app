from PyQt6.QtGui import QStandardItemModel
import PyQt6.QtCore

class VocabularyModel(QStandardItemModel):
    def __init__(self):
        super().__init__(0,3)
        self._configure()

    def _configure(self):
        self.setHeaderData(0, PyQt6.QtCore.Qt.Orientation.Horizontal, "Word")
        self.setHeaderData(1, PyQt6.QtCore.Qt.Orientation.Horizontal, "Meanings")
        self.setHeaderData(2, PyQt6.QtCore.Qt.Orientation.Horizontal, "Parts of Speech")

    def modify_row(self, row_index: int, new_meaning, new_part_of_speech):
        self.setData(self.index(row_index, 1), new_meaning)
        self.setData(self.index(row_index, 2), new_part_of_speech)

    def append_vocabulary(self, word, item):
        self.appendRow(item)
        self.setHeaderData(self.rowCount() - 1, PyQt6.QtCore.Qt.Orientation.Vertical, word)