from PyQt5.QtWidgets import QApplication, QLineEdit, QWidget, QFormLayout, QDesktopWidget
import sys


class lineEditDemo(QWidget):
    def __init__(self, parent=None):
        super(lineEditDemo, self).__init__(parent)
        self.setWindowTitle("QLineEdit例子")

        formLayout = QFormLayout()
        pNormal = QLineEdit()
        pNoEcho = QLineEdit()
        pPassword = QLineEdit()
        pPasswordEchoOn = QLineEdit()

        formLayout.addRow("Normal", pNormal)
        formLayout.addRow("NoEcho", pNoEcho)
        formLayout.addRow("Password", pPassword)
        formLayout.addRow("PasswordEchoOn", pPasswordEchoOn)

        pNormal.setPlaceholderText("Normal")
        pNoEcho.setPlaceholderText("NoEcho")
        pPassword.setPlaceholderText("Password")
        pPasswordEchoOn.setPlaceholderText("PasswordEchoOnEdit")

        pNormal.setEchoMode(QLineEdit.Normal)
        pNoEcho.setEchoMode(QLineEdit.NoEcho)
        pPassword.setEchoMode(QLineEdit.Password)
        pPasswordEchoOn.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)

        screen = QDesktopWidget().screenGeometry()
        x = (screen.width() - self.width()) / 2
        y = (screen.height() - self.height()) / 2

        self.move(x, y)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    win = lineEditDemo()
    win.show()
    sys.exit(app.exec())
