from PyQt6.QtWidgets import QHBoxLayout, QWidget
from PyQt6.QtWidgets import QTableView

from ...vocabulary.manager import VocabularyManager

from .sentence_table_view import SentenceTableView

class UpLeftWidget(QWidget):
    """Widget containing vocabulary and sentence table view. """
    def __init__(self, central_widget: QWidget, vocabulary_manager: VocabularyManager, card_text_view):
        super().__init__(central_widget) # Init this widget as a child of central widget
        self.central_widget = central_widget
        
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)
        self.vocabulary_manager = vocabulary_manager
        
        self.vocabulary_list_view = self._configure_vocabulary_list_view() # View for retrieved words
        self.layout.addWidget(self.vocabulary_list_view)
        
        self.sentence_view = SentenceTableView(self.central_widget, self.vocabulary_manager.sentence_model, vocabulary_manager)
        self.sentence_view.configure(card_text_view) 
        self.layout.addWidget(self.sentence_view)

    def _configure_vocabulary_list_view(self):
        """ Initialize word view and set up signals. """
        view = QTableView()
        view.setModel(self.vocabulary_manager.vocabulary_model) # Use vocabulary.manager.vocabulary_model as model
        view_item_selection = view.selectionModel()
    
        view_item_selection.selectionChanged.connect(lambda x: self.vocabulary_manager.refresh_sentence_model(view.currentIndex().row())) # Change sentences view to current word
        view_item_selection.selectionChanged.connect(lambda x: self.vocabulary_manager.refresh_sentence_model(view.currentIndex().row()))

        return view