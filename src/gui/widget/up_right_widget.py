from PyQt6.QtWidgets import QVBoxLayout, QPushButton, QWidget
from ...vocabulary.manager import VocabularyManager
from .buttons.add_one_word import AddOneWordLayout
from .buttons.choose_file import ChooseFileButton
from .buttons.add_to_anki_list import AddToAnkiListButton
from .buttons.create_package import CreatePackageButton

class UpRightWidget(QWidget):
    def __init__(self, central_widget: QWidget, vocabulary_manager: VocabularyManager, up_left_widget, anki_manager):
        super().__init__(central_widget) # Init this widget as a child of central widget
        
        self.layout = QVBoxLayout(self) # Init the main layout of the widget as a child of the widget
        self.setLayout(self.layout)
        
        self.central_widget = central_widget
        self.vocabulary_manager = vocabulary_manager
        self.up_left_widget = up_left_widget
        
        self.layout.addLayout(AddOneWordLayout(vocabulary_manager))
        self.layout.addWidget(ChooseFileButton(central_widget, vocabulary_manager))   
        self.layout.addWidget(AddToAnkiListButton(self.up_left_widget.sentence_view, self.vocabulary_manager))
        self.layout.addWidget(CreatePackageButton(anki_manager))
    
    def _get_create_package_button(self):
        button = QPushButton("Create Package")
        button.clicked.connect(self._anki_manager.generate_deck)

        return button