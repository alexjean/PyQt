# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 下午 7:14
# @Author  : AlexJean
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
 

class Table(QWidget):
    def __init__(self):
        super(Table, self).__init__()
        self.initUI()

    def initUI(self):
        self.setWindowTitle("QTableWidget例子")
        self.resize(400,300)
        layout=QHBoxLayout()
        tableWidget=QTableWidget()
        tableWidget.setRowCount(4)
        tableWidget.setColumnCount(3)
        layout.addWidget(tableWidget)
        tableWidget.setHorizontalHeaderLabels(['姓名','性别','体重'])


        tableWidget.setItem(0,0,QTableWidgetItem('张三'))
        # tableWidget.setItem(0,1,QTableWidgetItem('男'))
        comboBox=QComboBox()
        comboBox.addItem('男')
        comboBox.addItem('女')
        comboBox.setCurrentIndex(1)
        comboBox.setStyleSheet("QComboBox{margin:3px};")
        tableWidget.setCellWidget(0,1,comboBox)
        #tableWidget.setItem(0,2,QTableWidgetItem('160'))
        btn=QPushButton("修改")
        btn.setDown(True)
        btn.setStyleSheet("QPushButton{margin:3px};")
        tableWidget.setCellWidget(0,2,btn)
        self.setLayout(layout)


if __name__ == "__main__":
    app=QApplication(sys.argv)
    win=Table()
    win.show()
    sys.exit(app.exec())

