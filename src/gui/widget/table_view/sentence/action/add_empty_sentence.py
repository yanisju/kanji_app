from PyQt6.QtGui import QAction, QIcon

class AddEmptySentenceAction(QAction):
    def __init__(self, parent):
        super().__init__(parent)
        self.setText("Add Empty Sentence")
        self.setIcon(QIcon("data/icons/plus.png"))