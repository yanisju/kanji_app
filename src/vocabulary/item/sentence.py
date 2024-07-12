from PyQt6.QtGui import QStandardItem

class SentenceItem():
    """Representing a line of items in the Sentence Model."""

    def __init__(self, lang_from, lang_to, transcription, word, meaning):
        lang_from_item = QStandardItem(lang_from)
        lang_to_item = QStandardItem(lang_to)
        transcription_item = QStandardItem(transcription)
        word1 = QStandardItem(word)
        word1_meaning = QStandardItem(meaning)
        self.list = [lang_from_item, lang_to_item, transcription_item, word1, word1_meaning]