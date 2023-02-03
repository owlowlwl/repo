import sys
from random import randint

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor, QBrush


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setWindowTitle('Жёлтые окружности')
        self.draw = False
        self.pushButton.clicked.connect(self.btn)
        self.update()

    def paintEvent(self, event):
        super().paintEvent(event)
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            side = randint(10, 300)
            col = QColor(255, 255, 0)
            qp.setPen(col)
            qp.setBrush(col)
            qp.drawEllipse(120, 120, side, side)
            qp.end()

    def btn(self):
        self.draw = True
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
