from PyQt6.QtGui import QAction, QIcon

class DeleteVocabularyAction(QAction):
    def __init__(self, parent, vocabulary_manager) -> None:
        super().__init__(parent)
        self.vocabulary_manager = vocabulary_manager
        self.setText("Delete Vocabulary")
        self.setIcon(QIcon("data/icons/minus.png"))
        self.triggered.connect(self._action)

    def _action(self):
        self.vocabulary_manager.delete_vocabulary(self.parent().row)
        