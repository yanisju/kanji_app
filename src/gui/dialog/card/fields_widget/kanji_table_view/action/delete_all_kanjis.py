from PyQt6.QtGui import QAction, QIcon

class DeleteAllKanjisAction(QAction):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setText("Delete All Kanjis")
        self.setIcon(QIcon("data/icons/trashbin.png"))
        self.triggered.connect(self._action)

    def _action(self):
        self.parent().parent().kanji_data.clear()
        self.parent().parent().parent().sentence_attributes_widget.word1_combobox.clear()
        self.parent().parent().parent().sentence_attributes_widget.word2_combobox.clear()