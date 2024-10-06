from .kanji_data import *
from ..meaning.retriever import *
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

    def get_data(self, word, word_meaning_object, quick_init):
        """
        Retrieves data for a given word, including example sentences, translations, kanji readings, 
        meanings, and positions within sentences.

        Args:
        -----
        word : str
            The vocabulary word for which data is to be retrieved.
        word_meaning : VocabularyMeaning
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
        word_meaning = word_meaning_object.meaning
        word_part_of_speech = word_meaning_object.part_of_speech
        kanji_data = self._get_kanji_data(transcriptions, word, word_meaning)
        
        return (sentences, sentences_lang_to, kanji_data)
    
    def _get_kanji_data(self, transcriptions, word: str, word_meaning: str):
        """
        Retrieve kanji data for each sentence, returning a dictionary where kanji are the keys and their readings, 
        meanings, and positions in the sentence are the values.

        This method processes a list of sentence transcriptions and generates kanji data for each sentence.
        It handles cases where the word does not appear exactly as written in the kanji data by updating the 
        dictionary when kana is involved. The final kanji data includes the reading, meaning, and position of the 
        word in the sentence.

        Args:
        -----
        transcriptions : list of str
            List of transcriptions for the sentences containing the word.
        word : str
            The target word whose kanji data needs to be processed.
        word_meaning : str
            The meaning of the word, used to update the kanji data if necessary.

        Returns:
        --------
        tuple of dict
            A tuple where each element is a dictionary representing kanji data for a sentence. The dictionary has kanji 
            characters as keys and their values as a tuple of (reading, meaning, position).
        """

        sentences_kanji_data = []

        for transcription in transcriptions:
            kanji_data = get_kanji_reading_meaning_position(transcription)

            # Check if the word appears in the kanji data
            if not is_word_in_dict(kanji_data, word):
                # If the word contains kana, update the kanji data accordingly
                if check_word_contains_kana(word):
                    kanji_data.update_data_kanji_kana(word)
                else:
                    kanji_data.update_data_only_kanji(word)

            # Check again if the word appears in the updated kanji data
            if is_word_in_dict(kanji_data, word):
                # Update the word's reading, meaning, and position
                word_reading, _, word_position = kanji_data[word]
                kanji_data.add(word, word_reading, word_meaning, word_position)

            # Add the kanji data to the list of sentence kanji data
            sentences_kanji_data.append(kanji_data)

        return tuple(sentences_kanji_data)
