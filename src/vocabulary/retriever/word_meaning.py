from requests_html import HTMLSession

def retrieve_meaning(word):
    """ Retrieve meaning through Jisho website. """
    json_meaning = retrieve_json_meaning(word)
    return deserialize_json_meaning(json_meaning, word)
        
def retrieve_json_meaning(word):
    http_request = "https://jisho.org/api/v1/search/words?keyword=" + word
    json_meaning = HTMLSession().get(http_request)
    return json_meaning.json()

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
            return [meanings, parts_of_speech]
        else: 
            raise ValueError #TODO: Modify exception