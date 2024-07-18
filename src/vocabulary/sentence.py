from PyQt6.QtGui import QStandardItem

class Sentence():
    def __init__(self, lang_from, lang_to, transcription, word, meaning):
        self.update_attributes(lang_from, lang_to, transcription, word, meaning)

    def update_attributes(self, lang_from, lang_to, transcription, word, meaning, word2 = "", word2_meaning = ""):
        self.lang_from = lang_from
        self.lang_to = lang_to
        self.transcription = transcription
        self.word1 = word
        self.word1_meaning = meaning
        self.word2 = word2
        self.word2_meaning = word2_meaning
        self.fields = [lang_from, lang_to, transcription, word, meaning, self.word2, self.word2_meaning]
        self.standard_item = None # QStandardItem in order to be inserted in the model
        self.compute_standard_item()

    def compute_standard_item(self):
        item_list = []
        for i in range(len(self.fields)):
            item_list.append(QStandardItem(self.fields[i]))
        self.standard_item = item_list 
