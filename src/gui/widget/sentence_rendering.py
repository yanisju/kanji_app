from PyQt6.QtCore import Qt
from PyQt6.QtCore import QSize

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy
from ..widget.card_text_view import CardTextView

class SentenceRenderingWidget(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel("Sentence Rendering", self)
        label.setStyleSheet("font-size: 16px; font-weight: bold;")
        label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(label)

        self.card_text_view = CardTextView(True) # View for retrieved words
        layout.addWidget(self.card_text_view)

    def sizeHint(self):
        width = int(self.parentWidget().width()) 
        height = int(self.parentWidget().height() * 0.33) 
        return QSize(width, height)