# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 下午 7:04
# @Author  : AlexJean
import sys
from PyQt5.QtWidgets import QListWidget,QMessageBox,QApplication


class ListWidget(QListWidget):
    def __init__(self):
        super(ListWidget, self).__init__()
        self.resize(300, 120)
        self.move(300,300)
        self.addItem("Alex")
        self.addItem("Alan")
        self.addItem("Fred")
        self.addItem("William")
        self.setWindowTitle('QListWidget例子')
        self.itemClicked.connect(self.clicked)

    def clicked(self, item):
        QMessageBox.information(self, "ListWidget", "选择了: " + item.text())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = ListWidget()
    win.show()
    sys.exit(app.exec())
