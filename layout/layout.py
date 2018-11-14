import sys
from PyQt5.QtWidgets import QApplication,QWidget
from Ui_layout import *

class MyWidget(QWidget,Ui_Form):
    def __init__(self,parent=None):
        super(MyWidget,self).__init__(parent)
        self.setupUi(self)

    def pushButton_Clicked(self):
        print("Sharp比_min:", self.spinBox_sharp_min.text())
        print("Sharp比_max:", self.spinBox_sharp_max.text())

if __name__=="__main__":
    app=QApplication(sys.argv)
    ui=MyWidget()
    ui.show()
    sys.exit(app.exec())
