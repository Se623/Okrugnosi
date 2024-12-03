import random

from PyQt6 import uic
from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtGui import QPainter, QColor
import sys

class Square1(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.flag = False
        self.coords = []
        self.btn.clicked.connect(self.draw)


    def draw(self):
        self.size = random.randint(10, 100)
        self.flag = True
        self.update()

    def paintEvent(self, event):
        color = "yellow"
        if self.flag:
            qp = QPainter()
            qp.begin(self)
            qp.setPen(QColor(color))
            qp.setBrush(QColor(color))
            self.x, self.y = random.randint(100, 800 - 100), random.randint(100, 900 - 100)
            qp.drawEllipse(self.x, self.y, self.size, self.size)
            qp.end()


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Square1()
    ex.show()
    sys.excepthook = except_hook
    sys.exit(app.exec())