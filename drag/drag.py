# -*- coding: utf-8 -*-
# @Time    : 2017/11/16 下午 5:02
# @Author  : AlexJean
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import *
 
class Combo(QComboBox):
    def __init__(self,title,parent):
        super(Combo, self).__init__(parent)
        self.setAcceptDrops(True)

    def dragEnterEvent(self, dragEnterEvent):
        print(dragEnterEvent.mimeData().hasText())
        if dragEnterEvent.mimeData().hasText():
            dragEnterEvent.accept()
        else:
            dragEnterEvent.ignore()

    def dropEvent(self, dropEvent):
        self.addItem(dropEvent.mimeData().text())


class Example(QWidget):
    def __init__(self):
        super(Example, self).__init__()
        self.initUI()

    def initUI(self):
        layout=QFormLayout()
        layout.addRow(QLabel("请把左边的本文托到右边的下拉菜单"))
        edit=QLineEdit()
        edit.setDragEnabled(True)
        combo=Combo("Button",self)
        layout.addRow(edit,combo)
        self.setLayout(layout)
        self.setWindowTitle('简单的Drag例子')
        self.move(400,400)


if __name__ == "__main__":
    app=QApplication(sys.argv)
    win=Example()
    win.show()
    sys.exit(app.exec())
