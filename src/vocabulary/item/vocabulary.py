from PyQt6.QtGui import QStandardItem

class VocabularyItem():
    """Representing a vocabulary in the Vocabulary Model."""

    def __init__(self, word, meaning):
        word_item = QStandardItem(word)
        meaning_item = QStandardItem(meaning)        
        self.list = [word_item, meaning_item]