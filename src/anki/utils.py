
def get_word_anki_format(word_reading):
    color = "a" # TODO: get color in data
    return f"[{word_reading};{color}]"

def get_sentence_anki_format(sentence_str, kanji_data):
    sentence_anki_format = sentence_str
    added_word_index = 0
    for word_data in kanji_data:
        word, word_reading, *_  = word_data
        word_position = sentence_anki_format.find(word)
        if word_position != -1:
            word_anki_format = get_word_anki_format(word_reading)
            position = word_position + len(word)  # Position to put brackets
            sentence_anki_format = sentence_anki_format[:position] + word_anki_format + " " + sentence_anki_format[position:] 
            added_word_index += len(word) + len(word_anki_format)  + 1
            if word_position != 0 and word_position != " ":
                sentence_anki_format = sentence_anki_format[:word_position] + " " + sentence_anki_format[word_position:]

    return sentence_anki_format

def get_word_n_anki_format(word, word_reading):
    word_reading_anki_format = get_word_anki_format(word_reading)
    return word + word_reading_anki_format

def get_fields_as_list(sentence):
    fields_list = []
    fields_list.append(get_sentence_anki_format(sentence.sentence, sentence.kanji_data))
    fields_list.append(sentence.translation)
    
    if sentence.word1_data:
        word1, word1_reading, word1_meaning = sentence.word1_data
        fields_list.append(get_word_n_anki_format(word1, word1_reading))
        fields_list.append(word1_meaning)
    else: 
        fields_list.append("")
        fields_list.append("")

    if sentence.word2_data:
        word2, word2_reading, word2_meaning = sentence.word2_data
        fields_list.append(get_word_n_anki_format(word2, word2_reading))
        fields_list.append(word2_meaning)
    else: 
        fields_list.append("")
        fields_list.append("")

    fields_list.append("")

    return fields_list

