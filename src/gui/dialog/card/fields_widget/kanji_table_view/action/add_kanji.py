from PyQt6.QtGui import QAction, QIcon


class AddKanjiAction(QAction):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setText("Add Kanji")
        self.setIcon(QIcon("data/icons/plus.png"))
        self.triggered.connect(self._action)

    def _action(self):
        self.parent().parent().kanji_data.add_empty()
