from .data_retriever import DataRetriever

from .vocabulary import Vocabulary

from .model.vocabulary_model import VocabularyModel
from .model.sentence_model import SentenceModel

class VocabularyManager:
    def __init__(self, anki_deck):
        self.data_retriever = DataRetriever(5, "jpn", "eng")
        
        self.vocabularies = dict() # Dictionnary of vocabularies instance
        
        self.vocabulary_model = VocabularyModel() # Model for retrieved words
        self.sentence_model = SentenceModel()

        self.sentence_added_model = SentenceModel(anki_deck)
    
    def add_word(self, word):
        """ Add word to dictionnary and refresh model. """
        vocabulary = Vocabulary(word, self.data_retriever)
        self.vocabularies.update({word : vocabulary})
        self.vocabulary_model.add_vocabulary(vocabulary)

    def refresh_sentence_model(self, row):
        word = self.vocabulary_model.item(row, 0).text()
        vocabulary = self.vocabularies[word]
        self.sentence_model.refresh(vocabulary.sentences)   
        
    

        
            
            
        