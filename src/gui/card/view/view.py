from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtGui import QFont

from ....vocabulary.sentence import Sentence
from .sentences import *

class CardView(QTextEdit):
    """View of the card in Anki. """

    def __init__(self) -> None:
        super().__init__()
        self.furiganas = dict() # Dictionnary containing kanji and its furigana, updated each time vocabulary field is modified

        self.setReadOnly(True)
        self.setMouseTracking(True)

        stylesheet_location = "src/gui/card/view/stylesheet.css" # TODO: Change as parameter
        with open(stylesheet_location, 'r') as file:
            stylesheet = file.read()
        self.setStyleSheet(stylesheet)

    def get_furigana(self, kanji):
        try:
            return self.furiganas[kanji]
        except:
            pass # TODO: Add ExceptionDialog window

    def mouseMoveEvent(self, event): 
        """Show transcription when mouse howers a kanji. """
        show_transcription(self, event)

    def set_card_view(self, sentence_fields):
        """Set card view, based on vocabulary fields. """
        self.furiganas.clear()

        if isinstance(sentence_fields, Sentence):
            sentence_fields = sentence_fields.fields

        card_text = get_text(self.furiganas, sentence_fields)
        self.setHtml(card_text)

    def refresh_when_double_clicked(self, table_view):
        table_view.clicked.connect(lambda x: self.set_card_view(table_view.model_on.get_sentence_by_row(table_view.currentIndex().row())))