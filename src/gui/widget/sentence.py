from PyQt6.QtCore import Qt
from PyQt6.QtCore import QSize

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy
from ...vocabulary.manager import VocabularyManager
from .table_view.sentence import SentenceTableView

class SentenceWidget(QWidget):
    def __init__(self, parent: QWidget, label_name : str, vocabulary_manager: VocabularyManager, card_text_view, is_added_sentence = False) -> None:
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout = QVBoxLayout()
        self.setLayout(layout)

        label = QLabel(label_name, self)
        label.setStyleSheet("font-size: 16px; font-weight: bold;")
        label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(label)

        self.sentence_view = SentenceTableView(parent, vocabulary_manager, card_text_view)
        if is_added_sentence:
            self.sentence_view.setModel(vocabulary_manager.sentence_added_model)
        
        layout.addWidget(self.sentence_view)

    def sizeHint(self):
        width = int(self.parentWidget().width() * 0.5) 
        height = int(self.parentWidget().height() * 0.33) 
        return QSize(width, height)