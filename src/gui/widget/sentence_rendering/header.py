from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel

class SentenceRenderingHeader(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)
        layout = QHBoxLayout(self)

        label = QLabel("Sentence Rendering", self)
        label.setProperty("class", "title")
        label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(label)
