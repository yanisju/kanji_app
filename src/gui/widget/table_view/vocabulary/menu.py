from PyQt6.QtWidgets import QMenu
from .action.del_one_vocabulary import DeleteVocabularyAction
from .action.delete_all_vocabularies import DeleteAllVocabulariesAction

class VocabularyTableViewMenu(QMenu):
    """Menu displayed when user right-clicks on vocabulary table view. """
    
    def __init__(self, parent, vocabulary_manager):
        super().__init__(parent)
        self.row = -1
        self.column = -1

        self.set_actions(vocabulary_manager)
        

    def set_actions(self, vocabulary_manager):
        self.del_one_vocabulary_action = DeleteVocabularyAction(self)
        self.addAction(self.del_one_vocabulary_action)
        self.del_one_vocabulary_action.triggered.connect(lambda: vocabulary_manager.delete_vocabulary(self.row))

        self.del_every_vocabulary_action = DeleteAllVocabulariesAction(self)
        self.addAction(self.del_every_vocabulary_action)
        self.del_every_vocabulary_action.triggered.connect(lambda: vocabulary_manager.delete_all_vocabularies())
    
    def set_current_position(self, row: int, column: int):
        self.row = row
        self.column = column

        if(row == -1):
            self.del_one_vocabulary_action.setEnabled(False)
        else:
            self.del_one_vocabulary_action.setEnabled(True)
