from PyQt6.QtGui import QAction, QIcon

class DeleteVocabularyAction(QAction):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setText("Delete Vocabulary")
        self.setIcon(QIcon("data/icons/minus.png"))

        