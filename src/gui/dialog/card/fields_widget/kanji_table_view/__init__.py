from PyQt6.QtWidgets import QTableView

from PyQt6.QtWidgets import QHeaderView

class KanjiTableView(QTableView):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
    