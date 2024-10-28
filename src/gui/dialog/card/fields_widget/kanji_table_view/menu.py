from PyQt6.QtWidgets import QMenu
from .action.set_as_word1 import SetAsWord1Action
from .action.set_as_word2 import SetAsWord2Action
from .action.add_kanji import AddKanjiAction
from .action.look_up_on_jisho import LookupOnJishoAction
from .action.delete_one_kanji import DeleteOneKanjiAction
from .action.delete_all_kanjis import DeleteAllKanjisAction
from .action.add_to_vocabulary_list import AddToVocabularyListAction


class KanjiTableViewMenu(QMenu):
    """Menu displayed when user right-clicks on sentence table view. """
    def __init__(self, parent):
        super().__init__(parent)
        self.row = -1
        self.column = -1
        self._set_actions()

    def _set_actions(self):
        """Set actions data and behaviors."""
        self.set_as_word1_action = SetAsWord1Action(self)
        self.addAction(self.set_as_word1_action)

        self.set_as_word2_action = SetAsWord2Action(self)
        self.addAction(self.set_as_word2_action)

        self.addSeparator()

        self.add_to_vocabulary_list_action = AddToVocabularyListAction(self)
        self.addAction(self.add_to_vocabulary_list_action)

        self.look_up_on_jisho_action = LookupOnJishoAction(self)
        self.addAction(self.look_up_on_jisho_action)

        self.addSeparator()

        self.add_kanji_action = AddKanjiAction(self)
        self.addAction(self.add_kanji_action)

        self.addSeparator()

        self.remove_kanji_action = DeleteOneKanjiAction(self)
        self.addAction(self.remove_kanji_action)

        self.delete_all_kanjis_action = DeleteAllKanjisAction(self)
        self.addAction(self.delete_all_kanjis_action)



    def set_current_position(self, row: int, column: int):
        self.row = row
        self.column = column

        if(row == -1):
            self.remove_kanji_action.setEnabled(False)
            self.set_as_word1_action.setEnabled(False)
            self.set_as_word2_action.setEnabled(False)
            self.look_up_on_jisho_action.setEnabled(False)
        else:
            self.remove_kanji_action.setEnabled(True)
            self.set_as_word1_action.setEnabled(True)
            self.set_as_word2_action.setEnabled(True)
            self.look_up_on_jisho_action.setEnabled(True)