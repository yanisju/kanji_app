from .vocabulary.manager import VocabularyManager
from .gui.main_window import MainWindow
from PyQt6.QtWidgets import QApplication
from .anki import AnkiManager

import sys

class App:
    def __init__(self):
        anki_manager = AnkiManager()
        self.vocabulary_manager = VocabularyManager()

        self.app = QApplication(sys.argv)
        self.main_window = MainWindow(self.vocabulary_manager, anki_manager)

    def start(self):
        self._resize_and_center()
        self.main_window.show()
        sys.exit(self.app.exec())
    
    def _resize_and_center(self):
        screen_rect = self.main_window.screen().availableGeometry()
        self.main_window.resize(screen_rect.width() - 200, screen_rect.height() - 100)

        x_center = int((screen_rect.width() - self.main_window.width()) / 2)
        y_center = int((screen_rect.height()-self.main_window.height()) / 2)
        self.main_window.move(x_center, y_center)

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

    
    
    
        
    
    