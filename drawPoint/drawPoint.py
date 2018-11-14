# -*- coding: utf-8 -*-
# @Time    : 2017/11/14 下午 4:14
# @Author  : AlexJean
import sys,math
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt


class Drawing(QWidget):
    def __init__(self,parent=None):
        super(Drawing, self).__init__(parent)
        self.resize(300,200)
        self.move(400,400)
        self.setWindowTitle("Widget中画点")

    def paintEvent(self, paintEvent):
        qp=QPainter()
        qp.begin(self)
        qp.setPen(QColor(100,88,250))
        qp.setFont(QFont('SimSun',10))
        qp.drawText(paintEvent.rect(),Qt.AlignBottom | Qt.AlignCenter,"欢迎到技术分析世界")
        self.drawPoints(qp)
        qp.end()

    def drawPoints(self,qp):
        qp.setPen(Qt.red)
        size=self.geometry()
        w2=size.width()/2.0
        h2=size.height()/2.0
        print("x=%s y=%s" % (w2,h2))
        for i in range(1000):
            x=(-1+2*i/1000)*100
            y=-0.68*h2*math.sin(x*math.pi/50)+h2
            qp.drawPoint(x*0.8*w2/100+w2,y)


if __name__ == "__main__":
    app=QApplication(sys.argv)
    win=Drawing()
    win.show()
    sys.exit(app.exec())


