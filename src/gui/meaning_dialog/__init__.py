from PyQt6.QtWidgets import QDialog, QHBoxLayout, QVBoxLayout, QPushButton, QTableView, QHeaderView, QFormLayout, QLabel
from PyQt6.QtGui import QStandardItemModel, QFont
from PyQt6.QtCore import pyqtSignal

from .text_view import MeaningTextView
from .selection_spin_box import SelectionSpinBox

from .utils import get_copy_standard_item_model

class MeaningDialog(QDialog):
    confirm_button_clicked_signal = pyqtSignal(QStandardItemModel, int)

    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setWindowTitle("Word Meaning Editor")

        font = QFont()
        font.setPointSize(11)
        self.setFont(font)
        self.resize(int(parent.parent().width() * 0.6), int(parent.parent().height() * 0.6))
        self.current_selection = 1
        self._init_layout()

    def _init_layout(self):
        layout = QVBoxLayout(self) # Main layout of Dialog
        self.setLayout(layout)

        
        label = QLabel("Current Selection: ", self)
        self.spin_box = SelectionSpinBox()
        self.spin_box.valueChanged.connect(self._set_current_selection)
        form_layout = QFormLayout()
        form_layout.addRow(label, self.spin_box)
        layout.addLayout(form_layout)
        
        meaning_layout = QHBoxLayout() # Layout for card view and fields 
        layout.addLayout(meaning_layout)

        self.meaning_view = MeaningTextView()
        meaning_layout.addWidget(self.meaning_view)

        self.table_view = QTableView()
        self.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        
        meaning_layout.addWidget(self.table_view)

        buttons_layout = QHBoxLayout() # Layout for bottom buttons
        layout.addLayout(buttons_layout)
        self._init_buttons_layout(buttons_layout)

    def _set_current_selection(self, new_current_selection):
        self.current_selection = new_current_selection

    def _init_buttons_layout(self, layout):
        self.confirm_button = QPushButton("Confirm")
        cancel_button = QPushButton("Cancel")
        layout.addWidget(self.confirm_button)
        layout.addWidget(cancel_button)
        self.confirm_button.clicked.connect(self._confirm_button_clicked) 
        cancel_button.clicked.connect(self.reject)

    def _confirm_button_clicked(self):
        self.confirm_button_clicked_signal.emit(self.table_view.model(), 
                                                self.current_selection)
        self.accept()

    
    def open(self, vocabulary):
        self.vocabulary = vocabulary
        meaning_object = vocabulary.meaning_object

        self.current_selection = meaning_object.current_selection
        self.meaning_model = get_copy_standard_item_model(meaning_object.standard_item_model)
        self.table_view.setModel(self.meaning_model)   
        self.meaning_view.set_text(self.meaning_model)

        self.spin_box.refresh(self.current_selection, self.meaning_model.rowCount())
        super().open()