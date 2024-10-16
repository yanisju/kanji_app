from PyQt6.QtWidgets import QComboBox
from PyQt6.QtCore import QVariant

class VocabularyComboBox(QComboBox):
    """Class defining ComboBox for words in CardDialog."""

    def __init__(self, add_empty_value) -> None:
        super().__init__()
        self.add_empty_value = add_empty_value

    def set_kanji_data_model(self, kanji_data_model):
        if hasattr(self, "kanji_data_model"):
            kanji_data_model.itemChanged.disconnect(self.is_kanji_data_model_modified)
        kanji_data_model.itemChanged.connect(self.is_kanji_data_model_modified)

    def insert_new(self, kanji_data):
        self.clear()
        # sorted_kanji_data = sorted(kanji_data, key=lambda item: item[3])

        index = 0
        for data in kanji_data:
            self.add_row(data, index)
            index += 1
        if self.add_empty_value:
            self._add_empty_value()
    
    def add_row(self, data, index):
        text = self.get_text(data, index)
        self.addItem(text, QVariant(data))

    def add_empty_row(self):
        data = ("", "", "")
        if self.add_empty_value:
            self.removeItem(self.count() - 1)
            self.add_row(data, self.count())
            self._add_empty_value()
        else:
            self.add_row(data, self.count())


    def get_text(self, data: tuple, row):
        kanji, _, meaning = data
        return f"{row + 1}: {kanji} - {meaning}"
    
    def modify_row(self, row: int, column: int, item_modified):
        data = self.itemData(row)
        if column == 0 or column == 2:
            if column == 0: # Kanji modified
                _, reading, meaning = data
                kanji = item_modified.text()
            elif column == 2: # Meaning modified
                kanji, reading, *_ = data
                meaning = item_modified.text()
        else: # Reading modified
            kanji, _, meaning = data
            reading = item_modified.text()
        
        data = (kanji, reading, meaning)
        text = self.get_text(data, row)
        self.removeItem(row)
        self.insertItem(row, text, QVariant(data))

    def is_kanji_data_model_modified(self, item):
        index_row, index_column = item.row(), item.column()
        previous_index = self.currentIndex()
        self.modify_row(index_row, index_column, item)
        if previous_index == index_row:
            self.setCurrentIndex(index_row)
        
    def _add_empty_value(self):
        self.addItem("None", None)

    def set_to_empty_value(self):
        self.setCurrentIndex(self.count() - 1)

    def clear(self):
        super().clear()
        if self.add_empty_value:
            self._add_empty_value()