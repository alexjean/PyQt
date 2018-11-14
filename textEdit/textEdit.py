# -*- coding: utf-8 -*-
# @Time    : 2017/11/14 下午 3:36
# @Author  : AlexJean
from PyQt5.QtWidgets import QApplication,QWidget,QTextEdit,QVBoxLayout,QPushButton
import sys

class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo, self).__init__(parent)
        self.setWindowTitle("QTextEdit 例子")
        self.resize(300,270)
        self.move(400,400)
        self.textEdit=QTextEdit()
        self.btnPress1=QPushButton("显示本文")
        self.btnPress2=QPushButton("显示HTML")
        layout=QVBoxLayout()
        layout.addWidget(self.textEdit)
        layout.addWidget(self.btnPress1)
        layout.addWidget(self.btnPress2)
        self.setLayout(layout)
        self.btnPress1.clicked.connect(self.btnPress1_Clicked)
        self.btnPress2.clicked.connect(self.btnPress2_Clicked)

    def btnPress1_Clicked(self):
        self.textEdit.setPlainText("Hello PyQt5!\n 单击按钮")

    def btnPress2_Clicked(self):
        self.textEdit.setHtml("<font color='red' size='6'>Hello PyQt5!<br> 单击按钮</font>")


if __name__ == "__main__":
    app=QApplication(sys.argv)
    win=Demo()
    win.show()
    sys.exit(app.exec())

