from .sentence.manager import SentenceManager
from .meaning.meaning import VocabularyMeaning

from PyQt6.QtGui import QStandardItem
from PyQt6.QtCore import QObject

from PyQt6.QtCore import pyqtSignal


class Vocabulary(QObject):
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

    standard_item_modified = pyqtSignal(str, list)

    def __init__(self, word, sentence_retriever, quick_init = False):
        super().__init__()
        self.word = word
        self.meaning_object = VocabularyMeaning(word)
        self.meaning_object.fetch_from_jisho(quick_init)

        self.sentence_retriever = sentence_retriever
        self.sentence_manager = SentenceManager(self)
        self.sentence_manager.sentences_model.modified.connect(self.set_standard_item)

        self._get_data(quick_init)

        self.standard_item = [QStandardItem(self.word), QStandardItem(self.meaning_object.meaning), QStandardItem(self.meaning_object.part_of_speech), QStandardItem(str(len(self.sentence_manager)))]

    def _get_data(self, quick_init):
        """
        Retrieves data associated with the vocabulary word.

        This method uses the sentence_retriever to obtain sentences, their translations,
        kanji data, the meaning of the word, and parts of speech. It then populates
        the sentences attribute with Sentence objects."""

        sentences, translations, kanjis_data = self.sentence_retriever.get_data(self.word, self.meaning_object, quick_init) # Retrieve sentences from DataRetriever
        
        sentences_count = len(sentences)
        for i in range(0, sentences_count):
            self.sentence_manager.append_from_sentence_data(sentences[i], translations[i], kanjis_data[i])

    def remove_one_sentence(self, row):
        """
        Deletes a sentence from the sentences list based on its position.

        Args:
        -----
        row : int
            The index of the sentence to be deleted.
        """
        self.sentences.pop(row)
        self.sentences_model.remove_row(row)

    def remove_all_sentence(self):
        self.sentences.clear()
        self.sentences_model.remove_all_rows()

    def set_standard_item(self):
        self.standard_item = [QStandardItem(self.word), QStandardItem(self.meaning_object.meaning), QStandardItem(self.meaning_object.part_of_speech), QStandardItem(str(len(self.sentence_manager)))]
        self.standard_item_modified.emit(self.word, self.standard_item)