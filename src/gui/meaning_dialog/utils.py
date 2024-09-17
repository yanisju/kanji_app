from PyQt6.QtGui import QStandardItemModel
import PyQt6.QtCore

def get_copy_standard_item_model(model_from):
        new_model = QStandardItemModel(0, 2)
        new_model.setHeaderData(0, PyQt6.QtCore.Qt.Orientation.Horizontal, "Meanings")
        new_model.setHeaderData(1, PyQt6.QtCore.Qt.Orientation.Horizontal, "Parts of speech")

        new_row = []
        for i in range(model_from.rowCount()):
            for j in range(model_from.columnCount()):
                new_row.append(model_from.item(i, j).clone()) 
            new_model.appendRow(new_row)
            new_row.clear()
        return new_model