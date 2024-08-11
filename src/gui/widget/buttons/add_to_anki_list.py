from PyQt6.QtWidgets import QPushButton

class AddToAnkiListButton(QPushButton):
    def __init__(self, sentence_view, vocabulary_manager):
        super().__init__()
        self.sentence_view = sentence_view
        self.vocabulary_manager = vocabulary_manager
        self.setText("Add to Anki List")
        self.clicked.connect(self._add_to_anki_list_action)
    
    def _add_to_anki_list_action(self):
        row_number = self.sentence_view.currentIndex().row()
        sentence_to_clone = self.vocabulary_manager.sentence_model.get_sentence_by_row(row_number) # Original sentence
        sentence_to_add = sentence_to_clone.clone()
        self.vocabulary_manager.sentence_added_model.append_sentence(sentence_to_add)