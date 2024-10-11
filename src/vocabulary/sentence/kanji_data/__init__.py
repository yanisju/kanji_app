from .str_utils import *
from .kanji_data_model import KanjiDataModel

class KanjiData(dict):
    def __init__(self) -> None:
        self.model = KanjiDataModel()
        # self.model.itemChanged.connect(self._model_is_modified)

    def add(self, kanji, reading, meaning, position):
        #TODO: check if kanji already exists + add to model
        
        if kanji in self:
            row = list(self.keys()).index(kanji)
            print(list(self.keys()), row)
            self.model.modify_reading_meaning(row, reading, meaning)
        else:
            self.model.add_row(kanji, reading, meaning)
        self[kanji] = (reading, meaning, position)

    def remove(self, kanji):
        #TODO: check if kanji already exists + remove from model
        self.pop(kanji)

    def _sort_dict(self): # Sort dict by kanji position
        sorted_dict = dict(sorted(self.items(), key=lambda item: item[1][2])) # Sort dict by position
        self.clear()

        i = 0
        for kanji in sorted_dict.keys(): # Since position is incorrect, need to all positions
            reading, meaning, _ = sorted_dict[kanji]
            self.add(kanji, reading, meaning, i)
            i += 1

    def update_data_kanji_kana(self, word: str):
        """Update dictionnary if word contains both kanjis and kanas."""
        word_reading = ""
        word_position = -1
        first_kanji = True

        for i in range(len(word)): # For each char of word
            if check_char_is_kana(word[i]):
                word_reading += word[i]
            else:
                try:
                    reading, meaning, position = self.remove(word[i])
                    word_reading += reading
                    if first_kanji:
                        word_meaning = meaning
                        word_position = position
                except: # Sometimes, word doesn't appear completely in sentence
                    word_meaning = ""
                    word_position = -1
        self.add(word, word_reading, word_meaning, word_position)
        self._sort_dict()

    def update_data_only_kanji(self, word: str):
        """
        Updates kanji data for a word composed solely of kanji characters by merging data.

        Args:
        -----
        kanji_data : dict
            A dictionary where kanji characters are keys and values are tuples of (reading, meaning, position).
        word : str
            The word composed solely of kanji characters to update in the dictionary.

        Returns:
        --------
        dict
            An updated and sorted dictionary with merged kanji data for the specified word.
        
        Raises:
        -------
        Exception
            If the word is not found in the kanji data.
        """
        kanjis = find_kanjis_in_dict(self, word)
        new_position = self[kanjis[0]][2] # Get position of the first kanji

        data_to_merge = []
        for kanji in kanjis:
            data_to_merge.append(self.remove(kanji))
        
        new_reading, new_meaning = "", ""
        for data in data_to_merge:
            data_reading, data_meaning, _ = data
            new_reading += data_reading
            new_meaning += data_meaning
        self.add(word, new_reading, new_meaning, new_position)

        self._sort_dict()
        print(self.model.rowCount())

    # def _model_is_modified(self, item):
    #     """Modify its own dictionnary to fit with modifications.
    #     Key: kanji
    #     Item: reading, meaning, position"""

    #     index = self.model.indexFromItem(item)
    #     if index.column() != 0:  # If reading or meaning is modified
    #         kanji = self.model.item(index.row(), 0).text()

    #         if index.column() == 1: # Modify reading
    #             self[kanji] = (
    #                 item.text(),
    #                 self[kanji][1],
    #                 index.row(),
    #             )
    #         else:  # Modify meaning / index.column == 2
    #             self[kanji] = (
    #                 self[kanji][0],
    #                 item.text(),
    #                 index.row(),
    #             )
    #     else:  # If kanji is modified
    #         kanji_to_del = [
    #             item for item, v in self.items() if v[2] == index.row()
    #         ]
    #         self[item.text()] = self[kanji_to_del[0]]
    #         del self[kanji_to_del[0]]

    #     # TODO: modify textview position_kanji_sentence
    #     # self.set_position_kanji_sentence(self.sentence, self.keys())

    def set_model(self, new_model):
        self.model = new_model

    def clone(self):
        new_kanji_data = KanjiData()
        for key, value in (self.items()):
            new_kanji_data[key] = value
        new_kanji_data.set_model(self.model.get_a_copy())
        return new_kanji_data