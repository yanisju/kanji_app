from PyQt6.QtGui import QAction, QIcon

class AddEmptySentenceAction(QAction):
    def __init__(self, parent, vocabulary_manager):
        super().__init__(parent)
        self.vocabulary_manager = vocabulary_manager
        self.setText("Add Empty Sentence")
        self.setIcon(QIcon("data/icons/plus.png"))

        self.triggered.connect(self._action)

    def _action(self):
        pass