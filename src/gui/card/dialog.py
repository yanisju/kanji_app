from PyQt6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QPushButton
from .view import CardView
from .fields import CardDialogFields

class CardDialog(QDialog):
    """Pop-up window for creating and editing a Anki card and its field. """
    
    def init_buttons_layout(self, layout):
        confirm_button = QPushButton("Confirm")
        cancel_button = QPushButton("Cancel")
        layout.addWidget(confirm_button)
        layout.addWidget(cancel_button)
        confirm_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
    
    def __init__(self, central_widget):
        super().__init__(central_widget) # Init this widget as a child of central widget
        
        self.layout = QVBoxLayout(self) # Main layout of Dialog
        self.setLayout(self.layout)
        
        card_layout = QHBoxLayout() # Layout for card view and fields 
        self.layout.addLayout(card_layout)

        card_view = CardView() # TextEdit to view current card in Anki
        card_layout.addWidget(card_view)
        self.fields_layout = CardDialogFields(self) # Layout to modify card fields / Modify card view
        card_layout.addLayout(self.fields_layout)
        self.fields_layout.init_fields()
        card_view.set_card_view(self.fields_layout.field_line_edit_list) # Init card view with card fields
        
        buttons_layout = QHBoxLayout() # Layout for bottom buttons
        self.layout.addLayout(buttons_layout)
        self.init_buttons_layout(buttons_layout)
        
  
    
    def open_card_dialog(self, items_list):
        self.fields_layout.fill_fields(items_list)
        self.open()
        