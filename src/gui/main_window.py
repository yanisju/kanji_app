
from PyQt6.QtWidgets import QMainWindow, QWidget, QGridLayout, QToolBar, QFormLayout, QLineEdit, QStatusBar

from .up_right_widget import UpRightWidget
from .up_left_widget import UpLeftWidget
from .card.view.view import CardView

from .card.dialog import CardDialog

from .sentence_view import SentenceTableView

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
    
    def _add_words_to_list_model(self, words, list_model):
        words_to_add = []
        for word in words:
            words_to_add.append(word)
        list_model.setStringList(words)
        
    
    def _create_window_skeleton(self):
        self.central_grid_layout = QGridLayout(self.centralWidget)
        self.centralWidget.setLayout(self.central_grid_layout)
        
        self.down_left_widget = CardView()
        self.card_dialog = CardDialog(self.centralWidget, self.down_left_widget)
        self.up_left_widget = UpLeftWidget(self.centralWidget, self.vocabulary_manager, self.card_dialog)
        self.up_right_widget = UpRightWidget(self.centralWidget, self.vocabulary_manager, self.up_left_widget, self._anki_manager)
        self.down_right_widget = SentenceTableView(self.vocabulary_manager.sentence_added_model, self.card_dialog, self.vocabulary_manager)
        


        self.down_left_widget.refresh_when_clicked(self.up_left_widget.sentence_view)
        self.down_left_widget.refresh_when_clicked(self.down_right_widget)
        # self.down_left_widget.set_card_view()

        self.central_grid_layout.addWidget(self.up_left_widget, 0, 0)
        self.central_grid_layout.addWidget(self.up_right_widget, 0, 1)
        self.central_grid_layout.addWidget(self.down_left_widget, 1, 0)
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


