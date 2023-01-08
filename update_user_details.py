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

FORM_MAIN, _ = loadUiType('ui/update_user_details.ui')


class UpdateUserWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()

        db=DBHandler()
        user = db.select(table_name="users", columns="*", condition="id=1")[0]
        self.txt_name.setText(user[1])
        self.txt_email.setText(user[2])
        self.txt_contact.setText(user[3])
        self.txt_username.setText(user[4])

    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.Save_User)
        self.btn_clear.clicked.connect(self.Clear_User)
        self.btn_cancel.clicked.connect(self.close)

    def Save_User(self):
        name = self.txt_name.text()
        email = self.txt_email.text()
        contact = self.txt_contact.text()
        username = self.txt_username.text()
        if name and email and contact and username != "":
            try:
                db=DBHandler()
                db.conn.execute("UPDATE users SET name=?, email=?, contact=?, username=? WHERE id=1", (name, email, contact, username))
                db.conn.commit()
                QMessageBox.information(self, "Success", "User has been added")
                db.close()
                self.close()
            except Exception as e:
                QMessageBox.warning(self, "Error", f"User has not been added {e}")
        else:
            QMessageBox.warning(self, "Error", "Fields cannot be empty")
        
    def Clear_User(self):
        self.txt_name.setText("")
        self.txt_email.setText("")
        self.txt_contact.setText("")
        self.txt_username.setText("")

def main():
    app = QApplication(sys.argv)
    window = UpdateUserWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

