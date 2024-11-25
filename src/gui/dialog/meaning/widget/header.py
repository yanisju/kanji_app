from PyQt6.QtWidgets import QGroupBox, QVBoxLayout, QLabel

from .meaning.spin_box import MeaningSpinBox

class DialogMeaningHeader(QGroupBox):
    def __init__(self, parent):
        super().__init__(parent)
        layout = QVBoxLayout(self)

        label = QLabel("Word Meanings", self)
        label.setProperty("class", "title")
        layout.addWidget(label)

        self.selection_spin_box = MeaningSpinBox(parent)
        layout.addWidget(self.selection_spin_box)
