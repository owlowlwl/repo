import sys
from random import randint

from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from UI import Ui_MainWindow


class MyWidget(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
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
            col = QColor(randint(0, 255), randint(0, 255), randint(0, 255))
            qp.setPen(col)
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