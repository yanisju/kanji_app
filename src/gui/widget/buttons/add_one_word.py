from PyQt6.QtWidgets import QHBoxLayout, QFormLayout, QLineEdit, QPushButton

class AddOneWordLayout(QHBoxLayout):
    """Button to add a single word."""
    
    def __init__(self, vocabulary_manager) -> None:
        super().__init__()
        self.vocabulary_manager = vocabulary_manager
        formLayout = QFormLayout()
        self.line_edit = QLineEdit()
        formLayout.addRow("Enter Kanji:", self.line_edit)
        self.button = QPushButton("Confirm")

        self.addLayout(formLayout)
        self.addWidget(self.button)
        
        self.button.clicked.connect(self.add_word_to_manager) # Add word to manager
        # self.button.clicked.connect(self.up_left_widget.vocabulary_list_view.scrollToBottom) # Scroll to bottom 
        
    def get_text(self):
        text = self.line_edit.text().strip()
        return text
    
    def add_word_to_manager(self):
        word = self.get_text()
        self.vocabulary_manager.add_word(word)