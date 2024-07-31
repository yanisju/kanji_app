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

def show_transcription(view, event):
    """Show a QToolTip containing furigana"""
    cursor = view.cursorForPosition(event.pos())
    cursor.select(QTextCursor.SelectionType.WordUnderCursor)
    selected_text = cursor.selectedText()
    
    if is_kanji(selected_text):
        kana_transcription = view.get_furigana(selected_text)

        # cursor.movePosition(cursor.MoveOperation.PreviousCharacter, cursor.MoveMode.KeepAnchor)
        cursor_rect = view.cursorRect(cursor)
        text_position = cursor_rect.center()
        global_position = view.mapToGlobal(text_position)

        QToolTip.showText(global_position, kana_transcription, view)
    else:
        QToolTip.hideText()
