import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QMainWindow
from PyQt5.uic import loadUi


class RMSHelperQT5ItemDetail(QDialog):
    def __init__(self):
        super(RMSHelperQT5ItemDetail, self).__init__()
        loadUi("itemdetail.ui", self)
        self.pb_select.clicked.connect(self.fn_select)
        self.pb_label_print.clicked.connect(self.fn_label_print)
        self.pb_pq.clicked.connect(self.fn_pq)
        self.pb_clear.clicked.connect(self.fn_clear)
        self.pb_exit.clicked.connect(self.fn_exit)


    def fn_exit(self):
        print("EXIT pb_exit")

    def fn_clear(self):
        print("CLEAR pb_clear")

    def fn_pq(self):
        print("PQ pb_pq")

    def fn_label_print(self):
        print("LABEL PRINT pb_label_print")

    def fn_select(self):
        print("SELECT pb_select")
