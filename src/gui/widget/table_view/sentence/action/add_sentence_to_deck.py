from PyQt6.QtGui import QAction, QIcon

class AddSentenceToDeckAction(QAction):
    def __init__(self, parent, vocabulary_manager):
        super().__init__(parent)
        self.vocabulary_manager = vocabulary_manager
        self.setText("Add Sentence To Deck")
        self.setIcon(QIcon("data/icons/plus.png"))

        self.triggered.connect(self._action)

    def _action(self):
        vocabulary = self.parent().parent().model().vocabulary
        sentence = vocabulary.get_sentence(self.parent().row)
        self.vocabulary_manager.add_sentence_to_deck(sentence)