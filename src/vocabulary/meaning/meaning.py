from .retriever import get_meaning
from PyQt6.QtGui import QStandardItem

class VocabularyMeaning():
    def __init__(self, word) -> None:
        self.word = word
        self.count = 0 
        self._meanings = []
        self._part_of_speech = []
        self.current_selection = 0
        self._standard_item = []

    def add(self, meaning, part_of_speech):
        self._meanings.insert(meaning)
        self._part_of_speech.insert(part_of_speech)
        self._standard_item.insert(QStandardItem(meaning), QStandardItem(part_of_speech))

    def remove(self, index):
        del self._meanings[index]
        del self._part_of_speech[index]
        del self._standard_item[index]
    
    def remove_all(self):
        self._meanings.clear()
        self._part_of_speech.clear()
        self._standard_item.clear()

    def __getitem__(self, index):
        return tuple([self._meanings[index], self._part_of_speech[index]]) 
    
    def __setitem__(self, index, meaning, part_of_speech):
        self._meanings[index] = meaning
        self._part_of_speech[index] = part_of_speech
        self._standard_item.insert(QStandardItem(meaning), QStandardItem(part_of_speech))

    @property
    def meaning(self):
        return self._meanings[self.current_selection]
    
    @property
    def part_of_speech(self):
        return self._part_of_speech[self.current_selection]
    
    def fetch_from_jisho(self, quick_init):
        self._meanings, self._part_of_speech = get_meaning(self.word, quick_init)