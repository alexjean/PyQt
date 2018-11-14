# -*- coding: utf-8 -*-
# @Time    : 2017/11/16 上午 11:50
# @Author  : AlexJean
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class FileDialogDemo(QWidget):
    def __init__(self, parent=None):
        super(FileDialogDemo, self).__init__(parent)
        layout = QVBoxLayout()
        self.btn = QPushButton("加载图片")
        self.btn.clicked.connect(self.getfile)
        layout.addWidget(self.btn)
        self.le = QLabel("")
        layout.addWidget(self.le)
        self.btn1 = QPushButton("加载本文文件")
        self.btn1.clicked.connect(self.getfiles)
        layout.addWidget(self.btn1)
        self.contents = QTextEdit()
        layout.addWidget(self.contents)
        self.setLayout(layout)
        self.setWindowTitle("QFileDialog 例子")
        self.move(400, 400)

    def getfile(self):
        fname, _ = QFileDialog.getOpenFileName(self, 'OpenFile', '~', "Image Files (*.jpg *.gif)")
        self.le.setPixmap(QPixmap(fname))

    def getfiles(self):
        dlg = QFileDialog()
        dlg.setFileMode(QFileDialog.AnyFile)
        dlg.setFilter(QDir.Files)
        if dlg.exec():
            filenames = dlg.selectedFiles()
            with open(filenames[0], 'r') as f:
                data = f.read()
                self.contents.setText(data)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = FileDialogDemo()
    win.show()
    sys.exit(app.exec())
