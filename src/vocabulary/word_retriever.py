class WordRetriever:
    """ Used to retrieve the vocabulary, inserted by the user using different methods."""

    def __init__(self):
        pass
                
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

    def get_word_from_file(self, file_location):
        words = []
        with open(file_location, encoding="utf8") as file:
            for vocabulary in file:
                vocabulary = vocabulary.strip() # Remove uselesse characters
                if vocabulary:  # if not empty
                    words.append(vocabulary)
        return words

    @property
    def vocabularys_list(self):
        return self._vocabularys_list

    @vocabularys_list.setter
    def vocabularys_list(self, value):
        self._vocabularys_list = value
