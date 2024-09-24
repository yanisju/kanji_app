from PyQt6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QPushButton
from PyQt6.QtGui import QFont
from ..text_view import CardTextView
from .fields import FieldsLayout
from ....vocabulary.sentence.sentence import Sentence

from PyQt6.QtCore import pyqtSignal

class CardDialog(QDialog):
    """Pop-up window for creating and editing a Anki card and its field. """

    confirm_button_clicked_signal = pyqtSignal(Sentence, int)

    def __init__(self, central_widget, main_card_view):
        super().__init__(central_widget) 
        self.setWindowTitle("Anki Card Editor")

        font = QFont()
        font.setPointSize(11)
        self.setFont(font)

        self.resize(int(central_widget.parent().width() * 0.7), int(central_widget.parent().height() * 0.7))

        self.main_card_view = main_card_view
        self._init_layout()
    
    def _init_layout(self):
        layout = QVBoxLayout(self) # Main layout of Dialog
        self.setLayout(layout)
        
        card_layout = QHBoxLayout() # Layout for card view and fields 
        layout.addLayout(card_layout)

        self.card_view = CardTextView() # TextEdit to view current card in Anki
        card_layout.addWidget(self.card_view)

        self.fields_layout = FieldsLayout(self.card_view) # Layout to modify card fields / Modify card view
        card_layout.addLayout(self.fields_layout)
        
        buttons_layout = QHBoxLayout() # Layout for bottom buttons
        layout.addLayout(buttons_layout)
        self._init_buttons_layout(buttons_layout)

    def _init_buttons_layout(self, layout):
        self.confirm_button = QPushButton("Confirm")
        cancel_button = QPushButton("Cancel")
        layout.addWidget(self.confirm_button)
        layout.addWidget(cancel_button)
        self.confirm_button.clicked.connect(self._confirm_button_clicked) 
        cancel_button.clicked.connect(self.reject)

    def _confirm_button_clicked(self):
        self.fields_layout.refresh_fields_value() # TODO: move this and that
        self._update_sentence_attributes()
        self.confirm_button_clicked_signal.emit(self.sentence, self.sentence_row)
        self.accept()

    def _update_sentence_attributes(self): # TODO: put it in another class
        """Update current sentence with modified attributes in view. """
        self.sentence.update_attributes(tuple(self.fields_layout.fields_value), 
                                        self.fields_layout.kanji_data_model.kanji_data)
        self.sentences_model.modify_row(self.sentence, self.sentence_row)
        if hasattr(self, "sentence"): # Update CardView from Main Application as well
            self.main_card_view.set_card_view(self.sentence, 
                                    self.sentence.position_kanji_sentence,
                                    self.sentence.kanji_data)
        

    def update(self, sentences_model, sentence: Sentence, sentence_row):
        """If Dialog is opened, dialog view and fields must be updated 
        to the current sentence."""

        self._init_variables(sentences_model, sentence, sentence_row)
        self.fields_layout.update(sentence)

    def _init_variables(self, sentences_model, sentence: Sentence, sentence_row):
        """Initialiaze sentences variables for the CardDialog. """

        self.sentence = sentence 
        self.sentence_row = sentence_row # Row number in the view
        self.sentences_model = sentences_model
        
        self.fields_layout.fill_fields(self.sentence)
        self.fields_layout.kanji_table_view # Contains each kanji, theirs readings and meanings of the sentence.

        self.card_view.set_card_view(self.sentence, 
                                    self.fields_layout.kanji_data_model.position_kanji_sentence,
                                    self.fields_layout.kanji_data_model.kanji_data) # Init card view with card fields
        