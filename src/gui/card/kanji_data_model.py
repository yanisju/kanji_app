from PyQt6.QtGui import QStandardItemModel, QStandardItem
from ...vocabulary.str_utils import *

class KanjiDataModel(QStandardItemModel):
    """Model containg kanjis, theirs readings and theirs meanings for TableView.
    self.kanji_data is a dictionnary containing in real time the data about kanjis: theirs readings / meanings / positions in view.
    """

    def __init__(self):
        super().__init__(0, 0)
        self.kanji_data = None
        self.position_kanji_sentence = None
        self.sentence = None
        self.itemChanged.connect(self.is_modified)

    def refresh(self, kanji_data: dict, sentence: str):
        """Refresh model with a new dictionnary containing kanjis data."""
        if self.kanji_data != None:  # If model is not empty
            self.clear()
        self.kanji_data = dict(sorted(kanji_data.items(), key=lambda item: item[1][2]))

        for kanji in self.kanji_data.keys():
            reading, meaning, _ = kanji_data[kanji]
            self.appendRow(
                [QStandardItem(kanji), QStandardItem(reading), QStandardItem(meaning)]
            )

        self.sentence = sentence

        self.position_kanji_sentence = get_position_kanji_sentence(self.sentence, self.kanji_data.keys())

    def is_modified(self, item):
        """Modify its own kanji_data dictionnary to fit with modifications."""

        index = self.indexFromItem(item)
        if index.column() != 0:  # If reading or meaning is modified
            kanji = self.item(index.row(), 0).text()

            if index.column() == 1:
                self.kanji_data[kanji] = (
                    item.text(),
                    self.kanji_data[kanji][1],
                    index.row(),
                )
            else:  # Modify meaning / index.column == 2
                self.kanji_data[kanji] = (
                    self.kanji_data[kanji][0],
                    item.text(),
                    index.row(),
                )
        else:  # If kanji is modified
            kanji_to_del = [
                item for item, v in self.kanji_data.items() if v[2] == index.row()
            ]
            self.kanji_data[item.text()] = self.kanji_data[kanji_to_del[0]]
            del self.kanji_data[kanji_to_del[0]]

        self.set_position_kanji_sentence(self.sentence, self.kanji_data.keys())

    def set_position_kanji_sentence(self, sentence, kanjis):
        """Modify dictionnary containing positions in sentence as keys, and kanjis as values."""
        kanjis_sorted = sorted(kanjis, key=len, reverse=True)

        self.position_kanji_sentence.clear()
        for word in kanjis_sorted:
            while(sentence.find(word) != -1):
                for i in range(sentence.find(word), sentence.find(word) + len(word)):
                    self.position_kanji_sentence[i] = word
                
                replacement = "_" * len(word)
                sentence = sentence.replace(word, replacement, 1)

        pass
    # def get_kanji_data(self):
    #     """Return a dictionnary containing kanji as keys, and a list containing theirs readings and meanings. """
    #     dict = {}
    #     for i in range(self.rowCount()):
    #         dict[self.item(i, 0).text()] = (self.item(i, 1).text(), self.item(i, 2).text(), i)
    #     return dict
