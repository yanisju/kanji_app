from .data_retriever import DataRetriever
from .vocabulary import Vocabulary
from .model.sentence import SentenceModel
from .model.vocabulary import VocabularyModel

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

    def __init__(self):
        self.data_retriever = DataRetriever(5, "jpn", "eng")
        
        self.vocabularies = dict() # Dictionnary of vocabularies instance
        
        self.vocabulary_model = VocabularyModel() # Model for retrieved words
        self.sentence_model = SentenceModel()
        self.sentence_added_model = SentenceModel()
    
    def add_word(self, word):
        """
        Adds a vocabulary word to the dictionary and to the vocabulary model.

        Args:
        -----
        word : str
            The vocabulary word to be added.
        """
        vocabulary = Vocabulary(word, self.data_retriever)
        self.vocabularies.update({word : vocabulary})
        self.vocabulary_model.appendRow(vocabulary.item)

    def add_word_quick_init(self, word):
        vocabulary = Vocabulary(word, self.data_retriever, quick_init=True)
        self.vocabularies.update({word : vocabulary})
        self.vocabulary_model.appendRow(vocabulary.item)

    def delete_vocabulary(self, row):
        """
        Deletes a vocabulary word from the dictionary and the model.

        Args:
        -----
        row : int
            The index of the vocabulary word to be deleted in the vocabulary model.
        """
        word = self.vocabulary_model.item(row, 0).text()

        self.vocabulary_model.removeRow(row)
        self.sentence_model.removeRows(0, self.sentence_model.rowCount())
        del self.vocabularies[word]

    def delete_all_vocabularies(self):
        """
        Deletes all vocabulary words from the dictionary and the models.
        """
        self.vocabulary_model.removeRows(0, self.vocabulary_model.rowCount())
        self.sentence_model.removeRows(0, self.sentence_model.rowCount())
        self.vocabularies.clear()

    def refresh_sentence_model(self, row):
        """
        Refreshes the sentence model with the sentences of the selected vocabulary word.

        When user select a new vocabulary in VocabularyTableView, sentences in SentenceTableView must be updated. This function modify the 
        contents of the SentenceTableView model, based on vocabulary sentences.

        Args:
        -----
        row : int
            The index of the selected vocabulary word in the vocabulary model.
        """

        if(row != -1):
            word = self.vocabulary_model.item(row, 0).text()
            vocabulary = self.vocabularies[word]
            self.sentence_model.refresh(vocabulary.sentences) 
    
    def remove_sentence(self, row):
        """
        Removes a sentence from the sentence model and the associated vocabulary.

        Args:
        -----
        row : int
            The index of the sentence to be removed in the sentence model.
        """
        sentence_vocabulary = self.sentence_model.sentences[row].vocabulary
        sentence_vocabulary.delete_sentence(row)
        self.sentence_model.remove_row(row)

    def remove_all_sentences(self):
        # TODO: finish to write this method
        sentence_vocabulary = self.sentence_model.sentences[0].vocabulary