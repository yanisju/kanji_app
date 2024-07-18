from PyQt6.QtWidgets import QTableView

class SentenceView(QTableView):
    """List """
    def __init__(self, model, card_dialog, vocabulary_manager):
        super().__init__()
        self.model_on = model
        self.setModel(model)
        
        self.card_dialog = card_dialog
        self.vocabulary_manager = vocabulary_manager

        self.doubleClicked.connect(self.double_clicked_action)
    
    def double_clicked_action(self):
        self.card_dialog.open_card_dialog(self.model_on,
            self.vocabulary_manager.sentence_model.get_sentence_by_row(self.currentIndex().row()), 
                                            self.vocabulary_manager.dictionnary.find_vocabulary_by_word(self.vocabulary_manager.sentence_model.item(self.currentIndex().row(), 3).text()),
                                            self.currentIndex().row())
