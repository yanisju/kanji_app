from PyQt6.QtGui import QStandardItemModel, QStandardItem

class KanjiModel(QStandardItemModel):
    """Model containg kanjis, theirs readings and theirs meanings for TableView."""

    def __init__(self, kanji_data: dict):
        super().__init__(0,0)
        
        for kanji in kanji_data.keys():
            reading, meaning, _ = kanji_data[kanji]
            self.appendRow([QStandardItem(kanji), QStandardItem(reading), QStandardItem(meaning)])
    
    def get_kanji_data(self):
        """Return a dictionnary containing kanji as keys, and a list containing theirs readings and meanings. """
        dict = {}
        for i in range(self.rowCount()):
            print(self.item(i, 0).text())
            print(self.item(i, 1).text())
            print(self.item(i, 2).text())
            dict[self.item(i, 0).text()] = (self.item(i, 1).text(), self.item(i, 2).text(), i)
        return dict