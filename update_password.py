import datetime
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from db_handler import DBHandler

import sys
from os import path
from PyQt5.uic import loadUiType

FORM_MAIN, _ = loadUiType('ui/update_password.ui')


class ChangePasswordWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()

    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.change_password)
        self.btn_clear.clicked.connect(self.Clear)
        self.btn_cancel.clicked.connect(self.close)

    def change_password(self):
        old_password = self.txt_old_pwd.text()
        new_password = self.txt_new_pwd.text()
        confirm_password = self.txt_confirm_pwd.text()

        db = DBHandler()
        password = db.conn.execute(f"SELECT password FROM users WHERE password = '{old_password}'").fetchone()

        if password == None:
            QMessageBox.warning(self, "Error", "Old password is incorrect")
        else: password = password[0]
        if password == old_password:
            if new_password == confirm_password:
                db.conn.execute(f"UPDATE users SET password = '{new_password}' WHERE password = '{old_password}'")
                db.conn.commit()
                QMessageBox.information(self, "Success", "Password changed successfully")
                self.Clear()
            else:
                QMessageBox.warning(self, "Error", "New password and confirm password do not match")

        

    def Clear(self):
        self.txt_old_pwd.setText('')
        self.txt_new_pwd.setText('')
        self.txt_confirm_pwd.setText('')

def main():
    app = QApplication(sys.argv)
    window = ChangePasswordWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
