from PyQt6.QtGui import QStandardItemModel
import PyQt6.QtCore

class VocabularyModel(QStandardItemModel):
    def __init__(self):
        super().__init__(0,4)
        self._configure()

    def _configure(self):
        self.setHeaderData(0, PyQt6.QtCore.Qt.Orientation.Horizontal, "Word")
        self.setHeaderData(1, PyQt6.QtCore.Qt.Orientation.Horizontal, "Meanings")
        self.setHeaderData(2, PyQt6.QtCore.Qt.Orientation.Horizontal, "Parts of Speech")
        self.setHeaderData(3, PyQt6.QtCore.Qt.Orientation.Horizontal, "Sentences Count")

    def modify_row(self, row_index: int, standard_item):
        for column_index in range(self.columnCount()):
            self.setItem(row_index, column_index, standard_item[column_index])

    def append_vocabulary(self, word, item):
        self.appendRow(item)
        self.setHeaderData(self.rowCount() - 1, PyQt6.QtCore.Qt.Orientation.Vertical, word)