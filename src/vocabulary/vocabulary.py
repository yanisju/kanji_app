from .sentence.sentence import Sentence
from .meaning.meaning import VocabularyMeaning
from .model.sentence import SentenceModel

from PyQt6.QtGui import QStandardItem

from .data_retriever import find_kanjis_in_dict,  check_word_contains_kana

class Vocabulary:
    """
    Represents a single vocabulary word and its associated example sentences.

    Attributes:
    -----------
    word : str
        The vocabulary word itself.
    sentence_retriever : DataRetriever
        An instance responsible for retrieving sentences and related data for the vocabulary word.
    quick_init : boolean
        TODO: complete
    """

    def __init__(self, word, sentence_retriever, quick_init = False):
        self.word = word
        self.meaning_object = VocabularyMeaning(word)
        self.meaning_object.fetch_from_jisho(quick_init)

        self.sentence_retriever = sentence_retriever
        self.sentences = [] # TODO: create a SentenceManger instead
        self.sentences_model = SentenceModel(self)

        self._get_data(quick_init)

        self.item = [QStandardItem(self.word), QStandardItem(self.meaning_object.meaning), QStandardItem(self.meaning_object.part_of_speech)]
    
    def _get_data(self, quick_init):
        """
        Retrieves data associated with the vocabulary word.

        This method uses the sentence_retriever to obtain sentences, their translations,
        kanji data, the meaning of the word, and parts of speech. It then populates
        the sentences attribute with Sentence objects."""

        sentences, translations, kanjis_data = self.sentence_retriever.get_data(self.word, self.meaning_object, quick_init) # Retrieve sentences from DataRetriever
        
        sentences_count = len(sentences)
        for i in range(0, sentences_count):
            if check_word_contains_kana(self.word) or find_kanjis_in_dict(kanjis_data[i], self.word) is not None:
                self.add_sentence(sentences[i], translations[i], kanjis_data[i])


    def add_sentence(self, sentence_str, translation_str, kanjis_data):
        new_sentence = Sentence(self, sentence_str, translation_str, kanjis_data, self.word)
        self.sentences.append(new_sentence)  
        self.sentences_model.append_sentence(new_sentence)

        
    def delete_sentence(self, row):
        """
        Deletes a sentence from the sentences list based on its position.

        Args:
        -----
        row : int
            The index of the sentence to be deleted.
        """
        self.sentences.pop(row)
        self.sentences_model.remove_row(row)


    def set_meaning_standard_item(self, model):
        self.meaning_object.standard_item_model = model