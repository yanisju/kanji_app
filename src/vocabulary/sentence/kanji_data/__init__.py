from .str_utils import *
from .kanji_data_model import KanjiDataModel
from .kanji import Kanji

class KanjiData(list):
    def __init__(self) -> None:
        self.model = KanjiDataModel()
    
    def bound_to_sentence(self, sentence):
        self.sentence = sentence
        self.model.itemChanged.connect(self._model_is_modified)

    def _find_kanji_index(self, word):
        for index, kanji in enumerate(self):
            if kanji.word == word:
                return index
        return -1
    
    def get_data_by_kanji(self, kanji: str):
        index = self._find_kanji_index(kanji)
        _, reading, meaning = self[index]
        return (reading, meaning, index)

    def add(self, kanji, reading, meaning):
        kanji_index = self._find_kanji_index(kanji)
        if kanji_index == -1:
            new_kanji = Kanji(kanji, reading, meaning)
            self.append(new_kanji)
            self.model.add_row(new_kanji)
        else:
            raise IndexError

    def remove(self, kanji):
        #TODO: check if kanji already exists + remove from model
        index = self._find_kanji_index(kanji)
        if index != -1:
            self.model.remove(index)
            return self.pop(index) # /!\ TODO: Return kanji as well
        else:
            raise IndexError

    def remove_by_row(self, row):
        self.model.remove(row)
        self.pop(row)

    def clear(self):
        super().clear()
        self.model.clear()

    def update_data_kanji_kana(self, word: str):
        """Update dictionnary if word contains both kanjis and kanas."""
        word_reading = ""
        first_kanji = True
        word_meaning = ""

        for i in range(len(word)): # For each char of word
            if check_char_is_kana(word[i]):
                word_reading += word[i]
            else:
                try:
                    _, reading, meaning = self.remove(word[i])
                    
                    word_reading += reading
                    if first_kanji:
                        word_meaning = meaning
                        first_kanji = False
                except: # Sometimes, word doesn't appear completely in sentence
                    pass
        self.add(word, word_reading, word_meaning)

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

        data_to_merge = []
        for kanji in kanjis:
            data_to_merge.append(self.remove(kanji))
        
        new_reading, new_meaning = "", ""
        for data in data_to_merge:
            _, data_reading, data_meaning = data
            new_reading += data_reading
            new_meaning += data_meaning
        self.add(word, new_reading, new_meaning)

    def update_kanji_meaning(self, kanji: str, meaning: str):
        kanji_index = self._find_kanji_index(kanji)
        if kanji_index != -1:
            self[kanji_index].meaning = meaning
            self.model.modify_row(kanji_index, self[kanji_index])
        else:
            raise IndexError

    
    def _model_is_modified(self, item):
        """Modify its own list to fit with modifications."""

        index = self.model.indexFromItem(item)
        kanji = self.model.item(index.row(), 0).text()
        reading = self.model.item(index.row(), 1).text()
        meaning = self.model.item(index.row(), 2).text()
        
        self[index.row()].update_attributes(kanji, reading, meaning)
        self.sentence._update_position_kanji()

    def set_model(self, new_model):
        self.model = new_model

    def clone(self):
        new_kanji_data = KanjiData()
        for data in (self):
            kanji, reading, meaning = data
            new_kanji_data.add(kanji, reading, meaning)
        new_kanji_data.set_model(self.model.get_a_copy())
        return new_kanji_data