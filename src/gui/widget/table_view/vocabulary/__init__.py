from PyQt6.QtWidgets import QTableView
from .menu import VocabularyTableViewMenu

class VocabularyTableView(QTableView):

    def __init__(self, vocabulary_manager, parent = None) -> None:
        super().__init__()
        self.setModel(vocabulary_manager.vocabulary_model)
        self.menu = VocabularyTableViewMenu(self, vocabulary_manager)
        
        view_item_selection = self.selectionModel()
    
        view_item_selection.selectionChanged.connect(lambda x: vocabulary_manager.refresh_sentence_model(self.currentIndex().row())) # Change sentences view to current word
        
    def contextMenuEvent(self, event):
        row = self.rowAt(event.pos().y())
        column = self.columnAt(event.pos().x())

        self.menu.set_current_position(row, column)

        self.menu.exec(event.globalPos())