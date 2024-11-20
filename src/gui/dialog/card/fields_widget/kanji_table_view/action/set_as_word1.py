from PyQt6.QtGui import QAction, QIcon


class SetAsWord1Action(QAction):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setText("Set as Word 1")
        self.setIcon(QIcon("data/icons/gear.png"))
        self.triggered.connect(self._action)

    def _action(self):
        row, _ = self.parent().rows_columns[0]
        self.parent().parent().parent(
        ).sentence_attributes_widget.word1_combobox.setCurrentIndex(row)
