# -*- coding: utf-8 -*-
# @Time    : 2017/11/17 下午 11:10
# @Author  : AlexJean
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QDate, QTime, QDateTime


class Demo(QWidget):
    def __init__(self):
        super(Demo, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QDateTimeEdit 例子")
        self.setGeometry(400, 400, 300, 90)
        layout = QVBoxLayout()
        self.dateEdit = QDateTimeEdit(QDateTime.currentDateTime())
        self.dateEdit.setDisplayFormat("yyyy-MM-dd HH:mm:ss")
        self.dateEdit.setMinimumDate(QDate.currentDate().addDays(-365))
        self.dateEdit.setMaximumDate(QDate.currentDate().addDays(365))
        self.dateEdit.setCalendarPopup(True)
        self.dateEdit.dateChanged.connect(self.onDateChanged)
        self.dateEdit.dateTimeChanged.connect(self.onDateTimeChanged)
        self.dateEdit.timeChanged.connect(self.onTimeChanged)

        self.btn = QPushButton('获得日期和时间')
        self.btn.clicked.connect(self.onButtonClick)

        layout.addWidget(self.dateEdit)
        layout.addWidget(self.btn)
        self.setLayout(layout)

    def onDateChanged(self, date):
        print(date)

    def onDateTimeChanged(self, dateTime):
        print(dateTime)

    def onTimeChanged(self, time):
        print(time)

    def onButtonClick(self):
        dateTime = self.dateEdit.dateTime()
        maxDate = self.dateEdit.maximumDate()
        maxDateTime = self.dateEdit.maximumDateTime()
        maxTime = self.dateEdit.maximumTime()
        minDate = self.dateEdit.minimumDate()
        minDateTime = self.dateEdit.minimumDateTime()
        minTime = self.dateEdit.minimumTime()
        print('dateTime=%s' % str(dateTime))
        print('maxDate =%s' % str(maxDate))
        print('maxTime =%s' % str(maxTime))
        print('maxDateTime=%s' % str(maxDateTime))
        print('minDate =%s' % str(minDate))
        print('minTime =%s' % str(minTime))
        print('minDateTime=%s' % str(minDateTime))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Demo()
    win.show()
    sys.exit(app.exec())
