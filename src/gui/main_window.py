
from PyQt6.QtWidgets import QMainWindow, QWidget, QGridLayout

from .up_right_widget import UpRightWidget
from .up_left_widget import UpLeftWidget
from .down_left_widget import DownLeftWidget

from .card.dialog import CardDialog

from .sentence_view import SentenceView

class MainWindow(QMainWindow):
    def __init__(self, vocabulary_manager):
        super().__init__(parent=None)
        self.setWindowTitle("Vocanki")
        
        self.centralWidget = QWidget(self)  # Central widget
        self.setCentralWidget(self.centralWidget)
        
        self.vocabulary_manager = vocabulary_manager
    
        self._create_window_skeleton()
    
    def _add_words_to_list_model(self, words, list_model):
        words_to_add = []
        for word in words:
            words_to_add.append(word)
        list_model.setStringList(words)
        
    
    def _create_window_skeleton(self):
        self.central_grid_layout = QGridLayout(self.centralWidget)
        self.centralWidget.setLayout(self.central_grid_layout)

        self.card_dialog = CardDialog(self.centralWidget)
        
        self.up_left_widget = UpLeftWidget(self.centralWidget, self.vocabulary_manager, self.card_dialog)
        self.up_right_widget = UpRightWidget(self.centralWidget, self.vocabulary_manager, self.up_left_widget)
        self.down_left_widget = DownLeftWidget(self.centralWidget)
        self.down_right_widget = SentenceView(self.vocabulary_manager.sentence_added_model, self.card_dialog, self.vocabulary_manager)
        
        self.central_grid_layout.addWidget(self.up_left_widget, 0, 0)
        self.central_grid_layout.addWidget(self.up_right_widget, 0, 1)
        self.central_grid_layout.addWidget(self.down_left_widget, 1, 0)
        self.central_grid_layout.addWidget(self.down_right_widget, 1, 1)

        
    
    # def _createMenu(self):
    #     menu = self.menuBar().addMenu("&Menu")
    #     menu.addAction("&Exit", self.close)

    # def _createToolBar(self):
    #     tools = QToolBar(parent=self)
    #     layout = QFormLayout()
    #     layout.addRow("Name:", QLineEdit())
        
    #     tools.addWidget(layout)
    #     self.addToolBar(tools)

    # def _createStatusBar(self):
    #     status = QStatusBar()
    #     status.showMessage("I'm the Status Bar")
    #     self.setStatusBar(status)


