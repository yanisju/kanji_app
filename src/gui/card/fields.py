from PyQt6.QtWidgets import QFormLayout, QLineEdit 

class CardDialogFields(QFormLayout):
    def __init__(self, card_dialog):
        super().__init__()
        self.fields_name = ["Sentence:", "Meaning:", "Anki format:", "Word 1: ", "Word 1 meaning:", "Word 2: ", "Word 2 meaning:"]
        self.field_line_edit_list = [] # All QLineEdit for each fields of the vocabulary.
    
    def init_fields(self):
        """Initialize all fields based on vocabulary attributes. """
        
        for i in range(len(self.fields_name)):
            field_line_edit = QLineEdit()
            self.field_line_edit_list.append(field_line_edit)
            self.addRow(self.fields_name[i], field_line_edit)
        
    def fill_fields(self, items_list):
        for i in range(5):
            self.field_line_edit_list[i].setText(items_list[i].text())
            