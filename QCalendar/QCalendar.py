# -*- coding: utf-8 -*-
# @Time    : 2017/11/17 下午 9:44
# @Author  : AlexJean
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate


class CalendarExample(QWidget):
    def __init__(self):
        super(CalendarExample, self).__init__()
        self.initUI()

    def initUI(self):
        layout=QVBoxLayout()
        self.cal = QCalendarWidget()
        self.cal.setMinimumDate(QDate(1980, 1, 1))
        self.cal.setMaximumDate(QDate(2100, 1, 1))
        self.cal.setGridVisible(True)
        self.cal.move(20, 20)
        self.cal.clicked[QDate].connect(self.showDate)
        date = self.cal.selectedDate()
        layout.addWidget(self.cal)
        self.lbl = QLabel(self)
        self.lbl.setText(date.toString("yyyy-MM-dd dddd"))
        layout.addWidget(self.lbl)
        self.setLayout(layout)
        self.move(400,400)

    def showDate(self, date):
        self.lbl.setText(date.toString("yyyy-MM-dd dddd"))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = CalendarExample()
    win.show()
    sys.exit(app.exec())
