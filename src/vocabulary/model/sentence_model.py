from PyQt6.QtGui import QStandardItemModel

class SentenceModel(QStandardItemModel):

    def __init__(self):
        super().__init__(0,0)

    def modify_row(self, sentence, row):
        for j in range(len(sentence.standard_item)):
            sentence.compute_standard_item()
            self.setItem(row, j, sentence.standard_item[j])
        
    def refresh(self, sentences):
        self.removeRows(0, self.rowCount())
        for i in range(len(sentences)):
            for j in range(len(sentences[i].standard_item)):
                sentences[i].compute_standard_item()
                self.setItem(i, j, sentences[i].standard_item[j])
            
    def get_sentence_item_by_row(self, row):
        item_row = []
        for i in range(self.columnCount()):
            item_row.append(self.item(row, i))
        return item_row
    