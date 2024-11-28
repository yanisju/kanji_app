import pytest
from PyQt6.QtGui import QStandardItem
from src.vocabulary.sentence.kanji_data import KanjiDataModel

@pytest.fixture
def kanji_data_model_instance():
    model = KanjiDataModel()
    model.add_row(KanjiMock("日", "にち", "day"))
    model.add_row(KanjiMock("本", "ほん", "book"))
    return model

class KanjiMock:
    def __init__(self, kanji, reading, meaning):
        self.kanji = kanji
        self.reading = reading
        self.meaning = meaning

    def get_item(self):
        return [
            QStandardItem(self.kanji),
            QStandardItem(self.reading),
            QStandardItem(self.meaning),
        ]

def test_initialization(kanji_data_model_instance):
    assert kanji_data_model_instance.rowCount() == 2
    assert kanji_data_model_instance.columnCount() == 3

def test_add_row(kanji_data_model_instance):
    kanji_data_model_instance.add_row(KanjiMock("人", "じん", "person"))
    assert kanji_data_model_instance.rowCount() == 3
    assert kanji_data_model_instance.item(2, 0).text() == "人"
    assert kanji_data_model_instance.item(2, 1).text() == "じん"
    assert kanji_data_model_instance.item(2, 2).text() == "person"

def test_modify_row(kanji_data_model_instance):
    kanji_data_model_instance.modify_row(0, KanjiMock("日", "ひ", "sun"))
    assert kanji_data_model_instance.item(0, 0).text() == "日"
    assert kanji_data_model_instance.item(0, 1).text() == "ひ"
    assert kanji_data_model_instance.item(0, 2).text() == "sun"

def test_modify_reading_meaning(kanji_data_model_instance):
    kanji_data_model_instance.modify_reading_meaning(0, "ひ", "sun")
    assert kanji_data_model_instance.item(0, 0).text() == "日"
    assert kanji_data_model_instance.item(0, 1).text() == "ひ"
    assert kanji_data_model_instance.item(0, 2).text() == "sun"

def test_clone(kanji_data_model_instance):
    cloned_model = kanji_data_model_instance.clone()
    assert cloned_model is not kanji_data_model_instance
    assert cloned_model.rowCount() == kanji_data_model_instance.rowCount()
    assert cloned_model.item(0, 0).text() == kanji_data_model_instance.item(0, 0).text()

def test_get_all_rows(kanji_data_model_instance):
    rows = kanji_data_model_instance.get_all_rows()
    assert rows == [["日", "にち", "day"], ["本", "ほん", "book"]]

def test_remove(kanji_data_model_instance):
    kanji_data_model_instance.remove(0)
    assert kanji_data_model_instance.rowCount() == 1
    assert kanji_data_model_instance.item(0, 0).text() == "本"

def test_clear(kanji_data_model_instance):
    kanji_data_model_instance.clear()
    assert kanji_data_model_instance.rowCount() == 0
    assert kanji_data_model_instance.columnCount() == 3

def test_set_position_kanji_sentence():
    model = KanjiDataModel()
    model.position_kanji_sentence = {}
    model.set_position_kanji_sentence("日本語", ["日", "本", "語"])
    assert model.position_kanji_sentence == {0: "日", 1: "本", 2: "語"}
