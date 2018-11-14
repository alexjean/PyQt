from PyQt5.QtWidgets import QApplication,QWidget,QLabel,QVBoxLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap,QPalette
import sys


class WinDemo(QWidget):
    def __init__(self):
        super().__init__()
        label1=QLabel(self)
        label2=QLabel(self)
        label3=QLabel(self)
        label4=QLabel(self)

        label1.setText('这是一个本文标签')
        label1.setAutoFillBackground(True)
        palette=QPalette()
        palette.setColor(QPalette.Window,Qt.blue)
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)
        #没http:// 会抓档案
        label2.setText("<a href='XP.jpg'>欢迎使用 Python GUI应用</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('这是一个图片标签')
        label3.setPixmap(QPixmap("./XP.jpg"))

        label4.setText("<a href='http://www.cnblogs.com/wangshuo1/'>欢迎访问Alex的小屋</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超链接标签')

        vbox=QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addStretch()
        vbox.addWidget(label2)
        vbox.addStretch()
        vbox.addWidget(label3)
        vbox.addStretch()
        vbox.addWidget(label4)

        label2.setOpenExternalLinks(True)
        label4.setOpenExternalLinks(True)
        label4.linkActivated.connect(link_clicked)

        label2.linkHovered.connect(link_hovered)
        label1.setTextInteractionFlags(Qt.TextSelectableByMouse)

        self.setLayout(vbox)
        self.setWindowTitle("QLabel例子")


def link_hovered():
        print("当鼠标滑过label-2時,触发事件")

def link_clicked():
        print("当鼠标触击label-4時,触发事件")


if __name__ == "__main__":
    app=QApplication(sys.argv)
    win=WinDemo()
    win.show()
    sys.exit(app.exec())

