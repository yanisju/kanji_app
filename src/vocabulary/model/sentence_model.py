# TODO Need to think if QAbstractTableModel or QStandardItemModel

from PyQt6.QtGui import QStandardItemModel, QStandardItem

class SentenceModel(QStandardItemModel):
    def __init__(self):
        super().__init__(0,0)
        
    def set_sentence_model(self, vocabulary):
        """Modify sentence model based on vocabulary data."""
        
        self.clear()
        for i in range(vocabulary.sentence_count):
            lang_from_sentence_item = QStandardItem(vocabulary.lang_from_sentence[i])
            lang_to_sentence_item = QStandardItem(vocabulary.lang_to_sentence[i])
            sentence_transcription_item = QStandardItem(vocabulary.sentence_transcription[i])
            item_list = [lang_from_sentence_item, lang_to_sentence_item, sentence_transcription_item]
            self.insertRow(i, item_list)  