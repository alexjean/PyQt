# -*- coding: utf-8 -*-
# @Time    : 2017/11/27 上午 12:12
# @Author  : AlexJean
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QColor, QBrush


class Table(QWidget):
    def __init__(self):
        super(Table, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget例子")
        self.setGeometry(300, 300, 600, 800)
        layout = QHBoxLayout()
        tableWidget = QTableWidget()
        tableWidget.setColumnCount(4)
        tableWidget.setRowCount(30)
        layout.addWidget(tableWidget)
        for i in range(30):
            for j in range(4):
                itemContent = '(%d,%d)' % (i, j)
                tableWidget.setItem(i, j, QTableWidgetItem(itemContent))
        self.setLayout(layout)
        text = "(10,1)"
        items = tableWidget.findItems(text, Qt.MatchExactly)
        if len(items) > 0:
            item = items[0]
            item.setSelected(True)
            item.setForeground(QBrush(QColor(255,0,0)))
            row = item.row()
            tableWidget.setRowHeight(row,60)
            tableWidget.verticalScrollBar().setSliderPosition(row)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Table()
    win.show()
    sys.exit(app.exec())
