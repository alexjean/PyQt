# -*- coding: utf-8 -*-
# @Time    : 2017/11/16 上午 1:51
# @Author  : AlexJean
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()
        self.setWindowTitle("QMessageBox 例子")
        self.resize(300,100)
        self.move(400,400)
        self.myButton=QPushButton(self)
        self.myButton.setText("点击弹出消息框")
        self.myButton.clicked.connect(self.msg)

    def msg(self):
        reply=QMessageBox.information(self,"标题","消息正文",QMessageBox.Yes | QMessageBox.No ,QMessageBox.Yes )
        print(reply)


if __name__ == "__main__":
    app=QApplication(sys.argv)
    win=MyWindow()
    win.show()
    sys.exit(app.exec())
