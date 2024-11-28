from PyQt6.QtWidgets import QMessageBox


class ImportationErrorMessageBox(QMessageBox):
    def __init__(self, parent) -> None:
        super().__init__(
            QMessageBox.Icon.Warning,
            "Importation error",
            "",
            QMessageBox.StandardButton.Ok,
            parent)

    def _set_text(self, bad_words: list):
        if len(bad_words) <= 5:
            failed_words = "\n".join(word for word in bad_words)
            error_text = f"{len(bad_words)} word could not be imported:\n{failed_words}"
        else:
            error_text = f"{len(bad_words)} words could not be imported."
        self.setText(error_text)

    def exec(self, bad_words):
        self._set_text(bad_words)
        super().exec()
