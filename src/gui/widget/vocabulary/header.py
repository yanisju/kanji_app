from PyQt6.QtWidgets import QWidget, QHBoxLayout, QLabel

from .button.add_word import AddWordWidget

from ....vocabulary.manager import VocabularyManager

class VocabularyHeader(QWidget):
    def __init__(self, parent: QWidget, vocabulary_manager: VocabularyManager, vocabulary_list_view) -> None:
        super().__init__(parent)
        layout = QHBoxLayout(self)
        
        label = QLabel("Vocabulary List", self)
        label.setProperty("class", "title")
        layout.addWidget(label)

        add_word_button = AddWordWidget(
            vocabulary_manager, vocabulary_list_view)
        layout.addWidget(add_word_button)