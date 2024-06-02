from .word_retriever import VocabularyWordRetriever
from .vocabulary import Vocabulary
from .data_retriever import VocabularyDataRetriever

class VocabularyManager:
    def __init__(self):
        self.vocabulary_retriever = VocabularyWordRetriever()
        self.vocabularys_list = []

    def start(self):
        # vocabularies_retrieved = self.vocabulary_retriever.get_vocabulary_from_console()
        vocabularies_retrieved = self.vocabulary_retriever.get_vocabulary_from_file("data/input", "kanjis.txt")
        
        sentence_retriever = VocabularyDataRetriever(3, "jpn", "eng") 
        for vocabulary in vocabularies_retrieved: # For each vocabulary, create a new Vocabulary class
            self.vocabularys_list.append(Vocabulary(vocabulary, sentence_retriever))
        for i in range(len(self.vocabularys_list )):
            self.vocabularys_list[i].get_data()
            
            
        