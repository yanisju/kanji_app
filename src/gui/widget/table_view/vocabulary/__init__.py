from PyQt6.QtWidgets import QTableView, QHeaderView
from PyQt6.QtGui import QFont

from .menu import VocabularyTableViewMenu
from ....meaning_dialog import MeaningDialog



class VocabularyTableView(QTableView):
    """
    A custom QTableView for displaying and managing vocabulary items in a table format.

    This class is designed to allow users to view vocabulary words,
    display a context menu, edit word meanings through a dialog interface and interact with VocabularyManager.

    Attributes:
    -----------
    vocabulary_manager : VocabularyManager
        The manager responsible for handling the vocabulary data and model.
    menu : VocabularyTableViewMenu
        The context menu for interacting with table items.
    meaning_dialog : MeaningDialog
        A dialog for viewing and modifying vocabulary meanings.
    
    Methods:
    --------
    contextMenuEvent(event):
        Displays a context menu at the position of the mouse event.
    
    _double_clicked():
        Opens the `MeaningDialog` when a row in the table is double-clicked.
    
    _meaning_dialog_confirm_action(model: QStandardItemModel, current_selection: int):
        Updates the vocabulary item based on the confirmed selection from the `MeaningDialog`.
    """

    def __init__(self, vocabulary_manager) -> None:
        """
        Initializes the VocabularyTableView instance with the given vocabulary manager.

        Args:
        -----
        vocabulary_manager : VocabularyManager
            The manager responsible for providing the vocabulary data model and operations.
        """
        super().__init__()
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)

        font = QFont()
        font.setPointSize(11)
        self.setFont(font)

        self.vocabulary_manager = vocabulary_manager
        self.setModel(vocabulary_manager.vocabulary_model)
        self.setEditTriggers(self.EditTrigger.NoEditTriggers)

        self.menu = VocabularyTableViewMenu(self, vocabulary_manager)
        self.meaning_dialog = MeaningDialog(self)
        self.meaning_dialog.confirm_button_clicked_signal.connect(self._meaning_dialog_confirm_action)
        self.doubleClicked.connect(self._double_clicked)

        # Change sentence view when a different word is selected
        view_item_selection = self.selectionModel()
        view_item_selection.selectionChanged.connect(lambda x: vocabulary_manager.refresh_sentence_model(self.currentIndex().row()))

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

    def _double_clicked(self):
        """
        Handles the event when a table row is double-clicked.
        
        Opens the `MeaningDialog` to allow editing of the vocabulary item's meaning.
        """
        row = self.currentIndex().row()
        vocabulary = self.vocabulary_manager[row]
        self.meaning_dialog.open(vocabulary)

    def _meaning_dialog_confirm_action(self, model, current_selection: int):
        """
        Handles the confirmation of a new meaning selection from the `MeaningDialog`.

        Args:
        -----
        model : QStandardItemModel
            The data model containing the updated meanings.
        current_selection : int
            The index of the selected meaning from the dialog.
        
        Modifies the selected vocabulary item's meaning and updates the table view.
        """
        row = self.currentIndex().row()
        self.vocabulary_manager[row].set_meaning_standard_item(model)  # Modify the StandardItemModel of the vocabulary

        # Update the current selection for the meaning object
        self.vocabulary_manager[row].meaning_object.current_selection = current_selection
        new_meaning = model.data(model.index(current_selection - 1, 0))
        new_part_of_speech = model.data(model.index(current_selection - 1, 1))

        # Update the vocabulary model in the table view
        self.vocabulary_manager.vocabulary_model.modify_row(row, new_meaning, new_part_of_speech)
