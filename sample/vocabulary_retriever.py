class VocabularyRetriever:
    """ Used to retrieve the vocabulary, inserted by the user using different methods."""

    def __init__(self):
        self._vocabularys_list = []  

    def start(self, input_method):
        vocabularys_console = []
    
        if input_method == 1:
            self._vocabularys_list = self.get_vocabulary_from_console()
        elif input_method == 1:
            self._vocabularys_list = self.get_vocabulary_from_file()
                
    def get_vocabulary_from_console(self):
        vocabulary_input = 'O'
        vocabularys_console = []
        i = 0
        while vocabulary_input: # While input char is not empty
                    if i == 0:
                         print("Enter vocabulary: ", end="")
                         i += 1
                    else:
                        print("Current vocabularys: ", end="")
                        print(vocabularys_console)
                        print("Type nothing if you want to stop, type D if you want to erase last vocabulary or enter new vocabulary: ", end="")
                    vocabulary_input = input()
                    if vocabulary_input == "D":
                        vocabularys_console.pop()
                    elif vocabulary_input:
                        vocabularys_console.append(vocabulary_input)
        return vocabularys_console

    def get_vocabulary_from_file(self, filename, file_location):
        vocabularys_file = []
        file = open(file_location + filename)
        for vocabulary in file:
             vocabularys_file.append(vocabulary)
        return vocabularys_file

    @property
    def vocabularys_list(self):
        return self._vocabularys_list

    @vocabularys_list.setter
    def vocabularys_list(self, value):
        self._vocabularys_list = value
