from PyQt6.QtWidgets import QHBoxLayout, QWidget
from PyQt6.QtWidgets import QListView, QTableView

from ..vocabulary.manager import Manager

class UpLeftWidget(QWidget):
    def __init__(self, central_widget: QWidget, vocabulary_manager: Manager):
        super().__init__(central_widget) # Init this widget as a child of central widget
        
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)
        self.vocabulary_manager = vocabulary_manager
        
        self.vocabulary_list_view = self._configure_vocabulary_list_view() # View for retrieved words
        self.layout.addWidget(self.vocabulary_list_view)
        
        self.sentence_table_view = self._configure_sentence_table_view()
        self.layout.addWidget(self.sentence_table_view)
    
    def refresh_sentence_view(self, word):
        self.sentence_table_view.setModel(self.vocabulary_manager.sentence_model)

    def _configure_vocabulary_list_view(self):
        """ Initialize word view and set up signals. """
        view = QTableView()
        view.setModel(self.vocabulary_manager.vocabulary_model) # Use vocabulary.manager.vocabulary_model as model
        view_item_selection = view.selectionModel()
        view_item_selection.selectionChanged.connect(lambda x: self.vocabulary_manager.refresh_sentence_model(view.currentIndex().data())) # Change sentences view to current word
        return view
            
    
    def _configure_sentence_table_view(self):
        view = QTableView() 
        view.setModel(self.vocabulary_manager.sentence_model)
        
        return view
        