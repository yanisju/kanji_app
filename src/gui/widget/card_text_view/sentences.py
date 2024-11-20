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
    """
    Return the formatted meaning of two words as HTML.

    Args:
        word1_data (tuple): Data for the first word (word, reading, meaning, kanji_data, position).
        word2_data (tuple): Data for the second word (same format as word1_data).

    Returns:
        str: Formatted HTML string showing word and its meaning.
    """
    result = ""
    if word1_data is not None:
        word1, _, word1_meaning, *_ = word1_data
        result += f"<b>{word1}</b> - <i>{word1_meaning}</i>"

    if word2_data is not None:
        word2, _, word2_meaning, *_ = word2_data
        result += f"<br><b>{word2}</b> - <i>{word2_meaning}</i>"

    return result


def get_text(sentence_fields):
    """
    Generate formatted HTML content for the Anki card.

    Args:
        sentence_fields (list): A list containing sentence, translation, word1_data, word2_data.

    Returns:
        str: Formatted HTML string for the sentence, translation, and word meanings.
    """
    if len(sentence_fields) == 0:
        return ""

    # Unpack sentence fields
    sentence, translation, word1_data, word2_data = sentence_fields

    # Build the sentence and translation sections
    card_text = f"<div class='sentence'><span>{
        get_sentence_from(sentence)}</span></div>"
    card_text += "<hr>"
    card_text += f"<div class='translation'>{translation}</div><br>"

    # Append word meanings
    card_text += f"<div class='word-meanings'>{
        get_sentence_meaning(
            word1_data, word2_data)}</div>"

    return card_text
