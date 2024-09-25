from PyQt6.QtGui import QAction, QIcon

class DeleteAllVocabulariesAction(QAction):
    def __init__(self, parent, vocabulary_manager) -> None:
        super().__init__(parent)
        self.vocabulary_manager = vocabulary_manager
        self.setText("Delete all Vocabularies")
        self.setIcon(QIcon("data/icons/trashbin.png"))
        self.triggered.connect(self._action)

    def _action(self):
        self.vocabulary_manager.delete_all_vocabularies()

        