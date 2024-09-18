from .retriever import get_meaning
from PyQt6.QtGui import QStandardItem, QStandardItemModel

class VocabularyMeaning:
    """
    A class to represent the meanings and part-of-speech information for a vocabulary word.

    This class stores multiple meanings and parts of speech for a given word, allowing users to
    add, remove, and manage these meanings. 

    Attributes:
    -----------
    word : str
        The vocabulary word.
    count : int
        The count of meanings (not actively used).
    _meanings : list of str
        List of meanings for the word.
    _part_of_speech : list of str
        List of corresponding part-of-speech tags for each meaning.
    current_selection : int
        The index of the currently selected meaning.
    standard_item_model : QStandardItemModel
        A model to store the meanings and parts of speech for GUI representation.

    Methods:
    --------
    add(meaning: str, part_of_speech: str):
        Adds a new meaning and part of speech to the word.
    
    remove(index: int):
        Removes the meaning and part of speech at the specified index.
    
    remove_all():
        Removes all meanings and parts of speech for the word.
    
    __getitem__(index: int) -> tuple:
        Returns the meaning and part of speech at the specified index.
    
    __setitem__(index: int, meaning: str, part_of_speech: str):
        Updates the meaning and part of speech at the specified index.
    
    meaning -> str:
        Returns the currently selected meaning based on `current_selection`.
    
    part_of_speech -> str:
        Returns the part of speech corresponding to the current selection.
    
    fetch_from_jisho(quick_init: bool):
        Fetches meanings and part-of-speech data from an external source (Jisho) for the word.
    """

    def __init__(self, word) -> None:
        """
        Initializes the VocabularyMeaning instance with a word and sets up internal storage for meanings and parts of speech.

        Args:
        -----
        word : str
            The vocabulary word for which meanings and part-of-speech information will be stored.
        """
        self.word = word
        self.count = 0 
        self._meanings = []
        self._part_of_speech = []
        self.current_selection = 1
        self.standard_item_model = QStandardItemModel()

    def add(self, meaning, part_of_speech):
        """
        Adds a new meaning and part of speech for the word and updates the GUI model.

        Args:
        -----
        meaning : str
            The meaning to be added.
        part_of_speech : str
            The part of speech associated with the meaning.
        """
        self._meanings.append(meaning)
        self._part_of_speech.append(part_of_speech)
        self.standard_item_model.appendRow([QStandardItem(meaning), QStandardItem(part_of_speech)])

    def remove(self, index):
        """
        Removes the meaning and part of speech at the specified index and updates the model.

        Args:
        -----
        index : int
            The index of the meaning and part of speech to be removed.
        """
        del self._meanings[index]
        del self._part_of_speech[index]
        self.standard_item_model.removeRow(index)

    def remove_all(self):
        """
        Clears all meanings and parts of speech from both internal storage and the GUI model.
        """
        self._meanings.clear()
        self._part_of_speech.clear()
        self.standard_item_model.clear()

    def __getitem__(self, index):
        """
        Returns the meaning and part of speech as a tuple at the specified index.

        Args:
        -----
        index : int
            The index of the desired meaning and part of speech.

        Returns:
        --------
        tuple:
            A tuple containing the meaning and part of speech at the specified index.
        """
        return tuple([self._meanings[index], self._part_of_speech[index]])

    def __setitem__(self, index, meaning, part_of_speech):
        """
        Updates the meaning and part of speech at the specified index.

        Args:
        -----
        index : int
            The index of the meaning and part of speech to update.
        meaning : str
            The new meaning to be set.
        part_of_speech : str
            The new part of speech to be set.
        """
        self._meanings[index] = meaning
        self._part_of_speech[index] = part_of_speech
        self.standard_item_model.setItem(index, [QStandardItem(meaning), QStandardItem(part_of_speech)])

    @property
    def meaning(self):
        """
        Returns the currently selected meaning.

        Returns:
        --------
        str:
            The meaning at the index `current_selection - 1`.
        """
        return self._meanings[self.current_selection - 1]

    @property
    def part_of_speech(self):
        """
        Returns the part of speech for the currently selected meaning.

        Returns:
        --------
        str:
            The part of speech at the index `current_selection - 1`.
        """
        return self._part_of_speech[self.current_selection - 1]

    def fetch_from_jisho(self, quick_init):
        """
        Fetches meanings and parts of speech for the word from an external dictionary (Jisho) and adds them to the instance.

        Args:
        -----
        quick_init : bool
            Whether to perform a quick initialization (used to determine how to fetch data).
        """
        meanings, part_of_speech = get_meaning(self.word, quick_init)
        for one_meaning, one_part_of_speech in zip(meanings, part_of_speech):
            self.add(one_meaning, one_part_of_speech)