from PyQt6.QtCore import QSize

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy
from ...vocabulary.manager import VocabularyManager
from .table_view.vocabulary import VocabularyTableView

from .button.add_word import AddWordWidget

from .button.add_word import AddWordWidget


class VocabularyWidget(QWidget):
    def __init__(
            self,
            parent: QWidget,
            vocabulary_manager: VocabularyManager,
            sentence_rendering_widget,
            sentence_table_view) -> None:
        super().__init__(parent)
        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding)
        layout = QVBoxLayout(self)

        up_layout = QHBoxLayout()
        layout.addLayout(up_layout)

        label = QLabel("Vocabulary List", self)
        label.setStyleSheet("font-size: 16px; font-weight: bold;")
        # label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        # up_layout.setAlignment(label, Qt.AlignmentFlag.AlignVCenter)
        up_layout.addWidget(label)

        vocabulary_list_view = VocabularyTableView(
            parent,
            vocabulary_manager,
            sentence_rendering_widget,
            sentence_table_view)  # View for retrieved words
        layout.addWidget(vocabulary_list_view)

        add_word_button = AddWordWidget(
            vocabulary_manager, vocabulary_list_view)
        up_layout.addWidget(add_word_button)

    def sizeHint(self):
        width = int(self.parentWidget().width() * 0.85)
        height = int(self.parentWidget().height() * 0.33)
        return QSize(width, height)
