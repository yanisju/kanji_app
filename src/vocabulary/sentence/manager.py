from .sentence import Sentence
from ..model.sentence import SentenceModel

from .kanji_data import KanjiData

class SentenceManager(list):
    def __init__(self, vocabulary = None) -> None:
        super().__init__()
        self.vocabulary = vocabulary
        self.sentences_model = SentenceModel(self)

    def append(self, sentence):
        super().append(sentence)
        self.sentences_model.append_sentence(sentence)
        
    def append_from_sentence_data(self, sentence_str, translation_str, kanjis_data):
        new_sentence = Sentence(self.vocabulary, sentence_str, translation_str, kanjis_data, self.vocabulary.word)
        super().append(new_sentence)
        self.sentences_model.append_sentence(new_sentence)
        
    def append_empty_sentence(self):
        if self.vocabulary != None:
            word = self.vocabulary.word
        else:
            word = None
        empty_sentence = Sentence(self.vocabulary, "", "", KanjiData(), word)
        self.append(empty_sentence)
        

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

    def clear(self):
        super().clear()
        self.sentences_model.remove_all_rows()
        