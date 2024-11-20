from PyQt6.QtGui import QAction, QIcon

import webbrowser


class LookupOnJishoAction(QAction):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setText("Lookup on Jisho")
        self.setIcon(QIcon("data/icons/magnifying_glass.png"))

        self.triggered.connect(self._action)

    def _action(self):
        for row, _ in self.parent().rows_columns:
            word = self.parent().parent().model().item(row, 0).text()
            if word != "":
                url = "https://jisho.org/search/" + word
                webbrowser.open(url, 0)
