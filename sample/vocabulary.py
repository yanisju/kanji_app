class Vocabulary:
    """ A class used to represent a single vocabulary.
    """
    def __init__(self, symbol, sentence_retriever):
        self.symbol = symbol # 
        self.sentence_retriever = sentence_retriever
        self.lang_from_sentence = []
        self.lang_to_sentence = []
        self.sentence_transcription = []
        
    def retrieve_sentences(self):
        sentences = self.sentence_retriever.start(self.symbol)
        self.lang_from_sentence = sentences[0]
        self.lang_to_sentence = sentences[1]
        self.sentence_transcription = sentences[2]
        print(sentences)