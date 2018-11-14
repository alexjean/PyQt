import sys
from PyQt5.QtWidgets import QApplication,QMainWindow
from Ui_mainwindow import *
from apprcc_rc import *

class MyMainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MyMainWindow,self).__init__(parent)
        self.setupUi(self)

if __name__ == "__main__":
    app=QApplication(sys.argv)
    win=MyMainWindow()
    win.show()
    sys.exit(app.exec())