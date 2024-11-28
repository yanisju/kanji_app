import pytest
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QStandardItem
from src.vocabulary.model.vocabulary import VocabularyModel


# ==== Fixtures ====

@pytest.fixture
def vocabulary_model():
    return VocabularyModel()


@pytest.fixture
def sample_standard_item():
    return [
        QStandardItem("日本語"),              # Word
        QStandardItem("Japanese language"), # Meanings
        QStandardItem("Noun"),              # Parts of Speech
        QStandardItem("私は日本語を勉強します。")  # Sentences
    ]


# ==== Tests ====

def test_initialization(vocabulary_model):
    assert vocabulary_model.rowCount() == 0
    assert vocabulary_model.columnCount() == 4


def test_append_vocabulary(vocabulary_model, sample_standard_item):
    vocabulary_model.append_vocabulary("日本語", sample_standard_item)
    assert vocabulary_model.rowCount() == 1
    assert vocabulary_model.item(0, 0).text() == "日本語"
    assert vocabulary_model.item(0, 1).text() == "Japanese language"
    assert vocabulary_model.item(0, 2).text() == "Noun"
    assert vocabulary_model.item(0, 3).text() == "私は日本語を勉強します。"


def test_modify_row(vocabulary_model, sample_standard_item):
    vocabulary_model.append_vocabulary("日本語", sample_standard_item)
    
    updated_item = [
        QStandardItem("英語"),              # Word
        QStandardItem("English language"), # Meanings
        QStandardItem("Noun"),             # Parts of Speech
        QStandardItem("私は英語を話します。")  # Sentences
    ]
    vocabulary_model.modify_row(0, updated_item)

    assert vocabulary_model.item(0, 0).text() == "英語"
    assert vocabulary_model.item(0, 1).text() == "English language"
    assert vocabulary_model.item(0, 2).text() == "Noun"
    assert vocabulary_model.item(0, 3).text() == "私は英語を話します。"


def test_vertical_header_set(vocabulary_model, sample_standard_item):
    vocabulary_model.append_vocabulary("日本語", sample_standard_item)
    header = vocabulary_model.headerData(0, Qt.Orientation.Vertical)
    assert header == "日本語"
