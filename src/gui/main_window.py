
from PyQt6.QtWidgets import QMainWindow, QWidget, QGridLayout, QToolBar, QFormLayout, QLineEdit, QStatusBar

from .widget.up_right_widget import UpRightWidget
from .widget.up_left_widget import UpLeftWidget
from .card.text_view import CardTextView

from .widget.sentence_table_view import SentenceTableView

class MainWindow(QMainWindow):
    def __init__(self, vocabulary_manager, anki_manager):
        super().__init__(parent=None)
        self.setWindowTitle("Vocanki")
        
        self.centralWidget = QWidget(self)  # Central widget
        self.setCentralWidget(self.centralWidget)
        
        self.vocabulary_manager = vocabulary_manager
        self._anki_manager = anki_manager
    
        self._create_window_skeleton()
        self._createMenu()
        # self._createToolBar()
        self._createStatusBar()
        
    
    def _create_window_skeleton(self):
        self.central_grid_layout = QGridLayout(self.centralWidget)
        self.centralWidget.setLayout(self.central_grid_layout)
        
        self.card_text_view = CardTextView()
        self.up_left_widget = UpLeftWidget(self.centralWidget, self.vocabulary_manager, self.card_text_view)
        self.up_right_widget = UpRightWidget(self.centralWidget, self.vocabulary_manager, self.up_left_widget, self._anki_manager)
        self.down_right_widget = SentenceTableView(self.centralWidget, self.vocabulary_manager.sentence_added_model, self.vocabulary_manager, self.card_text_view)
        
        self.card_text_view.refresh_when_clicked(self.up_left_widget.sentence_view)
        self.card_text_view.refresh_when_clicked(self.down_right_widget)

        self.central_grid_layout.addWidget(self.up_left_widget, 0, 0)
        self.central_grid_layout.addWidget(self.up_right_widget, 0, 1)
        self.central_grid_layout.addWidget(self.card_text_view, 1, 0)
        self.central_grid_layout.addWidget(self.down_right_widget, 1, 1)
    
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


