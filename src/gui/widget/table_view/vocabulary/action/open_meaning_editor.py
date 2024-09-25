from PyQt6.QtGui import QAction, QIcon

class OpenMeaningEditorAction(QAction):
    def __init__(self, parent, table_view) -> None:
        super().__init__(parent)
        self.table_view = table_view
        self.setText("Open Meaning Editor")
        self.setIcon(QIcon("data/icons/editor.png"))
        self.triggered.connect(self._action)

    def _action(self):
        self.table_view._double_clicked()
        