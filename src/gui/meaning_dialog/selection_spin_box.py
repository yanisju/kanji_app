from PyQt6.QtWidgets import QSpinBox, QWidget

class SelectionSpinBox(QSpinBox):
    def __init__(self) -> None:
        super().__init__(None)
        self.setMinimum(1)

    def refresh(self, current_selection, row_length):
        """Refresh values and set maximum of SpinBox."""
        self.setValue(current_selection)
        self.setMaximum(row_length)