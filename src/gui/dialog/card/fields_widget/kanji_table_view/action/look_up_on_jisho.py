from PyQt6.QtGui import QAction, QIcon

import webbrowser

class LookupOnJishoAction(QAction):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setText("Lookup on Jisho")
        self.setIcon(QIcon("data/icons/magnifying_glass.png"))
        
        self.triggered.connect(self._action)

    def _action(self):
        word = self.parent().parent().model().item(self.parent().row, 0).text()
        url = "https://jisho.org/search/" + word
        webbrowser.open(url, 0)