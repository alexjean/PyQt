# -*- coding: utf-8 -*-
# @Time    : 2017/11/18 上午 12:54
# @Author  : AlexJean
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class ToolBarDemo(QMainWindow):
    def __init__(self, parent=None):
        super(ToolBarDemo, self).__init__(parent)
        self.setWindowTitle("QToolBar例子")
        self.setGeometry(400, 400, 300, 200)
        toolBar = self.addToolBar("File")
        new = QAction(QIcon("./new.png"), "new", self)
        toolBar.addAction(new)
        actOpen = QAction(QIcon("./open.png"), "open", self)
        toolBar.addAction(actOpen)
        save = QAction(QIcon("./save.png"), "save", self)
        toolBar.addAction(save)
        toolBar.actionTriggered[QAction].connect(self.toolbtnpressed)

    def toolbtnpressed(self, a):
        print("pressed tool button is ", a.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ToolBarDemo()
    win.show()
    sys.exit(app.exec())
