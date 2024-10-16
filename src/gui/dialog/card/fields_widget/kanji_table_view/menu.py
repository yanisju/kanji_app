from PyQt6.QtWidgets import QMenu
from .action.add_kanji import AddKanjiAction
from .action.delete_one_kanji import DeleteOneKanjiAction
from .action.delete_all_kanjis import DeleteAllKanjisAction


class KanjiTableViewMenu(QMenu):
    """Menu displayed when user right-clicks on sentence table view. """
    def __init__(self, parent):
        super().__init__(parent)
        self.row = -1
        self.column = -1
        self._set_actions()

    def _set_actions(self):
        """Set actions data and behaviors."""
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

        # if self.parent().model().rowCount() == 0:
        #     self.del_all_sentence_action.setEnabled(False)
        # else:
        #     self.del_all_sentence_action.setEnabled(True)
                

        if(row == -1):
            self.remove_kanji_action.setEnabled(False)
        else:
            self.remove_kanji_action.setEnabled(True)