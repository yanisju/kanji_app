from PyQt6.QtWidgets import QDialog, QWidget, QFormLayout, QVBoxLayout, QLabel, QLineEdit

class DeckOptionsDialog(QDialog):
    def __init__(self, parent: QWidget, anki_manager) -> None:
        super().__init__(parent)
        self.anki_manager = anki_manager
        self.setWindowTitle("Deck Options")
        self._configure()

    def _configure(self):
        layout = QVBoxLayout(self)
        self.setLayout(layout)
        deck_attributes_form_layout = QFormLayout()
        layout.addLayout(deck_attributes_form_layout)

        line_edit = QLineEdit()
        line_edit.setText(str(self.anki_manager.deck_id))
        line_edit.textEdited.connect(self._deck_id_changed)
        deck_attributes_form_layout.addRow(QLabel("Deck ID: "), line_edit)

        line_edit = QLineEdit()
        line_edit.setText(self.anki_manager.deck_name)
        line_edit.textEdited.connect(self._deck_name_changed)
        deck_attributes_form_layout.addRow(QLabel("Deck Name: "), line_edit)


    def _deck_id_changed(self, id):
        self.anki_manager.deck_id = id

    def _deck_name_changed(self, name):
        self.anki_manager.deck_name = name