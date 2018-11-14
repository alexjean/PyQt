# -*- coding: utf-8 -*-
# @Time    : 2017/12/4 上午 12:01
# @Author  : AlexJean
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import pyqtSignal, QObject, Qt, pyqtSlot
from Ui_tblMenu import *


class Table(QWidget,Ui_Form):
    def __init__(self):
        super(Table, self).__init__()
        self.setupUi(self)
        self.move(300,300)

#    def setupUi(self):
#        self.setWindowTitle("QTableWidget Demo")
#        self.resize(500, 300)
#        layout = QHBoxLayout()
#        self.tableWidget = QTableWidget()
#        self.tableWidget.setRowCount(5)
#        self.tableWidget.setColumnCount(3)
#        layout.addWidget(self.tableWidget)

#        self.tableWidget.setHorizontalHeaderLabels(['姓名', '性别', '体重'])
#        self.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
#        self.tableWidget.setItem(0, 0, QTableWidgetItem('张三'))
#        self.tableWidget.setItem(0, 1, QTableWidgetItem('男'))
#        self.tableWidget.setItem(0, 2, QTableWidgetItem('160'))
#        self.tableWidget.setItem(1, 0, QTableWidgetItem('李四'))
#        self.tableWidget.setItem(1, 1, QTableWidgetItem('女'))
#        self.tableWidget.setItem(1, 2, QTableWidgetItem('170'))

#        self.tableWidget.setContextMenuPolicy(Qt.CustomContextMenu)
#        self.tableWidget.customContextMenuRequested.connect(self.generateMenu)

#        self.setLayout(layout)

    def generateMenu(self, pos):
        row_num = -1
        tbl=self.tableWidget;
        for i in tbl.selectionModel().selection().indexes():
            row_num = i.row()
        if row_num < 2:
            menu = QMenu()
            item1 = menu.addAction("选项一")
            item2 = menu.addAction("选项二")
            item3 = menu.addAction("选项三")
            action = menu.exec(self.tableWidget.mapToGlobal(pos))
            if action in [item1,item2,item3]:
                print('你选了 %s ,文字内容是 %s' % (action.text(), tbl.item(row_num,0).text()))
            else:
                print('Selection None!')


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Table()
    win.show()
    sys.exit(app.exec())
