from PyQt6.QtWidgets import QTableView

from .menu import SentenceTableViewMenu

from ....card.dialog import CardDialog

from PyQt6.QtWidgets import QHeaderView


class SentenceTableView(QTableView):
    """Table view for the different sentences of one vocabulary."""
    
    def __init__(self, central_widget, vocabulary_manager, main_card_view = None):
        super().__init__(central_widget)
        self.card_text_view = main_card_view
        
        self.setEditTriggers(self.EditTrigger.NoEditTriggers) # Disable editing
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        self.menu = SentenceTableViewMenu(self, vocabulary_manager)
        self.card_dialog = CardDialog(central_widget, main_card_view)

        self.clicked.connect(self.clicked_action)
        self.doubleClicked.connect(self.double_clicked_action)
        
    def contextMenuEvent(self, event):
        """
        Opens the context menu at the position of the mouse event.

        Args:
        -----
        event : QContextMenuEvent
            The event object containing the position of the mouse click.
        """
        row = self.rowAt(event.pos().y())
        column = self.columnAt(event.pos().x())

        self.menu.set_current_position(row, column)
        self.menu.exec(event.globalPos())

    def clicked_action(self):
        """When a sentence is double-clicked, update card view."""
        sentence_clicked = self.model().get_sentence_by_row(self.currentIndex().row())
        self.card_text_view.set_card_view(sentence_clicked,
            sentence_clicked.position_kanji_sentence,
            sentence_clicked.kanji_data)
            # ,True)
    
    def double_clicked_action(self):
        """When a sentence is double-clicked, opens a new CardDialog to edit its fields."""
        row = self.currentIndex().row()
        sentence = self.model().get_sentence_by_row(row)

        self.card_dialog.update(self.model(), sentence, row)
        self.card_dialog.open()
