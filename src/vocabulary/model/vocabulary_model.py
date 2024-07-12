from PyQt6.QtGui import QStandardItemModel, QStandardItem

class VocabularyModel(QStandardItemModel):
    """ Model for retrieved word from the user. 
    Since it will be used with a QListView, it inherits from QStandardItemModel"""
    
    def __init__(self):
        super().__init__(0,0)
    
    def add_vocabulary(self, vocabulary):
        """ Add a vocabulary to the model."""
        
        self.appendRow(vocabulary.item.list)  
        