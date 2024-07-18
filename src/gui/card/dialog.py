from PyQt6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QPushButton
from .view import CardView
from .fields import CardDialogFields

class CardDialog(QDialog):
    """Pop-up window for creating and editing a Anki card and its field. """
    
    def init_buttons_layout(self, layout):
        self.confirm_button = QPushButton("Confirm")
        cancel_button = QPushButton("Cancel")
        layout.addWidget(self.confirm_button)
        layout.addWidget(cancel_button)
        self.confirm_button.clicked.connect(self.accept)
        
        cancel_button.clicked.connect(self.reject)
    
    def __init__(self, central_widget, vocabulary_manager):
        super().__init__(central_widget) # Init this widget as a child of central widget
        self.vocabulary_manager = vocabulary_manager
        
        self.layout = QVBoxLayout(self) # Main layout of Dialog
        self.setLayout(self.layout)
        
        card_layout = QHBoxLayout() # Layout for card view and fields 
        self.layout.addLayout(card_layout)

        self.card_view = CardView() # TextEdit to view current card in Anki
        card_layout.addWidget(self.card_view)
        self.fields_layout = CardDialogFields(self, self.card_view) # Layout to modify card fields / Modify card view
        card_layout.addLayout(self.fields_layout)
        self.fields_layout.init_fields()
        
        
        buttons_layout = QHBoxLayout() # Layout for bottom buttons
        self.layout.addLayout(buttons_layout)
        self.init_buttons_layout(buttons_layout)
    
    def modify_sentence(self, vocabulary, sentence_row):
        lang_from = self.fields_layout.fields_value[0]
        lang_to = self.fields_layout.fields_value[1]
        transcription = self.fields_layout.fields_value[2] 
        word1 = self.fields_layout.fields_value[3] 
        word1_meaning = self.fields_layout.fields_value[4]
        word2 = self.fields_layout.fields_value[5] 
        word2_meaning = self.fields_layout.fields_value[6]
        vocabulary.sentences[sentence_row].update_attributes(lang_from, lang_to, transcription, word1, word1_meaning, word2, word2_meaning)

    def open_card_dialog(self, sentence, vocabulary, sentence_row):
        """Open a new dialog menu for a card. """

        self.sentence = sentence
        self.vocabulary = vocabulary
        self.sentence_row = sentence_row # Row number in the view

        self.fields_layout.fill_fields(sentence)

        self.confirm_button.clicked.connect(lambda x: self.modify_sentence(self.vocabulary, self.sentence_row))
        self.confirm_button.clicked.connect(lambda x: self.vocabulary_manager.sentence_model.modify_row(self.vocabulary.sentences[sentence_row], self.sentence_row))

        self.card_view.set_card_view(self.fields_layout.fields_value) # Init card view with card fields
        self.open()
        