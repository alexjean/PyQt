from PyQt5.QtWidgets import  *
import sys
from Ui_QLabel2 import *

class MyDialog(QDialog,Ui_Dialog):
    def __init__(self):
        super(MyDialog,self).__init__()
        self.setupUi(self)

if __name__ == "__main__":
    app=QApplication(sys.argv)
    demo=MyDialog()
    demo.show()
    sys.exit(app.exec())




