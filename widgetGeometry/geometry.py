from PyQt5.QtWidgets import QApplication,QWidget,QPushButton
import sys

def report(msg,geo):
    print(msg)
    print("w.x()=%d" % geo.x())
    print("w.y()=%d" % geo.y())
    print("w.width()=%d" % geo.width())
    print("w.height()=%d" % geo.height())


app=QApplication(sys.argv)
widget=QWidget()
btn=QPushButton(widget)
btn.setText("Button")
btn.move(20,20)
widget.resize(300,400)
widget.move(350,280)
widget.setWindowTitle("PyQt坐标系统例子")
widget.show()
report("QWidget",widget)
report("Geometry",widget.geometry())
report("frameGeometry",widget.frameGeometry())

sys.exit(app.exec())