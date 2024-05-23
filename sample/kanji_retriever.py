class KanjiRetriever:

    def __init__(self):
        self.kanji = "集中"
        self._kanjis_list = []  

    def start(self, input_method):
        kanjis_console = []
    
        if input_method == 1:
            _kanjis_list = self.get_kanji_from_console()
        elif input_method == 1:
            _kanjis_list = self.get_kanji_from_file()
                
    def get_kanji_from_console(self):
        kanji_input = 'O'
        kanjis_console = []
        i = 0
        while kanji_input != 'S':
                    if i == 0:
                         print("Enter kanji: ", end="")
                         i += 1
                    else:
                        print("Current kanjis: ", end="")
                        print(kanjis_console)
                        print("Enter new kanji, type S if you want to stop, type D if you want to erase last kanji: ", end="")
                    kanji_input = input()
                    if kanji_input == "D":
                        kanjis_console.pop()
                    elif kanji_input == 'S':
                        get_kanji_loop = False 
                    else:
                        kanjis_console.append(kanji_input)
        return kanjis_console

    def get_kanji_from_file(self, filename, file_location):
        kanjis_file = []
        file = open(file_location + filename)
        for kanji in file:
             kanjis_file.append(kanji)
        return kanjis_file

    @property
    def kanjis_list(self):
        return self._kanjis_list

    @kanjis_list.setter
    def kanjis_list(self, value):
        self._kanjis_list = value
