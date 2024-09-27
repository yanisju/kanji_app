from PyQt6.QtGui import QAction, QIcon

class DeleteAllSentenceAction(QAction):
    def __init__(self, parent):
        super().__init__(parent)
        self.setText("Delete all Sentences")
        self.setIcon(QIcon("data/icons/trashbin.png"))

        self.triggered.connect(self._action)

    def _action(self):
        vocabulary = self.parent().parent().model().vocabulary
        vocabulary.remove_all_sentence()