from .vocabulary.manager import VocabularyManager
from .gui.main_window import MainWindow
from PyQt6.QtWidgets import QApplication
from .anki import AnkiManager

import sys

class App:
    def __init__(self):
        self.anki_manager = AnkiManager()
        self.vocabulary_manager = VocabularyManager()

        self.app = QApplication(sys.argv)
        self.main_window = MainWindow(self.vocabulary_manager, self.anki_manager)

    def start(self):
        self.main_window.show()
        sys.exit(self.app.exec())

    def quick_init(self, words_file):
        path = "data/input/" + words_file
        with open(path, encoding="utf-8") as file:
            lines = file.readlines()
            for line in lines:
                if line[-1] == "\n":
                    line = line[:-1]
                self.vocabulary_manager.add_word_quick_init(line)
        self.start()
        

if __name__ == "__main__":
    app = App()
    if len(sys.argv) > 1 and sys.argv[1] == "--quick-init":
        app.quick_init(sys.argv[2])
    else:
        app.start()

    
    
    
        
    
    