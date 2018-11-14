# -*- coding: utf-8 -*-
# @Time    : 2017/11/13 下午 11:26
# @Author  : AlexJean

from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout,QDesktopWidget
from PyQt5.QtGui import QIntValidator, QDoubleValidator, QRegExpValidator
from PyQt5.QtCore import QRegExp
import sys


class LineEditDemo(QWidget):
    def __init__(self, parent=None):
        super(LineEditDemo, self).__init__(parent)
        self.setWindowTitle("QLineEdit 验证器")

        formLayout = QFormLayout()
        intEdit = QLineEdit()
        doubleEdit = QLineEdit()
        validatorEdit = QLineEdit()

        formLayout.addRow("整数", intEdit)
        formLayout.addRow("浮点数", doubleEdit)
        formLayout.addRow("字母和数字", validatorEdit)

        intEdit.setPlaceholderText("整数")
        doubleEdit.setPlaceholderText("浮点数")
        validatorEdit.setPlaceholderText("字母和数字")

        intValidator = QIntValidator(self)
        intValidator.setRange(1, 99)
        doubleValidator = QDoubleValidator(self)
        doubleValidator.setRange(-360, 360)
        doubleValidator.setNotation(QDoubleValidator.StandardNotation)
        doubleValidator.setDecimals(2)

        reg = QRegExp("[a-zA-Z0-9]+$")
        regValidator = QRegExpValidator(self)
        regValidator.setRegExp(reg)

        intEdit.setValidator(intValidator)
        doubleEdit.setValidator(doubleValidator)
        validatorEdit.setValidator(regValidator)

        self.setLayout(formLayout)

        screen=QDesktopWidget().screenGeometry()
        print('screen.width %s ' % screen.width())
        # self还没显示 , 640*480
        print('self.width %s' % self.width())
        print('self.height %s' % self.height())
        x=screen.width()-self.width()
        y=screen.height()-self.height()
        self.move(x/2,y/2)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = LineEditDemo()
    win.show()
    sys.exit(app.exec())
