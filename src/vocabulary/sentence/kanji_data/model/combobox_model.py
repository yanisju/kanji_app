from PyQt6.QtGui import QStandardItemModel, QStandardItem
from ..kanji_data import KanjiData

from .....constants import KanjiDataComboBoxModelMode

class KanjiDataComboBoxModel(QStandardItemModel):
    def __init__(self, mode):
        super().__init__()
        self.mode = mode
        if mode == KanjiDataComboBoxModelMode.SECOND_COMBO_BOX:
            self._add_empty_value()

    def _add_empty_value(self):
        super().appendRow(QStandardItem("None"))

    def _get_text(self, row: int, kanji_data: KanjiData):
        text = f"{row + 1}: {kanji_data.word} - {kanji_data.meaning}"
        return text
    
    def appendRowText(self, text: str):
        if self.mode == KanjiDataComboBoxModelMode.FIRST_COMBO_BOX:
            row = self.rowCount()
        else:
            row = self.rowCount() - 1
        super().insertRow(row, QStandardItem(text))
    
    def insertRow(self, row: int,  kanji_data: KanjiData):
        text = self._get_text(row, kanji_data)
        item_to_insert = QStandardItem(text)
        super().insertRow(row, item_to_insert)

    def appendRow(self, kanji_data: KanjiData):
        if self.mode == KanjiDataComboBoxModelMode.FIRST_COMBO_BOX:
            row = self.rowCount()
        else:
            row = self.rowCount() - 1
        self.insertRow(row, kanji_data)

    def append_empty_row(self):
        empty_kanji_data = KanjiData("", "", "")
        self.appendRow(empty_kanji_data)

    def modify_row(self, row: int, kanji_data: KanjiData):
        text = self._get_text(row, kanji_data)
        self.setItem(row, QStandardItem(text))

    def clear(self):
        super().clear()
        if self.mode == KanjiDataComboBoxModelMode.SECOND_COMBO_BOX:
            self._add_empty_value()

    def clone(self):
        new_model = KanjiDataComboBoxModel(self.mode)
        if self.mode == KanjiDataComboBoxModelMode.FIRST_COMBO_BOX:
            row_count = self.rowCount()
        else:
            row_count = self.rowCount() - 1
        for row in range(row_count):
            text = self.item(row, 0).text()
            new_model.appendRowText(text)
        return new_model

    def actualize_items_text(self):
        for i in range(self.rowCount()):
            item = self.item(i)
            if item:  
                text = item.text()
                if ": " in text:
                    _, string_part = text.split(": ", 1)
                    item.setText(f"{i + 1}: {string_part}")



        
    