# -*- coding: utf-8 -*-
# @Time    : 2017/11/16 下午 1:31
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
        self.setGeometry(300,300,365,280)
        self.setWindowTitle('画刷例子')
        self.show()

    def paintEvent(self, event):
        qp=QPainter()
        qp.begin(self)
        self.draws(qp)
        qp.end()

    def brushLine(self,qp,x,y,pattern):
        qp.setBrush(QBrush(pattern))
        qp.drawRect(x,y,90,60)

    def draws(self,qp):
        self.brushLine(qp,10,15,Qt.SolidPattern)
        self.brushLine(qp,130,15,Qt.Dense1Pattern)
        self.brushLine(qp,250,15,Qt.Dense2Pattern)
        self.brushLine(qp,10 ,105,Qt.Dense3Pattern)
        self.brushLine(qp,10 ,105,Qt.DiagCrossPattern)
        self.brushLine(qp,130,105,Qt.Dense5Pattern)
        self.brushLine(qp,250,105,Qt.Dense6Pattern)
        self.brushLine(qp,10,195,Qt.HorPattern)
        self.brushLine(qp,130,195,Qt.VerPattern)
        self.brushLine(qp,250,195,Qt.BDiagPattern)


if __name__ == "__main__":
    app=QApplication(sys.argv)
    win=Drawing()
    win.show()
    sys.exit(app.exec())






 
