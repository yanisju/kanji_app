from PyQt6.QtWidgets import QComboBox
from PyQt6.QtCore import QVariant

class VocabularyComboBox(QComboBox):
    """Class defining ComboBox for words in CardDialog."""

    def __init__(self) -> None:
        super().__init__()

    def insert_new(self, kanji_data):
        self.clear()
        sorted_kanji_data = dict(sorted(kanji_data.items(), key=lambda item: item[1][2]))

        for kanji, data in sorted_kanji_data.items():
            text = self.get_text(kanji, data)
            self.addItem(text, QVariant(data))

    def get_text(self, kanji: str, data: tuple):
        _, meaning, row = data
        return f"{row + 1}: {kanji} - {meaning}"
    
    def modify_row(self, row: int, data: tuple):
        kanji, reading, meaning = data
        self.removeItem(row)
        text = self.get_text(kanji, (reading, meaning, row))
        self.insertItem(row, text, QVariant(data))
