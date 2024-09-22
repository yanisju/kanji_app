from PyQt6.QtCore import Qt

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QLabel,QSizePolicy
from ...vocabulary.manager import VocabularyManager
from .table_view.vocabulary import VocabularyTableView

class VocabularyWidget(QWidget):
    def __init__(self, parent: QWidget, vocabulary_manager: VocabularyManager) -> None:
        super().__init__(parent)
        self.setMinimumSize(800, 175)
        self.setMaximumSize(600, 175)

        self.layout = QVBoxLayout()
        self.setLayout(self.layout)



        # policy = QSizePolicy()
        # policy.setHorizontalPolicy(QSizePolicy.Policy.MinimumExpanding)
        # policy.setVerticalPolicy(QSizePolicy.Policy.MinimumExpanding)
        # self.setSizePolicy(policy)

        self.label = QLabel("Vocabulary List", self)
        self.label.setStyleSheet("font-size: 17px; font-weight: bold;")
        self.label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        self.layout.addWidget(self.label)

        self.vocabulary_list_view = VocabularyTableView(vocabulary_manager) # View for retrieved words
        self.layout.addWidget(self.vocabulary_list_view)