from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QFileDialog, QWidget
from ...vocabulary.manager import VocabularyManager

class UpRightWidget(QWidget):
    def __init__(self, central_widget: QWidget, vocabulary_manager: VocabularyManager, up_left_widget, anki_manager):
        super().__init__(central_widget) # Init this widget as a child of central widget
        
        self.layout = QVBoxLayout(self) # Init the main layout of the widget as a child of the widget
        self.setLayout(self.layout)
        
        self.central_widget = central_widget
        self.vocabulary_manager = vocabulary_manager
        self.up_left_widget = up_left_widget
        self._anki_manager = anki_manager
        
        self.layout.addLayout(self._create_one_word_button_layout())
        self.layout.addWidget(self._create_choose_kanji_file_button_widget())   
        self.layout.addWidget(self._get_add_to_anki_list_button())
        self.layout.addWidget(self._get_create_package_button())
    
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
        
        if(file[0] != ""):
            self.vocabulary_manager.get_word_from_text(file[0])
    
    def _create_choose_kanji_file_button_widget(self):
        button = QPushButton("Choose File")
        button.clicked.connect(self._choose_kanji_file_action)
        
        return button
    
    def _add_to_anki_list_action(self):
        row_number = self.up_left_widget.sentence_view.currentIndex().row()
        sentence_to_add = self.vocabulary_manager.sentence_model.get_sentence_by_row(row_number)
        self.vocabulary_manager.sentence_added_model.append_sentence(sentence_to_add)

    def _get_add_to_anki_list_button(self):
        button = QPushButton("Add to Anki List")
        button.clicked.connect(self._add_to_anki_list_action)

        return button
    
    def _get_create_package_button(self):
        button = QPushButton("Create Package")
        button.clicked.connect(self._anki_manager.generate_deck)

        return button