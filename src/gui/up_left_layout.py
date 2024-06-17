from PyQt6.QtWidgets import QHBoxLayout, QWidget
from PyQt6.QtWidgets import QListView
from PyQt6.QtCore import QStringListModel

from ..vocabulary.manager import Manager

class UpLeftLayout(QHBoxLayout):
    def __init__(self, central_widget: QWidget, vocabulary_manager: Manager):
        super().__init__() # Init this widget as a child of central widget
        
        self.word_model = QStringListModel() # Model for retrieved words / How words data is set
        self.word_table = QListView() # View for retrieved words / List
        self.word_table.setModel(self.word_model)
        
        string_test = ["kanji1", "kanji2"] # TODO delete
        self.word_model.setStringList(string_test)
        
        self.addWidget(self.word_table)
        
        right_table = QListView() # TODO modify
        self.addWidget(right_table)
        
        
        