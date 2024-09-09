from requests_html import HTMLSession

from . import find_kanjis_in_dict,  check_word_contains_kana

def create_sentences_html_request(word, lang_from, lang_to):
    """ Create HTML request: fetch through Tatoeba website."""
    
    http_request = "https://tatoeba.org/en/api_v0/search?from=" + lang_from + "&to=" + lang_to + "&query=" + word
    params = "&orphans=no&sort=relevance&trans_filter=limit&trans_orphan=no&trans_unapproved=no&unapproved=no&word_count_min=1"
    print(http_request + params) # TODO: Remove one day
    return http_request + params    
        
def retrieve_sentences(word, lang_from, lang_to):
    session = HTMLSession()
    json_sentences = session.get(create_sentences_html_request(word, lang_from, lang_to))
    return json_sentences.json()

def deserialize_json_sentence(json_sentences, sentence_desired_count, word):
    """ 
    Processes JSON formatted sentences and returns a tuple containing example sentences, their translations, and transcriptions.

    This function extracts a specified number of example sentences, their translations, and transcriptions from a JSON structure. It checks if the desired word appears in each sentence before including it in the results.

    Args:
    -----
    json_sentences : dict
        A dictionary containing sentences in JSON format, typically returned from an API.
    sentence_desired_count : int
        The number of example sentences to retrieve.
    word : str
        The word that must appear in the example sentences.

    Returns:
    --------
    tuple
        A tuple containing three lists:
        - `lang_from_sentence` (list of str): The example sentences in the original language.
        - `lang_to_sentence` (list of str): The translations of the example sentences.
        - `sentence_transcription` (list of str): The transcriptions of the example sentences (especially useful for Japanese).
    """
    
    lang_from_sentence = []
    lang_to_sentence = []
    sentence_transcription = [] 
    
    if(sentence_desired_count > len(json_sentences['results'])): # Sometimes, there aren't enough example sentences
        example_sentences_count = len(json_sentences['results'])
    else:
        example_sentences_count = sentence_desired_count
    
    for i in range(example_sentences_count): # For the number of sentences retrieved
        this_lang_from_sentence = json_sentences['results'][i]["text"]
        if check_word_contains_kana(word) or word in this_lang_from_sentence: # Add sentence if word does appear in sentence
            lang_from_sentence.append(this_lang_from_sentence)
            
            j = 0
            while(json_sentences['results'][i]["translations"][j] == []): # Sometimes the first translation is empty
                j += 1
            
            k = 0
            while(json_sentences['results'][i]["translations"][j][k] == []): # Same
                k += 1
            lang_to_sentence.append(json_sentences['results'][i]["translations"][j][k]["text"])
            
            sentence_transcription.append(json_sentences['results'][i]["transcriptions"][0]["text"])
    return (lang_from_sentence, lang_to_sentence, sentence_transcription)

def get_sentences(word, lang_from, lang_to, sentence_desired_count):
    json_sentences = retrieve_sentences(word, lang_from, lang_to)
    return deserialize_json_sentence(json_sentences, sentence_desired_count, word)