from PyQt6.QtWidgets import QWidget, QTableView, QHeaderView
from PyQt6.QtCore import QSize


class MeaningTableView(QTableView):
    def __init__(self, parent: QWidget) -> None:
        super().__init__(parent)

        with open("styles/meaning/table_view.css", "r") as css_file:
            self.setStyleSheet(css_file.read())
    
    def _configure_header_section(self):
        self.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Fixed)
        
        width = self.horizontalHeader().width()
        self.setColumnWidth(0, int(width * 0.8))
        self.setColumnWidth(1, int(width * 0.2))
        
        self.horizontalHeader().setStretchLastSection(True)
        
    def sizeHint(self):
        width = int(self.parentWidget().width() * 0.6)
        height = int(self.parentWidget().height())
        return QSize(width, height)
    
    def resizeEvent(self, event):
        super().resizeEvent(event)
        self._configure_header_section()