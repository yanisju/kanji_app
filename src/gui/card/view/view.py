from PyQt6.QtWidgets import QTextEdit

from ....vocabulary.sentence.sentence import Sentence
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

    def set_card_view(self, sentence_fields):
        """Set card view, based on vocabulary fields. """
        
        if isinstance(sentence_fields, Sentence): # TODO: change this
            self.furiganas = sentence_fields.kanji_readings
            self.sentence = sentence_fields
            sentence_fields = sentence_fields.fields
            

        card_text = get_text(self.furiganas, sentence_fields)
        self.setHtml(card_text)

    def refresh_when_double_clicked(self, table_view):
        table_view.clicked.connect(lambda x: self.set_card_view(table_view.model_on.get_sentence_by_row(table_view.currentIndex().row())))

    def mouseMoveEvent(self, event): 
        """Show transcription when mouse howers a kanji. """
        if hasattr(self, 'sentence'):
            show_transcription(self, event, self.sentence)