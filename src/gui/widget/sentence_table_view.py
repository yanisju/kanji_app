from PyQt6.QtWidgets import QTableView

from ..card.dialog import CardDialog

class SentenceTableView(QTableView):
    """Table view for the different sentences of one vocabulary."""
    
    def __init__(self, central_widget, model, vocabulary_manager):
        super().__init__(central_widget)
        self.central_widget = central_widget
        self.model_on = model
        self.setModel(model)
        
        self.vocabulary_manager = vocabulary_manager

        self.doubleClicked.connect(self.double_clicked_action)

    def configure(self, card_text_view):
        """Configure sentence table view, to display sentence text view when a line is clicked."""
        self.clicked.connect(
            lambda x: card_text_view.set_card_view(
                self.model_on.get_sentence_by_row(self.currentIndex().row()),
                self.model_on.get_sentence_by_row(self.currentIndex().row()).position_kanji_sentence,
                self.model_on.get_sentence_by_row(self.currentIndex().row()).kanji_data
            )
        )
    
    def double_clicked_action(self):
        """When a sentence is double-clicked, opens a new CardDialog to edit its fields."""
        row = self.currentIndex().row()
        sentence = self.model_on.get_sentence_by_row(row)
        vocabulary = self.vocabulary_manager.dictionnary.find_vocabulary_by_word(self.vocabulary_manager.sentence_model.item(row, 2).text())

        card_dialog = CardDialog(self.central_widget, None, self.model_on, sentence, vocabulary, row)
        card_dialog.open()
