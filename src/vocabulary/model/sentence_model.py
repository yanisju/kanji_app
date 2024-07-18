from PyQt6.QtGui import QStandardItemModel

class SentenceModel(QStandardItemModel):

    def __init__(self):
        super().__init__(0,0)
        self.sentences = [] # Current Sentences hold by the model

    def append_sentence(self, sentence):
        self.sentences.append(sentence)
        sentence.compute_standard_item()
        self.appendRow(sentence.standard_item)

    def modify_row(self, sentence, row):
        self.sentences[row] = sentence
        for j in range(len(sentence.standard_item)):
            sentence.compute_standard_item()
            self.setItem(row, j, sentence.standard_item[j])
        
    def refresh(self, sentences):
        self.removeRows(0, self.rowCount())
        self.sentences.clear()

        for i in range(len(sentences)):
            self.sentences.append(sentences[i])
            for j in range(len(sentences[i].standard_item)):
                sentences[i].compute_standard_item()
                self.setItem(i, j, sentences[i].standard_item[j])
            
    def get_sentence_by_row(self, row):
        return self.sentences[row - 1]
    