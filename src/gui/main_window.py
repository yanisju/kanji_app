
from PyQt6.QtWidgets import QMainWindow, QToolBar, QFormLayout, QLineEdit, QStatusBar

from .central_widget import CentralWidget


class MainWindow(QMainWindow):
    def __init__(self, vocabulary_manager, anki_manager):
        super().__init__(None)
        self.setWindowTitle("Vocanki")
        self._resize_and_center()
        
        centralWidget = CentralWidget(self, vocabulary_manager, anki_manager) 
        self.setCentralWidget(centralWidget)
    
        self._createMenu()
        # self._createToolBar()
        self._createStatusBar()

    def _createMenu(self):
        menu = self.menuBar().addMenu("&Menu")
        menu.addAction("&Exit", self.close)

    def _createToolBar(self):
        tools = QToolBar(parent=self)
        layout = QFormLayout()
        layout.addRow("Name:", QLineEdit())
        
        tools.addWidget(layout)
        self.addToolBar(tools)

    def _createStatusBar(self):
        status = QStatusBar()
        status.showMessage("I'm the Status Bar")
        self.setStatusBar(status)

    def _resize_and_center(self):
        screen_rect = self.screen().availableGeometry()
        self.resize(screen_rect.width() - 200, screen_rect.height() - 100)

        x_center = int((screen_rect.width() - self.width()) / 2)
        y_center = int((screen_rect.height()-self.height()) / 2)
        self.move(x_center, y_center)


