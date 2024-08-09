from .kanji_data import *
from .word_meaning import *
from .sentence import *

class DataRetriever():
    """Used to retrieve vocabulary data, such as:
    * Example sentences, theirs translations, theirs translations...
    * Vocabulary meaning
    * Kanji readings, meanings and positions in sentences (if needed)"""

    def __init__(self, sentence_desired_count, lang_from, lang_to):
        self.sentences = []
        self.sentence_desired_count = sentence_desired_count # Number of sentences desired
        self.lang_from = lang_from
        self.lang_to = lang_to

    def get_data(self, word, word_meaning):
        sentences, sentences_lang_to, transcriptions = get_sentences(word, self.lang_from, self.lang_to, self.sentence_desired_count)
        word_meaning, word_part_of_speech = get_meaning(word)

        kanji_data = []
        for transcription in transcriptions:
            kanji_data.append(get_kanji_data(transcription, word, word_meaning))
        
        return (sentences, sentences_lang_to, tuple(kanji_data), word_meaning, word_part_of_speech)