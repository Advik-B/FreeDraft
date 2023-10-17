from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PyQt6.QtGui import QAction
from PyQt6.uic import loadUi
from path import Path
from sys import argv


class AppUI(QMainWindow):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.init_ui()
        self.register_ui()
        self.show()

    def init_ui(self):
        loadUi(Path(__file__).parent / "form.ui", self)

    def register_ui(self):
        self.aboutAction = self.findChild(QAction, "actionAbout")
        self.aboutActionQt = self.findChild(QAction, "actionAbout_Qt")

        self.aboutAction.triggered.connect(self.about)
        self.aboutActionQt.triggered.connect(self.about_qt)

    def about(self):
        QMessageBox.about(self, "About", "About")

    def about_qt(self):
        QMessageBox.aboutQt(self, "About Qt")


if __name__ == "__main__":
    app = QApplication(argv)
    window = AppUI()
    app.exec()
