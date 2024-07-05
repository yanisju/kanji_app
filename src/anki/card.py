import genanki
import re

class AnkiCard():
    """ A class representing a single card / note inside the deck."""
    def __init__(self, model):
        self.model = model
        self.note = None
            
    def get_japanese_word_transcription(self, sentence, word):
            pattern = r'\S+\[\S+?;\S+?\]\S*'
            anki_words = re.findall(pattern, sentence)
            for anki_word in anki_words:
                # Remove content inside brackets and the brackets themselves
                stripped_word = re.sub(r'\[\S+?;\S+?\]', '', anki_word)
                if stripped_word == word:
                    return anki_word
            return None
         
    def get_vocabulary_meaning_to_str(self, vocabulary_meaning):
        """ Since meaning is typed as list in Vocabulary, it needs to be transformed as a human-readable str."""
        
        meaning_str = ""
        for i in range(len(vocabulary_meaning)):
            if i == len(vocabulary_meaning) - 1:
                meaning_str += vocabulary_meaning[i]
            else:
                meaning_str += vocabulary_meaning[i] + ", "
        return meaning_str
            
    
    def fill_fields_jap_sentence(self, vocabulary, card_count):
        """Fill fields for a japanese sentence model."""
        sentence_transcription = vocabulary.sentence_transcription[0]
        sentence_transcription_anki = self.get_japanese_sentence_anki(sentence_transcription)
        word_transcription_anki = self.get_japanese_word_transcription(sentence_transcription_anki, vocabulary.word)
        meaning_str = self.get_vocabulary_meaning_to_str(vocabulary.meaning[0]) # TODO Only take first meaning for now
        
        card_fields=["0", 
                    sentence_transcription_anki, 
                    vocabulary.lang_to_sentence[0],
                    word_transcription_anki,
                    meaning_str,
                    "test",
                    "test",
                    "test",
                    ]
        
        card_note = genanki.Note(
            model=self.model,
            fields = card_fields)
            
        
        self.note = card_note
        
    