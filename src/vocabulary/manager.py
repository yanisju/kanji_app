from .data_retriever import *
from .vocabulary import Vocabulary
from .sentence.manager import SentenceManager
from .model.vocabulary import VocabularyModel


class VocabularyAlreadyExists(Exception):
    pass


class VocabularyManager:
    """
    Manages a collection of vocabulary words and their associated example sentences.

    Attributes:
    -----------
    data_retriever : DataRetriever
        An instance of DataRetriever used to fetch data for vocabulary words.
    vocabularies : dict
        A dictionary where the keys are vocabulary words and the values are instances of the Vocabulary class.
    vocabulary_model : VocabularyModel
        A model for managing the list of retrieved vocabulary words.
    sentence_model : SentenceModel
        A model for managing the sentences associated with a selected vocabulary word.
    sentence_added_model : SentenceModel
        A model for managing sentences that are supposed to be added to Anki deck.
    """

    def __init__(self, anki_manager):
        self.data_retriever = DataRetriever("jpn", "eng", RetrieverMode.LOCAL)

        self.vocabularies = {}  # Dictionnary of vocabularies instance

        self.vocabulary_model = VocabularyModel()  # Model for retrieved words
        self.sentence_added_to_deck = SentenceManager()

        self.anki_manager = anki_manager

    def add_word(self, word):
        """
        Adds a vocabulary word to the dictionary and to the vocabulary model.

        Args:
        -----
        word : str
            The vocabulary word to be added.
        """
        try:
            self.get_index_by_word(word)
        except ValueError:
            vocabulary = Vocabulary(word, self.data_retriever)
            vocabulary.standard_item_modified.connect(
                self._change_vocabulary_model_item)
            self.vocabularies.update({word: vocabulary})
            self.vocabulary_model.append_vocabulary(
                word, vocabulary.standard_item)
        else:
            raise VocabularyAlreadyExists(word)

    def add_sentence_to_deck(self, sentence):
        sentence_to_add = sentence.clone()
        self.sentence_added_to_deck.append(sentence_to_add)

    def delete_vocabulary(self, row):
        """
        Deletes a vocabulary word from the dictionary and the model.

        Args:
        -----
        row : int
            The index of the vocabulary word to be deleted in the vocabulary model.
        """
        word = self.get_word(row)
        self.vocabularies[word].sentence_manager.clear()
        self.vocabulary_model.removeRow(row)
        del self.vocabularies[word]

    def delete_all_vocabularies(self):
        """
        Deletes all vocabulary words from the dictionary and the models.
        """
        self.vocabulary_model.removeRows(0, self.vocabulary_model.rowCount())
        self.vocabularies.clear()

    def __getitem__(self, index):
        return list(self.vocabularies.values())[index]

    def get_word(self, index):
        return list(self.vocabularies.keys())[index]

    def get_index_by_word(self, word):
        return list(self.vocabularies).index(word)

    def generate_deck(self):
        self.anki_manager.generate_deck(self.sentence_added_to_deck)

    def _change_vocabulary_model_item(self, word, standard_item):
        index = self.get_index_by_word(word)
        self.vocabulary_model.modify_row(index, standard_item)
