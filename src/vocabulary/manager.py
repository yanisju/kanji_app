
from PyQt6.QtGui import QStandardItemModel

from .data_retriever import DataRetriever
from .vocabulary import Vocabulary
from .model.sentence_model import SentenceModel

class VocabularyManager:
    def __init__(self):
        self.data_retriever = DataRetriever(5, "jpn", "eng")
        
        self.vocabularies = dict() # Dictionnary of vocabularies instance
        
        self.vocabulary_model = QStandardItemModel(0,2) # Model for retrieved words
        self.sentence_model = SentenceModel()

        self.sentence_added_model = SentenceModel()
    
    def add_word(self, word):
        """ Add word to dictionnary and refresh model. """
        vocabulary = Vocabulary(word, self.data_retriever)
        self.vocabularies.update({word : vocabulary})
        self.vocabulary_model.appendRow(vocabulary.item)

    def delete_vocabulary(self, row):
        " Delete word from dictionnary and model."
        word = self.vocabulary_model.item(row, 0).text()

        self.vocabulary_model.removeRow(row)
        self.sentence_model.clear()
        del self.vocabularies[word]

    def delete_all_vocabularies(self):
        """Delete every word from dictionnary and models. """
        self.vocabulary_model.clear()
        self.sentence_model.clear()
        self.vocabularies.clear()

    def refresh_sentence_model(self, row):
        if(row != -1):
            word = self.vocabulary_model.item(row, 0).text()
            vocabulary = self.vocabularies[word]
            self.sentence_model.refresh(vocabulary.sentences)   