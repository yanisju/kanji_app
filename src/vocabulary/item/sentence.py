from PyQt6.QtGui import QStandardItem

class SentenceItem():
    """Representing a line of items in the Sentence Model."""

    def __init__(self, lang_from, lang_to, transcription, word, meaning):
        lang_from_item = QStandardItem(lang_from)
        lang_to_item = QStandardItem(lang_to)
        transcription_item = QStandardItem(transcription)
        word1 = QStandardItem(word)
        word1_meaning = QStandardItem(meaning)
        word2 = QStandardItem("")
        word2_meaning = QStandardItem("")
        self.list = [lang_from_item, lang_to_item, transcription_item, word1, word1_meaning, word2, word2_meaning]

    def set_list(self, new_list):
        self.list = new_list
        pass