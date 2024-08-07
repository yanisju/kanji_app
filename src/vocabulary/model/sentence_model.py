from PyQt6.QtGui import QStandardItemModel

class SentenceModel(QStandardItemModel):

    def __init__(self, anki_deck = None):
        super().__init__(0,0)
        self.sentences = [] # Current Sentences hold by the model

        self._anki_deck = anki_deck

    def append_sentence(self, sentence):
        self.sentences.append(sentence)
        sentence.compute_standard_item()
        self.appendRow(sentence.standard_item)

        if self._anki_deck is not None:
            self._anki_deck.add(sentence.fields)
            pass

    def modify_row(self, sentence, row):
        self.sentences[row] = sentence
        for j in range(len(sentence.standard_item)):
            sentence.compute_standard_item()
            self.setItem(row, j, sentence.standard_item[j])

        if self._anki_deck is not None:
            self._anki_deck.modify(sentence.fields, row)
        
    def refresh(self, sentences):
        self.removeRows(0, self.rowCount())
        self.sentences.clear()

        for i in range(len(sentences)):
            self.sentences.append(sentences[i])
            for j in range(len(sentences[i].standard_item)):
                sentences[i].compute_standard_item()
                self.setItem(i, j, sentences[i].standard_item[j])
            
    def get_sentence_by_row(self, row):
        return self.sentences[row]
    