from PyQt6.QtGui import QAction, QIcon

class AddToVocabularyListAction(QAction):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setText("Add to Vocabulary List")
        self.setIcon(QIcon("data/icons/plus.png"))
        self.triggered.connect(self._action)

    def _action(self):
        word = self.parent().parent().model().item(self.parent().row, 0).text()
        self.parent().parent().parent().parent().vocabulary_manager.add_word(word)