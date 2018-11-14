# -*- coding: utf-8 -*-
# @Time    : 2017/11/14 下午 2:44
# @Author  : AlexJean
from PyQt5.QtWidgets import QApplication, QWidget, QLineEdit, QFormLayout
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QFont
from PyQt5.QtCore import Qt
import sys


# noinspection PyPep8Naming
class Demo(QWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        e1 = QLineEdit()
        e1.setValidator(QIntValidator())
        e1.setMaxLength(4)
        e1.setAlignment(Qt.AlignRight)
        e1.setFont(QFont("Arial", 20))

        e2 = QLineEdit()
        e2.setValidator(QDoubleValidator(0.99, 99.99, 2))

        formLayout = QFormLayout()
        formLayout.addRow("IntValidator", e1)
        formLayout.addRow("DoubleValidator", e2)

        e3 = QLineEdit()
        e3.setInputMask('+99_9999_999999')
        formLayout.addRow("InputMask", e3)
        e4 = QLineEdit()
        e4.textChanged.connect(self.textchanged)
        formLayout.addRow("TextChanged", e4)
        e5 = QLineEdit()
        e5.setEchoMode(QLineEdit.Password)
        formLayout.addRow("Password", e5)
        e6 = QLineEdit()
        e6.setText("这不能编辑")
        e6.setReadOnly(True)
        e5.editingFinished.connect(self.enterPress)
        formLayout.addRow("ReadOnly", e6)
        self.setLayout(formLayout)
        self.setWindowTitle("QLineEdit04例子")
        self.move(400, 400)

    def textchanged(self, text):
        print("输入的内容为:" + text)

    def enterPress(self):
        print("已输入Password")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Demo()
    win.show()
    sys.exit(app.exec())
