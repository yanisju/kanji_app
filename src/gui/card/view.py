from PyQt6.QtWidgets import QTextEdit
from ...vocabulary.sentence import Sentence

import re

class CardView(QTextEdit):
    """View of the card in Anki. """
    def __init__(self) -> None:
        super().__init__()
        self.setReadOnly(True)

    def get_color(self, tag):
            colors = {
                'h': 'red',
                'n4': 'blue',
                'a': 'green',
                'n5': 'purple'
            }
            return colors.get(tag, 'black')  # Default black if tag not found

    def colorize_transcription(self, match):
        kanji = match.group(1)
        transcription = match.group(2)
        tag = match.group(3)
        color = self.get_color(tag)
        return f'{kanji}<span style="color:{color}">{transcription}</span>'
    
    def get_sentence_original(self, text):
        pattern = r'(\w+)\[(.*?)\;(.*?)\]'

        result = "<span style=\"font-size:22px\">"
        result += re.sub(pattern, self.colorize_transcription, str(text))
        result += "</span>"
        return result
    
    def get_sentence_translated(self, text):
        result = "<span style=\"font-size:22px\">" + text + "</span>" + "<br>"
        return result
    
    def get_sentence_meaning(self, text1, text2, text3, text4):
        result = "<span style=\"font-size:22px\">"
        result += text1 + " - " + text2
        if text3 and text4:
             result += "<br>" + text3 + " - " + text4
        result += "</span>"
        return result

    def set_card_view(self, vocabulary_fields):
        if isinstance(vocabulary_fields, Sentence):
            vocabulary_fields = vocabulary_fields.fields

        card_text = self.get_sentence_original(vocabulary_fields[2])
        card_text += "<hr>" 
        card_text += self.get_sentence_translated(vocabulary_fields[1])
        card_text += self.get_sentence_meaning(vocabulary_fields[3], vocabulary_fields[4], vocabulary_fields[5], vocabulary_fields[6])

        self.setHtml(card_text)

    def refresh_when_double_clicked(self, table_view):
        table_view.clicked.connect(lambda x: self.set_card_view(table_view.model_on.get_sentence_by_row(table_view.currentIndex().row())))