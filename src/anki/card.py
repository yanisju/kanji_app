import genanki
import re

class AnkiCard():
    """ A class representing a single card / note inside the deck."""
    def __init__(self, model):
        self.model = model
        self.note = None
        
    def get_japanese_sentence_anki(self, sentence):
        """ Transform sentences in order to get furiganas and highlighting in Anki."""
        # Define the regex pattern for the initial format
        pattern = r'\[([^\|\[\]]+)\|([^\[\]]+)\]'
        
        # Define the tags to be applied sequentially
        tags = ['h', 'n4', 'a', 'n5', 'n2']
        tag_index = 0

        # Function to replace each match with the desired format
        def replace_match(match):
            nonlocal tag_index
            kanji = match.group(1)
            reading = match.group(2)
            
            # Remove any extra '|' in the reading part
            reading = reading.replace('|', '')
            
            # Check if the kanji is composed only of Roman characters or digits
            if kanji.isalnum() and all(c.isdigit() or 'A' <= c <= 'Z' or 'a' <= c <= 'z' for c in kanji):
                # If so, just return the kanji without annotation
                return kanji
            
            # Assign the current tag from the tags list
            tag = tags[tag_index]
            
            # Increment the tag_index for the next kanji
            tag_index = (tag_index + 1) % len(tags)
            
            # Construct the new format with spaces before and after
            return f' {kanji}[{reading};{tag}] '
        
        # Apply the transformation using the regex pattern and the replace function
        transformed_sentence = re.sub(pattern, replace_match, sentence)
        
        # Remove any extra spaces that might be introduced at the start or end of the sentence
        transformed_sentence = transformed_sentence.strip()
        
        return transformed_sentence
            
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
        
    