from PyQt6.QtWidgets import QPushButton
from ...dialog.deck_options import DeckOptionsDialog


class DeckOptionsButtons(QPushButton):
    def __init__(self, parent, anki_manager):
        super().__init__("Deck Options", parent)
        self.deck_option_dialog = DeckOptionsDialog(
            self.parent(), anki_manager)
        self.clicked.connect(self.deck_option_dialog.open)
