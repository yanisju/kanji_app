from PyQt6.QtGui import QAction, QIcon

class DeleteAllSentenceAction(QAction):
    def __init__(self, parent, card_text_view):
        super().__init__(parent)
        self.card_text_view = card_text_view
        self.setText("Delete all Sentences")
        self.setIcon(QIcon("data/icons/trashbin.png"))

        self.triggered.connect(self._action)

    def _action(self):
        sentence_manager = self.parent().parent().model().sentence_manager

        if self.card_text_view.sentence in sentence_manager:
            self.card_text_view.clear()
        sentence_manager.clear()