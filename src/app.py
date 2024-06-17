from .vocabulary.manager import Manager
from .vocabulary.data_retriever import VocabularyDataRetriever
from .anki.manager import AnkiManager

class App:
    def __init__(self):
        pass

if (__name__ == '__main__'):
    vocabularytest = Manager()
    vocabularytest.start()
    vocabulary_list = vocabularytest.vocabularys_list
    anki_manager = AnkiManager(vocabulary_list[0])
    anki_manager.turn_vocabulary_to_card(vocabulary_list[0])