import pytest
from src.vocabulary.sentence.manager import SentenceManager
from src.vocabulary.model.sentence import SentenceModel
from src.vocabulary.sentence.manager import Sentence
from src.vocabulary.sentence.kanji_data import KanjiDataList, KanjiData


# ==== Fixtures ====

@pytest.fixture
def sentence_manager():
    return SentenceManager()


@pytest.fixture
def kanji_data_list1():
    kanji_data_list = KanjiDataList()
    kanji_data_list.add("今", "いま", "now")
    kanji_data_list.add("日", "にち", "day")
    kanji_data_list.add("時", "とき", "time")
    return kanji_data_list

@pytest.fixture
def sentence1(kanji_data_list1):
    return Sentence(
        None,
        "今日はとてもいい天気ですが、少し寒いですね。",
        "Today is very nice weather, but it's a bit cold.",
        kanji_data_list1,
        None
    )

@pytest.fixture
def kanji_data_list2():
    kanji_data_list = KanjiDataList()
    kanji_data_list.add("明", "あした", "tomorrow")
    kanji_data_list.add("新", "あたらしい", "new")
    kanji_data_list.add("計", "けい", "plan")
    return kanji_data_list


@pytest.fixture
def sentence2(kanji_data_list2):
    return Sentence(
        None,
        "明日は新しいプロジェクトを始める予定です。",
        "Tomorrow, we plan to start a new project.",
        kanji_data_list2,
        None
    )


# ==== Tests ====

def test_initialization():
    manager = SentenceManager()
    assert len(manager) == 0
    assert isinstance(manager.sentences_model, SentenceModel)


def test_append_sentence(sentence_manager, sentence1):
    sentence_manager.append(sentence1)
    assert len(sentence_manager) == 1
    assert sentence_manager[0] == sentence1
    assert sentence1 in sentence_manager


def test_append_from_sentence_data(sentence_manager, kanji_data_list2):
    sentence_str = "来週は友達と旅行に行く予定です。"
    translation_str = "Next week, I plan to go on a trip with friends."

    sentence_manager.append_from_sentence_data(sentence_str, translation_str, kanji_data_list2)
    assert len(sentence_manager) == 1
    sentence = sentence_manager[0]
    assert isinstance(sentence, Sentence)
    assert sentence.sentence == sentence_str
    assert sentence.translation == translation_str
    assert sentence.kanji_data_list == kanji_data_list2


def test_append_empty_sentence(sentence_manager):
    sentence_manager.append_empty_sentence()
    assert len(sentence_manager) == 1
    sentence = sentence_manager[0]
    assert isinstance(sentence, Sentence)
    assert sentence.sentence == ""
    assert sentence.translation == ""
    assert isinstance(sentence.kanji_data_list, KanjiDataList)


def test_sort_by_sentence_length(sentence_manager, sentence1, sentence2):
    shorter_kanji_data_list = KanjiDataList()
    shorter_kanji_data_list.add("雨", "あめ", "rain")
    shorter_sentence = Sentence(
        None,
        "雨が降っています。",
        "It is raining.",
        shorter_kanji_data_list,
        None
    )

    sentence_manager.append(sentence1)
    sentence_manager.append(sentence2)
    sentence_manager.append(shorter_sentence)

    sentence_manager.sort_by_sentence_length()

    assert sentence_manager[0].sentence == "雨が降っています。"
    assert sentence_manager[1].sentence == "明日は新しいプロジェクトを始める予定です。"
    assert sentence_manager[2].sentence == "今日はとてもいい天気ですが、少し寒いですね。"
    assert all(sentence in sentence_manager for sentence in sentence_manager)


def test_pop_sentence(sentence_manager, sentence1):
    sentence_manager.append(sentence1)
    popped_sentence = sentence_manager.pop(0)
    assert popped_sentence == sentence1
    assert len(sentence_manager) == 0


def test_clear_sentences(sentence_manager, sentence1, sentence2):
    sentence_manager.append(sentence1)
    sentence_manager.append(sentence2)
    sentence_manager.clear()
    assert len(sentence_manager) == 0
    assert sentence_manager.sentences_model.rowCount() == 0
