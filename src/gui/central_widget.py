from PyQt6.QtWidgets import QVBoxLayout, QHBoxLayout, QWidget

from .widget.vocabulary import VocabularyWidget
from .widget.sentence import SentenceWidget
from .widget.sentence_rendering import SentenceRenderingWidget

from .dialog.card import CardDialog

from .widget.sentence import SentenceWidgetMode


class CentralWidget(QWidget):
    def __init__(self, parent: QWidget, vocabulary_manager) -> None:
        super().__init__(parent)
        layout = QVBoxLayout(self)

        card_dialog = CardDialog(self, vocabulary_manager)
        sentence_rendering_widget = SentenceRenderingWidget(self, card_dialog)
        card_dialog.sentence_modified.connect(
            sentence_rendering_widget.card_text_view.set_card_view)
        sentence_widget = SentenceWidget(
            self,
            "Sentence List",
            vocabulary_manager,
            sentence_rendering_widget.card_text_view,
            card_dialog,
            SentenceWidgetMode.VOCABULARY_SENTENCE)

        vocabulary_layout = QHBoxLayout()
        vocabulary_layout.addWidget(
            VocabularyWidget(
                self,
                vocabulary_manager,
                sentence_rendering_widget,
                sentence_widget.sentence_table_view))
        layout.addLayout(vocabulary_layout)

        sentence_layout = QHBoxLayout()
        sentence_layout.addWidget(sentence_widget)
        added_sentence_widget = SentenceWidget(
            self,
            "Added Sentence List",
            vocabulary_manager,
            sentence_rendering_widget.card_text_view,
            card_dialog,
            SentenceWidgetMode.ADDED_SENTENCE)
        sentence_layout.addWidget(added_sentence_widget)
        layout.addLayout(sentence_layout)

        layout.addWidget(sentence_rendering_widget)
