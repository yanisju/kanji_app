from PyQt6.QtGui import QStandardItemModel, QStandardItem

class VocabularyModel(QStandardItemModel):
    """ Model for retrieved word from the user. 
    Since it will be used with a QListView, it inherits from QStandardItemModel"""
    
    def __init__(self):
        super().__init__(0,0)
    
    def add_vocabulary(self, vocabulary):
        """ Add a vocabulary to the model."""
        word_item = QStandardItem(vocabulary.word)
        meaning_item = QStandardItem(vocabulary.meaning_str)        
        item_list = [word_item, meaning_item]
        self.appendRow(item_list)  
        