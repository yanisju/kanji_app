from PyQt6.QtGui import QAction, QIcon


class SetAsWord2Action(QAction):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setText("Set as Word 2")
        self.setIcon(QIcon("data/icons/gear.png"))
        self.triggered.connect(self._action)

    def _action(self):
        row, _ = self.parent().rows_columns[0]
        self.parent().parent().parent(
        ).sentence_attributes_widget.word2_combobox.setCurrentIndex(row)
