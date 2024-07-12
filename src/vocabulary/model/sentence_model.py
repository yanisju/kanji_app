from PyQt6.QtGui import QStandardItemModel

class SentenceModel(QStandardItemModel):
    def __init__(self):
        super().__init__(0,0)
        self.all_item_list = []
        
    def set_sentence_model(self, vocabulary):
        """Modify sentence model based on vocabulary data."""
        self.clear()
        self.all_item_list = []

        for i in range(vocabulary.sentence_count):
            self.insertRow(i, vocabulary.sentences_item[i].list)  
            self.all_item_list.append(vocabulary.sentences_item[i].list)
            
    def get_sentence_model_by_row(self, row):
        return self.all_item_list[row - 1]