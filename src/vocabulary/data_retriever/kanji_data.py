import re

def check_char_is_kana(char):
    if ord(char) >= 12352 and ord(char) <= 12543:
        return True
    else:
        return False

def check_word_contains_kana(word: str):
    for char in word:
        if check_char_is_kana(char): 
            return True
    return False

def is_word_in_dict(kanji_data: dict, word: str):
    return word in kanji_data.keys()

def sort_dict(kanji_data : dict): # Sort dict by kanji position
    sorted_dict = dict(sorted(kanji_data.items(), key=lambda item: item[1][2])) # Sort dict by position

    i = 0
    for kanji in sorted_dict.keys(): # Since position is incorrect, need to all positions
        reading, meaning, _ = sorted_dict[kanji]
        sorted_dict[kanji] = (reading, meaning, i)
        i += 1
    return sorted_dict

def find_kanjis_in_dict(kanjis_data: dict, kanji_to_find: str):
    """
    Finds and returns a tuple of kanji characters from a dictionary that matches a specific kanji string.

    Args:
    -----
    kanjis_data : dict
        A dictionary where kanji characters are keys.
    kanji_to_find : str
        The kanji string to find in the dictionary.

    Returns:
    --------
    tuple 
        A tuple of kanji characters found in the dictionary, or None if not found.
    """
    merged_keys = ""
    for key in kanjis_data.keys(): # Merge all kanjis in one string
        merged_keys += key
    if kanji_to_find in merged_keys:
        position_start = merged_keys.index(kanji_to_find)
        position_end = position_start + len(kanji_to_find) - 1

        current_position = 0
        kanjis_in_dict = []
        for key in kanjis_data.keys():
            pass
            if current_position >= position_start and current_position <= position_end:
                kanjis_in_dict.append(key)
            current_position += len(key)
        return tuple(kanjis_in_dict)
    else:
        return None

def update_data_only_kanji(kanji_data: dict, word: str):
    """
    Updates kanji data for a word composed solely of kanji characters by merging data.

    Args:
    -----
    kanji_data : dict
        A dictionary where kanji characters are keys and values are tuples of (reading, meaning, position).
    word : str
        The word composed solely of kanji characters to update in the dictionary.

    Returns:
    --------
    dict
        An updated and sorted dictionary with merged kanji data for the specified word.
    
    Raises:
    -------
    Exception
        If the word is not found in the kanji data.
    """
    kanjis = find_kanjis_in_dict(kanji_data, word)
    new_position = kanji_data[kanjis[0]][2] # Get position of the first kanji

    data_to_merge = []
    for kanji in kanjis:
        data_to_merge.append(kanji_data.pop(kanji))
    
    new_reading, new_meaning = "", ""
    for data in data_to_merge:
        data_reading, data_meaning, _ = data
        new_reading += data_reading
        new_meaning += data_meaning
    kanji_data[word] = (new_reading, new_meaning, new_position)

    return sort_dict(kanji_data)

def update_data_kanji_kana(kanji_data: dict, word: str):
    """Update dictionnary if word contains both kanjis and kanas."""
    word_reading = ""
    word_position = -1
    first_kanji = True

    for i in range(len(word)): # For each char of word
        if check_char_is_kana(word[i]):
            word_reading += word[i]
        else:
            try:
                reading, meaning, position = kanji_data.pop(word[i])
                word_reading += reading
                if first_kanji:
                    word_meaning = meaning
                    word_position = position
            except: # Sometimes, word doesn't appear completely in sentence
                word_meaning = ""
                word_position = -1
            
    word_data = (word_reading, word_meaning, word_position)
    kanji_data[word] = word_data

    return sort_dict(kanji_data)
        
def get_kanji_reading_meaning_position(sentence: str): 
    """
    Returns a dictionary containing kanji as keys and a tuple (reading, meaning, position) as values.

    This function extracts kanji data (reading, meaning, position) from a sentence transcription
    and returns it as a dict.

    Args:
    -----
    sentence : str
        The sentence containing the kanji to extract.

    Returns:
    --------
    dict
        A dictionary where kanji characters are keys and values are tuples of (reading, meaning, position).
    """
    pattern = r'\[([^\|\[\]]+)\|([^\[\]]+)\]'
    result = re.findall(pattern, sentence) 
    dict = {}
    i = 0
    for match in result:
            kanji, reading = match
            reading = reading.replace('|', '')
            dict[kanji] = (reading, "", i)
            i += 1
    return dict