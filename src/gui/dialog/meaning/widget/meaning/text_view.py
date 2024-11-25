from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtGui import QStandardItemModel
from PyQt6.QtCore import QSize


class MeaningTextView(QTextEdit):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setReadOnly(True)

    def set_text(self, model: QStandardItemModel):
        with open("styles/meaning/text_view.html", "r") as html_file:
            text = html_file.read()

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
    
    def sizeHint(self):
        width = int(self.parentWidget().width() * 0.4)
        height = int(self.parentWidget().height())
        return QSize(width, height)
