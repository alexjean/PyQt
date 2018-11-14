# -*- coding: utf-8 -*-
# @Time    : 2017/11/18 上午 12:27
# @Author  : AlexJean
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MenuDemo(QMainWindow):
    def __init__(self, parent=None):
        super(MenuDemo, self).__init__(parent)
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("New")
        save = QAction("Save", self)
        save.setShortcut("Ctrl+S")
        file.addAction(save)
        edit = file.addMenu("Edit")
        edit.addAction("copy")
        edit.addAction("paste")
        actQuit = QAction("Quit", self)
        file.addAction(actQuit)
        file.triggered[QAction].connect(self.processtrigger)
        self.setWindowTitle("QMenu 例子")
        self.move(40, 30)

    def processtrigger(self, q):
        print(q.text() + " is triggered")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = MenuDemo()
    win.show()
    sys.exit(app.exec())
