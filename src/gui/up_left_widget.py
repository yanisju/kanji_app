from PyQt6.QtWidgets import QHBoxLayout, QWidget
from PyQt6.QtWidgets import QListView, QTableView

from ..vocabulary.manager import Manager

class UpLeftWidget(QWidget):
    def __init__(self, central_widget: QWidget, vocabulary_manager: Manager):
        super().__init__(central_widget) # Init this widget as a child of central widget
        
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)
        self.vocabulary_manager = vocabulary_manager
        
        self.vocabulary_list_view = QListView() # View for retrieved words / Use vocabulary.manager.vocabulary_model as model
        self.vocabulary_list_view.setModel(self.vocabulary_manager.vocabulary_model)
        self.layout.addWidget(self.vocabulary_list_view)
        
        self.sentence_table_view = QTableView() 
        self.sentence_table_view.setModel(self.vocabulary_manager.sentence_model)
        self.layout.addWidget(self.sentence_table_view)
    
    def refresh_sentence_view(self, word):
        self.vocabulary_manager.refresh_sentence_model(word)
        self.sentence_table_view.setModel(self.vocabulary_manager.sentence_model)
        
        