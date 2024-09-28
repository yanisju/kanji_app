from .sentence import Sentence
from ..model.sentence import SentenceModel
from ..data_retriever import DataRetriever


class SentenceManager(list):
    def __init__(self, vocabulary = None) -> None:
        self.vocabulary = vocabulary
        self.sentences_model = SentenceModel(vocabulary)

    def append(self, sentence):
        super().append(sentence)
        self.sentences_model.append_sentence(sentence)
        
    def append_from_sentence_data(self, sentence_str, translation_str, kanjis_data):
        new_sentence = Sentence(self, sentence_str, translation_str, kanjis_data, self.vocabulary.word)
        super().append(new_sentence)
        self.sentences_model.append_sentence(new_sentence)

    def pop(self, index):
        """
        Deletes a sentence from the sentences list based on its position.

        Args:
        -----
        index : int
            The index of the sentence to be deleted.
        """
        super().pop(index)
        self.sentences_model.remove_row(index)

    def remove_all_sentence(self):
        super().clear()
        self.sentences_model.remove_all_rows()
        