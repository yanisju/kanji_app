from PyQt6.QtWidgets import QMenu
from .action.open_card_editor import OpenMeaningEditorAction
from .action.add_sentence_to_deck import AddSentenceToDeckAction
from .action.delete_one_sentence import DeleteOneSentenceAction
from .action.delete_all_sentences import DeleteAllSentenceAction
from .action.add_empty_sentence import AddEmptySentenceAction

class SentenceTableViewMenu(QMenu):
    """Menu displayed when user right-clicks on sentence table view. """
    def __init__(self, parent, vocabulary_manager, is_added_sentence):
        super().__init__(parent)
        self.row = -1
        self.column = -1
        self.is_added_sentence = is_added_sentence
        self._set_actions(vocabulary_manager)

    def _set_actions(self, vocabulary_manager):
        """Set actions data and behaviors."""

        self.open_card_editor_action = OpenMeaningEditorAction(self)
        self.addAction(self.open_card_editor_action)


        if not self.is_added_sentence:
            self.add_sentence_to_deck_action = AddSentenceToDeckAction(self, vocabulary_manager)
            self.addAction(self.add_sentence_to_deck_action)

        self.addSeparator()

        self.add_empty_sentence_action = AddEmptySentenceAction(self, vocabulary_manager)
        self.addAction(self.add_empty_sentence_action)

        self.addSeparator()

        self.del_one_sentence_action = DeleteOneSentenceAction(self)
        self.addAction(self.del_one_sentence_action)

        self.del_all_sentence_action = DeleteAllSentenceAction(self)
        self.addAction(self.del_all_sentence_action)
        

    def set_current_position(self, row: int, column: int):
        self.row = row
        self.column = column

        if self.parent().model().rowCount() == 0:
            self.del_all_sentence_action.setEnabled(False)
        else:
            self.del_all_sentence_action.setEnabled(True)
                

        if(row == -1):
            self.del_one_sentence_action.setEnabled(False)
        else:
            self.del_one_sentence_action.setEnabled(True)