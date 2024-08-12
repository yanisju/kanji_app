from .notes import Notes
import genanki 

class AnkiManager():
    def __init__(self):
        self._model = self._get_model()
        self._deck = self._get_deck(1301981488, 'Test_Kanjis')
        self.notes = Notes(self._model)
        
    def _get_model(self):
        # TODO: Modify and set as parameters
        file_template_front = open("D:/Workspace/kanji_app/data/parameters/template_front.txt", "r", encoding='utf-8')
        file_template_back = open("D:/Workspace/kanji_app/data/parameters/template_back.txt", "r", encoding='utf-8')
        template_front = file_template_front.read()
        template_back = file_template_back.read()
        
        model = genanki.Model(
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
        return model
        
         
    def _get_deck(self, id, name):
        deck = genanki.Deck(
            id,
            name)
        return deck

    def generate_deck(self):
        for note in self.notes:
            self._deck.add_note(note)

        genanki.Package(self._deck).write_to_file('D:/Workspace/kanji_app/data/output/output.apkg')

    def add_sentence(self, sentence):
        self.notes.add(sentence)

    def modify_sentence(self, sentence, row):
        self.notes.modify(sentence, row)

    def delete_sentence(self, sentence_row):
        pass 