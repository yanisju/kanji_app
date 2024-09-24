from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget

from .widget.vocabulary import VocabularyWidget
from .widget.action import ActionWiget
from .widget.sentence import SentenceWidget
from .widget.sentence_rendering import SentenceRenderingWidget

class CentralWidget(QWidget):
    def __init__(self, parent: QWidget, vocabulary_manager, anki_manager) -> None:
        super().__init__(parent)
        layout = QVBoxLayout(self)

        sentence_rendering_widget = SentenceRenderingWidget(self)
        sentence_widget = SentenceWidget(parent, "Sentence List", vocabulary_manager.sentence_model, vocabulary_manager, sentence_rendering_widget.card_text_view)
        
        vocabulary_layout = QHBoxLayout()
        vocabulary_layout.addWidget(VocabularyWidget(self, vocabulary_manager))
        vocabulary_layout.addWidget(ActionWiget(self, vocabulary_manager, sentence_widget, anki_manager))
        layout.addLayout(vocabulary_layout)

        sentence_layout = QHBoxLayout()
        sentence_layout.addWidget(sentence_widget)
        added_sentence_widget = SentenceWidget(self, "Added Sentence List", vocabulary_manager.sentence_added_model, vocabulary_manager, sentence_rendering_widget.card_text_view)
        sentence_layout.addWidget(added_sentence_widget)
        layout.addLayout(sentence_layout)

        layout.addWidget(sentence_rendering_widget)