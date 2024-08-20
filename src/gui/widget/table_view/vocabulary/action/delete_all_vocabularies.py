from PyQt6.QtGui import QAction, QIcon

class DeleteAllVocabulariesAction(QAction):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setText("Delete all Vocabularies")
        self.setIcon(QIcon("data/icons/trashbin.png"))

        