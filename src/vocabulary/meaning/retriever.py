from requests_html import HTMLSession
import json

def retrieve_json_meaning(word):
    http_request = "https://jisho.org/api/v1/search/words?keyword=" + word
    json_meaning = HTMLSession().get(http_request)
    return json_meaning.json()

def retrieve_json_meaning_quick_init(word):
    path = "data/quick_init/meanings/" + word + ".txt"
    with open(path, encoding="utf-8") as file:
        meanings = file.read()
    return json.loads(meanings)

def find_data_index(word, data):
    """Find the accurate number in data JSON."""
    index = 0
    found = False
    while(index < len(data) and found != False):
        if word == data[index].get("slug"):
            found = True
    if found == True:
        return index
    else:
        return -1
    
def deserialize_meaning_part_of_speech(word, json_data):
    meanings = [] # Every differents meanings of the word
    one_meaning = "" # One meaning containing all synonyms of that meaning
    parts_of_speech = []
    one_part_of_speech = ""

    data_index = find_data_index(word, json_data)
    json_data_word_senses = json_data[data_index].get("senses")
    for i in range(len(json_data_word_senses)):
        for j in range(len(json_data_word_senses[i].get("english_definitions"))):
            if one_meaning != "":
                one_meaning += ", "
            one_meaning += json_data_word_senses[i].get("english_definitions")[j]
        for j in range(len(json_data_word_senses[i].get("parts_of_speech"))):
            if one_part_of_speech != "":
                one_part_of_speech += ", "
            one_part_of_speech += json_data_word_senses[i].get("parts_of_speech")[j]
        meanings.append(one_meaning)
        parts_of_speech.append(one_part_of_speech)
        one_meaning= ""
        one_part_of_speech = ""
            
    if(len(meanings) != 0):
        return (meanings, parts_of_speech)
    else: 
        return ("can't find meanings", "same")
        raise ValueError #TODO: Modify exception

def deserialize_json_meaning(json_meaning, word):
    status_code = json_meaning.get("meta").get("status") # Get HTML status code
    if status_code != 200:
        raise ValueError # TODO: Modify exception
    else:
        return deserialize_meaning_part_of_speech(word, json_meaning.get("data"))

def get_meaning(word, quick_init):
    if quick_init:
        json_meaning = retrieve_json_meaning_quick_init(word)
    else:
        json_meaning = retrieve_json_meaning(word)
    meanings, parts_of_speech = deserialize_json_meaning(json_meaning, word)
    
    return meanings, parts_of_speech