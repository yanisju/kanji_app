from PyQt6.QtCore import QSize
from PyQt6.QtWidgets import QSizePolicy

from PyQt6.QtWidgets import QWidget, QHBoxLayout, QFormLayout, QLineEdit, QPushButton

class AddWordWidget(QWidget):
    """Button to add a single word."""
    
    def __init__(self, vocabulary_manager, vocabulary_list_view) -> None:
        super().__init__()
        self.vocabulary_manager = vocabulary_manager

        layout = QHBoxLayout(self)
        
        formLayout = QFormLayout()
        self.line_edit = QLineEdit()
        formLayout.addRow("Enter Kanji:", self.line_edit)
        self.button = QPushButton("Confirm")

        layout.addLayout(formLayout)
        layout.addWidget(self.button)
        
        self.button.clicked.connect(self.add_word_to_manager) # Add word to manager
        self.button.clicked.connect(vocabulary_list_view.scrollToBottom) # Scroll to bottom 

        self.setSizePolicy(QSizePolicy.Policy.Maximum, QSizePolicy.Policy.Fixed)
        
    def get_text(self):
        text = self.line_edit.text().strip()
        return text
    
    def add_word_to_manager(self):
        word = self.get_text()
        self.vocabulary_manager.add_word(word)