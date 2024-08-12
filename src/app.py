from .vocabulary.manager import VocabularyManager
from .gui.main_window import MainWindow
from PyQt6.QtWidgets import QApplication
from .anki import AnkiManager

import sys

class App:
    def __init__(self):
        pass

if __name__ == "__main__":
    anki_manager = AnkiManager()
    vocabulary_manager = VocabularyManager()
    

    app = QApplication(sys.argv)
    main_window = MainWindow(vocabulary_manager, anki_manager)
    
    main_window.show()
    
    sys.exit(app.exec())