import sys
from PyQt5.QtWidgets import QMainWindow,QApplication,QDesktopWidget
from PyQt5.QtGui import QIcon
from Ui_mainWin import *

class MainWindow(QMainWindow,Ui_MainWindow):
    def __init__(self,parent=None):
        super(MainWindow,self).__init__(parent)
        self.setupUi(self)
        self.statusbar.showMessage("这是状态栏提示",5000)
        self.setWindowTitle("PyQt MainWindow 荧幕置中例子")
        self.center()

    def center(self):
        screen=QDesktopWidget().screenGeometry()
        size  =self.geometry()
        x=screen.width()-size.width()
        y=screen.height()-size.height()
        self.move(x/2,y/2)

if __name__ == "__main__":
    app=QApplication(sys.argv)
    #app.setWindowIcon(QIcon(":/pic/Sunset.ico"))
    form=MainWindow();
    form.show()
    sys.exit(app.exec())
