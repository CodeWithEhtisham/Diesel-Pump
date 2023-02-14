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
from resources_rc import *

FORM_MAIN, _ = loadUiType('ui/add_customer.ui')


class UpdateCustomerWindow(QMainWindow, FORM_MAIN):
    def __init__(self,id):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.db=DBHandler()
        self.id = id
        self.Handle_Buttons()
        self.update()

    def update(self):
        data = self.db.select(
            table_name='Customers',
            columns="name,phone,vehicle,address,balance_type,balance",
            condition="custmer_id={}".format(self.id)
        )
        self.txt_name.setText(data[0][0])
        self.txt_phone.setText(data[0][1])
        self.txt_vehicle.setText(data[0][2])
        self.txt_address.setText(data[0][3])
        self.balance_type.setCurrentText(data[0][4])
        self.txt_balance.setText(str(data[0][5]))
        self.txt_balance.setReadOnly(True)
        self.balance_type.setDisabled(True)

    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.Add_Customer)
        # self.btn_clear.clicked.connect(self.Clear_Fields)
        self.btn_cancel.clicked.connect(self.close)

    def Add_Customer(self):
        name = self.txt_name.text()
        phone = self.txt_phone.text()
        vehicle = self.txt_vehicle.text()
        address = self.txt_address.text()
        if name and phone and vehicle and address :
            try:
                self.db.conn.execute(
                    "UPDATE Customers SET name=?,phone=?,vehicle=?,address=? WHERE custmer_id=?",
                    (name, phone, vehicle, address, self.id)
                )
                self.db.conn.commit()
                self.db.close()
                self.close()
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Customer has not been added {e}")
        else:
            QMessageBox.warning(self, "Error", "Fields cannot be empty")



        

def main():
    app = QApplication(sys.argv)
    window = UpdateCustomerWindow(1)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
