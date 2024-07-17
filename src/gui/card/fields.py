from PyQt6.QtWidgets import QFormLayout, QLineEdit 

class CardDialogFields(QFormLayout):
    def __init__(self, card_dialog, card_view):
        super().__init__()
        self.card_view = card_view

        self.field_line_edit_list = [] # All QLineEdit for each fields of the vocabulary.
        self.fields_name = ["Sentence:", "Meaning:", "Anki format:", "Word 1: ", "Word 1 meaning:", "Word 2: ", "Word 2 meaning:"]
        self.fields_value = []

    
    def init_fields(self):
        """Initialize all fields based on vocabulary attributes. """
        
        for i in range(len(self.fields_name)):
            field_line_edit = QLineEdit()
            self.field_line_edit_list.append(field_line_edit)
            self.addRow(self.fields_name[i], field_line_edit)
        
        for i in range(len(self.fields_name)):
            self.field_line_edit_list[i].textEdited.connect(self.refresh_fields_value) # Modify view when one of the field is modified

    def fill_fields(self, items_list):
        """Fill each fields for the card with the current items. """

        self.fields_value.clear()
        for i in range(len(items_list)):
            self.fields_value.append(items_list[i].text())
            self.field_line_edit_list[i].setText(items_list[i].text())

    def refresh_fields_value(self):
        self.fields_value.clear()
        for i in range(len(self.field_line_edit_list)):
            self.fields_value.append(self.field_line_edit_list[i].text())
        self.card_view.set_card_view(self.fields_value)        
            