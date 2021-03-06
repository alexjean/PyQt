# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWin.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(842, 630)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.splitter = QtWidgets.QSplitter(Form)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.listWidget = QtWidgets.QListWidget(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.listWidget.sizePolicy().hasHeightForWidth())
        self.listWidget.setSizePolicy(sizePolicy)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout.addWidget(self.listWidget)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.groupBox = QtWidgets.QGroupBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox.sizePolicy().hasHeightForWidth())
        self.groupBox.setSizePolicy(sizePolicy)
        self.groupBox.setMaximumSize(QtCore.QSize(132, 16777215))
        self.groupBox.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.groupBox.setFlat(False)
        self.groupBox.setObjectName("groupBox")
        self.btnDraw = QtWidgets.QPushButton(self.groupBox)
        self.btnDraw.setEnabled(False)
        self.btnDraw.setGeometry(QtCore.QRect(2, 62, 121, 25))
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnDraw.sizePolicy().hasHeightForWidth())
        self.btnDraw.setSizePolicy(sizePolicy)
        self.btnDraw.setMaximumSize(QtCore.QSize(128, 16777215))
        self.btnDraw.setObjectName("btnDraw")
        self.leStart = QtWidgets.QLineEdit(self.groupBox)
        self.leStart.setGeometry(QtCore.QRect(2, 31, 121, 25))
        self.leStart.setMaximumSize(QtCore.QSize(128, 16777215))
        self.leStart.setObjectName("leStart")
        self.horizontalLayout_2.addWidget(self.groupBox)
        self.labelDraw = QtWidgets.QLabel(self.layoutWidget)
        self.labelDraw.setMinimumSize(QtCore.QSize(112, 112))
        self.labelDraw.setAutoFillBackground(False)
        self.labelDraw.setText("")
        self.labelDraw.setObjectName("labelDraw")
        self.horizontalLayout_2.addWidget(self.labelDraw)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.btnLoadMnist = QtWidgets.QPushButton(self.layoutWidget)
        self.btnLoadMnist.setMaximumSize(QtCore.QSize(128, 16777215))
        self.btnLoadMnist.setObjectName("btnLoadMnist")
        self.horizontalLayout.addWidget(self.btnLoadMnist)
        self.btnTraining = QtWidgets.QPushButton(self.layoutWidget)
        self.btnTraining.setEnabled(False)
        self.btnTraining.setMaximumSize(QtCore.QSize(128, 16777215))
        self.btnTraining.setObjectName("btnTraining")
        self.horizontalLayout.addWidget(self.btnTraining)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.tableWidget = QtWidgets.QTableWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(3)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setRowCount(10)
        self.tableWidget.setColumnCount(5)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.verticalHeader().setVisible(True)
        self.horizontalLayout_3.addWidget(self.splitter)

        self.retranslateUi(Form)
        self.btnLoadMnist.clicked.connect(Form.loadMnistData)
        self.btnTraining.clicked.connect(Form.training)
        self.btnDraw.clicked.connect(Form.drawImageOnTable)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "MNIST"))
        self.groupBox.setTitle(_translate("Form", "Draw from"))
        self.btnDraw.setText(_translate("Form", "Draw"))
        self.leStart.setText(_translate("Form", "100"))
        self.btnLoadMnist.setText(_translate("Form", "Load"))
        self.btnTraining.setText(_translate("Form", "Training"))

