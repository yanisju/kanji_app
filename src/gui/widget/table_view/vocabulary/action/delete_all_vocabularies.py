from PyQt6.QtGui import QAction, QIcon

class DeleteAllVocabulariesAction(QAction):
    def __init__(self, parent, vocabulary_manager, sentence_rendering_widget) -> None:
        super().__init__(parent)
        self.vocabulary_manager = vocabulary_manager
        self.sentence_rendering_widget = sentence_rendering_widget
        self.setText("Delete all Vocabularies")
        self.setIcon(QIcon("data/icons/trashbin.png"))
        self.triggered.connect(self._action)

    def _action(self):
        self.vocabulary_manager.delete_all_vocabularies()
        self.sentence_rendering_widget.card_text_view.clear()

        