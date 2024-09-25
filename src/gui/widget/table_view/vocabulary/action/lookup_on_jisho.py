from PyQt6.QtGui import QAction, QIcon

import webbrowser

class LookupOnJishoAction(QAction):
    def __init__(self, parent, vocabulary_manager) -> None:
        super().__init__(parent)
        self.vocabulary_manager = vocabulary_manager
        self.setText("Lookup on Jisho")
        self.setIcon(QIcon("data/icons/magnifying_glass.png"))
        
        self.triggered.connect(self._action)

    def _action(self):
        word = self.vocabulary_manager.get_word(self.parent().row)
        url = "https://jisho.org/search/" + word
        webbrowser.open(url, 0)