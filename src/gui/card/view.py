from PyQt6.QtWidgets import QTextEdit
import re

class CardView(QTextEdit):
    def __init__(self) -> None:
        super().__init__()
        self.setReadOnly(True)

    def get_color(self, tag):
            colors = {
                'h': 'red',
                'n4': 'blue',
                'a': 'green',
                'n5': 'purple'
                # Ajoutez d'autres couleurs selon les besoins
            }
            return colors.get(tag, 'black')  # Noir par défaut si le tag n'est pas trouvé

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
        card_text = self.get_sentence_original(vocabulary_fields[2].text())
        card_text += "<hr>" 
        card_text += self.get_sentence_translated(vocabulary_fields[1].text())
        card_text += self.get_sentence_meaning(vocabulary_fields[3].text(), vocabulary_fields[4].text(), vocabulary_fields[5].text(), vocabulary_fields[6].text())

        self.setHtml(card_text)