from PyQt6.QtWidgets import QTableView
from PyQt6.QtGui import QFont

from .menu import SentenceTableViewMenu

from ....card.dialog import CardDialog

from PyQt6.QtWidgets import QHeaderView


class SentenceTableView(QTableView):
    """Table view for the different sentences of one vocabulary."""
    
    def __init__(self, central_widget, model, vocabulary_manager, main_card_view = None):
        super().__init__(central_widget)
        self.model_on = model
        self.setModel(model)
        self.card_text_view = main_card_view

        font = QFont()
        font.setPointSize(11)
        self.setFont(font)
        
        self.setEditTriggers(self.EditTrigger.NoEditTriggers) # Disable editing
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        self.menu = SentenceTableViewMenu(self, vocabulary_manager)
        
        self.card_dialog = CardDialog(central_widget, main_card_view)

        self.clicked.connect(self.clicked_action)
        self.doubleClicked.connect(self.double_clicked_action)
        
    def contextMenuEvent(self, event):
        row = self.rowAt(event.pos().y())
        column = self.columnAt(event.pos().x())

        self.menu.set_current_position(row, column)

        self.menu.exec(event.globalPos())

    def clicked_action(self):
        """When a sentence is double-clicked, update card view."""
        sentence_clicked = self.model_on.get_sentence_by_row(self.currentIndex().row())
        self.card_text_view.set_card_view(sentence_clicked,
            sentence_clicked.position_kanji_sentence,
            sentence_clicked.kanji_data,
            True)
    
    def double_clicked_action(self):
        """When a sentence is double-clicked, opens a new CardDialog to edit its fields."""
        row = self.currentIndex().row()
        sentence = self.model_on.get_sentence_by_row(row)

        self.card_dialog.update(self.model_on, sentence, row)
        self.card_dialog.open()
