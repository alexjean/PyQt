# -*- coding: utf-8 -*-
# @Time    : 2017/11/15 下午 9:52
# @Author  : AlexJean
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo, self).__init__(parent)
        self.setWindowTitle("SpinBox 例子")
        self.resize(300,100)
        self.move(400,400)

        layout=QVBoxLayout()
        self.l1=QLabel("Current value:")
        self.l1.setAlignment(Qt.AlignCenter)
        layout.addWidget(self.l1)
        self.sp=QSpinBox()
        layout.addWidget(self.sp)
        self.sp.valueChanged.connect(self.valueChange)
        self.setLayout(layout)

    def valueChange(self):
        self.l1.setText("Current value: "+str(self.sp.value()))


if __name__ == "__main__":
    app=QApplication(sys.argv)
    win=Demo()
    win.show()
    sys.exit(app.exec())



