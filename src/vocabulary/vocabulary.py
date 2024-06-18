from PyQt6.QtGui import QStandardItemModel, QStandardItem

class Vocabulary:
    """ A class used to represent a single vocabulary.
    """

    def __init__(self, word, data_retriever):
        self.word = word  # Vocabulary itself
        self.data_retriever = data_retriever
        self.lang_from_sentence = [] # Example sentences in the original language
        self.lang_to_sentence = [] # Example sentences in the desired language
        self.sentence_transcription = []
        self.sentence_count = 0  # Number of sentences
        self.meaning = []
        self.meaning_count = 0 # Number of meanings
        self.part_of_speech = []
        
        self._get_data()
        
        self.sentence_model = self.get_sentence_model()
        
        

    def compute_sentence_count(self):
        """ Compute the number of sentences retrieved. (from, to and transcription)
        Raise a value error if each length is different."""
        if (len(self.lang_from_sentence) != len(self.lang_to_sentence) and len(self.lang_from_sentence) != len(self.sentence_transcription)):
            raise ValueError
        self.sentence_count = len(self.lang_from_sentence)
    
    def compute_meaning_count(self):
        """ Compute the number of meanings retrieved. """
        self.meaning_count = len(self.meaning)

    def _get_data(self):
        """ Retrieve data with the vocabulary. """
        
        data = self.data_retriever.start(self.word) # Retrieve data from DataRetriever
        self.lang_from_sentence = data[0]
        self.lang_to_sentence = data[1]
        self.sentence_transcription = data[2]
        self.meaning = data[3]
        self.part_of_speech = data[4]
        self.compute_sentence_count()
        
    def get_sentence_model(self):
        model = QStandardItemModel(0, 3)
        for i in range(self.sentence_count):
            lang_from_sentence_item = QStandardItem(self.lang_from_sentence[i])
            lang_to_sentence_item = QStandardItem(self.lang_to_sentence[i])
            sentence_transcription_item = QStandardItem(self.sentence_transcription[i])
            item_list = [lang_from_sentence_item, lang_to_sentence_item, sentence_transcription_item]
            model.insertRow(i, item_list)        
        return model
