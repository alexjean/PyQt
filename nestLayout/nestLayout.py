# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 下午 3:35
# @Author  : AlexJean
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from Ui_nestLayout import *


class MyWindow(QWidget,Ui_Form):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setupUi(self)


if __name__ == "__main__":
    app=QApplication(sys.argv)
    win=MyWindow()
    win.show()
    sys.exit(app.exec())


