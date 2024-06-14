from src.anki.card import AnkiCard

class TestAnkiCard:
    
    def test_card_word_transcription_one(self):
        card = AnkiCard(42)
        word_transcrition = card.get_japanese_word_transcription("電車[でんしゃ;h,a] は たった今[たったいま;n4] 出[で,でる;k1]た 所[ところ;h] です ", "たった今")
        assert word_transcrition == "たった今[たったいま;n4]"
        
    def test_card_word_transcription_two(self):
        card = AnkiCard(42)
        word_transcrition = card.get_japanese_word_transcription("空[そら;a] が 暗[くら,くらい;h]く なって 、 今[いま;a]にも 雨[あめ;a] が 降[ふ,ふる;k1]り そう です 。", "今にも")
        assert word_transcrition == "今[いま;a]にも"
        
    def test_card_word_transcription_three(self):
        card = AnkiCard(42)
        word_transcrition = card.get_japanese_word_transcription("この頃[このごろ;h] 、 寒[さむ,さむい;k2]い 日[ひ;h] が 多[おお,おおい;k1,k2]い です ね 。", "この頃")
        assert word_transcrition == "この頃[このごろ;h]"
        
        
    def test_card_sentence_transcription_one(self):
        card = AnkiCard(42)
        sentence_transcription = card.get_japanese_sentence_anki("[例|たと]えば、これはペンです。")
        assert sentence_transcription == "例[たと;h] えば、これはペンです。"
        
    def test_card_sentence_transcription_two(self):
        card = AnkiCard(42)
        sentence_transcription = card.get_japanese_sentence_anki("[電車|でん|しゃ]が[来|く]るよ！")
        assert sentence_transcription == "電車[でんしゃ;h] が 来[く;n4] るよ！"
        
    def test_card_sentence_transcription_three(self):
        card = AnkiCard(42)
        sentence_transcription = card.get_japanese_sentence_anki("[A|えい][型|がた][血友病|けつ|ゆう|びょう]の[小児|しょう|に][患者|かん|じゃ]を[対象|たい|しょう]とした[国際|こく|さい][的|てき]な[研究|けん|きゅう]が[2|に][本|ほん][行|おこな]われている[最中|さい|ちゅう]だ。")
        assert sentence_transcription == "A 型[がた;h]  血友病[けつゆうびょう;n4] の 小児[しょうに;a]  患者[かんじゃ;n5] を 対象[たいしょう;n2] とした 国際[こくさい;h]  的[てき;n4] な 研究[けんきゅう;a] が2 本[ほん;n5]  行[おこな;n2] われている 最中[さいちゅう;h] だ。"