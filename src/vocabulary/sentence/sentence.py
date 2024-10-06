from PyQt6.QtGui import QStandardItem
from ..str_utils import *
from ..data_retriever.kanji_data import is_word_in_dict
from .kanji_data import KanjiData

class Sentence():
    """
    Represents a single sentence in the context of vocabulary learning.

    Attributes:
    -----------
    vocabulary : Vocabulary
        The vocabulary class associated with this sentence.
    word : str
        The primary word in the sentence that is the focus of the vocabulary learning.
    sentence : str
        The sentence itself.
    translation : str
        The English translation of the sentence.
    word1_data : tuple
        A tuple containing the first word's kanji, reading, meaning, and position in the sentence.
    word2_data : tuple or None
        A tuple containing the second word's kanji, reading, meaning, and position in the sentence, or None if there is no second word.
    attributes : tuple
        A tuple containing the sentence, translation, word1_data, and word2_data.
    kanji_data : dict
        A dictionary containing kanji as keys and their readings, meanings, and positions as values.
    position_kanji_sentence : dict
        A dictionary containing the positions of kanji in the sentence as keys and the corresponding kanji as values.
    standard_item : list or None
        A list of QStandardItems representing the sentence data for insertion into a model, or None if not yet computed.
    """
    def __init__(self, vocabulary, sentence, translation, kanji_data, word, word2 = None):
        self.vocabulary = vocabulary
        self.word = word
        self.sentence = sentence
        self.translation = translation
        self.kanji_data = kanji_data

        if bool(kanji_data) is False: # If kanji_data is empty
            word1_reading, word1_meaning, word1_position = "", "", -1
        elif is_word_in_dict(kanji_data, word):
            word1_reading, word1_meaning, word1_position = kanji_data[word]
        else: # If word does not appear in kanji_data, takes first element
            word1_reading, word1_meaning, word1_position = kanji_data[next(iter(kanji_data))]
        self.word1_data = (word, word1_reading, word1_meaning, word1_position)
        
        if word2:
            word2_reading, word2_meaning, word2_position = kanji_data[word2]
            self.word2_data = (word2, word2_reading, word2_meaning, word2_position)
        else:
            self.word2_data = None  
        self.attributes = (sentence, translation, self.word1_data, self.word2_data)

        self.kanji_data = kanji_data # Dict containing kanji and theirs readings.
        self.position_kanji_sentence = get_position_kanji_sentence(sentence, kanji_data.keys()) # Dict containg positions in text as keys and kanjis as values.

        self.standard_item = None # QStandardItem in order to be inserted in the model
        self.compute_standard_item() # TODO: class does not contain standard item, but method return it directly

    def compute_standard_item(self):
        """Update standard item to insert in Sentence model, based on current sentences attributes. """
        word1_kanji, word2_kanji = None, None
        if self.word1_data != None:
            word1_kanji = self.word1_data[0]
        if self.word2_data != None:
            word2_kanji = self.word2_data[0]
        self.standard_item = [QStandardItem(self.sentence), QStandardItem(self.translation), QStandardItem(word1_kanji), QStandardItem(word2_kanji)] 

    def update_attributes(self, attributes: tuple, new_kanji_data_model):
        """
        Updates the sentence attributes.

        Args:
        -----
        attributes : tuple
            A tuple containing the sentence, translation, word1_data, and word2_data.
        kanji_data : dict
            A dictionary containing kanji as keys and their readings, meanings, and positions as values.
        """

        self.sentence, self.translation, self.word1_data, self.word2_data = attributes
        self.attributes = attributes
        
        self.kanji_data.set_model(new_kanji_data_model)
        self.position_kanji_sentence = get_position_kanji_sentence(self.sentence, self.kanji_data.keys())

    def clone(self):
        """
        Creates and returns a new Sentence instance with the same attributes.

        Returns:
        --------
        Sentence
            A new Sentence instance with the same attributes as the original.
        """
        vocabulary, sentence, translation, kanji_data, word1_data, word2_data = self.vocabulary, self.sentence, self.translation, self.kanji_data, self.word1_data, self.word2_data
        word1, *_ = word1_data
        if word2_data:
            word2, *_ = word2_data
        else:
            word2 = None
        new_kanji_data = kanji_data.clone()
        return Sentence(vocabulary, sentence, translation, new_kanji_data, word1, word2)