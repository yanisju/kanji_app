from PyQt6.QtGui import QAction, QIcon

class DeleteOneSentenceAction(QAction):
    def __init__(self, parent, card_text_view):
        super().__init__(parent)
        self.card_text_view = card_text_view
        self.setText("Delete Sentence")
        self.setIcon(QIcon("data/icons/minus.png"))

        self.triggered.connect(self._action)

    def _action(self):
        sentence_manager = self.parent().parent().model().sentence_manager
        
        row = self.parent().row 
        sentence = sentence_manager[row]
        sentence_manager.pop(row)
        
        if sentence == self.card_text_view.sentence:
            self.card_text_view.clear()