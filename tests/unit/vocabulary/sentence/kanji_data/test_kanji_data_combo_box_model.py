import pytest
from src.vocabulary.sentence.kanji_data.model.combobox import KanjiDataComboBoxModel
from src.vocabulary.sentence.kanji_data import KanjiData
from src.constants import KanjiDataComboBoxModelMode

@pytest.fixture
def first_combobox_model():
    return KanjiDataComboBoxModel(KanjiDataComboBoxModelMode.FIRST_COMBO_BOX)

@pytest.fixture
def second_combobox_model():
    return KanjiDataComboBoxModel(KanjiDataComboBoxModelMode.SECOND_COMBO_BOX)

@pytest.fixture
def kanji_data_example():
    return KanjiData("日", "にち", "day")

def test_initialization_first_combobox(first_combobox_model):
    assert first_combobox_model.rowCount() == 0

def test_initialization_second_combobox(second_combobox_model):
    assert second_combobox_model.rowCount() == 1
    assert second_combobox_model.item(0).text() == "None"

def test_appendRow(first_combobox_model, kanji_data_example):
    first_combobox_model.appendRow(kanji_data_example)
    assert first_combobox_model.rowCount() == 1
    assert first_combobox_model.item(0).text() == "1: 日 - day"

def test_appendRow_second_combobox(second_combobox_model, kanji_data_example):
    second_combobox_model.appendRow(kanji_data_example)
    assert second_combobox_model.rowCount() == 2
    assert second_combobox_model.item(0).text() == "1: 日 - day"
    assert second_combobox_model.item(1).text() == "None"

def test_append_empty_row(first_combobox_model):
    first_combobox_model.append_empty_row()
    assert first_combobox_model.rowCount() == 1
    assert first_combobox_model.item(0).text() == "1:  - "

def test_insertRow(first_combobox_model, kanji_data_example):
    first_combobox_model.insertRow(0, kanji_data_example)
    assert first_combobox_model.rowCount() == 1
    assert first_combobox_model.item(0).text() == "1: 日 - day"

def test_modify_row(first_combobox_model, kanji_data_example):
    first_combobox_model.appendRow(kanji_data_example)
    modified_data = KanjiData("本", "ほん", "book")
    first_combobox_model.modify_row(0, modified_data)
    assert first_combobox_model.item(0).text() == "1: 本 - book"

def test_clear(first_combobox_model, second_combobox_model):
    first_combobox_model.appendRow(KanjiData("日", "にち", "day"))
    first_combobox_model.clear()
    assert first_combobox_model.rowCount() == 0

    second_combobox_model.appendRow(KanjiData("日", "にち", "day"))
    second_combobox_model.clear()
    assert second_combobox_model.rowCount() == 1
    assert second_combobox_model.item(0).text() == "None"

def test_clone(first_combobox_model, kanji_data_example):
    first_combobox_model.appendRow(kanji_data_example)
    cloned_model = first_combobox_model.clone()
    assert cloned_model.rowCount() == 1
    assert cloned_model.item(0).text() == "1: 日 - day"

def test_actualize_items_text(first_combobox_model):
    first_combobox_model.appendRow(KanjiData("日", "にち", "day"))
    first_combobox_model.appendRow(KanjiData("本", "ほん", "book"))
    first_combobox_model.actualize_items_text()
    assert first_combobox_model.item(0).text() == "1: 日 - day"
    assert first_combobox_model.item(1).text() == "2: 本 - book"
