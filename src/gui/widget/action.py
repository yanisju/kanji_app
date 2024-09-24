from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QWidget, QSizePolicy
from ...vocabulary.manager import VocabularyManager
from .button.add_one_word import AddOneWordLayout
from .button.choose_file import ChooseFileButton
from .button.add_to_anki_list import AddToAnkiListButton
from .button.create_package import CreatePackageButton

from PyQt6.QtCore import QSize

class ActionWiget(QWidget):
    def __init__(self, parent: QWidget, vocabulary_manager: VocabularyManager, sentence_widget, anki_manager):
        super().__init__(parent)
        layout = QVBoxLayout(self)
        self.setSizePolicy(QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Expanding)

        layout.addLayout(AddOneWordLayout(vocabulary_manager))
        layout.addWidget(ChooseFileButton(parent, vocabulary_manager))
        add_to_anki_list_button = AddToAnkiListButton(sentence_widget.sentence_view, vocabulary_manager)
        layout.addWidget(add_to_anki_list_button)
        layout.addWidget(CreatePackageButton(anki_manager))
    
    def _get_create_package_button(self):
        button = QPushButton("Create Package")
        button.clicked.connect(self._anki_manager.generate_deck)

        return button
    
    def sizeHint(self):
        width = int(self.parentWidget().width() * 0.15) 
        height = int(self.parentWidget().height() * 0.33) 
        return QSize(width, height)