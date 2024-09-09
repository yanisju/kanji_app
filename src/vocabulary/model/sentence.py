from PyQt6.QtGui import QStandardItemModel
import PyQt6.QtCore

class SentenceModel(QStandardItemModel):
    """
    A model that manages and displays sentences with their associated data.

    This class is an extension of QStandardItemModel designed to handle sentences, including their translations
    and key words, in a structured table format.

    Attributes:
    -----------
    sentences : list
        A list containing the Sentence objects currently held by the model.

    Methods:
    --------
    append_sentence(sentence):
        Adds a new sentence to the model.
    modify_row(sentence, row):
        Modifies an existing sentence in the model at the specified row.
    refresh(sentences):
        Clears and repopulates the model with a new list of sentences.
    get_sentence_by_row(row):
        Retrieves a sentence by its row index in the model.
    remove_row(row):
        Removes a sentence from the model and its corresponding row.
    """

    def __init__(self):
        """
        Initializes the SentenceModel with a predefined structure of four columns.
        """
        super().__init__(0, 4)
        self.sentences = []  # Current Sentences held by the model
        self._configure()

    def _configure(self):
        """
        Configures the model headers to label each column.
        """
        self.setHeaderData(0, PyQt6.QtCore.Qt.Orientation.Horizontal, "Sentence")
        self.setHeaderData(1, PyQt6.QtCore.Qt.Orientation.Horizontal, "Meaning")
        self.setHeaderData(2, PyQt6.QtCore.Qt.Orientation.Horizontal, "Word 1")
        self.setHeaderData(3, PyQt6.QtCore.Qt.Orientation.Horizontal, "Word 2")
        
    def append_sentence(self, sentence):
        """
        Adds a new sentence to the model.

        This method appends a Sentence object to the model and updates the corresponding row with the sentence's data.

        Args:
        -----
        sentence : Sentence
            The Sentence object to be added to the model.
        """
        self.sentences.append(sentence)
        sentence.compute_standard_item()
        self.appendRow(sentence.standard_item)

    def modify_row(self, sentence, row):
        """
        Modifies an existing sentence in the model at the specified row.

        This method updates the Sentence object and its display data in the model at the given row index.

        Args:
        -----
        sentence : Sentence
            The Sentence object with updated data.
        row : int
            The index of the row to be modified.
        """
        self.sentences[row] = sentence
        for j in range(len(sentence.standard_item)):
            sentence.compute_standard_item()
            self.setItem(row, j, sentence.standard_item[j])
        
    def refresh(self, sentences):
        """
        Clears and repopulates the model with a new list of sentences.

        This method removes all existing rows and repopulates the model with the provided list of Sentence objects.

        Args:
        -----
        sentences : list
            A list of Sentence objects to repopulate the model with.
        """
        self.removeRows(0, self.rowCount())
        self.sentences.clear()

        for i in range(len(sentences)):
            self.sentences.append(sentences[i])
            for j in range(len(sentences[i].standard_item)):
                sentences[i].compute_standard_item()
                self.setItem(i, j, sentences[i].standard_item[j])
            
    def get_sentence_by_row(self, row):
        """
        Retrieves a sentence by its row index in the model.

        Args:
        -----
        row : int
            The index of the row for which to retrieve the sentence.

        Returns:
        --------
        Sentence
            The Sentence object corresponding to the given row index.
        """
        return self.sentences[row]
    
    def remove_row(self, row):
        """
        Removes a sentence from the model and its corresponding row.

        This method deletes a sentence from the model and removes its associated row.

        Args:
        -----
        row : int
            The index of the row to be removed.
        """
        self.removeRow(row)
        self.sentences.pop(row)
