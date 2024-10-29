from PyQt6.QtGui import QAction, QIcon

class DeleteVocabularyAction(QAction):
    def __init__(self, parent, vocabulary_manager, sentence_rendering_widget, sentence_table_view) -> None:
        super().__init__(parent)
        self.vocabulary_manager = vocabulary_manager
        self.sentence_rendering_widget = sentence_rendering_widget
        self.sentence_table_view = sentence_table_view
        self.setText("Delete Vocabulary")
        self.setIcon(QIcon("data/icons/minus.png"))
        self.triggered.connect(self._action)

    def _action(self):
        """Delete vocabulary from vocabulary and check if one of the sentences of the vocabylary is currently printed in card text view."""
        self.vocabulary_manager.delete_vocabulary(self.parent().row)

        word = self.vocabulary_manager[(self.parent().row)]
        if self.sentence_table_view.model() == word.sentence_manager.sentences_model:
            self.sentence_table_view.setModel(None)
        