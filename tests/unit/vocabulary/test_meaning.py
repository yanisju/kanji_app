import pytest
from unittest.mock import patch
from src.vocabulary.meaning.meaning import VocabularyMeaning


# ==== Fixtures ====

@pytest.fixture
def mock_get_meaning():
    with patch("src.vocabulary.meaning.meaning.get_meaning") as mock:
        mock.return_value = (
            ["Japanese language", "Book"],
            ["Noun", "Noun"]
        )
        yield mock


@pytest.fixture
def vocabulary_meaning(mock_get_meaning):
    return VocabularyMeaning("日本語")


# ==== Tests ====

def test_initialization(vocabulary_meaning: VocabularyMeaning, mock_get_meaning):
    mock_get_meaning.assert_called_once_with("日本語")
    assert vocabulary_meaning.word == "日本語"
    assert len(vocabulary_meaning._meanings) == 2
    assert vocabulary_meaning._meanings == ["Japanese language", "Book"]
    assert vocabulary_meaning._part_of_speech == ["Noun", "Noun"]
    assert vocabulary_meaning.standard_item_model.rowCount() == 2


def test_add_meaning(vocabulary_meaning):
    vocabulary_meaning.add("Language", "Noun")
    assert len(vocabulary_meaning._meanings) == 3
    assert vocabulary_meaning._meanings[-1] == "Language"
    assert vocabulary_meaning._part_of_speech[-1] == "Noun"
    assert vocabulary_meaning.standard_item_model.rowCount() == 3
    assert vocabulary_meaning.standard_item_model.item(2, 0).text() == "Language"


def test_remove_meaning(vocabulary_meaning):
    vocabulary_meaning.remove(0)
    assert len(vocabulary_meaning._meanings) == 1
    assert vocabulary_meaning._meanings[0] == "Book"
    assert vocabulary_meaning.standard_item_model.rowCount() == 1
    assert vocabulary_meaning.standard_item_model.item(0, 0).text() == "Book"


def test_remove_all(vocabulary_meaning):
    vocabulary_meaning.remove_all()
    assert len(vocabulary_meaning._meanings) == 0
    assert len(vocabulary_meaning._part_of_speech) == 0
    assert vocabulary_meaning.standard_item_model.rowCount() == 0


def test_clone_model(vocabulary_meaning):
    clone = vocabulary_meaning.clone_model()
    assert clone.rowCount() == vocabulary_meaning.standard_item_model.rowCount()
    assert clone.columnCount() == vocabulary_meaning.standard_item_model.columnCount()
    for row in range(clone.rowCount()):
        for col in range(clone.columnCount()):
            assert clone.item(row, col).text() == vocabulary_meaning.standard_item_model.item(row, col).text()


def test_set_item(vocabulary_meaning):
    vocabulary_meaning[0] = ("Updated Meaning", "Updated POS")
    assert vocabulary_meaning._meanings[0] == "Updated Meaning"
    assert vocabulary_meaning._part_of_speech[0] == "Updated POS"
    assert vocabulary_meaning.standard_item_model.item(0, 0).text() == "Updated Meaning"
    assert vocabulary_meaning.standard_item_model.item(0, 1).text() == "Updated POS"
