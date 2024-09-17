from .retriever import get_meaning
from PyQt6.QtGui import QStandardItem, QStandardItemModel

class VocabularyMeaning():
    def __init__(self, word) -> None:
        self.word = word
        self.count = 0 
        self._meanings = []
        self._part_of_speech = []
        self.current_selection = 1
        self.standard_item_model = QStandardItemModel()

    def add(self, meaning, part_of_speech):
        self._meanings.append(meaning)
        self._part_of_speech.append(part_of_speech)
        self.standard_item_model.appendRow([QStandardItem(meaning), QStandardItem(part_of_speech)])

    def remove(self, index):
        del self._meanings[index]
        del self._part_of_speech[index]
        self.standard_item_model.removeRow(index)
    
    def remove_all(self):
        self._meanings.clear()
        self._part_of_speech.clear()
        self.standard_item_model.clear()

    def __getitem__(self, index):
        return tuple([self._meanings[index], self._part_of_speech[index]]) 
    
    def __setitem__(self, index, meaning, part_of_speech):
        self._meanings[index] = meaning
        self._part_of_speech[index] = part_of_speech
        self.standard_item_model.setItem(index, [QStandardItem(meaning), QStandardItem(part_of_speech)])

    @property
    def meaning(self):
        return self._meanings[self.current_selection - 1]
    
    @property
    def part_of_speech(self):
        return self._part_of_speech[self.current_selection - 1]
    
    def fetch_from_jisho(self, quick_init):
        meanings, part_of_speech = get_meaning(self.word, quick_init)
        for one_meaning, one_part_of_speech in zip(meanings, part_of_speech):
            self.add(one_meaning, one_part_of_speech)