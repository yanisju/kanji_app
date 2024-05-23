from kanji_retriever import KanjiRetriever
from kanji import Kanji

class KanjiManager:
    def __init__(self):
        self.kanji_retriever = KanjiRetriever()
        self.kanjis_list = []

    def start(self):
        kanjis_retrieved = self.kanji_retriever.start(1)
        for kanji in kanjis_retrieved:
            self.kanjis_list.append(Kanji(kanji))
        