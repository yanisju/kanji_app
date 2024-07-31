from .retriever.word import WordRetriever
from .retriever.sentence import SentenceRetriever

from .vocabulary import Vocabulary
from .dictionnary import VocabularyDictionnary

from .model.vocabulary_model import VocabularyModel
from .model.sentence_model import SentenceModel

class VocabularyManager:
    def __init__(self, anki_deck):
        self.word_retriever = WordRetriever()
        self.data_retriever = SentenceRetriever(5, "jpn", "eng")
        
        self.dictionnary = VocabularyDictionnary() # Dictionnary of vocabularies instance
        
        self.vocabulary_model = VocabularyModel() # Model for retrieved words
        self.sentence_model = SentenceModel()

        self.sentence_added_model = SentenceModel(anki_deck)
    
    def refresh_sentence_model(self, row):
        if self.dictionnary.len() == 0:
            self.sentence_model.clean()
        else:
            word = self.vocabulary_model.item(row, 0).text()
            vocabulary = self.dictionnary.find_vocabulary_by_word(word)
            self.sentence_model.refresh(vocabulary.sentences)
            
    def refresh_vocabulary_model(self):
        words = self.dictionnary.get_words()
        vocabularies = self.dictionnary.get_vocabularies()
        self.vocabulary_model.refresh_model(words, vocabularies)    
            
    def add_to_dictionnary(self, word):
        """ Add word to dictionnary and refresh model. """
        vocabulary = Vocabulary(word, self.data_retriever)
        self.dictionnary.add(word, vocabulary)
        self.vocabulary_model.add_vocabulary(vocabulary)
    
    def get_word_from_text(self, file_location):
        """Read words from text file and add them to model."""
        words_retrieved = self.word_retriever.get_word_from_file(file_location)
        for word in words_retrieved:
            self.add_to_dictionnary(word)
        
            
            
        