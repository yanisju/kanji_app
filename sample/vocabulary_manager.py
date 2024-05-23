from vocabulary_retriever import VocabularyRetriever
from vocabulary import Vocabulary
from sentence_retriever import SentenceRetriever

class VocabularyManager:
    def __init__(self):
        self.vocabulary_retriever = VocabularyRetriever()
        self.vocabularys_list = []

    def start(self):
        self.vocabulary_retriever.start(1)
        vocabularys_retrieved = self.vocabulary_retriever.vocabularys_list
        
        sentence_retriever = SentenceRetriever(3, "jpn", "eng")
        for vocabulary in vocabularys_retrieved:
            self.vocabularys_list.append(Vocabulary(vocabulary, sentence_retriever))
        for i in range(len(self.vocabularys_list )):
            self.vocabularys_list[i].retrieve_sentences()
            
            
        