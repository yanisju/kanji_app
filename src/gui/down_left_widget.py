from PyQt6.QtWidgets import QHBoxLayout, QWidget, QTextEdit 

class DownLeftWidget(QWidget):
    def __init__(self, central_widget):
        super().__init__(central_widget) # Init this widget as a child of central widget
        
        self.layout = QHBoxLayout(self)
        self.setLayout(self.layout)
        
        text_widget = QTextEdit()
        self.layout.addWidget(text_widget)
        
        text = "<hr id=answer> <div style='font-size: 25px;'>test</div>"
        
        text_widget.setHtml(text)
        
    def parse_sentence_to_html(self, sentence):
        pass
        
    def parse_text_widget(self, vocabulary):
        text = ""
        # sentence_text = self.parse_sentence_to_html(pass)