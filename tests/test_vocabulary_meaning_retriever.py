from src.vocabulary.word_retriever import VocabularyWordRetriever
from src.vocabulary.data_retriever import VocabularyDataRetriever
from src.vocabulary.vocabulary import Vocabulary

class TestVocabularyMeaningRetriever:

    def test_retrieve_meaning_from_internet_one(self):
        word="例えば"
        data_retriever = VocabularyDataRetriever(3, "jpn", "eng")
        word_object = Vocabulary(word, data_retriever)
        word_object.get_data()
        assert word_object.meaning == [["for example", "for instance", "e.g."]]
        
    def test_retrieve_meaning_from_internet_two(self):
        word="塗る"
        data_retriever = VocabularyDataRetriever(3, "jpn", "eng")
        word_object = Vocabulary(word, data_retriever)
        word_object.get_data()
        first_condition = word_object.meaning == [["to paint",
                                        "to plaster",
                                        "to lacquer",
                                        "to varnish",
                                        "to spread",
                                        "to smear",
                                        "to put up (wallpaper)"]]
        second_condition = word_object.part_of_speech == [["Godan verb with 'ru' ending",
                                                           "Transitive verb"]]
        assert first_condition and second_condition
        
    def test_retrieve_meaning_from_internet_three(self):
        word="滋賀県"
        data_retriever = VocabularyDataRetriever(3, "jpn", "eng")
        word_object = Vocabulary(word, data_retriever)
        word_object.get_data()
        first_condition = word_object.meaning == [["Shiga Prefecture (Kinki area)"],
                                        ["Shiga Prefecture"],
                                        ["Shiga Prefecture"],]
        second_condition = word_object.part_of_speech == [["Noun"],
                                        ["Place"],
                                        ["Wikipedia definition"]]
        print(word_object.part_of_speech)
        assert first_condition and second_condition