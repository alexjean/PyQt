# -*- coding: utf-8 -*-
# @Time    : 2017/11/21 下午 7:12
# @Author  : AlexJean
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *


class Table(QWidget):
    def __init__(self,arg=None):
        super(Table, self).__init__(arg)
        self.setWindowTitle("QTableView 例子")
        self.setGeometry(400,400,500,300)
        self.model=QStandardItemModel(4,4)
        self.model.setHorizontalHeaderLabels(['标题1','标题2','标题3','标题4'])
        for row in range(4):
            for column in range(4):
                item=QStandardItem("row%s, col%s" % (row,column))
                self.model.setItem(row,column,item)
        self.tableView=QTableView()
        self.tableView.setModel(self.model)
        layout=QVBoxLayout()
        layout.addWidget(self.tableView)
        self.setLayout(layout)


if __name__ == "__main__":
    app=QApplication(sys.argv)
    win=Table()
    win.show()
    sys.exit(app.exec())