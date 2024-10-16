from PyQt6.QtGui import QAction, QIcon

class AddKanjiAction(QAction):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setText("Add Kanji")
        self.setIcon(QIcon("data/icons/plus.png"))
        self.triggered.connect(self._action)

    def _action(self):
        self.parent().parent().kanji_data.add_empty()
        self.parent().parent().parent().sentence_attributes_widget.word1_combobox.add_empty_row()
        self.parent().parent().parent().sentence_attributes_widget.word2_combobox.add_empty_row()