from PyQt6.QtCore import Qt
from PyQt6.QtCore import QSize

from PyQt6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QSizePolicy, QPushButton
from ...vocabulary.manager import VocabularyManager
from .table_view.sentence import SentenceTableView

class SentenceWidget(QWidget):
    def __init__(self, parent: QWidget, label_name : str, vocabulary_manager: VocabularyManager, card_text_view, card_dialog, is_added_sentence = False) -> None:
        super().__init__(parent)
        self.vocabulary_manager = vocabulary_manager

        self.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        layout = QVBoxLayout()
        self.setLayout(layout)

        up_layout = QHBoxLayout()
        label = QLabel(label_name, self)
        label.setStyleSheet("font-size: 16px; font-weight: bold;")
        label.setAlignment(Qt.AlignmentFlag.AlignLeft)
        up_layout.addWidget(label)

        if is_added_sentence:
            self.generate_deck_button = QPushButton("Generate Deck")
            self.generate_deck_button.setEnabled(False)
            self.generate_deck_button.clicked.connect(vocabulary_manager.generate_deck)
            vocabulary_manager.sentence_added_to_deck.sentences_model.modified.connect(self.enable_disable_generate_deck_button)
            up_layout.addWidget(self.generate_deck_button)    

        layout.addLayout(up_layout)

        self.sentence_table_view = SentenceTableView(parent, vocabulary_manager, card_text_view, card_dialog, is_added_sentence)
        if is_added_sentence:
            self.sentence_table_view.setModel(vocabulary_manager.sentence_added_to_deck.sentences_model)
        
        layout.addWidget(self.sentence_table_view)

    def sizeHint(self):
        width = int(self.parentWidget().width() * 0.5) 
        height = int(self.parentWidget().height() * 0.33) 
        return QSize(width, height)
    
    def enable_disable_generate_deck_button(self):
        if len(self.vocabulary_manager.sentence_added_to_deck) == 0:
            self.generate_deck_button.setEnabled(False)
        else:
            self.generate_deck_button.setEnabled(True)
