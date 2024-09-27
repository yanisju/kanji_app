from PyQt6.QtGui import QAction, QIcon

class DeleteOneSentenceAction(QAction):
    def __init__(self, parent):
        super().__init__(parent)
        self.setText("Delete Sentence")
        self.setIcon(QIcon("data/icons/minus.png"))

        self.triggered.connect(self._action)

    def _action(self):
        vocabulary = self.parent().parent().model().vocabulary
        vocabulary.remove_one_sentence(self.parent().row)