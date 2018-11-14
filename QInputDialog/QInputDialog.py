# -*- coding: utf-8 -*-
# @Time    : 2017/11/16 上午 2:15
# @Author  : AlexJean
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class InputdialogDemo(QWidget):
    def __init__(self, parent=None):
        super(InputdialogDemo, self).__init__(parent)
        layout = QFormLayout()
        self.btn1 = QPushButton("获得列表里的选项")
        self.btn1.clicked.connect(self.getItem)
        self.le1 = QLineEdit()
        layout.addRow(self.btn1, self.le1)

        self.btn2 = QPushButton("获得字串")
        self.btn2.clicked.connect(self.getIext)
        self.le2 = QLineEdit()
        #self.le2.setAttribute(Qt.WA_InputMethodEnabled,True)
        layout.addRow(self.btn2, self.le2)

        self.btn3 = QPushButton("获得整数")
        self.btn3.clicked.connect(self.getInt)
        self.le3 = QLineEdit()
        layout.addRow(self.btn3, self.le3)

        self.setLayout(layout)
        self.setWindowTitle("Input Dialog 例子")
        #self.setAttribute(Qt.WA_InputMethodEnabled,True)
        self.move(400,300)

    def getItem(self):
        items = ("C", "C++", "JAVA", "Python")
        item, ok = QInputDialog.getItem(self, "select input dialog", "语言列表", items, 0, False)
        if ok and item:
            self.le1.setText(item)

    def getIext(self):
        text, ok = QInputDialog.getText(self, 'Text Input Dialog', '输入姓名')
        if ok:
            self.le2.setText(str(text))

    def getInt(self):
        num, ok = QInputDialog.getInt(self, "integer input dialog", "输入数字")
        if ok:
            self.le3.setText(str(num))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = InputdialogDemo()
    win.show()
    sys.exit(app.exec())
