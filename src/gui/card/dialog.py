from PyQt6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QPushButton, QTableView
from .view.view import CardView
from .fields import CardDialogFields
from ...vocabulary.sentence.sentence import Sentence

class CardDialog(QDialog):
    """Pop-up window for creating and editing a Anki card and its field. """

    def __init__(self, central_widget):
        super().__init__(central_widget) # Init this widget as a child of central widget
        
        self.layout = QVBoxLayout(self) # Main layout of Dialog
        self.setLayout(self.layout)
        
        card_layout = QHBoxLayout() # Layout for card view and fields 
        self.layout.addLayout(card_layout)

        self.card_view = CardView() # TextEdit to view current card in Anki
        card_layout.addWidget(self.card_view)
        self.fields_layout = CardDialogFields(self.card_view) # Layout to modify card fields / Modify card view
        card_layout.addLayout(self.fields_layout)
        
        buttons_layout = QHBoxLayout() # Layout for bottom buttons
        self.layout.addLayout(buttons_layout)
        self.init_buttons_layout(buttons_layout)
    
    def init_buttons_layout(self, layout):
        self.confirm_button = QPushButton("Confirm")
        cancel_button = QPushButton("Cancel")
        layout.addWidget(self.confirm_button)
        layout.addWidget(cancel_button)
        self.confirm_button.clicked.connect(self.accept)
        
        cancel_button.clicked.connect(self.reject)

    def modify_sentence(self, vocabulary, sentence_row):
        new_sentence_fields = [field for field in self.fields_layout.fields_value]
        vocabulary.sentences[sentence_row].update_attributes(new_sentence_fields)

    def open_card_dialog(self, model, sentence, vocabulary, sentence_row):
        """Open a new dialog menu for a card. """

        self.sentence = sentence # Reference to the original sentence
        # self.sentence = copy.deepcopy(sentence) # Copy of sentence to work on / possible to edit
        self.vocabulary = vocabulary
        self.sentence_row = sentence_row # Row number in the view

        self.fields_layout.fill_fields(self.sentence)
        self.fields_layout.kanji_table_view # Contains each kanji, theirs readings and meanings of the sentence.

        self.confirm_button.clicked.connect(lambda x: self.modify_sentence(self.vocabulary, self.sentence_row))
        self.confirm_button.clicked.connect(lambda x: model.modify_row(self.vocabulary.sentences[sentence_row], self.sentence_row))

        self.card_view.set_card_view(self.sentence) # Init card view with card fields
        self.open()
        