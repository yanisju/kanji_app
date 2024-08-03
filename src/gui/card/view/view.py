from PyQt6.QtWidgets import QTextEdit

from ....vocabulary.sentence.sentence import Sentence
from .sentences import *


class CardView(QTextEdit):
    """Text view of the card in Anki."""

    def __init__(self) -> None:
        super().__init__()

        self.setReadOnly(True)
        self.setMouseTracking(True)

        stylesheet_location = (
            "src/gui/card/view/stylesheet.css"  # TODO: Change as parameter
        )
        with open(stylesheet_location, "r") as file:
            stylesheet = file.read()
        self.setStyleSheet(stylesheet)


    def set_card_view(self, sentence: Sentence, position_kanji: dict, kanji_data: dict):
        """Set card view, based on vocabulary fields."""
        pass

        self.sentence = sentence
        self.position_kanji = position_kanji
        self.kanji_data = kanji_data
        self.sentence_fields = sentence.fields

        card_text = get_text(self.sentence_fields)
        self.setHtml(card_text)

    def refresh_view(self, fields_values):
        """Refresh view, based on card fields values."""
        self.sentence_fields = fields_values
        card_text = get_text(fields_values)
        self.setHtml(card_text)

    def refresh_when_clicked(self, table_view):
        """When Sentence TableView is clicked, refresh the line."""

        table_view.clicked.connect(
            lambda x: self.set_card_view(
                table_view.model_on.get_sentence_by_row(table_view.currentIndex().row()),
                table_view.model_on.get_sentence_by_row(table_view.currentIndex().row()).position_kanji_sentence,
                table_view.model_on.get_sentence_by_row(table_view.currentIndex().row()).kanji_data
            )
        )
        # TODO: put it in table_view

    def mouseMoveEvent(self, event):
        """Show transcription when mouse howers a kanji."""
        if hasattr(self, "position_kanji") and hasattr(self, "kanji_data"):
            
            show_transcription(self, event, len(self.sentence_fields[0]), self.position_kanji, self.kanji_data)
