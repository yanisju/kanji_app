from PyQt6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QPushButton, QTableView
from .text_view import MeaningTextView

from .utils import get_copy_standard_item_model

class MeaningDialog(QDialog):
    def __init__(self, parent, flags = None) -> None:
        super().__init__(parent)
        self._init_layout()

    def _init_layout(self):
        self.layout = QVBoxLayout(self) # Main layout of Dialog
        self.setLayout(self.layout)

        meaning_layout = QHBoxLayout() # Layout for card view and fields 
        self.layout.addLayout(meaning_layout)

        self.meaning_view = MeaningTextView()
        meaning_layout.addWidget(self.meaning_view)

        self.table_view = QTableView()
        meaning_layout.addWidget(self.table_view)

        buttons_layout = QHBoxLayout() # Layout for bottom buttons
        self.layout.addLayout(buttons_layout)
        self._init_buttons_layout(buttons_layout)

    def _init_buttons_layout(self, layout):
        self.confirm_button = QPushButton("Confirm")
        self.cancel_button = QPushButton("Cancel")
        layout.addWidget(self.confirm_button)
        layout.addWidget(self.cancel_button)
        self.confirm_button.clicked.connect(self._confirm_button_clicked) 
        self.cancel_button.clicked.connect(self.reject)

    def _confirm_button_clicked(self):
        # TODO: complete
        self.accept()

    def open(self, meaning_model):
        # TODO: clone it
        self.meaning_model = get_copy_standard_item_model(meaning_model)
        self.table_view.setModel(self.meaning_model)   
        self.meaning_view.set_text(self.meaning_model)
        super().open()

    