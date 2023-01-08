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

FORM_MAIN, _ = loadUiType('ui/update_business_details.ui')


class UpdateBusinessWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()

        db= DBHandler()
        data= db.select_all('business','*')[0]
        self.txt_business_name.setText(data[1])
        self.txt_business_email.setText(data[2])
        self.txt_business_address.setText(data[4])
        self.txt_business_contact.setText(data[3])
        self.txt_business_owner.setText(data[5])
        db.close()

    def Handle_Buttons(self):
        self.btn_update.clicked.connect(self.Update_Business)
        self.btn_clear.clicked.connect(self.Clear)
        self.btn_cancel.clicked.connect(self.Cancel)

    def Update_Business(self):
        business_name = self.txt_business_name.text()
        business_email = self.txt_business_email.text()
        business_address = self.txt_business_address.text()
        business_phone = self.txt_business_contact.text()
        business_owner = self.txt_business_owner.text()

        if business_name and business_email and business_address and business_phone and business_owner:
            try:
                db= DBHandler()
                db.conn.execute("UPDATE business SET business_name=?, business_email=?, business_contact=?, business_address=?, business_owner=? WHERE id=1", (business_name, business_email, business_phone, business_address, business_owner))
                db.conn.commit()
                db.close()
                QMessageBox.information(self, "Success", "Business Details Updated")
                self.close()
            except Exception as e:
                QMessageBox.information(self, "Warning", f"Business Details Not Updated {e}")
        else:
            QMessageBox.information(self, "Warning", "Fields cannot be empty")

    def Clear(self):
        self.txt_business_name.setText("")
        self.txt_business_email.setText("")
        self.txt_business_address.setText("")
        self.txt_business_contact.setText("")
        self.txt_business_owner.setText("")

    def Cancel(self):
        self.close()
        

def main():
    app = QApplication(sys.argv)
    window = UpdateBusinessWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
