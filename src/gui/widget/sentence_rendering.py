from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from ..card.text_view import CardTextView

class SentenceRenderingWidget(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel("Sentence Rendering", self)
        self.label.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.label)

        self.card_text_view = CardTextView() # View for retrieved words
        self.layout.addWidget(self.card_text_view)