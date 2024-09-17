from PyQt6.QtWidgets import QTableView
from .menu import VocabularyTableViewMenu
from ....meaning_dialog import MeaningDialog

class VocabularyTableView(QTableView):
    """Table view for the vocabulary."""

    def __init__(self, vocabulary_manager) -> None:
        super().__init__()

        self.vocabulary_manager = vocabulary_manager
        self.setModel(vocabulary_manager.vocabulary_model)
        self.setEditTriggers(self.EditTrigger.NoEditTriggers)

        self.menu = VocabularyTableViewMenu(self, vocabulary_manager)
        self.meaning_dialog = MeaningDialog(self)
        self.meaning_dialog.confirm_button_clicked_signal.connect(self._meaning_dialog_confirm_action)
        self.doubleClicked.connect(self._double_clicked)

        view_item_selection = self.selectionModel()
        view_item_selection.selectionChanged.connect(lambda x: vocabulary_manager.refresh_sentence_model(self.currentIndex().row())) # Change sentences view to current word
        
    def contextMenuEvent(self, event):
        row = self.rowAt(event.pos().y())
        column = self.columnAt(event.pos().x())

        self.menu.set_current_position(row, column)

        self.menu.exec(event.globalPos())

    def _double_clicked(self):
        row = self.currentIndex().row()
        vocabulary = self.vocabulary_manager[row]
        self.meaning_dialog.open(vocabulary)

    def _meaning_dialog_confirm_action(self, model, current_selection: int):
        """When MeaningDialog confirm button is clicked, modify Vocabulary meaning """
        row = self.currentIndex().row()
        self.vocabulary_manager[row].set_meaning_standard_item(model) # Modify StandardItemModel of Vocabulary

        self.vocabulary_manager[row].meaning_object.current_selection = current_selection
        new_meaning = model.data(model.index(current_selection - 1, 0))
        new_part_of_speech = model.data(model.index(current_selection - 1, 1))
        self.vocabulary_manager.vocabulary_model.modify_row(row, new_meaning, new_part_of_speech)
