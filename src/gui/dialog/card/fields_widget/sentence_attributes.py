from PyQt6.QtWidgets import QWidget, QFormLayout, QLineEdit
from .vocabulary_combobox import VocabularyComboBox

class SentenceAttributesWidget(QWidget):
    def __init__(self, parent: QWidget, card_view, kanji_data_model) -> None:
        super().__init__(parent)
        layout = QFormLayout(self)
        self.setLayout(layout)

        self.card_view = card_view

        attributes_name = [
            "Sentence:",
            "Meaning:",
            "Word 1: ",
            "Word 2: ",
        ]

        self.widget_list = self._init_layout(layout, attributes_name, kanji_data_model)
        self.attributes_value = []

    def _init_layout(self, form_layout, attributes_name, kanji_data_model):
        widget_list = []

        line_edit = QLineEdit()
        widget_list.append(line_edit)
        form_layout.addRow(attributes_name[0], line_edit)
        line_edit.textEdited.connect(self._is_sentence_attribute_modified)

        line_edit = QLineEdit()
        widget_list.append(line_edit)
        form_layout.addRow(attributes_name[1], line_edit)
        line_edit.textEdited.connect(self._is_translation_attribute_modified)

        word1_combobox = VocabularyComboBox(False, kanji_data_model)
        widget_list.append(word1_combobox)
        form_layout.addRow(attributes_name[2], word1_combobox)
        word1_combobox.currentIndexChanged.connect(self._is_word1_attribute_modified)

        word2_combobox = VocabularyComboBox(True, kanji_data_model)
        widget_list.append(word2_combobox)
        form_layout.addRow(attributes_name[3], word2_combobox)
        word2_combobox.currentIndexChanged.connect(self._is_word2_attribute_modified)

        return tuple(widget_list)

    def _is_sentence_attribute_modified(self):
        text = self.widget_list[0].text()
        self.attributes_value[0] = text
        self.card_view.set_card_view_from_attributes_values(self.attributes_value)
    
    def _is_translation_attribute_modified(self):
        text = self.widget_list[1].text()
        self.attributes_value[1] = text
        self.card_view.set_card_view_from_attributes_values(self.attributes_value)
    
    def _is_word1_attribute_modified(self):
        data = self.widget_list[2].itemData(self.widget_list[2].currentIndex())
        self.attributes_value[2] = data
        self.card_view.set_card_view_from_attributes_values(self.attributes_value)
    
    def _is_word2_attribute_modified(self):
        data = self.widget_list[3].itemData(self.widget_list[3].currentIndex())
        self.attributes_value[3] = data
        self.card_view.set_card_view_from_attributes_values(self.attributes_value)
    
    
    def set_to_new_sentence(self, sentence):
        self.attributes_value = [None, None, None, None]
        for i in range(2):
            self.attributes_value[i] = sentence.attributes[i]
            self.widget_list[i].setText(sentence.attributes[i])

        self.widget_list[2].insert_new(sentence.kanji_data)
        if sentence.word1_data == None:
            self.widget_list[2].set_to_empty_value()
        else:
            self.widget_list[2].setCurrentIndex(sentence.word1_data[3])
        self.attributes_value[2] = self.widget_list[2].itemData(self.widget_list[2].currentIndex())

        self.widget_list[3].insert_new(sentence.kanji_data)
        if sentence.word2_data == None:
            self.widget_list[3].set_to_empty_value()
        else:
            self.widget_list[3].setCurrentIndex(sentence.word2_data[3])
        self.attributes_value[3] = self.widget_list[3].itemData(self.widget_list[3].currentIndex())
        
        
    
