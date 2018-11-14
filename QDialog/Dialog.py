# -*- coding: utf-8 -*-
# @Time    : 2017/11/16 上午 1:17
# @Author  : AlexJean
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class DialogDemo(QMainWindow):
    def __init__(self, parent=None):
        super(DialogDemo, self).__init__(parent)
        self.setWindowTitle("Dialog 例子")
        self.resize(350, 300)
        self.btn = QPushButton("hi",self)
        self.btn.move(50, 50)
        self.btn.clicked.connect(self.showdialog)
        self.move(400,400)

    def showdialog(self):
        dialog = QDialog()
        btn = QPushButton("ok", dialog)
        btn.move(50, 50)
        dialog.setWindowTitle("Dialog")
        dialog.setWindowModality(Qt.ApplicationModal)
        dialog.exec()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = DialogDemo()
    win.show()
    sys.exit(app.exec())
