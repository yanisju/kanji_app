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
        pattern = r'\[([^\|\[\]]+)\|([^\|\[\]]+)\]'
    
        # Define the tags to be applied sequentially
        tags = ['h', 'n4', 'a', 'n5', 'n2']
        tag_index = 0

        # Function to replace each match with the desired format
        def replace_match(match):
            nonlocal tag_index
            kanji = match.group(1)
            reading = match.group(2)
        
            # Assign the current tag from the tags list
            tag = tags[tag_index]
        
            # Increment the tag_index for the next kanji
            tag_index = (tag_index + 1) % len(tags)
        
            # Construct the new format
            return f'{kanji}[{reading};{tag}]'
    
        # Apply the transformation using the regex pattern and the replace function
        transformed_sentence = re.sub(pattern, replace_match, sentence)
    
        return transformed_sentence
        
    def get_japanese_word_transcription(self, sentence, word):
        pattern = re.compile(rf'\b{re.escape(word)}\[[^\]]+\]')
        match = pattern.search(sentence)
        return match.group(0)
         
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
        word_transcription_anki = self.get_japanese_word_transcription(sentence_transcription, vocabulary.word)
        meaning_str = self.get_vocabulary_meaning_to_str(vocabulary.meaning[0]) # TODO Only take first meaning for now
        
        card_fields=["0", 
                    sentence_transcription_anki, 
                    vocabulary.lang_to_sentence[0],
                    "test",# word_transcription_anki,
                    meaning_str,
                    "test",
                    "test",
                    "test",
                    ]
        
        card_note = genanki.Note(
            model=self.model,
            fields = card_fields)
            
        
        self.note = card_note
        
    