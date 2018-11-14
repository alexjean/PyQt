# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Spider.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(889, 704)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textBrowser = QtWidgets.QTextBrowser(Form)
        self.textBrowser.setOpenLinks(False)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cbHTML = QtWidgets.QCheckBox(Form)
        self.cbHTML.setObjectName("cbHTML")
        self.horizontalLayout.addWidget(self.cbHTML)
        self.btnBaidu = QtWidgets.QPushButton(Form)
        self.btnBaidu.setObjectName("btnBaidu")
        self.horizontalLayout.addWidget(self.btnBaidu)
        self.btnSohu = QtWidgets.QPushButton(Form)
        self.btnSohu.setObjectName("btnSohu")
        self.horizontalLayout.addWidget(self.btnSohu)
        self.btnBaidu_3 = QtWidgets.QPushButton(Form)
        self.btnBaidu_3.setText("")
        self.btnBaidu_3.setObjectName("btnBaidu_3")
        self.horizontalLayout.addWidget(self.btnBaidu_3)
        self.btnClear = QtWidgets.QPushButton(Form)
        self.btnClear.setObjectName("btnClear")
        self.horizontalLayout.addWidget(self.btnClear)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(Form)
        self.btnBaidu.clicked.connect(Form.slotBtnBaidu)
        self.btnSohu.clicked.connect(Form.slotBtnSohu)
        self.btnClear.clicked.connect(Form.slotBtnClear)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Spider"))
        self.cbHTML.setText(_translate("Form", "show HTML"))
        self.btnBaidu.setText(_translate("Form", "go  Baidu"))
        self.btnSohu.setText(_translate("Form", "go Sohu"))
        self.btnClear.setText(_translate("Form", "Clear"))

