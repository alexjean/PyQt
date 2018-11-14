# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SlotSignal.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("AR PL UKai TW")
        font.setPointSize(12)
        Form.setFont(font)
        self.radioButton = QtWidgets.QRadioButton(Form)
        self.radioButton.setGeometry(QtCore.QRect(120, 90, 117, 22))
        self.radioButton.setObjectName("radioButton")
        self.label = QtWidgets.QLabel(Form)
        self.label.setEnabled(True)
        self.label.setGeometry(QtCore.QRect(80, 170, 67, 17))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Form)
        self.lineEdit.setGeometry(QtCore.QRect(170, 170, 113, 27))
        self.lineEdit.setObjectName("lineEdit")

        self.retranslateUi(Form)
        self.radioButton.clicked['bool'].connect(self.label.setVisible)
        self.radioButton.clicked['bool'].connect(self.lineEdit.setEnabled)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.radioButton.setText(_translate("Form", "显示"))
        self.label.setText(_translate("Form", "阿凡达"))

