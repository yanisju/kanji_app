from . import AddEmptySentenceAction

class AddEmptySentenceVocabularyAction(AddEmptySentenceAction):
    def __init__(self, parent, vocabulary_manager):
        super().__init__(parent, vocabulary_manager)

    def _action(self):
        vocabulary = self.parent().parent().model().vocabulary
        vocabulary.add_sentence("", "", dict())