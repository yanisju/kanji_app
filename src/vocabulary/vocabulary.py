class Vocabulary:
    """ A class used to represent a single vocabulary.
    """

    def __init__(self, word, data_retriever):
        self.word = word  # Vocabulary itself
        self.data_retriever = data_retriever
        self.lang_from_sentence = [] # Example sentences in the original language
        self.lang_to_sentence = [] # Example sentences in the desired language
        self.sentence_transcription = []
        self.meaning = []
        self.part_of_speech = []
        self.sentence_count = 0  # Number of sentences

    def compute_sentence_count(self):
        """ Compute the number of sentences retrieved. (from, to and transcription)
        Raise a value error if each length is different."""
        if (len(self.lang_from_sentence) != len(self.lang_to_sentence) and len(self.lang_from_sentence) != len(self.sentence_transcription)):
            raise ValueError
        self.sentence_count = len(self.lang_from_sentence)

    def get_data(self):
        """ Retrieve data with the vocabulary. """
        
        data = self.data_retriever.start(self.word) # Retrieve data from DataRetriever
        self.lang_from_sentence = data[0]
        self.lang_to_sentence = data[1]
        self.sentence_transcription = data[2]
        self.meaning = data[3]
        self.part_of_speech = data[4]
        self.compute_sentence_count()
