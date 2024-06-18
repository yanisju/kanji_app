from .word_retriever import WordRetriever
from .vocabulary import Vocabulary
from .data_retriever import DataRetriever

from PyQt6.QtCore import QStringListModel

class Manager:
    def __init__(self):
        self.word_retriever = WordRetriever()
        self.data_retriever = DataRetriever(3, "jpn", "eng")
        self.file_location = ""
        
        self.vocabularies_list = [] # List of vocabularies instance
        self.vocabulary_model = QStringListModel() # Model for retrieved words / How words data is set
        self.vocabulary_model_item_count = 0

    def refresh_vocabulary_model(self):
        vocabularies_name = self.get_all_vocabulary_name_from_vocabulary_list()
        self.vocabulary_model_item_count = len(vocabularies_name)
        
        self.vocabulary_model.setStringList(vocabularies_name)

    def get_all_vocabulary_name_from_vocabulary_list(self):
        vocabularies_name = []
        for vocabulary in self.vocabularies_list:
            vocabularies_name.append(vocabulary.word)
        return vocabularies_name

    def add_vocabulary_from_qt_line(self, word):
        self.vocabularies_list.append(Vocabulary(word, self.data_retriever))
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
            
            
        