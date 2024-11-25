from PyQt6.QtWidgets import QWidget, QHBoxLayout

from .text_view import MeaningTextView
from .table_view import MeaningTableView

class MeaningWidget(QWidget):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        layout = QHBoxLayout(self)
        self.meaning_view = MeaningTextView(self)
        layout.addWidget(self.meaning_view)

        self.table_view = MeaningTableView(self)
        layout.addWidget(self.table_view)

    def set_to_new_vocabulary(self, meaning_model):
        self.table_view.setModel(meaning_model)
        self.meaning_view.set_text(meaning_model)