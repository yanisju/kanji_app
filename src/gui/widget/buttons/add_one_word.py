from PyQt6.QtWidgets import QHBoxLayout, QFormLayout, QLineEdit, QPushButton

class AddOneWordLayout(QHBoxLayout):
    """Button to add a single word."""
    
    def __init__(self) -> None:
        super().__init__()
        formLayout = QFormLayout()
        self.line_edit = QLineEdit()
        formLayout.addRow("Enter Kanji:", self.line_edit)
        self.button = QPushButton("Confirm")

        self.addLayout(formLayout)
        self.addWidget(self.button)
        
        # self.button.clicked.connect(lambda x: self.vocabulary_manager.add_to_dictionnary(self.get_text())) # Add word to model and refresh view
        # self.button.clicked.connect(self.up_left_widget.vocabulary_list_view.scrollToBottom) # Scroll to bottom 
        
    def get_text(self):
        text = self.line_edit.text().strip()
        return text