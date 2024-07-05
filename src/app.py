from .vocabulary.manager import VocabularyManager
from .gui.main_window import MainWindow
from PyQt6.QtWidgets import QApplication
from .anki.manager import AnkiManager


import sys

class App:
    def __init__(self):
        pass

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    
    main_window.show()
    
    sys.exit(app.exec())