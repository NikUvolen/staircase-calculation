from sys import argv, exit
from PySide6.QtWidgets import QApplication
from PySide6.QtGui import QIcon
from src import Window


if __name__ == '__main__':
    app = QApplication(argv)
    app.setWindowIcon(QIcon('./gui/icons/calc.png'))
    window = Window()
    window.show()

    exit(app.exec())