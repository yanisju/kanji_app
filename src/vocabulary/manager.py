from .word_retriever import WordRetriever
from .vocabulary import Vocabulary
from .data_retriever import DataRetriever

from .vocabulary_model import VocabularyModel

from PyQt6.QtCore import QStringListModel
from PyQt6.QtGui import QStandardItemModel

class Manager:
    def __init__(self):
        self.word_retriever = WordRetriever()
        self.data_retriever = DataRetriever(3, "jpn", "eng")
        
        self.vocabularies_list = [] # List of vocabularies instance
        
        self.vocabulary_model = VocabularyModel() # Model for retrieved words / How words data is set
        
        self.sentence_model = QStandardItemModel(0, 0)
    
    def refresh_sentence_model(self, word):
        if len(self.vocabularies_list) == 0:
            self.sentence_model = QStandardItemModel(0, 0)
        else:
            index_word = next((index for index, vocab_instance in enumerate(self.vocabularies_list) if vocab_instance.word == word), None)
            print(self.vocabularies_list[index_word].word)
            self.vocabularies_list[index_word].set_sentence_model(self.sentence_model)
            
    def refresh_vocabulary_model(self):
        words = self.get_words_from_vocabulary_list()
        self.vocabulary_model.refresh_model(words)

    def get_words_from_vocabulary_list(self):
        """ Retrieve every single word from vocabulary list."""
        vocabularies_name = []
        for vocabulary in self.vocabularies_list:
            vocabularies_name.append(vocabulary.word)
        return vocabularies_name

    def add_vocabulary_from_qt_line(self, word):
        new_vocabulary = Vocabulary(word, self.data_retriever)
        self.vocabularies_list.append(new_vocabulary)
    
    def _get_word_from_text(self, file_location):
        words_retrieved = self.word_retriever.get_word_from_file(file_location)
        for word in words_retrieved:
            self.vocabularies_list.append(Vocabulary(word, self.data_retriever))
        
            
            
        