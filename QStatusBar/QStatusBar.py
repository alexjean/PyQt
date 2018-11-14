# -*- coding: utf-8 -*-
# @Time    : 2017/11/18 上午 1:14
# @Author  : AlexJean
import sys
from PyQt5.QtWidgets import *


class StatusDemo(QMainWindow):
    def __init__(self, parent=None):
        super(StatusDemo, self).__init__(parent)
        bar = self.menuBar()
        file = bar.addMenu("File")
        file.addAction("show")
        file.triggered[QAction].connect(self.processTrigger)
        self.setCentralWidget(QTextEdit())
        self.statusBar = QStatusBar()
        self.setWindowTitle("QStatusBar例子")
        self.setStatusBar(self.statusBar)
        self.move(35,40)

    def processTrigger(self, action):
        if action.text() == "show":
            self.statusBar.showMessage(action.text() + " action被点击", 5000)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = StatusDemo()
    win.show()
    sys.exit(app.exec())