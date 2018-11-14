# -*- coding: utf-8 -*-
# @Time    : 2017/11/15 下午 7:41
# @Author  : AlexJean
import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class Demo(QWidget):
    def __init__(self,parent=None):
        super(Demo, self).__init__(parent)
        groupBox = QGroupBox("GroupBox contain CheckBoxes")
        # 似乎没用 setFlat
        groupBox.setFlat(True)

        layout=QHBoxLayout()
        self.checkBox1=QCheckBox("&CheckBox1")
        self.checkBox1.setChecked(True)
        self.checkBox1.stateChanged.connect(lambda : self.btnstate(self.checkBox1))
        layout.addWidget(self.checkBox1)

        self.checkBox2=QCheckBox("CheckBox2")
        self.checkBox2.stateChanged.connect(lambda : self.btnstate(self.checkBox2))
        layout.addWidget(self.checkBox2)

        self.checkBox3=QCheckBox("tristateBox")
        self.checkBox3.setTristate(True)
        self.checkBox3.setCheckState(Qt.PartiallyChecked)
        self.checkBox3.stateChanged.connect(lambda:self.btnstate(self.checkBox3))
        layout.addWidget(self.checkBox3)

        groupBox.setLayout(layout)
        mainLayout=QVBoxLayout()
        mainLayout.addWidget(groupBox)
        self.setLayout(mainLayout)
        self.setWindowTitle("CheckBox demo")
        self.move(400,400)

    def btnstate(self,btn):
        status= btn.text()+", isChecked="+str(btn.isChecked())+',checkState='+str(btn.checkState())
        print(status)


if __name__ == "__main__":
    app=QApplication(sys.argv)
    win=Demo()
    win.show()
    sys.exit(app.exec())
