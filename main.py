import sys

import io
from PyQt6 import uic
from random import randrange
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtWidgets import QApplication, QMainWindow
from UI import template


class YellowCircles(QMainWindow):
    def __init__(self):
        super().__init__()
        f = io.StringIO(template)
        uic.loadUi(f, self)
        self.do_paint = False
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
