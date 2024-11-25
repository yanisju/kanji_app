from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QWidget, QVBoxLayout, QSizePolicy, QGroupBox 

from ....vocabulary.manager import VocabularyManager

from .header import VocabularyHeader

from .table_view import VocabularyTableView


class VocabularyWidget(QGroupBox):
    def __init__(
            self,
            parent: QWidget,
            vocabulary_manager: VocabularyManager,
            sentence_rendering_widget,
            sentence_table_view) -> None:
        super().__init__(parent)

        self.setProperty("class", "styledParent")
        with open("styles/group_box.css", "r") as css_file:
            self.setStyleSheet(css_file.read())

        self.setSizePolicy(
            QSizePolicy.Policy.Expanding,
            QSizePolicy.Policy.Expanding)
        layout = QVBoxLayout(self)

        vocabulary_list_view = VocabularyTableView(
            parent,
            vocabulary_manager,
            sentence_rendering_widget,
            sentence_table_view)  # View for retrieved words
        layout.addWidget(vocabulary_list_view)

        header = VocabularyHeader(self, vocabulary_manager, vocabulary_list_view)
        layout.insertWidget(0, header)

    def sizeHint(self):
        width = int(self.parentWidget().width() * 0.6)
        height = int(self.parentWidget().height() * 0.35)
        return QSize(width, height)
