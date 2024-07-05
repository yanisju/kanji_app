from PyQt6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QTextEdit, QPushButton, QFormLayout
from .card_dialog_form import CardDialogForm

class CardDialog(QDialog):
    def init_card_layout(self, layout):
        text_widget = QTextEdit()
        layout.addWidget(text_widget)
        
        text = "<hr id=answer> <div style='font-size: 25px;'>test</div>"

        redText = "<span style=\" font-size:8pt; font-weight:600; color:#ff0000;\"> I want this text red </span>"
        text_widget.setHtml(redText)
        
        infos_layout = QVBoxLayout()
        layout.addLayout(infos_layout)
    
    def init_buttons_layout(self, layout):
        confirm_button = QPushButton("Confirm")
        cancel_button = QPushButton("Cancel")
        layout.addWidget(confirm_button)
        layout.addWidget(cancel_button)
        confirm_button.clicked.connect(self.accept)
        cancel_button.clicked.connect(self.reject)
    
    def __init__(self, central_widget):
        super().__init__(central_widget) # Init this widget as a child of central widget
        
        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)
        
        card_layout = QHBoxLayout()
        self.layout.addLayout(card_layout)
        self.init_card_layout(card_layout)
        
        buttons_layout = QHBoxLayout()
        self.layout.addLayout(buttons_layout)
        self.init_buttons_layout(buttons_layout)
        
        self.fields_layout = CardDialogForm(self)
        card_layout.addLayout(self.fields_layout)
        self.fields_layout.init_fields()
    
    def open_card_dialog(self, items_list):
        self.fields_layout.fill_fields(items_list)
        self.open()
        