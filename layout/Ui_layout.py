# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'layout.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(697, 352)
        font = QtGui.QFont()
        font.setFamily("AR PL UKai TW")
        font.setPointSize(12)
        Form.setFont(font)
        Form.setAutoFillBackground(True)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(90, 80, 481, 151))
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_6 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(2)
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.verticalLayout.addWidget(self.label_6)
        self.label = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(1)
        sizePolicy.setHeightForWidth(self.label_3.sizePolicy().hasHeightForWidth())
        self.label_3.setSizePolicy(sizePolicy)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.horizontalLayout.addItem(spacerItem)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_4 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_5 = QtWidgets.QLabel(self.widget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 1, 1, 1)
        self.spinBox_returns_min = QtWidgets.QSpinBox(self.widget)
        self.spinBox_returns_min.setObjectName("spinBox_returns_min")
        self.gridLayout.addWidget(self.spinBox_returns_min, 1, 0, 1, 1)
        self.spinBox_returns_max = QtWidgets.QSpinBox(self.widget)
        self.spinBox_returns_max.setObjectName("spinBox_returns_max")
        self.gridLayout.addWidget(self.spinBox_returns_max, 1, 1, 1, 1)
        self.spinBox_maxdrawdown_min = QtWidgets.QSpinBox(self.widget)
        self.spinBox_maxdrawdown_min.setObjectName("spinBox_maxdrawdown_min")
        self.gridLayout.addWidget(self.spinBox_maxdrawdown_min, 2, 0, 1, 1)
        self.spinBox_maxdrawdown_max = QtWidgets.QSpinBox(self.widget)
        self.spinBox_maxdrawdown_max.setObjectName("spinBox_maxdrawdown_max")
        self.gridLayout.addWidget(self.spinBox_maxdrawdown_max, 2, 1, 1, 1)
        self.spinBox_sharp_min = QtWidgets.QSpinBox(self.widget)
        self.spinBox_sharp_min.setObjectName("spinBox_sharp_min")
        self.gridLayout.addWidget(self.spinBox_sharp_min, 3, 0, 1, 1)
        self.spinBox_sharp_max = QtWidgets.QSpinBox(self.widget)
        self.spinBox_sharp_max.setObjectName("spinBox_sharp_max")
        self.gridLayout.addWidget(self.spinBox_sharp_max, 3, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.line = QtWidgets.QFrame(self.widget)
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.horizontalLayout.addWidget(self.line)
        spacerItem1 = QtWidgets.QSpacerItem(50, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setMinimumSize(QtCore.QSize(60, 60))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.label_3.setBuddy(self.spinBox_sharp_min)

        self.retranslateUi(Form)
        self.pushButton.clicked.connect(Form.pushButton_Clicked)
        QtCore.QMetaObject.connectSlotsByName(Form)
        Form.setTabOrder(self.spinBox_returns_min, self.spinBox_returns_max)
        Form.setTabOrder(self.spinBox_returns_max, self.spinBox_maxdrawdown_min)
        Form.setTabOrder(self.spinBox_maxdrawdown_min, self.spinBox_maxdrawdown_max)
        Form.setTabOrder(self.spinBox_maxdrawdown_max, self.spinBox_sharp_min)
        Form.setTabOrder(self.spinBox_sharp_min, self.spinBox_sharp_max)
        Form.setTabOrder(self.spinBox_sharp_max, self.pushButton)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "收益"))
        self.label_2.setText(_translate("Form", "最大回撤"))
        self.label_3.setText(_translate("Form", "&Sharp"))
        self.label_4.setText(_translate("Form", "最小值"))
        self.label_5.setText(_translate("Form", "最大值"))
        self.pushButton.setText(_translate("Form", "开始"))

