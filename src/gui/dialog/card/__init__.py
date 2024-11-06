from PyQt6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QPushButton
from ...widget.card_text_view import CardTextView
from .fields_widget import FieldsWidget
from ....vocabulary.sentence.sentence import Sentence

from PyQt6.QtCore import pyqtSignal

class CardDialog(QDialog):
    """Pop-up window for creating and editing a Anki card and its field. """

    sentence_modified = pyqtSignal(Sentence)

    def __init__(self, central_widget, vocabulary_manager):
        super().__init__(central_widget) 
        self.setWindowTitle("Anki Card Editor")

        self.resize(int(central_widget.parent().width() * 0.7), int(central_widget.parent().height() * 0.7))

        self.vocabulary_manager = vocabulary_manager
        self._init_layout()
    
    def _init_layout(self):
        layout = QVBoxLayout(self) # Main layout of Dialog
        self.setLayout(layout)
        
        card_layout = QHBoxLayout() # Layout for card view and attributes 
        layout.addLayout(card_layout)

        self.card_view = CardTextView(False) # TextEdit to view current card in Anki
        card_layout.addWidget(self.card_view)

        self.fields_widget = FieldsWidget(self, self.card_view) # Widget to modify card attributes / Modify card view
        card_layout.addWidget(self.fields_widget)
        
        buttons_layout = QHBoxLayout() # Layout for bottom buttons
        layout.addLayout(buttons_layout)
        self._init_buttons_layout(buttons_layout)

    def _init_buttons_layout(self, layout):
        self.confirm_button = QPushButton("Confirm")
        self.confirm_and_add_button = QPushButton("Confirm and Add to Deck")
        cancel_button = QPushButton("Cancel")
        layout.addWidget(self.confirm_button)
        layout.addWidget(self.confirm_and_add_button)
        layout.addWidget(cancel_button)
        self.confirm_and_add_button.clicked.connect(self._confirm_and_add_to_deck_clicked) 
        self.confirm_button.clicked.connect(self._confirm_button_clicked) 
        cancel_button.clicked.connect(self.reject)

    def _confirm_and_add_to_deck_clicked(self):
        self.vocabulary_manager.add_sentence_to_deck(self.sentence)
        self._confirm_button_clicked()

    def _confirm_button_clicked(self):
        self._update_sentence_attributes()
        self.accept()

    def _update_sentence_attributes(self): # TODO: put it in another class
        """Update current sentence with modified attributes in view. """
        self.sentence.update_attributes(tuple(self.fields_widget.sentence_attributes_widget.attributes_value), 
                                        self.fields_widget.kanji_table_view.model())
        self.sentences_model.modify_row(self.sentence, self.sentence_row)
        if hasattr(self, "sentence"): # Update CardView from Main Application as well
            self.sentence_modified.emit(self.sentence)
            # self.main_card_view.set_card_view(self.sentence)
        
    def sentence_changed(self, sentences_model, sentence: Sentence, sentence_row):
        self.sentence = sentence.clone()
        self.sentence_row = sentence_row # Row number in the view
        self.sentences_model = sentences_model

    def open(self):
        """If Dialog is opened, dialog view and fields must be updated 
        to the current sentence."""

        self.fields_widget.set_to_new_sentence(self.sentence)
        self.card_view.set_card_view(self.sentence) # Init card view with card fields
        
        super().open()
