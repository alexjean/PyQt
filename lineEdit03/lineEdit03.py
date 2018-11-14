# -*- coding: utf-8 -*-
# @Time    : 2017/11/14 下午 2:26
# @Author  : AlexJean
from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout
import sys


class Demo(QWidget):
    def __init__(self, parent=None):
        super(Demo, self).__init__(parent)
        self.setWindowTitle("QLineEdit 输入掩码例子")

        formLayout = QFormLayout()
        leIP = QLineEdit()
        leMAC = QLineEdit()
        leDate = QLineEdit()
        leLicense=QLineEdit()
        leLicense.setMinimumWidth(320)

        leIP.setInputMask("000.000.000.000;_")
        leMAC.setInputMask("HH:HH:HH:HH:HH:HH;_")
        leDate.setInputMask("0000-00-00")
        leLicense.setInputMask(">AAAAA-AAAAA-AAAAA-AAAAA-AAAAA;#")

        formLayout.addRow("数字掩码",leIP)
        formLayout.addRow("MAC掩码",leMAC)
        formLayout.addRow("日期掩码",leDate)
        formLayout.addRow("许可证掩码",leLicense)

        self.setLayout(formLayout)
        self.move(400,400)

if __name__ == "__main__":
    app=QApplication(sys.argv)
    win=Demo()
    win.show()
    sys.exit(app.exec())


