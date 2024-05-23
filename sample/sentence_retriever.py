from requests_html import HTMLSession # type: ignore
class SentenceRetriever():
    """ Used to retrieve examples sentences through Internet. Here sentences are fetched through "Tatoeba" website.
    """
    def __init__(self, sentence_count, lang_from, lang_to):
        self.sentences = []
        self.sentence_count = sentence_count
        self.lang_from = lang_from
        self.lang_to = lang_to
        self.session = HTMLSession()
        
    def create_html_request(self, vocabulary):
        http_request = "https://tatoeba.org/en/api_v0/search?from=" + self.lang_from + "&to=" + self.lang_to + "&query=" + vocabulary
        params = "&orphans=no&sort=relevance&trans_filter=limit&trans_orphan=no&trans_unapproved=no&unapproved=no&word_count_min=1"
        return http_request + params    
          
    def retrieve_sentences(self, vocabulary):
        json_sentences = self.session.get(self.create_html_request(vocabulary))
        return json_sentences.json()
        
    def deserialize_json_sentence(self, json_sentences):
        """ Returns from the fetched sentence:
        - Example sentence in the desired language.
        - Translation from the example sentence in the desired language.
        - Transcription of the example sentence. (especially for japanese)
        """
        
        lang_from_sentence = []
        lang_to_sentence = []
        sentence_transcription = [] 
        for i in range(self.sentence_count):
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
    
    def start(self, vocabulary):
        json_sentences = self.retrieve_sentences(vocabulary)
        return self.deserialize_json_sentence(json_sentences)
        
