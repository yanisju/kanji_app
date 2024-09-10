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

# TODO: can get mutliple meanings, the first one is often the most precise one. (senses[0])
# However. sometimes a word can have a lot of meaning: in that case, the program must open a new tab 
def deserialize_json_meaning(json_meaning, word):
    meanings = [] # Every differents meanings of the word
    one_meaning = [] # One meaning containing all synonyms of that meaning
    parts_of_speech = []
    one_part_of_speech = []
    
    status_code = json_meaning.get("meta").get("status") # Get HTML status code
    if status_code != 200:
        raise ValueError # TODO: Modify exception
    else:
        for i in range(len(json_meaning.get("data"))):
            if(json_meaning.get("data")[i].get("japanese")[0].get("word") == word): # Check if the word in dictionnary is the same
                for j in range(len(json_meaning.get("data")[i].get("senses"))):
                    # TODO: modify
                    for k in range(len(json_meaning.get("data")[i].get("senses")[0].get("english_definitions"))): # senses[0] / senses[j]
                        one_meaning.append(json_meaning.get("data")[i].get("senses")[0].get("english_definitions")[k])
                    for k in range(len(json_meaning.get("data")[i].get("senses")[j].get("parts_of_speech"))):
                        one_part_of_speech.append(json_meaning.get("data")[0].get("senses")[j].get("parts_of_speech")[k])
                    #  meanings.append(one_meaning)
                    meanings = one_meaning
                    parts_of_speech.append(one_part_of_speech)
                    one_meaning= []
                    one_part_of_speech = []
                    
        if(len(meanings) != 0):
            return (meanings, parts_of_speech[0])
        else: 
            raise ValueError #TODO: Modify exception
        
def get_meaning_str(meaning_list):
    meaning_str = ""
    for meaning in meaning_list:
        if len(meaning_str) == 0:
            meaning_str += meaning
        else:
            meaning_str = meaning_str + ", " + meaning
    return meaning_str

def get_meaning(word, quick_init):
    if quick_init:
        json_meaning = retrieve_json_meaning_quick_init(word)
    else:
        json_meaning = retrieve_json_meaning(word)
    meanings, part_of_speech = deserialize_json_meaning(json_meaning, word)
    word_meaning = get_meaning_str(meanings) 
    
    return word_meaning, part_of_speech