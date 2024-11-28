import pytest
from PyQt6.QtCore import Qt
from src.vocabulary.model.sentence import SentenceModel
from src.vocabulary.sentence.manager import SentenceManager, Sentence
from src.vocabulary.sentence.kanji_data import KanjiDataList, KanjiData


# ==== Fixtures ====

@pytest.fixture
def sentence_manager():
    return SentenceManager()


@pytest.fixture
def sentence_model(sentence_manager: SentenceManager):
    return sentence_manager.sentences_model


@pytest.fixture
def kanji_data_list():
    kanji_data_list = KanjiDataList()
    kanji_data_list.add("本", "ほん", "book")
    kanji_data_list.add("日", "にち", "day")
    kanji_data_list.add("語", "ご", "language")
    return kanji_data_list



@pytest.fixture
def sentence(kanji_data_list):
    return Sentence(
        None,
        "日本語の勉強を始めました。",
        "I started studying Japanese.",
        kanji_data_list,
        None
    )


# ==== Tests ====

def test_initialization(sentence_model: SentenceModel):
    assert sentence_model.rowCount() == 0
    assert sentence_model.columnCount() == 4


def test_append_sentence(sentence_model: SentenceModel, sentence: Sentence):
    sentence_model.append_sentence(sentence)
    assert sentence_model.rowCount() == 1
    assert sentence_model.item(0, 0).text() == "日本語の勉強を始めました。"
    assert sentence_model.item(0, 1).text() == "I started studying Japanese."


def test_modify_row(sentence_model: SentenceModel, sentence_manager: SentenceManager, sentence: Sentence):
    sentence_manager.append(sentence)

    updated_sentence = Sentence(
        None,
        "日本語の本を読みました。",
        "I read a Japanese book.",
        sentence.kanji_data_list,
        None
    )
    sentence_model.modify_row(updated_sentence, 0)

    assert sentence_model.item(0, 0).text() == "日本語の本を読みました。"
    assert sentence_model.item(0, 1).text() == "I read a Japanese book."


def test_get_sentence_by_row(sentence_model, sentence_manager, sentence):
    sentence_manager.append(sentence)
    retrieved_sentence = sentence_model.get_sentence_by_row(0)
    assert retrieved_sentence.sentence == "日本語の勉強を始めました。"
    assert retrieved_sentence.translation == "I started studying Japanese."


def test_remove_row(sentence_model: SentenceModel, sentence_manager: SentenceManager, sentence: Sentence):
    assert sentence_manager.sentences_model == sentence_model
    sentence_manager.append(sentence)
    assert sentence_model.rowCount() == 1
    sentence_model.remove_row(0)
    assert sentence_model.rowCount() == 0


def test_remove_all_rows(sentence_model, sentence_manager, sentence):
    sentence_manager.append(sentence)
    sentence_manager.append(sentence)
    assert sentence_model.rowCount() == 2
    sentence_model.remove_all_rows()
    assert sentence_model.rowCount() == 0