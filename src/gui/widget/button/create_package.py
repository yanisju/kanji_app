from PyQt6.QtWidgets import QPushButton

class CreatePackageButton(QPushButton):
    def __init__(self, anki_manager):
        super().__init__()
        self.setText("Create Package")
        self.clicked.connect(anki_manager.generate_deck)