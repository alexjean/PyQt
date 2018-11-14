import sys
from PyQt5.QtGui import QIcon,QFont
from PyQt5.QtWidgets import QWidget,QApplication,QToolTip

class Win(QWidget):
    def __init__(self,parent=None):
        super(Win,self).__init__(parent)
        self.initUI()

    def initUI(self):
        QToolTip.setFont(QFont('SansSerif',10))
        self.setToolTip('这是一个<b>气泡提示<b>')
        self.setGeometry(200,300,400,400)
        self.setWindowTitle('程序图标+气泡提示')
        self.setWindowIcon(QIcon('./Windows.ico'))

if __name__ == '__main__':
    app=QApplication(sys.argv)
    win=Win()
    win.show()
    sys.exit(app.exec())