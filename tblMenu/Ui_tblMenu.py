# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tblMenu.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(824, 548)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setContextMenuPolicy(QtCore.Qt.CustomContextMenu)
        self.tableWidget.setRowCount(5)
        self.tableWidget.setColumnCount(4)
        self.tableWidget.setObjectName("tableWidget")
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        icon = QtGui.QIcon.fromTheme("ok")
        item.setIcon(icon)
        self.tableWidget.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(1, 2, item)
        self.horizontalLayout.addWidget(self.tableWidget)

        self.retranslateUi(Form)
        self.tableWidget.customContextMenuRequested['QPoint'].connect(Form.generateMenu)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "QTableWidget例子"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("Form", "姓名"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("Form", "性别"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("Form", "体重"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("Form", "图形"))
        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        item = self.tableWidget.item(0, 0)
        item.setText(_translate("Form", "张三"))
        item = self.tableWidget.item(0, 1)
        item.setText(_translate("Form", "男"))
        item = self.tableWidget.item(0, 2)
        item.setText(_translate("Form", "160"))
        item = self.tableWidget.item(1, 0)
        item.setText(_translate("Form", "李四"))
        item = self.tableWidget.item(1, 1)
        item.setText(_translate("Form", "女"))
        item = self.tableWidget.item(1, 2)
        item.setText(_translate("Form", "170"))
        self.tableWidget.setSortingEnabled(__sortingEnabled)

