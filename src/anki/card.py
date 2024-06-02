import genanki
import re

class AnkiCard():
    """ A class representing a single card / note inside the deck."""
    def __init__(self, model):
        self._model = model
        
    def get_japanese_transcription(self, sentence):
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
    
    def fill_fields_jap_sentence(self, vocabulary, card_count):
        """Fill fields for a japanese sentence model."""
        sentence_transcription = vocabulary.sentence_transcription[0]
        japanese_transcription = self.get_japanese_transcription(sentence_transcription)
        my_note = genanki.Note(
            model=self._model,
            fields=[card_count, 
                    japanese_transcription, 
                    vocabulary.lang_to,
                    
                    ],)
        
    