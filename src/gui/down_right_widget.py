from PyQt6.QtWidgets import QTableView

class DownRightWidget(QTableView):
    def __init__(self, central_widget, vocabulary_manager):
        super().__init__(central_widget)
        self.vocabulary_manager = vocabulary_manager
        self.init_view()

    def init_view(self):
        self.setModel(self.vocabulary_manager.sentence_added_model)

