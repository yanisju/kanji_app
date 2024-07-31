from PyQt6.QtWidgets import QTextEdit

from ....vocabulary.sentence.sentence import Sentence
from .sentences import *

class CardView(QTextEdit):
    """Text view of the card in Anki. """

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

    def set_card_view(self, sentence: Sentence):
        """Set card view, based on vocabulary fields. """

        self.furiganas = sentence.kanji_readings
        self.sentence = sentence
        sentence_fields = sentence.fields
            
        card_text = get_text(self.furiganas, sentence_fields)
        self.setHtml(card_text)

    def refresh_view(self, fields_values):
        """Refresh view, based on card fields values. """
        card_text = get_text(self.furiganas, fields_values)
        self.setHtml(card_text)

    def refresh_when_double_clicked(self, table_view):
        """When Sentence TableView is double clicked, open the card editor. """

        table_view.clicked.connect(lambda x: self.set_card_view(table_view.model_on.get_sentence_by_row(table_view.currentIndex().row())))

    def mouseMoveEvent(self, event): 
        """Show transcription when mouse howers a kanji. """
        if hasattr(self, 'sentence'):
            show_transcription(self, event, self.sentence)