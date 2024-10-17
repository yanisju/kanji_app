from PyQt6.QtGui import QAction, QIcon

class DeleteOneKanjiAction(QAction):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setText("Delete Kanji")
        self.setIcon(QIcon("data/icons/minus.png"))
        self.triggered.connect(self._action)

    def _action(self):
        self.parent().parent().kanji_data.remove_by_row(self.parent().row)
        self.parent().parent().parent().sentence_attributes_widget.word1_combobox.delete_row(self.parent().row)
        self.parent().parent().parent().sentence_attributes_widget.word2_combobox.delete_row(self.parent().row)