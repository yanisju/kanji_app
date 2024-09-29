from PyQt6.QtWidgets import QComboBox
from PyQt6.QtCore import QVariant

class VocabularyComboBox(QComboBox):
    """Class defining ComboBox for words in CardDialog."""

    def __init__(self, add_empty_value, kanji_data_model) -> None:
        super().__init__()
        self.add_empty_value = add_empty_value
        kanji_data_model.itemChanged.connect(self.is_kanji_data_model_modified)

    def insert_new(self, kanji_data):
        self.clear()
        sorted_kanji_data = dict(sorted(kanji_data.items(), key=lambda item: item[1][2]))

        for kanji, data in sorted_kanji_data.items():
            text = self.get_text(kanji, data)
            data = (kanji,) + data
            self.addItem(text, QVariant(data))
        if self.add_empty_value:
            self._add_empty_value()

    def get_text(self, kanji: str, data: tuple):
        _, meaning, row = data
        return f"{row + 1}: {kanji} - {meaning}"
    
    def modify_row(self, row: int, colomn: int, item_modified):
        data = self.itemData(row)
        if colomn == 0 or colomn == 2:
            if colomn == 0: # Kanji modified
                _, reading, meaning, _ = data
                kanji = item_modified.text()
            elif colomn == 2: # Meaning modified
                kanji, reading, *_ = data
                meaning = item_modified.text()
        else: # Reading modified
            kanji, _, meaning, _ = data
            reading = item_modified.text()
        
        text = self.get_text(kanji, (reading, meaning, row))
        self.removeItem(row)
        data = (kanji,reading, meaning, row)
        self.insertItem(row, text, QVariant(data))

    def is_kanji_data_model_modified(self, item):
        index_row, index_colomn = item.row(), item.column()
        previous_index = self.currentIndex()
        self.modify_row(index_row, index_colomn, item)

        if previous_index == index_row:
            self.setCurrentIndex(index_row)

    def _add_empty_value(self):
        self.addItem("None", None)

    def set_to_empty_value(self):
        self.setCurrentIndex(self.count() - 1)