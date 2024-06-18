from PyQt6.QtWidgets import QHBoxLayout, QWidget
from PyQt6.QtWidgets import QListView

from ..vocabulary.manager import Manager

class UpLeftWidget(QWidget):
    def __init__(self, central_widget: QWidget, vocabulary_manager: Manager):
        super().__init__(central_widget) # Init this widget as a child of central widget
        
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)
        self.vocabulary_manager = vocabulary_manager
        
        self.word_table = QListView() # View for retrieved words / Use vocabulary.manager.vocabulary_model as model
        self.word_table.setModel(self.vocabulary_manager.vocabulary_model)
        
        self.layout.addWidget(self.word_table)
        
        right_table = QListView() # TODO modify
        self.layout.addWidget(right_table)
        
        
        
        