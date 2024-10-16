from PyQt6.QtWidgets import QTableView
from PyQt6.QtWidgets import QHeaderView

from .menu import KanjiTableViewMenu

class KanjiTableView(QTableView):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        self.menu = KanjiTableViewMenu(self)

    def set_to_new_sentence(self, sentence):
        self.kanji_data = sentence.kanji_data
        self.setModel(sentence.kanji_data.model)

    
    def contextMenuEvent(self, event):
        """
        Opens the context menu at the position of the mouse event.

        Args:
        -----
        event : QContextMenuEvent
            The event object containing the position of the mouse click.
        """
        row = self.rowAt(event.pos().y())
        column = self.columnAt(event.pos().x())

        self.menu.set_current_position(row, column)
        self.menu.exec(event.globalPos())