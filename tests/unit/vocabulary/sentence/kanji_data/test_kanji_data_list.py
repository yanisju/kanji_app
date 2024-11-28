import pytest
from src.vocabulary.sentence.kanji_data import KanjiDataList

@pytest.fixture
def kanji_data_list():
    kanji_data_list = KanjiDataList()
    kanji_data_list.add("日", "にち", "day")
    kanji_data_list.add("本", "ほん", "book")
    return kanji_data_list

def test_initialization(kanji_data_list):
    assert len(kanji_data_list) == 2

def test_get_kanji(kanji_data_list):
    kanji = kanji_data_list.get_kanji("日")
    assert kanji.word == "日"
    assert kanji.reading == "にち"
    assert kanji.meaning == "day"

def test_add_new_kanji(kanji_data_list):
    kanji_data_list.add("人", "じん", "person")
    assert len(kanji_data_list) == 3
    kanji = kanji_data_list.get_kanji("人")
    assert kanji.word == "人"
    assert kanji.reading == "じん"
    assert kanji.meaning == "person"

def test_add_existing_kanji(kanji_data_list):
    kanji_data_list.add("日", "にち", "day")
    assert len(kanji_data_list) == 2

def test_add_empty_kanji(kanji_data_list):
    kanji_data_list.add_empty()
    assert len(kanji_data_list) == 3
    kanji = kanji_data_list[-1]
    assert kanji.word == ""
    assert kanji.reading == ""
    assert kanji.meaning == ""

def test_remove_existing_kanji(kanji_data_list):
    kanji_data_list.remove("日")
    assert len(kanji_data_list) == 1
    assert kanji_data_list.get_kanji("日") is None

def test_remove_non_existing_kanji(kanji_data_list):
    with pytest.raises(IndexError):
        kanji_data_list.remove("人")

def test_clear(kanji_data_list):
    kanji_data_list.clear()
    assert len(kanji_data_list) == 0

def test_update_kanji_meaning(kanji_data_list):
    kanji_data_list.update_kanji_meaning("日", "sun")
    kanji = kanji_data_list.get_kanji("日")
    assert kanji.meaning == "sun"

def test_merge_kanjis(kanji_data_list):
    kanji_data_list.merge_kanjis([0, 1])
    assert len(kanji_data_list) == 1
    kanji = kanji_data_list[0]
    assert kanji.word == "日本"
    assert kanji.reading == "にちほん"
    assert kanji.meaning == "daybook"

def test_clone(kanji_data_list):
    cloned_list = kanji_data_list.clone()
    assert cloned_list is not kanji_data_list
    assert len(cloned_list) == len(kanji_data_list)
    assert cloned_list[0].word == kanji_data_list[0].word
