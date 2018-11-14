# -*- coding: utf-8 -*-
# @Time    : 2017/12/16 下午 09:33
# @Author  : AlexJean
import sys
from PyQt5.QtWidgets import *
from Ui_mainWin import *
import tensorflow as tf


class Form(Ui_Form, QWidget):
    def __init__(self):
        super(Form, self).__init__()
        self.setupUi(self)
        self.showMsg("Tensorflow Version %s" % tf.VERSION)

    def showMsg(self, msg):
        self.listWidget.addItem(msg)

    def training(self):
        self.showMsg("Training!")

    def inference(self):
        self.showMsg("Inference!")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Form()
    win.show()
    sys.exit(app.exec())
