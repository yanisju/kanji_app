from . import AddEmptySentenceAction

class AddEmptySentenceDeckAction(AddEmptySentenceAction):
    def __init__(self, parent, vocabulary_manager):
        super().__init__(parent, vocabulary_manager)

    def _action(self):
        sentence = self.vocabulary_manager.sentence_added_model
        self.vocabulary_manager.sentence_added_model.append_sentence()