from .str_utils import *

import re
from bs4 import BeautifulSoup

def remove_spaces_outside_spans(soup):
    new_contents = []
    for content in soup.contents:
        if isinstance(content, str):
            new_contents.append(re.sub(r'\s+', '', content))
        else:
            new_contents.append(str(content))
    return ''.join(new_contents)

def get_sentence_from(text):
    """Get sentence in japanese."""
    pattern = r"(\w+)\[(.*?)\;(.*?)\]"

    text = re.sub(pattern, colorize_transcription, str(text))

    soup = BeautifulSoup(text, 'html.parser')
    result = remove_spaces_outside_spans(soup)

    return result

def get_sentence_meaning(word1_data, word2_data):
    result = ""
    if word1_data != None:
        word1, _, word1_meaning, *_ = word1_data
        result += word1 + " - " + word1_meaning
    
    if word2_data != None:
        word2, _, word2_meaning, *_ = word2_data
        result += "<br>" + word2 + " - " + word2_meaning
    return result
        
def get_text(sentence_fields):
        if(len(sentence_fields) == 0):
            return ""
        sentence, translation, word1_data, word2_data = sentence_fields

        card_text = get_sentence_from(sentence)
        card_text += "<hr>" 
        card_text += translation + "<br>"
        card_text += get_sentence_meaning(word1_data, word2_data)
        return card_text