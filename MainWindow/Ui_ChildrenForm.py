# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ChildrenForm.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_ChildrenForm(object):
    def setupUi(self, ChildrenForm):
        ChildrenForm.setObjectName("ChildrenForm")
        ChildrenForm.resize(400, 300)
        font = QtGui.QFont()
        font.setFamily("AR PL UKai TW")
        font.setPointSize(12)
        ChildrenForm.setFont(font)
        self.textEdit = QtWidgets.QTextEdit(ChildrenForm)
        self.textEdit.setGeometry(QtCore.QRect(10, 20, 381, 261))
        self.textEdit.setObjectName("textEdit")

        self.retranslateUi(ChildrenForm)
        QtCore.QMetaObject.connectSlotsByName(ChildrenForm)

    def retranslateUi(self, ChildrenForm):
        _translate = QtCore.QCoreApplication.translate
        ChildrenForm.setWindowTitle(_translate("ChildrenForm", "Form"))
        self.textEdit.setHtml(_translate("ChildrenForm", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'AR PL UKai TW\'; font-size:12pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Ubuntu\'; font-size:11pt; color:#ff0000;\">Alex 瓜瓜叫!</span></p></body></html>"))

