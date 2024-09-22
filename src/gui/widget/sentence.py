from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from ...vocabulary.manager import VocabularyManager
from .table_view.sentence import SentenceTableView

class SentenceWidget(QWidget):
    def __init__(self, parent: QWidget, label_name : str, model, vocabulary_manager: VocabularyManager, card_text_view) -> None:
        super().__init__(parent)
        self.layout = QVBoxLayout()
        self.setLayout(self.layout)

        self.label = QLabel(label_name, self)
        self.label.setStyleSheet("font-size: 16px; font-weight: bold;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.label)

        self.sentence_view = SentenceTableView(parent, model, vocabulary_manager, card_text_view)
        self.layout.addWidget(self.sentence_view)