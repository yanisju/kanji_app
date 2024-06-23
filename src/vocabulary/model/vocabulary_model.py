from PyQt6.QtCore import QStringListModel  

class VocabularyModel(QStringListModel):
    """ Model for retrieved word from the user. 
    Since it will be used with a QListView, it inherits from QStringListModel"""
    
    def __init__(self):
        super().__init__()
        self.count = 0
    
    def refresh_model(self, words):
        """ Refresh view for the word view."""
        self.setStringList(words)