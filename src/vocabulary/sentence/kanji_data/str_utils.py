def check_char_is_kana(char):
    if ord(char) >= 12352 and ord(char) <= 12543:
        return True
    else:
        return False


def is_word_in_dict(kanji_data: dict, word: str):
    return word in kanji_data.keys()


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
    kanjis = [k for k, *_ in kanjis_data]
    for key in kanjis:  # Merge all kanjis in one string
        merged_keys += key
    if kanji_to_find in merged_keys:
        position_start = merged_keys.index(kanji_to_find)
        position_end = position_start + len(kanji_to_find) - 1

        current_position = 0
        kanjis_in_dict = []
        for key in kanjis:
            if current_position >= position_start and current_position <= position_end:
                kanjis_in_dict.append(key)
            current_position += len(key)
        return tuple(kanjis_in_dict)
    else:
        raise KeyError
