from PyQt6.QtCore import Qt
from PyQt6.QtCore import QSize

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel, QSizePolicy
from ...vocabulary.manager import VocabularyManager
from .table_view.vocabulary import VocabularyTableView

class VocabularyWidget(QWidget):
    def __init__(self, parent: QWidget, vocabulary_manager: VocabularyManager, sentence_rendering_widget, sentence_table_view) -> None:
        super().__init__(parent)
        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout = QVBoxLayout(self)


        label = QLabel("Vocabulary List", self)
        label.setStyleSheet("font-size: 17px; font-weight: bold;")
        label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        layout.addWidget(label)

        vocabulary_list_view = VocabularyTableView(parent, vocabulary_manager, sentence_rendering_widget, sentence_table_view) # View for retrieved words
        layout.addWidget(vocabulary_list_view)

    def sizeHint(self):
        width = int(self.parentWidget().width() * 0.85) 
        height = int(self.parentWidget().height() * 0.33) 
        return QSize(width, height)