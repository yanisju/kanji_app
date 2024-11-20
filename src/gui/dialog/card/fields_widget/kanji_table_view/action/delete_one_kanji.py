from PyQt6.QtGui import QAction, QIcon

class DeleteOneKanjiAction(QAction):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setText("Delete Kanji")
        self.setIcon(QIcon("data/icons/minus.png"))
        self.triggered.connect(self._action)

    def _action(self):
        for row, _ in reversed(self.parent().rows_columns):
            self.parent().parent().kanji_data.remove_by_row(row)