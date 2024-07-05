from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QFileDialog, QWidget
from ..vocabulary.manager import VocabularyManager

class UpRightWidget(QWidget):
    def __init__(self, central_widget: QWidget, vocabulary_manager: VocabularyManager, up_left_widget):
        super().__init__(central_widget) # Init this widget as a child of central widget
        
        self.layout = QVBoxLayout(self) # Init the main layout of the widget as a child of the widget
        self.setLayout(self.layout)
        
        self.central_widget = central_widget
        self.vocabulary_manager = vocabulary_manager
        self.up_left_widget = up_left_widget
        
        self.layout.addLayout(self._create_one_word_button_layout())
        self.layout.addWidget(self._create_choose_kanji_file_button_widget())   
    
    def _create_one_word_button_layout(self):
        """Create and configure button to add a single word."""
        layout = QHBoxLayout()  
        formLayout = QFormLayout()
        line_edit = QLineEdit()
        formLayout.addRow("Enter Kanji:", line_edit)
        enter_button = QPushButton("Confirm")
        
        layout.addLayout(formLayout)
        layout.addWidget(enter_button)
        
        enter_button.clicked.connect(lambda x: self.vocabulary_manager.add_to_dictionnary(line_edit.text())) # Add word to model and refresh view
        enter_button.clicked.connect(self.up_left_widget.vocabulary_list_view.scrollToBottom) # Scroll to bottom 
        
        return layout
    
    def _choose_kanji_file_action(self):
        """Create and configure button to add a multiple words from a single file."""
        file_selecter = QFileDialog(parent=self.central_widget)
        file = file_selecter.getOpenFileName(filter = "*.txt")
        
        self.vocabulary_manager._get_word_from_text(file[0])
        
        print(file[0])
    
    def _create_choose_kanji_file_button_widget(self):
        choose_kanji_file_button = QPushButton("Choose File")
        choose_kanji_file_button.clicked.connect(self._choose_kanji_file_action)
        
        return choose_kanji_file_button
    
        

    