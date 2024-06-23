from collections import UserDict

class VocabularyDictionnary(UserDict):
    def __init__(self):
        super().__init__()
        
    def add(self, word, vocabulary):
        self.data.update({word : vocabulary})
        
    def get_words(self):
        """ Return every single word from dictionnary. """
        return self.data.keys()
    
    def get_vocabularies(self):
        return self.data.values()
    
    def len(self):
        """ Return the number of key/value pairs in dictionnary."""
        return len(self.data)
    
    def find_vocabulary_by_word(self, word):
        """ Return vocabulary associated to word and raise an error if can't find the word."""
        return self.data[word] # TODO Add DialogError