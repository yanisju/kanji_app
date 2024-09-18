from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtGui import QStandardItemModel

class MeaningTextView(QTextEdit):
    
    def __init__(self) -> None:
        super().__init__()
        self.setReadOnly(True)
        self.setStyleSheet("font-size: 14px;")  # Set a base font size for the entire text view

    def set_text(self, model: QStandardItemModel):
        text = """
        <style>
            .meaning { font-size: 16px; font-weight: bold; }
            .part-of-speech { font-size: 14px; font-style: italic;}
            .index { font-size: 14px; font-weight: bold; }
            .entry { margin-bottom: 10px; }
        </style>
        """
        
        for i in range(model.rowCount()):
            meaning = model.item(i, 0).text()
            part_of_speech = model.item(i, 1).text()
            text += self._get_text_line(i, meaning, part_of_speech)
        
        self.setHtml(text)

    def _get_text_line(self, index, meaning, part_of_speech):
        return f"""
            <div class='entry'>
                <span class='index'>{index + 1}.</span>
                <span class='meaning'>{meaning}</span>
                <span class='part-of-speech'>({part_of_speech})</span>
            </div>
        """
