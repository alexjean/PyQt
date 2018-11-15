# -*- coding: utf-8 -*-
# @Time    : 2017/12/24 上午 12:22
# @Author  : AlexJean
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Ui_mainWin import *
from mnist import Mnist


class Form(Ui_Form, QWidget):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.setupUi(self)
        self.showMessage("Tensorflow Version=%s" % Mnist.tfVersion())
        pIntValidator = QIntValidator(self)
        pIntValidator.setRange(0, 54000)
        self.leStart.setValidator(pIntValidator)
        self.move(400, 200)
        self.mnist = None
        self.worker = None
        self.pic = QPixmap(self.labelDraw.size())
        self.pic.fill(Qt.white)
        self.labelDraw.setPixmap(self.pic)

    def setTableSize(self, table: QTableWidget):
        rowHeight = 30
        colWidth = 40
        #        h=table.verticalHeader().height()
        #        w=table.horizontalHeader().width()
        table.setRowCount(table.height()  / (rowHeight+1))
        table.setColumnCount(table.width() / (colWidth+1))
        table.rowHeight(rowHeight)
        for i in range(table.columnCount()):
            table.setColumnWidth(i, colWidth)
        #self.showMessage("Row<%d> Col<%d>" % (table.rowCount(), table.columnCount()))

    def loadMnistData(self):
        self.setTableSize(self.tableWidget)
        self.showMessage("Begin load Mnist data!")
        self.mnist = Mnist.inputData()
        self.showMessage("{ train test validation } loaded!")
        self.showMessage("num_examples %d %d %d" %
                         (self.mnist.train.num_examples,
                          self.mnist.test.num_examples,
                          self.mnist.validation.num_examples))
        self.btnDraw.setEnabled(True)
        self.btnTraining.setEnabled(True)
        imgs = self.mnist.train.images  # train有55000个image test 10000 validation 5000
        self.showMessage('type %s\nshape %s\ndtype %s\n' % (type(imgs), imgs.shape, imgs.dtype))

    def drawImageOnTable(self):
        self.setTableSize(self.tableWidget)
        imgs = self.mnist.train.images
        lbls = self.mnist.train.labels
        no = lbls[0].shape[0]
        i = int(self.leStart.text())
        for row in range(self.tableWidget.rowCount()):
            for col in range(self.tableWidget.columnCount()):
                img = Form.fromTuple2Image(imgs[i])
                lbl = lbls[i]
                for index in range(no):
                    if lbl[index] > 0.99:
                        self.setTableImage(row, col, img, str(index))
                        break
                QCoreApplication.processEvents()
                i = i + 1

    @staticmethod
    def fromTuple2Image(tup):
        img = QImage(28, 28, QImage.Format_Grayscale8)
        for y in range(28):
            j = y * 28
            for x in range(28):
                # mnist 里的颜色是0代表白色（背景），1.0代表黑色
                c = int((1.0 - tup[x+j]) * 255)
                img.setPixel(x, y, qRgb(c, c, c))
        return img

    def setTableImage(self, row, col, img: QImage, label):
        pixmap = QPixmap.fromImage(img)
        item = QTableWidgetItem(QIcon(pixmap), label)
        self.tableWidget.setItem(row, col, item)

    def showMessage(self, msg):
        self.listWidget.addItem(msg)

    def trainingFinished(self,msg):
        self.showMessage("Training completed!")
        self.showMessage(msg)
        self.btnTraining.setEnabled(True)

    def training(self):
        self.btnTraining.setEnabled(False)
        self.showMessage("Begin training...")
        QCoreApplication.processEvents()
        self.worker = TrainWorker(self.mnist)
        self.worker.finished.connect(self.trainingFinished)
        self.worker.start()


class TrainWorker(QThread):
    finished = pyqtSignal(str)

    def __init__(self, data):
        super(TrainWorker, self).__init__()
        self.mnist=data

    def run(self):
        msg = Mnist.train(self.mnist)
        self.finished.emit(msg)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = Form()
    win.show()
    sys.exit(app.exec())
