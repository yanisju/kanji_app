from PyQt6.QtWidgets import QWidget, QVBoxLayout, QTableView
from PyQt6.QtCore import QSize
from .sentence_attributes import SentenceAttributesWidget
from .kanji_data_model import KanjiDataModel

from PyQt6.QtWidgets import QHeaderView

class FieldsWidget(QWidget):
    def __init__(self, parent, card_view):
        super().__init__(parent)
        self.card_view = card_view

        self.field_widget_list = []  # All QLineEdit for each fields of the vocabulary.

        self._init_layout()

    def _init_layout(self):
        layout = QVBoxLayout(self)
        self.setLayout(layout)

        self.kanji_data_model = KanjiDataModel()
        self.sentence_attributes_widget = SentenceAttributesWidget(self, self.card_view, self.kanji_data_model)
        layout.addWidget(self.sentence_attributes_widget)

        self.kanji_table_view = QTableView(self)# View containg kanjis and theirs readings + meanings
        self.kanji_table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        
        self.kanji_table_view.setModel(self.kanji_data_model)
        layout.addWidget(self.kanji_table_view)

    def set_to_new_sentence(self, sentence):
        """Fill each fields for the card with the current items."""

        self.sentence_attributes_widget.set_to_new_sentence(sentence)
        self.kanji_data_model.refresh(sentence.kanji_data, self.sentence_attributes_widget.attributes_value[0])

    def sizeHint(self):
        return QSize(int(self.parent().width() / 2), int(self.parent().height() / 2))