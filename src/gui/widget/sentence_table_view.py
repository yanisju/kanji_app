from PyQt6.QtWidgets import QTableView

from ..card.dialog import CardDialog

class SentenceTableView(QTableView):
    """Table view for the different sentences of one vocabulary."""
    
    def __init__(self, model, vocabulary_manager):
        super().__init__()
        self.model_on = model
        self.setModel(model)
        
        self.vocabulary_manager = vocabulary_manager

        self.doubleClicked.connect(self.double_clicked_action)
    
    def double_clicked_action(self):
        """When a sentence is double-clicked, opens a new CardDialog to edit its fields."""
        row = self.currentIndex().row()
        sentence = self.vocabulary_manager.sentence_model.get_sentence_by_row(row)
        vocabulary = self.vocabulary_manager.dictionnary.find_vocabulary_by_word(self.vocabulary_manager.sentence_model.item(row, 2).text())

        card_dialog = CardDialog(None, None, self.model_on, sentence, vocabulary, row)
        card_dialog.open()
