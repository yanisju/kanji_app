from PyQt6.QtGui import QStandardItemModel, QStandardItem

class SentenceModel(QStandardItemModel):
    def __init__(self):
        super().__init__(0,0)
        self.all_item_list = []
        
    def set_sentence_model(self, vocabulary):
        """Modify sentence model based on vocabulary data."""
        self.clear()
        self.all_item_list = []
        
        for i in range(vocabulary.sentence_count):
            lang_from_sentence_item = QStandardItem(vocabulary.lang_from_sentence[i])
            lang_to_sentence_item = QStandardItem(vocabulary.lang_to_sentence[i])
            sentence_anki_format_item = QStandardItem(vocabulary.sentence_anki_format[i])
            word1 = QStandardItem(vocabulary.word)
            word1_meaning = QStandardItem(vocabulary.meaning_str)
            item_list = [lang_from_sentence_item, lang_to_sentence_item, sentence_anki_format_item, word1, word1_meaning]
            self.insertRow(i, item_list)  
            
            self.all_item_list.append(item_list)
            
    def get_sentence_model_by_row(self, row):
        return self.all_item_list[row - 1]