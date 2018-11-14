# -*- coding: utf-8 -*-
# @Time    : 2017/11/18 上午 1:23
# @Author  : AlexJean
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QSizePolicy, QAction
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QImage, QIcon, QPixmap, QPainter
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog


class Win(QMainWindow):
    def __init__(self, parent=None):
        super(Win, self).__init__(parent)
        self.setWindowTitle("打印图片")
        self.imageLabel = QLabel()
        self.imageLabel.setSizePolicy(QSizePolicy.Ignored, QSizePolicy.Ignored)
        self.setCentralWidget(self.imageLabel)
        self.image = QImage()
        self.createActions()
        self.createMenus()
        self.createToolBars()
        self.move(40,35)

        name="./Sunset1024.png"
        if self.image.load(name):
            self.imageLabel.setPixmap((QPixmap.fromImage(self.image)))
            self.resize(self.image.width(), self.image.height())
        else:
            print("ImageFile "+name+" not found!")

    def createActions(self):
        self.PrinterAction = QAction(QIcon("./printer.png"), "打印")
        self.PrinterAction.setShortcut("Ctrl+P")
        self.PrinterAction.setStatusTip("打印")
        self.PrinterAction.triggered.connect(self.slotPrint)

    def createMenus(self):
        printerMenu = self.menuBar().addMenu("打印")
        printerMenu.addAction(self.PrinterAction)

    def createToolBars(self):
        fileToolBar = self.addToolBar("Print")
        fileToolBar.addAction(self.PrinterAction)

    def slotPrint(self):
        printer = QPrinter()
        printDialog = QPrintDialog(printer, self)
        if printDialog.exec():
            painter = QPainter(printer)
            #painter.begin(self)
            rect = painter.viewport()
            size = self.image.size()
            size.scale(rect.size(), Qt.KeepAspectRatio)
            painter.setViewport(rect.x(), rect.y(), size.width(), size.height())
            painter.setWindow(self.image.rect())
            painter.drawImage(0, 0, self.image)
            painter.end()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Win()
    win.show()
    sys.exit(app.exec())
