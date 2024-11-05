from PyQt6.QtGui import QAction, QIcon
from PyQt6.QtWidgets import QFileDialog, QMessageBox

from .message_box.importation_error_message_box import ImportationErrorMessageBox

class ImportFromFileAction(QAction):
    def __init__(self, parent, vocabulary_manager):
        super().__init__(parent)
        self.vocabulary_manager = vocabulary_manager
        self.setText("Import from File")
        self.setIcon(QIcon("data/icons/plus.png"))

        self.triggered.connect(self._action)

    def _action(self):
        file_selecter = QFileDialog(self.parent())
        file = file_selecter.getOpenFileName(filter = "*.txt")
        file_location = file[0]
        
        if(file_location == ""):
            QMessageBox.critical(self.parent(), "Error", "No file selected.")
        else:
            words = self._read_words_from_file(file_location)
            
            bad_words = []
            for word in words:
                try:
                    self.vocabulary_manager.add_word(word)
                except:
                    bad_words += word
            
            if len(bad_words) > 0:
                ImportationErrorMessageBox(self.parent()).exec(bad_words)

            
    def _read_words_from_file(self, file_location):
        words = []
        with open(file_location, encoding="utf8") as file:
            for line in file:
                word = line.strip()
                if word:
                    words.append(word)
        return words