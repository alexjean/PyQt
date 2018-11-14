# -*- coding: utf-8 -*-
# @Time    : 2017/11/16 下午 1:05
# @Author  : AlexJean
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *


class Drawing(QWidget):
    def __init__(self):
        super(Drawing, self).__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 280, 270)
        self.setWindowTitle('钢笔样式例子')

    def paintEvent(self, qPaintEvent):
        qp = QPainter()
        qp.begin(self)
        self.drawLines(qp)
        qp.end()

    def line(self, qp, y, pen, style):
        pen.setStyle(style)
        qp.setPen(pen)
        qp.drawLine(20, y, 250, y)

    def drawLines(self, qp):
        pen = QPen(Qt.black, 2)
        self.line(qp, 40, pen, Qt.SolidLine)
        self.line(qp, 80, pen, Qt.DashLine)
        self.line(qp, 120, pen, Qt.DashDotLine)
        self.line(qp, 160, pen, Qt.DotLine)
        self.line(qp, 200, pen, Qt.DashDotDotLine)
        pen.setDashPattern([1,4,8,4])
        self.line(qp,240,pen,Qt.CustomDashLine)


if __name__ == "__main__":
    app=QApplication(sys.argv)
    win=Drawing()
    win.show()
    sys.exit(app.exec())

