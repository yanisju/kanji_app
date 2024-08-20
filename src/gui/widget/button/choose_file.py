from PyQt6.QtWidgets import QPushButton, QFileDialog

class ChooseFileButton(QPushButton):
    def __init__(self, central_widget, vocabulary_manager) -> None:
        super().__init__()
        self.central_widget = central_widget
        self.vocabulary_manager = vocabulary_manager
        self.setText("Choose File")
        self.clicked.connect(self._set_action)
        
    def _set_action(self):
        """Configure button to add a multiple words from a single file."""
        file_selecter = QFileDialog(parent=self.central_widget)
        file = file_selecter.getOpenFileName(filter = "*.txt")
        file_location = file[0]
        
        if(file_location != ""):
            words = []
            with open(file_location, encoding="utf8") as file:
                for vocabulary in file:
                    vocabulary = vocabulary.strip() # Remove useless characters
                    if vocabulary:  # if not empty
                        words.append(vocabulary)
            for word in words:
                self.vocabulary_manager.add_word(word)

        else:
            print("Can't open file") # TODO: Add DialogError