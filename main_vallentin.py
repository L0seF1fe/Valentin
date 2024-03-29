from PyQt6.QtCore import QSize, Qt
from PyQt6.QtGui import QPixmap
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLabel

import sys
import random

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Valentin")
        self.setFixedSize(QSize(800, 700))
        pixmap = QPixmap("image099-30.jpg")
        background_label = QLabel(self)
        background_label.setPixmap(pixmap)
        background_label.resize(self.size())
        background_label.setScaledContents(True)
        self.button()
        self.button_two()

    def button(self):
        self.button = QPushButton("Нажми если любишь", self)

        self.button.setFixedSize(QSize(150, 30))

        self.button.move(500, 200)

        self.button.clicked.connect(self.new_window)

    def button_two(self):
        self.button_two = QPushButton("Нажми если не любишь", self)

        self.button_two.setFixedSize(QSize(150, 30))

        self.button_two.move(100, 200)

        self.button_two.clicked.connect(self.moveButton)

    def moveButton(self):
        x = random.randint(0, 500)
        y = random.randint(0, 400)
        self.button_two.move(x, y)

    def new_window(self):
        self.new_widow = NewWindow()
        self.new_widow.show()
        self.close()

class NewWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Valentin")
        self.setFixedSize(QSize(800, 700))

        pixmap = QPixmap("1614626120_49-p-fon-s-serdechkami-dlya-fotoshopa-58.jpg")
        background_label = QLabel(self)
        background_label.setPixmap(pixmap)
        background_label.resize(self.size())
        background_label.setScaledContents(True)

        label = QLabel('Я тебя тоже люблю <3', self)
        label.setFixedSize(QSize(200, 30))
        label.move(330, 300)

        self.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    app.exec()
