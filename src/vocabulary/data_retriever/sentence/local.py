import pandas as pd

from . import SentenceRetriever

class SentenceLocalRetriever(SentenceRetriever):
    def __init__(self) -> None:
        pass

    def get_sentences(self, word):
        filename = "data/sentences_data/eng_to_jpn"
        transcriptions_filename = "data/sentences_data/transcriptions"

        data = read_csv(filename)
        transcriptions = read_transcriptions(transcriptions_filename)

        return find_phrases_containing_word(data, transcriptions, word)


def read_csv(filename):
    data = pd.read_csv(
        filename + '.tsv',
        sep='\t',
        usecols=[
            0,
            1,
            3],
        names=[
            "ID",
            "Sentence",
            "Translation"],
        header=None)
    return data


def read_transcriptions(filename):
    transcriptions = pd.read_csv(
        filename + '.csv',
        sep='\t',
        usecols=[
            0,
            4],
        names=[
            "ID",
            "Transcription"],
        header=None)
    return transcriptions


def find_phrases_containing_word(data, transcriptions, search_word) -> list:
    filtered_data = data[data["Sentence"].str.contains(search_word, na=False)]
    unique_rows = filtered_data.drop_duplicates(subset=["Sentence"])

    merged_data = pd.merge(unique_rows, transcriptions, on="ID", how="left")
    results_with_transcriptions = merged_data[[
        "Sentence", "Translation", "Transcription"]].values.tolist()
    return results_with_transcriptions
