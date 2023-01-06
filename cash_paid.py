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

FORM_MAIN, _ = loadUiType('ui/cash_paid.ui')

class CashPaidWindow(QMainWindow, FORM_MAIN):
    def __init__(self,id):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.user_id = id
        self.name,self.balance=DBHandler().select(table_name='suppliers',columns='name,balance',condition=f"supplier_id = {self.user_id}")[0]
        self.txt_name.setText(self.name)
        self.txt_previous.setText(str(self.balance))
        self.txt_amount.textChanged.connect(self.Calculate_Remaining)
        self.txt_date.setDate(QDate.currentDate())
        self.Handle_Buttons()

    def Calculate_Remaining(self):
        amount = self.txt_amount.text()
        previous = self.txt_previous.text()
        if amount == '' or previous == '':
            self.txt_remaining.setText('')
        else:
            try:
                if float(previous)>=0:
                    remaining = float(previous) + float(amount)
                else:
                    remaining = float(amount)+float(previous)
                self.txt_remaining.setText(str(round(remaining,2)))
            except Exception as e:
                print(f"Error: {e}")
                self.txt_remaining.setText('')

    def Handle_Buttons(self):

        self.btn_save.clicked.connect(self.Save)
        self.btn_clear.clicked.connect(self.Clear)
        self.btn_cancel.clicked.connect(self.close)

    def Save(self):
        name = self.txt_name.text()
        date = self.txt_date.text()
        payment_method = self.payment_method.currentText()
        amount = self.txt_amount.text()
        previous = self.txt_previous.text()
        remaining = self.txt_remaining.text()

        if name == '' or date == '' or payment_method == '' or amount == '' or previous == '' or remaining == '':
            QMessageBox.warning(self, 'Data Error', 'Please Fill All Fields')
        else:
            try:
                db=DBHandler()
                # drop  table if exists supplier_cash_paid;
                # db.conn.execute(f"DROP TABLE IF EXISTS supplier_cash_paid")
                # db.conn.execute(f"CREATE TABLE IF NOT EXISTS supplier_cash_paid (id INTEGER PRIMARY KEY AUTOINCREMENT,supplier_id INTEGER,date TEXT,payment_method TEXT,cash_paid REAL,remaining REAL,description TEXT DEFAULT 'Cash Received',quantity INTEGER DEFAULT 0,rate REAL DEFAULT 0,amount REAL DEFAULT 0,FOREIGN KEY(supplier_id) REFERENCES suppliers(supplier_id))")
                # db.conn.commit()
                

                db.conn.execute(f"INSERT INTO supplier_cash_paid (supplier_id,date,payment_method,cash_paid,remaining) VALUES ({self.user_id},'{date}','{payment_method}',{amount},{remaining})")
                db.conn.commit()
                db.conn.execute(
                    f"UPDATE suppliers SET balance = {remaining} WHERE supplier_id = {self.user_id}")
                db.conn.commit()
                QMessageBox.information(self, 'Success', 'Cash Paid Successfully')
                self.Clear()
            except Exception as e:
                QMessageBox.warning(self, 'Error', str(e))

    def Clear(self):
        self.txt_name.setText(self.name)
        self.txt_date.setDate(datetime.date.today())
        self.payment_method.setCurrentIndex(0)
        self.txt_amount.setText('')
        self.txt_previous.setText(str(self.balance))
        self.txt_remaining.setText('')


def main():
    app = QApplication(sys.argv)
    window = CashPaidWindow(1)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()





