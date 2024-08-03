from PyQt6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QPushButton
from .view.text_view import CardTextView
from .fields import CardDialogFields
from ...vocabulary.sentence.sentence import Sentence

class CardDialog(QDialog):
    """Pop-up window for creating and editing a Anki card and its field. """

    def __init__(self, central_widget, main_card_view):
        super().__init__(central_widget) # Init this widget as a child of central widget
        self.main_card_view = main_card_view
        
        self.layout = QVBoxLayout(self) # Main layout of Dialog
        self.setLayout(self.layout)
        
        card_layout = QHBoxLayout() # Layout for card view and fields 
        self.layout.addLayout(card_layout)

        self.card_view = CardTextView() # TextEdit to view current card in Anki
        card_layout.addWidget(self.card_view)
        self.fields_layout = CardDialogFields(self.card_view) # Layout to modify card fields / Modify card view
        card_layout.addLayout(self.fields_layout)
        
        buttons_layout = QHBoxLayout() # Layout for bottom buttons
        self.layout.addLayout(buttons_layout)
        self.init_buttons_layout(buttons_layout)
    
    def init_buttons_layout(self, layout):
        self.confirm_button = QPushButton("Confirm")
        self.cancel_button = QPushButton("Cancel")
        layout.addWidget(self.confirm_button)
        layout.addWidget(self.cancel_button)
        self.confirm_button.clicked.connect(lambda x: self._update_sentence_attributes(self.main_card_view))
        self.confirm_button.clicked.connect(self.accept)
        
        self.cancel_button.clicked.connect(self.reject)


    def _update_sentence_attributes(self, card_view):
        """Update current sentence with modified attributes in view. """
        self.sentence.update_attributes(self.fields_layout.fields_value, 
                                        self.fields_layout.kanji_data_model.kanji_data)
        self.sentences_model.modify_row(self.vocabulary.sentences[self.sentence_row], self.sentence_row)
        if hasattr(self, "sentence"): # Update CardView from Main Application as well
            pass
            card_view.set_card_view(self.sentence, 
                                    self.sentence.position_kanji_sentence,
                                    self.sentence.kanji_data)

    def open_card_dialog(self, sentences_model, sentence: Sentence, vocabulary, sentence_row):
        """Open a new dialog menu for a card. """

        self.sentence = sentence 
        self.vocabulary = vocabulary
        self.sentence_row = sentence_row # Row number in the view
        self.sentences_model = sentences_model
        
        self.fields_layout.fill_fields(self.sentence)
        self.fields_layout.kanji_table_view # Contains each kanji, theirs readings and meanings of the sentence.

        self.card_view.set_card_view(self.sentence, 
                                     self.fields_layout.kanji_data_model.position_kanji_sentence,
                                     self.fields_layout.kanji_data_model.kanji_data) # Init card view with card fields
        self.open()
        