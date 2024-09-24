from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel
from ...vocabulary.manager import VocabularyManager
from .table_view.sentence import SentenceTableView

class FinalSentenceWidget(QWidget):
    def __init__(self, parent: QWidget, vocabulary_manager: VocabularyManager, card_text_view) -> None:
        super().__init__(parent)
        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel("Final Sentence List", self)
        label.setStyleSheet("font-size: 16px; font-weight: bold;")
        label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(self.label)

        sentence_view = SentenceTableView(parent, vocabulary_manager.sentence_model, vocabulary_manager, card_text_view)
        layout.addWidget(sentence_view)