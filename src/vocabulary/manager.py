from .retriever.word_retriever import WordRetriever
from .retriever.data_retriever import DataRetriever

from .vocabulary import Vocabulary
from .dictionnary import VocabularyDictionnary

from .model.vocabulary_model import VocabularyModel
from .model.sentence_model import SentenceModel

from PyQt6.QtCore import QStringListModel
from PyQt6.QtGui import QStandardItemModel

class Manager:
    def __init__(self):
        self.word_retriever = WordRetriever()
        self.data_retriever = DataRetriever(3, "jpn", "eng")
        
        self.dictionnary = VocabularyDictionnary() # Dictionnary of vocabularies instance
        
        self.vocabulary_model = VocabularyModel() # Model for retrieved words / How words data is set
        self.sentence_model = SentenceModel()
    
    def refresh_sentence_model(self, word):
        if self.dictionnary.len() == 0:
            self.sentence_model.clean()
        else:
            vocabulary = self.dictionnary.find_vocabulary_by_word(word)
            self.sentence_model.set_sentence_model(vocabulary)
            
    def refresh_vocabulary_model(self):
        words = self.dictionnary.get_words()
        self.vocabulary_model.refresh_model(words)

    def add_to_dictionnary(self, word):
        """ Add word to dictionnary."""
        vocabulary = Vocabulary(word, self.data_retriever)
        self.dictionnary.add(word, vocabulary)    
    
    def _get_word_from_text(self, file_location):
        words_retrieved = self.word_retriever.get_word_from_file(file_location)
        for word in words_retrieved:
            self.add_to_dictionnary(word)
        
            
            
        