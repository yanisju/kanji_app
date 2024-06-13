from src.anki.card import AnkiCard

class TestAnkiCard:
    
    def test_card_word_transcription_one(self):
        card = AnkiCard(42)
        word_transcrition = card.extract_transcription("電車[でんしゃ;h,a] は たった今[たったいま;n4] 出[で,でる;k1]た 所[ところ;h] です ", "たった今")
        assert word_transcrition == "たった今[たったいま;n4]"
        
    def test_card_word_transcription_two(self):
        card = AnkiCard(42)
        word_transcrition = card.extract_transcription("空[そら;a] が 暗[くら,くらい;h]く なって 、 今[いま;a]にも 雨[あめ;a] が 降[ふ,ふる;k1]り そう です 。", "今にも")
        assert word_transcrition == "今[いま;a]にも"
        
    def test_card_word_transcription_three(self):
        card = AnkiCard(42)
        word_transcrition = card.extract_transcription("この頃[このごろ;h] 、 寒[さむ,さむい;k2]い 日[ひ;h] が 多[おお,おおい;k1,k2]い です ね 。", "この頃")
        assert word_transcrition == "この頃[このごろ;h]"