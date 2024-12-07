import sys

from random import randrange
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton


class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(0, 0, 800, 600)
        self.setWindowTitle('Первая программа')
        self.do_paint = False
        self.button_draw_circle = QPushButton(self)
        self.button_draw_circle.setText('Окружность')
        self.button_draw_circle.resize(80, 40)
        self.button_draw_circle.move(720, 560)
        self.button_draw_circle.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end()
        self.do_paint = False

    def paint(self):
        self.do_paint = True
        self.update()

    def draw_circle(self, qp):
        r = randrange(600)
        qp.setPen(QColor(randrange(255), randrange(255), randrange(255)))
        qp.drawEllipse(10, 20, r, r)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = YellowCircles()
    ex.show()
    sys.exit(app.exec())
