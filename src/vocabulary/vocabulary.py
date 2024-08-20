from .sentence.sentence import Sentence
from PyQt6.QtGui import QStandardItem

class Vocabulary:
    """ A class used to represent a single vocabulary, and its example sentence.
    """

    def __init__(self, word, sentence_retriever):
        self.word = word  # Vocabulary itself
        self.meaning = ""

        self.sentence_retriever = sentence_retriever
        self.sentences = [] # Each example sentences 
        self._get_data()

        self.item = [QStandardItem(self.word), QStandardItem(self.meaning)]
    
    def _get_data(self):
        """ Retrieve data with the vocabulary. """
        sentences, translations, kanjis_data, self.meaning, parts_of_speech = self.sentence_retriever.get_data(self.word, self.meaning) # Retrieve sentences from DataRetriever
        
        for i in range(0, len(sentences)):
            self.sentences.append(Sentence(sentences[i], translations[i], kanjis_data[i], self.word))  
        
