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

def get_sentence_meaning(text1, text2, text3, text4):
    result = text1 + " - " + text2
    if text3 and text4:
        result += "<br>" + text3 + " - " + text4
    return result

def set_furiganas(furiganas, sentence):
    """Set furiganas dictionnary thanks to sentence transcription."""
    pattern = re.compile(r"(\w+)\[(.*?)\;(.*?)\]")
    for match in pattern.finditer(sentence):
        furiganas.update({match.group(1): match.group(2)})
        
def get_text(furiganas, sentence_fields):
        set_furiganas(furiganas, sentence_fields[2])

        card_text = get_sentence_from(sentence_fields[0])
        card_text += "<hr>" 
        card_text += sentence_fields[1] + "<br>"
        card_text += get_sentence_meaning(sentence_fields[2], sentence_fields[3], sentence_fields[4], sentence_fields[5])
        return card_text

# lang_from, translation, word, meaning, self.word2, self.word2_meaning