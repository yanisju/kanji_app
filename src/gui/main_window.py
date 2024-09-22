
from PyQt6.QtWidgets import QMainWindow, QWidget, QGridLayout, QToolBar, QFormLayout, QLineEdit, QStatusBar
from PyQt6.QtGui import QScreen

from .widget.vocabulary import VocabularyWidget
from .widget.sentence import SentenceWidget

from .widget.action import ActionWiget
from .widget.sentence_rendering import SentenceRenderingWidget
from .card.text_view import CardTextView

from .widget.table_view.sentence import SentenceTableView

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
        # self.setContentsMargins(0, 0, 0, 0)
        self.central_grid_layout = QGridLayout(self.centralWidget)
        self.centralWidget.setLayout(self.central_grid_layout)
        
        self.central_grid_layout.setColumnStretch(0, 10)
        self.central_grid_layout.setColumnStretch(1, 1)
        
        self.central_grid_layout.setContentsMargins(5, 5, 5, 5)  # Réduit les marges autour de la grille
        # self.central_grid_layout.setSpacing(1)
        
        self.sentence_rendering_widget = SentenceRenderingWidget(self.centralWidget)
        self.vocabulary_widget = VocabularyWidget(self.centralWidget, self.vocabulary_manager)
        self.sentence_widget = SentenceWidget(self.centralWidget, "Sentence List",self.vocabulary_manager.sentence_model,self.vocabulary_manager, self.sentence_rendering_widget.card_text_view)
        self.added_sentence_widget = SentenceWidget(self.centralWidget, "Added Sentence List", self.vocabulary_manager.sentence_added_model,self.vocabulary_manager, self.sentence_rendering_widget.card_text_view)
        self.action_widget = ActionWiget(self.centralWidget, self.vocabulary_manager, self.sentence_widget, self._anki_manager)
        


        self.central_grid_layout.addWidget(self.vocabulary_widget, 0, 0)
        self.central_grid_layout.addWidget(self.action_widget, 0, 1)
        self.central_grid_layout.addWidget(self.sentence_widget, 1, 0)
        self.central_grid_layout.addWidget(self.added_sentence_widget, 1, 1)
        self.central_grid_layout.addWidget(self.sentence_rendering_widget, 2, 0, 1, 2)
        


        # self.up_right_widget.add_to_anki_list_button.add_to_anki_manager_signal.connect(self._anki_manager.add_sentence)
        # self.down_right_widget.card_dialog.confirm_button_clicked_signal.connect(self._anki_manager.modify_sentence)

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


