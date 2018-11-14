# -*- coding: utf-8 -*-
# @Time    : 2017/11/21 下午 11:41
# @Author  : AlexJean
import sys
import urllib.request
from PyQt5.QtWidgets import *
from Ui_Spider import *
import chardet


class Win(QWidget, Ui_Form):
    def __init__(self):
        super(Win, self).__init__()
        self.setupUi(self)
        self.move(400, 300)

    def showHtml(self, Url):
        with urllib.request.urlopen(Url) as resp:
            buf = resp.read()
            dic = chardet.detect(buf)
            code = dic['encoding']
            self.textBrowser.insertPlainText(
                "Response Code=%s Decode as '%s'\r\n------------------------------\r\n" % (resp.getcode(), code))
            str = buf.decode(code)
            if (self.cbHTML.isChecked()):
                self.textBrowser.insertHtml(str)
            else:
                self.textBrowser.insertPlainText(str)

    def slotBtnBaidu(self):
        self.showHtml("http://www.baidu.com")

    def slotBtnSohu(self):
        self.showHtml("http://www.sohu.com")

    def slotBtnClear(self):
        self.textBrowser.clear()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec())
