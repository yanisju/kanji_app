from src.vocabulary.word_retriever import VocabularyWordRetriever
from src.vocabulary.data_retriever import VocabularyDataRetriever
from src.vocabulary.vocabulary import Vocabulary

class TestVocabularyNameRetriever:
    
    def test_retrieve_vocabulary_from_user(self):
        vocab_name_retriever = VocabularyWordRetriever()
        vocab_retrieved = vocab_name_retriever.get_vocabulary_from_file("tests", "vocab_test_one.txt")
        assert vocab_retrieved == ["滋賀県", "読書", "紐", "例えば"]
    
    def test_retrieve_sentence_from_internet_one(self):
        word = "滋賀県"
        data_retriever = VocabularyDataRetriever(3, "jpn", "eng")
        data = data_retriever.start(word)
        assert data[0][0] == "滋賀県の県庁所在地は大津市です。"
        
    def test_retrieve_sentence_from_internet_two(self):
        word = "滋賀県"
        data_retriever = VocabularyDataRetriever(3, "jpn", "eng")
        data = data_retriever.start(word)
        assert data[1][0] == "Shiga Prefecture's capital is Otsu City."
        
    def test_retrieve_sentence_from_internet_three(self):
        word = "滋賀県"
        data_retriever = VocabularyDataRetriever(3, "jpn", "eng")
        data = data_retriever.start(word)
        assert data[2][0] == "[滋賀|し|が][県|けん]の[県庁|けん|ちょう][所在地|しょ|ざい|ち]は[大津|おお|つ][市|し]です。"
        

            
        