import sys
from PyQt5.QtWidgets import QApplication,QWidget
from Ui_SlotSignal import *

class MyUi(QWidget,Ui_Form):
    def __init__(self,parent=None):
        super(QWidget,self).__init__(parent)
        self.setupUi(self)


if __name__ =='__main__':
    app=QApplication(sys.argv)
    ui = MyUi()
    ui.show()
    sys.exit(app.exec())

