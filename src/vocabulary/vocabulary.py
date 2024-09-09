from .sentence.sentence import Sentence
from PyQt6.QtGui import QStandardItem

from .data_retriever import find_kanjis_in_dict,  check_word_contains_kana

class Vocabulary:
    """
    Represents a single vocabulary word and its associated example sentences.

    Attributes:
    -----------
    word : str
        The vocabulary word itself.
    meaning : str
        The meaning of the vocabulary word. (Placeholder for future implementation as a separate class)
    sentence_retriever : DataRetriever
        An instance responsible for retrieving sentences and related data for the vocabulary word.
    sentences : list
        A list of Sentence objects that provide example sentences using the vocabulary word.
    item : list
        A list containing QStandardItems representing the vocabulary word and its meaning, destined to be inserted in a model.
    """

    def __init__(self, word, sentence_retriever):
        self.word = word
        self.meaning = "" # TODO: create a class

        self.sentence_retriever = sentence_retriever
        self.sentences = [] # TODO: create a SentenceManger instead
        self._get_data()

        self.item = [QStandardItem(self.word), QStandardItem(self.meaning)]
    
    def _get_data(self):
        """
        Retrieves data associated with the vocabulary word.

        This method uses the sentence_retriever to obtain sentences, their translations,
        kanji data, the meaning of the word, and parts of speech. It then populates
        the sentences attribute with Sentence objects."""

        sentences, translations, kanjis_data, self.meaning, parts_of_speech = self.sentence_retriever.get_data(self.word, self.meaning) # Retrieve sentences from DataRetriever
        
        sentences_count = len(sentences)
        for i in range(0, sentences_count):
            if check_word_contains_kana(self.word) or find_kanjis_in_dict(kanjis_data[i], self.word) is not None:
                self.sentences.append(Sentence(self, sentences[i], translations[i], kanjis_data[i], self.word))  
        
    def delete_sentence(self, row):
        """
        Deletes a sentence from the sentences list based on its position.

        Args:
        -----
        row : int
            The index of the sentence to be deleted.
        """
        self.sentences.pop(row)