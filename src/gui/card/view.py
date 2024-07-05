from PyQt6.QtWidgets import QTextEdit

class CardView(QTextEdit):
    def __init__(self) -> None:
        super().__init__()

    def get_sentence_original(self, sentence_original):
        text = ""
        
        return text

    def set_card_view(self, vocabulary_fields):
        card_text = ""
        card_text += self.get_sentence_original(vocabulary_fields[0])

        self.setHtml(card_text)