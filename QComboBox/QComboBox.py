# -*- coding: utf-8 -*-
# @Time    : 2017/11/15 下午 9:11
# @Author  : AlexJean
import sys
from PyQt5.QtWidgets import *


class Demo(QWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.setWindowTitle("Combox 例子")
        self.resize(300, 90)
        layout = QVBoxLayout()
        self.lb1 = QLabel("")
        self.cb = QComboBox()
        self.cb.addItem("C")
        self.cb.addItem("C++")
        self.cb.addItems(["Java", "C#", "Python"])
        self.cb.currentIndexChanged.connect(self.selectionChange)
        layout.addWidget(self.cb)
        layout.addWidget(self.lb1)
        self.setLayout(layout)
        self.move(400, 400)

    def selectionChange(self, i):
        self.lb1.setText(self.cb.currentText())
        print("==== Items in the list are : ====")
        for count in range(self.cb.count()):
            print('item' + str(count) + '="' + self.cb.itemText(count) + '"')
        text = self.cb.currentText()
        print('Current index', i, ',selection changed to "', text + '"')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Demo()
    win.show()
    sys.exit(app.exec())
