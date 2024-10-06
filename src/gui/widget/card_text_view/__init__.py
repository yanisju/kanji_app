from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtCore import QSize

from ....vocabulary.sentence.sentence import Sentence
from .sentences import *


class CardTextView(QTextEdit):
    """Text view of the card in Anki."""

    def __init__(self, is_main_window: bool) -> None:
        super().__init__()
        self.is_main_window = is_main_window
        self.sentence = None

        self.setReadOnly(True)
        self.setMouseTracking(True)

        stylesheet_location = (
            "src/gui/widget/card_text_view/stylesheet.css"  # TODO: Change as parameter
        )
        with open(stylesheet_location, "r") as file:
            stylesheet = file.read()
        self.setStyleSheet(stylesheet)

    def set_card_view(self, sentence: Sentence, position_kanji: dict, kanji_data: dict):
        """Set card view, based on vocabulary fields."""

        self.sentence = sentence
        self.position_kanji = position_kanji
        self.kanji_data = kanji_data
        self.sentence_attributes = sentence.attributes

        card_text = get_text(self.sentence_attributes)
        self.setHtml(card_text)

    def set_card_view_from_attributes_values(self, attributes_values):
        """Refresh view, based on card fields values."""
        self.attributes_values = attributes_values
        card_text = get_text(attributes_values)
        self.setHtml(card_text)

    def mouseMoveEvent(self, event):
        """Show transcription when mouse howers a kanji."""
        if hasattr(self, "position_kanji") and hasattr(self, "kanji_data"):
            show_transcription(self, event, len(self.sentence_attributes[0]), self.position_kanji, self.kanji_data)
    
    def sizeHint(self):
        return QSize(int(self.parent().width() / 2), int(self.parent().height()))