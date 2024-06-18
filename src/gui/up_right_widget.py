from PyQt6.QtWidgets import QHBoxLayout, QVBoxLayout, QFormLayout, QLineEdit, QPushButton, QFileDialog, QWidget
from ..vocabulary.manager import Manager

class UpRightWidget(QWidget):
    def __init__(self, central_widget: QWidget, vocabulary_manager: Manager):
        super().__init__(central_widget) # Init this widget as a child of central widget
        
        self.layout = QVBoxLayout(self) # Init the main layout of the widget as a child of the widget
        self.setLayout(self.layout)
        
        self.central_widget = central_widget
        self.vocabulary_manager = vocabulary_manager
        
        self.layout.addLayout(self._create_one_word_button_layout(vocabulary_manager))
        self.layout.addWidget(self._create_choose_kanji_button_widget())
        
    def _create_one_word_button_layout(self, vocabulary_manager):
        layout = QHBoxLayout()  
        formLayout = QFormLayout()
        line_edit = QLineEdit()
        formLayout.addRow("Enter Kanji:", line_edit)
        enter_button = QPushButton("Confirm")
        
        layout.addLayout(formLayout)
        layout.addWidget(enter_button)
        
        enter_button.clicked.connect(lambda x: vocabulary_manager.get_word_from_qt_line(line_edit.text()))

        return layout
    
    def _choose_kanji_file_action(self):
        file_selecter = QFileDialog(parent=self.central_widget)
        file = file_selecter.getOpenFileName(filter = "*.txt")
        self.vocabulary_manager.file_location = file[0]
        
        print(self.vocabulary_manager.file_location)
    
    def _create_choose_kanji_button_widget(self):
        choose_kanji_file_button = QPushButton("Choose File")
        choose_kanji_file_button.clicked.connect(self._choose_kanji_file_action)
        
        return choose_kanji_file_button
    
        

    