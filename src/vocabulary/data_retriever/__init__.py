from .kanji_data import *
from .word_meaning import *
from .sentence import *

class DataRetriever():
    """
    A class used to retrieve vocabulary data, including example sentences, translations, meanings, and kanji details.

    The `DataRetriever` class is responsible for fetching and organizing various data associated with a given word. 
    This includes example sentences, their translations, word meanings, and detailed kanji information such as readings, 
    meanings, and positions within sentences.

    Attributes:
    -----------
    sentence_desired_count : int
        The number of example sentences desired for each word.
    lang_from : str
        The source language code for retrieving data (e.g., 'jpn' for Japanese).
    lang_to : str
        The target language code for retrieving data (e.g., 'eng' for English).
    sentences : list
        A list to store the retrieved sentences.

    Methods:
    --------
    get_data(word, word_meaning):
        Retrieves data for the specified word, including example sentences, translations, 
        kanji readings, meanings, and positions within sentences.
    """


    def __init__(self, sentence_desired_count, lang_from, lang_to):
        self.sentences = []
        self.sentence_desired_count = sentence_desired_count # Number of sentences desired
        self.lang_from = lang_from
        self.lang_to = lang_to

    def get_data(self, word, word_meaning, quick_init):
        """
        Retrieves data for a given word, including example sentences, translations, kanji readings, 
        meanings, and positions within sentences.

        Args:
        -----
        word : str
            The vocabulary word for which data is to be retrieved.
        word_meaning : str
            The initial meaning of the word (may be updated by the method).

        Returns:
        --------
        tuple
            A tuple containing the following elements:
            - sentences : list of str
                Example sentences containing the word in the source language.
            - sentences_lang_to : list of str
                Translations of the example sentences in the target language.
            - kanji_data : tuple of dict
                Kanji data including readings, meanings, and positions within the sentences.
            - word_meaning : str
                The meaning of the word.
            - word_part_of_speech : str
                The part of speech for the word (e.g., noun, verb).
        """

        sentences, sentences_lang_to, transcriptions = get_sentences(word, self.lang_from, self.lang_to, self.sentence_desired_count, quick_init)
        word_meaning, word_part_of_speech = get_meaning(word, quick_init)

        kanji_data = []
        for transcription in transcriptions:
            kanji_data.append(get_kanji_data(transcription, word, word_meaning))
        
        return (sentences, sentences_lang_to, tuple(kanji_data), word_meaning, word_part_of_speech)