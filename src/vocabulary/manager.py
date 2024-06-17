from .word_retriever import WordRetriever
from .vocabulary import Vocabulary
from .data_retriever import DataRetriever

class Manager:
    def __init__(self):
        self.word_retriever = WordRetriever()
        self.data_retriever = DataRetriever(3, "jpn", "eng")
        self.file_location = ""
        
        self.vocabularys_list = [] # List of vocabularies instance

    def get_word_from_qt_line(self, word):
        self.vocabularys_list.append(Vocabulary(word, self.data_retriever))
        print(word)
    
    def _get_word_from_text(self):
        words_retrieved = self.word_retriever.get_word_from_file(self.file_location)
        for word in words_retrieved:
            self.vocabularys_list.append(Vocabulary(word, self.data_retriever))
        
    def start(self):
        for vocabulary in vocabularies_retrieved: # For each vocabulary, create a new Vocabulary class
            self.vocabularys_list.append(Vocabulary(vocabulary, sentence_retriever))
        for i in range(len(self.vocabularys_list )):
            self.vocabularys_list[i].get_data()
            
            
        