import sys
from PyQt6.QtWidgets import QMainWindow, QApplication, QWidget, QGridLayout

from .up_right_widget import UpRightWidget
from .up_left_widget import UpLeftWidget

from ..vocabulary.manager import Manager

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__(parent=None)
        self.setWindowTitle("Vocanki")
        
        self.centralWidget = QWidget(self)  # Central widget
        self.setCentralWidget(self.centralWidget)
        
        self.vocabulary_manager = Manager()
    
        self._create_window_skeleton()
    
    def _add_words_to_list_model(self, words, list_model):
        words_to_add = []
        for word in words:
            words_to_add.append(word)
        list_model.setStringList(words)
        
    
    def _create_window_skeleton(self):
        self.central_grid_layout = QGridLayout(self.centralWidget)
        self.centralWidget.setLayout(self.central_grid_layout)
        
        
        self.up_right_vertical_widget = UpRightWidget(self.centralWidget, self.vocabulary_manager)
        self.up_left_vertical_widget = UpLeftWidget(self.centralWidget, self.vocabulary_manager)
        
        self.central_grid_layout.addWidget(self.up_left_vertical_widget, 0, 0)
        self.central_grid_layout.addWidget(self.up_right_vertical_widget, 0, 1)
        # self._add_words_to_list_model(["test1", "test2"], self.up_left_vertical_layout.itemAt(0).model())
        
    
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    main_window = MainWindow()
    
    main_window.show()
    
    sys.exit(app.exec())
