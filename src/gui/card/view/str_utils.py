from PyQt6.QtGui import QTextCursor
from PyQt6.QtWidgets import QToolTip

def get_color(tag):
    colors = {"h": "blue", 
              "n": "orange", 
              "o": "green",
              "a": "red",
              "k": "purple"
              }
    return colors.get(tag[0], "black")  # Default black if tag not found

def colorize_transcription(match):
    kanji = match.group(1)
    tag = match.group(3)
    color = get_color(tag)
    return f'<span style="color:{color}">{kanji}</span>'

def is_kanji(text):
    return any("\u4e00" <= char <= "\u9faf" for char in text)

def show_transcription(view, event, sentence):
    """Show a QToolTip containing furigana"""

    cursor = view.cursorForPosition(event.pos()) # Get cursor for position
    char_position = cursor.position() # Get the position of the character under the cursor

    if char_position <= len(sentence.lang_from):
        cursor.setPosition(char_position) # Place the cursor at this position and select the character
        cursor.movePosition(QTextCursor.MoveOperation.Right, QTextCursor.MoveMode.KeepAnchor, 1)
        char = cursor.selectedText()
        
        if is_kanji(char):
            kanji = sentence.position_kanji[cursor.position() - 1]
            kana_transcription = sentence.kanji_readings[kanji]

            print_furigana(view, cursor, kana_transcription)
        else:
            QToolTip.hideText()
    else:
        cursor.select(QTextCursor.SelectionType.WordUnderCursor)
        word = cursor.selectedText()

        if is_kanji(word):
            try:
                kana_transcription = sentence.kanji_readings[word]
                print_furigana(view, cursor, kana_transcription)
            except:
                QToolTip.hideText()
        else:
            QToolTip.hideText()

def print_furigana(view, cursor, kana_transcription):
    cursor_rect = view.cursorRect(cursor)
    text_position = cursor_rect.center()
    global_position = view.mapToGlobal(text_position)
    QToolTip.showText(global_position, kana_transcription, view)