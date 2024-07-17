from PyQt6.QtWidgets import QHBoxLayout, QWidget
from PyQt6.QtWidgets import QTableView

from ..vocabulary.manager import VocabularyManager
from .card.dialog import CardDialog

class UpLeftWidget(QWidget):
    def __init__(self, central_widget: QWidget, vocabulary_manager: VocabularyManager):
        super().__init__(central_widget) # Init this widget as a child of central widget
        self.central_widget = central_widget
        
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)
        self.vocabulary_manager = vocabulary_manager
        
        self.vocabulary_list_view = self._configure_vocabulary_list_view() # View for retrieved words
        self.layout.addWidget(self.vocabulary_list_view)
        
        self.sentence_table_view = self._configure_sentence_table_view()
        self.layout.addWidget(self.sentence_table_view)
    
    def _configure_vocabulary_list_view(self):
        """ Initialize word view and set up signals. """
        view = QTableView()
        view.setModel(self.vocabulary_manager.vocabulary_model) # Use vocabulary.manager.vocabulary_model as model
        view_item_selection = view.selectionModel()
    
        view_item_selection.selectionChanged.connect(lambda x: self.vocabulary_manager.refresh_sentence_model(view.currentIndex().row())) # Change sentences view to current word
        return view
    
    def _configure_sentence_table_view(self):
        view = QTableView() 
        view.setModel(self.vocabulary_manager.sentence_model)
        
        card_dialog = CardDialog(self.central_widget, self.vocabulary_manager)

        
        view.doubleClicked.connect(lambda x: card_dialog.open_card_dialog(self.vocabulary_manager.sentence_model.get_sentence_item_by_row(view.currentIndex().row()), 
                                                                          self.vocabulary_manager.dictionnary.find_vocabulary_by_word(self.vocabulary_manager.sentence_model.item(view.currentIndex().row(), 3).text()),
                                                                          view.currentIndex().row())) # 
        
        return view
        