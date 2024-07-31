from PyQt6.QtGui import QStandardItemModel, QStandardItem

class KanjiModel(QStandardItemModel):
    """Model containg kanjis, theirs readings and theirs meanings for TableView."""

    def __init__(self, kanji_readings: dict, main_word, main_word_meanings):
        super().__init__(0,0)
        
        for kanji in kanji_readings.keys():
            if kanji == main_word:
                self.appendRow([QStandardItem(kanji), QStandardItem(kanji_readings[kanji]), QStandardItem(main_word_meanings)])
            else:
                self.appendRow([QStandardItem(kanji), QStandardItem(kanji_readings[kanji])])
    
    def get_kanji_data(self):
        """Return a dictionnary containing kanji as keys, and a lsit containing theirs readings and meanings. """
        dict = {}
        for i in range(self.rowCount()):
            dict[self.item(i, 1).text()] = [self.item(i, 1).text(), self.item(i, 2).text()]
        return dict