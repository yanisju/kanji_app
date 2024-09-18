from PyQt6.QtWidgets import QHBoxLayout, QWidget, QSizePolicy

from ...vocabulary.manager import VocabularyManager

from .table_view.vocabulary import VocabularyTableView
from .table_view.sentence import SentenceTableView

class UpLeftWidget(QWidget):
    """Widget containing vocabulary and sentence table view. """
    def __init__(self, central_widget: QWidget, vocabulary_manager: VocabularyManager, card_text_view):
        super().__init__(central_widget) # Init this widget as a child of central widget
        self.central_widget = central_widget

        policy = QSizePolicy()
        policy.setHorizontalPolicy(QSizePolicy.Policy.MinimumExpanding)
        self.setSizePolicy(policy)
        
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)
        
        self.vocabulary_list_view = VocabularyTableView(vocabulary_manager) # View for retrieved words
        self.layout.addWidget(self.vocabulary_list_view)
        
        self.sentence_view = SentenceTableView(self.central_widget, vocabulary_manager.sentence_model, vocabulary_manager, card_text_view)
        self.sentence_view.configure(card_text_view) 
        self.layout.addWidget(self.sentence_view)
