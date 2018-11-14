# -*- coding: utf-8 -*-
import sys
from PyQt5.QtWidgets import QApplication,QMainWindow,QWidget,QFileDialog
from Ui_MainForm import *
from Ui_ChildrenForm import *


class MyChildrenForm(QWidget,Ui_ChildrenForm):
    def __init__(self,parent=None):
        super(MyChildrenForm,self).__init__(parent)
        self.setupUi(self)


class MyMainForm(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MyMainForm,self).__init__(parent)
        self.setupUi(self)
        self.child = MyChildrenForm()

    def openMsg(self):
        file,ok=QFileDialog.getOpenFileName(self,"../","AllFiles (*);;TextFiles (*.txt)")
        self.statusbar.showMessage(file)

    def childShow(self):
        self.MaingridLayout.addWidget(self.child)
        self.child.show()


if __name__=="__main__":
    app=QApplication(sys.argv)
    win=MyMainForm()
    win.show()
    sys.exit(app.exec())
