# -*- coding: utf-8 -*-
# @Time    : 2017/11/15 下午 11:23
# @Author  : AlexJean
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont


class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo, self).__init__(parent)
        self.setWindowTitle("QSlider 例子")
        self.resize(300,100)
        self.move(400,400)
        layout=QVBoxLayout()
        self.l1=QLabel("Hello PyQt5")
        self.l1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l1)

        self.s1=QSlider(Qt.Horizontal)
        self.s1.setMinimum(10)
        self.s1.setMaximum(50)
        self.s1.setSingleStep(3)
        self.s1.setValue(20)
        self.s1.setTickPosition(QSlider.TicksBelow)
        self.s1.setTickInterval(5)
        layout.addWidget(self.s1)
        self.s1.valueChanged.connect(self.valuechange)

        self.l2=QLabel("size= 20")
        self.l2.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l2)
        self.setLayout(layout)


    def valuechange(self):
        print('current slider value=%s' % self.s1.value())
        size=self.s1.value()
        self.l1.setFont(QFont("Arial",size))
        self.l2.setText('size= %s' % size)



if __name__ == "__main__":
    app=QApplication(sys.argv)
    win=Demo()
    win.show()
    sys.exit(app.exec())



