from PyQt6.QtWidgets import QWidget, QVBoxLayout
from PyQt6.QtCore import QSize
from .sentence_attributes import SentenceAttributesWidget
from .kanji_table_view import KanjiTableView

class FieldsWidget(QWidget):
    def __init__(self, parent, card_view):
        super().__init__(parent)
        self.card_view = card_view

        self.field_widget_list = []  # All QLineEdit for each fields of the vocabulary.

        self._init_layout()

    def _init_layout(self):
        layout = QVBoxLayout(self)
        self.setLayout(layout)

        self.sentence_attributes_widget = SentenceAttributesWidget(self, self.card_view)
        layout.addWidget(self.sentence_attributes_widget)

        self.kanji_table_view = KanjiTableView(self)# View containg kanjis and theirs readings + meanings
        layout.addWidget(self.kanji_table_view)

    def set_to_new_sentence(self, sentence):
        """Fill each fields for the card with the current items."""
        self.kanji_table_view.setModel(sentence.kanji_data.model)
        self.sentence_attributes_widget.set_to_new_sentence(sentence)

    def sizeHint(self):
        return QSize(int(self.parent().width() / 2), int(self.parent().height()))