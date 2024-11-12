from PyQt6.QtGui import QAction, QIcon

class MergeKanjisAction(QAction):
    def __init__(self, parent) -> None:
        super().__init__(parent)
        self.setText("Merge Kanjis")
        self.setIcon(QIcon("data/icons/merge.png"))
        
        self.triggered.connect(self._action)

    def _action(self):
        rows_columns = self.parent().rows_columns
        rows = []
        for i in range(len(rows_columns)):
            rows.append(rows_columns[i][0])
        self.parent().parent().model().kanji_data.merge_kanjis(rows)
