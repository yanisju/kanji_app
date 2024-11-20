from PyQt6.QtWidgets import QComboBox


class VocabularyComboBox(QComboBox):
    """Class defining ComboBox for words in CardDialog."""

    def __init__(self) -> None:
        super().__init__()

    def set_kanji_data_model(self, kanji_data_model):
        self.setModel(kanji_data_model)

    def set_to_empty_value(self):
        self.setCurrentIndex(self.count() - 1)

    def hide_and_change_index(self, index):
        view = self.view()
        for row in range(self.count()):
            view.setRowHidden(row, False)
        view.setRowHidden(index, True)
        if self.currentIndex() == index:
            self.set_to_empty_value()
