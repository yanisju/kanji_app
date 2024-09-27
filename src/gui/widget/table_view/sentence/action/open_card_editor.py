from PyQt6.QtGui import QAction, QIcon

class OpenMeaningEditorAction(QAction):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setText("Open Card Editor")
        self.setIcon(QIcon("data/icons/editor.png"))
        self.triggered.connect(self._action)

    def _action(self):
        self.parent().parent().double_clicked_action()
        