from PyQt6.QtWidgets import QTableView, QHeaderView
from PyQt6.QtCore import QItemSelectionModel

from .menu import KanjiTableViewMenu


class KanjiTableView(QTableView):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents)
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

        rows_columns = self._get_selected_rows_columns()
        self.menu.set_current_position(rows_columns)
        self.menu.exec(event.globalPos())

    def _get_selected_rows_columns(self):
        model_indexes = self.selectionModel().selectedIndexes()
        row_column_pairs = [(index.row(), index.column())
                            for index in model_indexes]
        row_column_pairs.sort(key=lambda pair: pair[0])
        return row_column_pairs
