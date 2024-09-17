from PyQt6.QtWidgets import QTextEdit
from PyQt6.QtGui import QStandardItemModel

class MeaningTextView(QTextEdit):
    
    def __init__(self) -> None:
        super().__init__()
        self.setReadOnly(True)

    def set_text(self, model : QStandardItemModel):
        text = ""
        for i in range(model.rowCount()):
            meaning = model.item(i, 0).text()
            part_of_speech = model.item(i, 1).text()
            text += self._get_text_line(i, meaning, part_of_speech)
            text += "<br>"
        self.setHtml(text)

    def _get_text_line(self, index, meaning, part_of_speech):
        return "" + str(index + 1) + ". " + meaning + " (" + part_of_speech + ")"

