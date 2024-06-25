from requests_html import HTMLSession
class DataRetriever():
    """ Used to retrieve examples sentences through Internet. Here sentences are fetched through "Tatoeba" website.
    """
    def __init__(self, sentence_desired_count, lang_from, lang_to):
        self.sentences = []
        self.sentence_desired_count = sentence_desired_count # Number of sentences desired
        self.lang_from = lang_from
        self.lang_to = lang_to
        self.session = HTMLSession()
        
    def create_sentences_html_request(self, vocabulary):
        """ Create HTML request: fetch through Tatoeba website."""
        
        http_request = "https://tatoeba.org/en/api_v0/search?from=" + self.lang_from + "&to=" + self.lang_to + "&query=" + vocabulary
        params = "&orphans=no&sort=relevance&trans_filter=limit&trans_orphan=no&trans_unapproved=no&unapproved=no&word_count_min=1"
        print(http_request + params)
        return http_request + params    
          
    def retrieve_sentences(self, vocabulary):
        json_sentences = self.session.get(self.create_sentences_html_request(vocabulary))
        return json_sentences.json()
    
    def retrieve_meaning(self, vocabulary):
        """ Retrieve meaning through Jisho website. """
        
        http_request = "https://jisho.org/api/v1/search/words?keyword=" + vocabulary
        json_meaning = self.session.get(http_request)
        return json_meaning.json()
        
    
    def deserialize_json_sentence(self, json_sentences):
        """ Returns from the fetched sentence:
        - Example sentence in the desired language.
        - Translation from the example sentence in the desired language.
        - Transcription of the example sentence. (especially for japanese)
        """
        
        lang_from_sentence = []
        lang_to_sentence = []
        sentence_transcription = [] 
        
        if(self.sentence_desired_count > len(json_sentences['results'])): # Sometimes, there aren't enough example sentences
            example_sentences_count = len(json_sentences['results'])
        else:
            example_sentences_count = self.sentence_desired_count
        
        for i in range(example_sentences_count): # For the number of sentences retrieved
            lang_from_sentence.append(json_sentences['results'][i]["text"])
            
            j = 0
            while(json_sentences['results'][i]["translations"][j] == []): # Sometimes the first translation is empty
                j += 1
            
            k = 0
            while(json_sentences['results'][i]["translations"][j][k] == []): # Same
                k += 1
            lang_to_sentence.append(json_sentences['results'][i]["translations"][j][k]["text"])
            
            sentence_transcription.append(json_sentences['results'][i]["transcriptions"][0]["text"])
        return [lang_from_sentence, lang_to_sentence, sentence_transcription]
    
    # TODO: can get mutliple meanings, the first one is often the most precise one. (senses[0])
    # However. sometimes a word can have a lot of meaning: in that case, the program must open a new tab 
    def deserialize_json_meaning(self, json_meaning, word):
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
            
    def start(self, vocabulary):
        json_sentences = self.retrieve_sentences(vocabulary)
        sentences = self.deserialize_json_sentence(json_sentences)
        
        json_meaning = self.retrieve_meaning(vocabulary)
        both_meanings_part_of_speech = self.deserialize_json_meaning(json_meaning, vocabulary)
        meanings = both_meanings_part_of_speech[0]
        part_of_speech = both_meanings_part_of_speech[1]
        
        return [sentences[0], sentences[1], sentences[2], meanings, part_of_speech]
        
