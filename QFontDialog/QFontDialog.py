# -*- coding: utf-8 -*-
# @Time    : 2017/11/16 上午 10:24
# @Author  : AlexJean
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt


class FontDialogDemo(QWidget):
    def __init__(self, parent=None):
        super(FontDialogDemo, self).__init__(parent)
        layout = QVBoxLayout()
        self.fontButton = QPushButton("choose Font")
        self.fontButton.clicked.connect(self.getFont)
        layout.addWidget(self.fontButton)
        self.fontLineEdit = QLabel("Hello,测试字体例子")
        layout.addWidget(self.fontLineEdit)
        self.setLayout(layout)
        self.setWindowTitle("Font Dialog 例子")
        self.move(600,400)

    def getFont(self):
        font, ok = QFontDialog.getFont()
        if ok:
            self.fontLineEdit.setFont(font)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = FontDialogDemo()
    win.show()
    sys.exit(app.exec())
