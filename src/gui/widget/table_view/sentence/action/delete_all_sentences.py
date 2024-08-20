from PyQt6.QtGui import QAction, QIcon

class DeleteAllSentenceAction(QAction):
    def __init__(self, parent):
        super().__init__(parent)
        self.setText("Delete all Sentences")
        self.setIcon(QIcon("data/icons/trashbin.png"))