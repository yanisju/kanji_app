from PyQt6.QtWidgets import QVBoxLayout, QFormLayout, QLineEdit, QTableView
from ..kanji_data_model import KanjiDataModel
from .vocabulary_combobox import VocabularyComboBox


class FieldsLayout(QVBoxLayout):
    def __init__(self, card_view):
        super().__init__()
        self.card_view = card_view

        self.field_form_layout = QFormLayout()  # Form layout containg fields
        self.kanji_table_view = (
            QTableView()
        )  # View containg kanjis and theirs readings + meanings
        self.addLayout(self.field_form_layout)
        self.addWidget(self.kanji_table_view)

        self.kanji_data_model = KanjiDataModel()
        self.kanji_table_view.setModel(self.kanji_data_model)

        self.field_widget_list = (
            []
        )  # All QLineEdit for each fields of the vocabulary.
        self.fields_name = [
            "Sentence:",
            "Meaning:",
            "Word 1: ",
            "Word 2: ",
        ]
        self.fields_value = []

        self._init_fields()

    def _init_fields(self):
        """Initialize all fields based on vocabulary attributes."""

        for i in range(2):
            field_line_edit = QLineEdit()
            self.field_widget_list.append(field_line_edit)
            self.field_form_layout.addRow(self.fields_name[i], field_line_edit)

        for i in range(2, 4):
            field_combobox = VocabularyComboBox()
            self.field_widget_list.append(field_combobox)
            self.field_form_layout.addRow(self.fields_name[i], field_combobox)

        for i in range(2):
            self.field_widget_list[i].textEdited.connect(
                self.refresh_fields_value
            )  # Modify view when one of the field is modified

    def fill_fields(self, sentence):
        """Fill each fields for the card with the current items."""

        self.fields_value.clear()
        for i in range(2):
            self.fields_value.append(sentence.fields[i])
            self.field_widget_list[i].setText(sentence.fields[i])
        self.kanji_data_model.refresh(sentence.kanji_data, self.fields_value[0])

    def refresh_fields_value(self):
        self.fields_value.clear()
        for i in range(len(self.field_widget_list)):
            self.fields_value.append(self.field_widget_list[i].text())
        self.card_view.refresh_view(self.fields_value)