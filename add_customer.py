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


class AddCustomerWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()

    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.Add_Customer)
        self.btn_clear.clicked.connect(self.Clear_Fields)
        self.btn_cancel.clicked.connect(self.close)

    def Add_Customer(self):
        name = self.txt_name.text()
        phone = self.txt_phone.text()
        vehicle = self.txt_vehicle.text()
        address = self.txt_address.text()
        balance_type = self.balance_type.currentText()
        balance = self.txt_balance.text()
        if name and phone and vehicle and address and balance != "":
            try:
                db=DBHandler()
                if balance_type == 'Cash In':
                    balance = float(balance)
                else:
                    balance = -float(balance)

                db.insert(table_name="Customers", columns="name, phone, vehicle, address, balance_type, balance",
                values=f"'{name}', '{phone}', '{vehicle}', '{address}', '{balance_type}', '{balance}'")

                    # self.conn.execute(f"CREATE TABLE IF NOT EXISTS customer_cash_received (id INTEGER PRIMARY KEY AUTOINCREMENT,customer_id INTEGER,date TEXT,payment_method TEXT,cash_received REAL,remaining REAL,description TEXT DEFAULT 'Cash Received',quantity INTEGER DEFAULT 0,rate REAL DEFAULT 0,amount REAL DEFAULT 0,FOREIGN KEY(customer_id) REFERENCES customers(customer_id))")
                db.insert(table_name="customer_cash_received", columns="customer_id, date, payment_method, remaining, description",values=f"'{db.cursor.lastrowid}', '{QDate.currentDate().toString('dd/MM/yyyy')}', 'Cash', '{balance}', 'Opening - {balance_type}'")
                

                db.conn.commit()
                QMessageBox.information(self, "Success", "Customer has been added")
                db.close()
                self.close()
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Customer has not been added {e}")
        else:
            QMessageBox.warning(self, "Error", "Fields cannot be empty")

    def Clear_Fields(self):
        self.txt_name.setText("")
        self.txt_phone.setText("")
        self.txt_vehicle.setText("")
        self.txt_address.setText("")
        self.txt_balance.setText("")

        

def main():
    app = QApplication(sys.argv)
    window = AddCustomerWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
