from .card import AnkiCard
import genanki 
import re

class AnkiManager:
    def __init__(self):
        self.vocabulary = "vocabulary"
        self.card_count = 0 # Number of cards in the deck, used to sort deck
        _anki_cards = []
        
        """
        # TODO: Modify and set as parameters
        file_template_front = open("C:/Workspace/kanji-app/kanji_app/data/parameters/template_front.txt", "r", encoding='utf-8')
        file_template_back = open("C:/Workspace/kanji-app/kanji_app/data/parameters/template_back.txt", "r", encoding='utf-8')
        template_front = file_template_front.read()
        template_back = file_template_back.read()
        
        self.my_model = genanki.Model(
            1422169361,
            'Sentence_test',
            fields=[
                {'name': 'Sort'},
                {'name': 'Expression'},
                {'name': 'Meaning'},
                {'name': 'Vocab1'},
                {'name': 'Vocab1 Meaning'},
                {'name': 'Vocab2'},
                {'name': 'Vocab2 Meaning'},
                {'name': 'Audio'},
            ],
            templates=[
                {
                    'name': 'Sentence',
                    'qfmt': template_front,
                    'afmt': template_back,
                }, # TODO: Add "style" field / else won't display card correctly
            ])
        

        self.my_deck = genanki.Deck(
            1301981488,
            'Test_Kanjis')
        """
         
    def turn_vocabulary_to_card(self, vocabulary):
        new_card = AnkiCard(self.my_model)
        new_card.fill_fields_jap_sentence(vocabulary, self.card_count)
        
        self.my_deck.add_note(new_card.note)
        genanki.Package(self.my_deck).write_to_file('data/output/output.apkg')
        
        
        

    def create_anki_cards(self):
        pass

    def start(self):
        pass
