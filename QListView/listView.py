# -*- coding: utf-8 -*-
# @Time    : 2017/11/22 下午 6:24
# @Author  : AlexJean
import sys
from PyQt5.QtWidgets import QApplication,QWidget,QVBoxLayout,QListView,QMessageBox
from PyQt5.QtCore import QStringListModel
 

class ListViewDemo(QWidget):
    def __init__(self,parent=None):
        super(ListViewDemo, self).__init__(parent)
        self.setWindowTitle("QListView 例子")
        self.resize(300,270)
        layout=QVBoxLayout()
        listView=QListView()
        slm=QStringListModel()
        self.qList=['Alex','Alan','Fred','Geroge']
        slm.setStringList(self.qList)
        listView.setModel(slm)
        listView.clicked.connect(self.clicked)
        layout.addWidget(listView)
        self.setLayout(layout)

    def clicked(self,qModelIndex):
        QMessageBox.information(self,"ListWidget","你选择了:"+self.qList[qModelIndex.row()])


if __name__ == "__main__":
    app=QApplication(sys.argv)
    win=ListViewDemo()
    win.show()
    sys.exit(app.exec())
