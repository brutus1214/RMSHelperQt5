import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi
import RMSHelperQT5_item_detail


class RMSHelperQT5Login(QMainWindow):
    def __init__(self):
        super(RMSHelperQT5Login, self).__init__()
        loadUi("login.ui", self)
        self.pb_login.clicked.connect(self.fn_login)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)

    def fn_login(self):
        server = self.sever
        user_name = self.user_name
        password = self.password
        db_name = self.database_name
        print(server, user_name, password, db_name)


app = QApplication(sys.argv)
login_window = RMSHelperQT5Login()
widget = QtWidgets.QStackedWidget()
widget.addWidget(login_window)
widget.show()
app.exec_()
