# TODO: USE LATER THIS FILE TO CREATE ANKI NOTES

def _transform_transcription_to_anki_format(self, sentence):
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

def get_anki_format(self, original_transcriptions):
    """Transform original transcription to Anki cards supported transcription. """
    sentences_anki_format = []
    for transcription in original_transcriptions:
        sentences_anki_format.append(self._transform_transcription_to_anki_format(transcription))
    return sentences_anki_format