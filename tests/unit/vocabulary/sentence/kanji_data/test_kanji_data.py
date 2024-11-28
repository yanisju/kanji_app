import pytest
from PyQt6.QtGui import QStandardItem
from src.vocabulary.sentence.kanji_data import KanjiData


@pytest.fixture
def kanji_data():
    return KanjiData("日", "にち", "day")


def test_initialization():
    kanji = KanjiData("日", "にち", "day")
    assert kanji.word == "日"
    assert kanji.reading == "にち"
    assert kanji.meaning == "day"


def test_get_method(kanji_data):
    word, reading, meaning = kanji_data.__get__()
    assert word == "日"
    assert reading == "にち"
    assert meaning == "day"


def test_iteration(kanji_data):
    result = list(iter(kanji_data))
    assert result == ["日", "にち", "day"]


def test_get_item(kanji_data):
    items = kanji_data.get_item()
    assert len(items) == 3
    assert isinstance(items[0], QStandardItem)
    assert items[0].text() == "日"
    assert items[1].text() == "にち"
    assert items[2].text() == "day"


def test_update_attributes(kanji_data):
    kanji_data.update_attributes("本", "ほん", "book")
    assert kanji_data.word == "本"
    assert kanji_data.reading == "ほん"
    assert kanji_data.meaning == "book"
