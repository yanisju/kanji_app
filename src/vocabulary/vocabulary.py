import re

class Vocabulary:
    """ A class used to represent a single vocabulary.
    """

    def __init__(self, word, data_retriever):
        self.word = word  # Vocabulary itself
        self.data_retriever = data_retriever
        self.lang_from_sentence = [] # Example sentences in the original language
        self.lang_to_sentence = [] # Example sentences in the desired language
        self.sentences_transcription = [] # Example sentences in the original languages with word transcription (for japanese)
        self.sentence_anki_format = [] # Example sentences in the original languages, applied to Anki format (for japanese)
        self.sentence_count = 0  # Number of sentences
        self.meaning = []
        self.meaning_str = ""
        self.meaning_count = 0 # Number of meanings
        self.part_of_speech = []
        
        self.get_data()
    
    def _compute_sentence_count(self):
        """ Compute the number of sentences retrieved. (from, to and transcription)
        Raise a value error if each length is different."""
        if (len(self.lang_from_sentence) != len(self.lang_to_sentence) and len(self.lang_from_sentence) != len(self.sentences_transcription)):
            raise ValueError
        self.sentence_count = len(self.lang_from_sentence)
    
    def compute_meaning_count(self):
        """ Compute the number of meanings retrieved. """
        self.meaning_count = len(self.meaning)

    def _set_meaning_str(self):
        meaning_str = ""
        for meaning in self.meaning:
            if len(meaning_str) == 0:
                meaning_str = meaning
            else:
                meaning_str = meaning_str + ", " + meaning
        self.meaning_str = meaning_str
    
    def transform_transcription_to_anki_format(self, sentence):
        """ Transform sentences in order to get furiganas and highlighting in Anki."""
        # Define the regex pattern for the initial format
        pattern = r'\[([^\|\[\]]+)\|([^\[\]]+)\]'
        
        # Define the tags to be applied sequentially
        tags = ['h', 'n4', 'a', 'n5', 'n2']
        tag_index = 0

        # Function to replace each match with the desired format
        def replace_match(match):
            nonlocal tag_index
            kanji = match.group(1)
            reading = match.group(2)
            
            # Remove any extra '|' in the reading part
            reading = reading.replace('|', '')
            
            # Check if the kanji is composed only of Roman characters or digits
            if kanji.isalnum() and all(c.isdigit() or 'A' <= c <= 'Z' or 'a' <= c <= 'z' for c in kanji):
                # If so, just return the kanji without annotation
                return kanji
            
            # Assign the current tag from the tags list
            tag = tags[tag_index]
            
            # Increment the tag_index for the next kanji
            tag_index = (tag_index + 1) % len(tags)
            
            # Construct the new format with spaces before and after
            return f' {kanji}[{reading};{tag}] '
        
        # Apply the transformation using the regex pattern and the replace function
        transformed_sentence = re.sub(pattern, replace_match, sentence)
        
        # Remove any extra spaces that might be introduced at the start or end of the sentence
        transformed_sentence = transformed_sentence.strip()
        
        return transformed_sentence

    def set_sentence_anki_format(self):
        sentences_anki_format = []
        for transcription in self.sentences_transcription:
            sentences_anki_format.append(self.transform_transcription_to_anki_format(transcription))
        self.sentence_anki_format = sentences_anki_format
    
    def get_data(self):
        """ Retrieve data with the vocabulary. """
        
        data = self.data_retriever.start(self.word) # Retrieve data from DataRetriever
        self.lang_from_sentence = data[0]
        self.lang_to_sentence = data[1]
        self.sentences_transcription = data[2]
        self.set_sentence_anki_format()          
        self.meaning = data[3]
        self.part_of_speech = data[4]
        self._compute_sentence_count()
        self._set_meaning_str()    
        
