import datetime
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from cash_received import CashReceivedWindow
from db_handler import DBHandler
import sys
from os import path
from PyQt5.uic import loadUiType

FORM_MAIN, _ = loadUiType('ui/account_details.ui')


class AccountDetailsWindow(QMainWindow, FORM_MAIN):
    def __init__(self,user_id):
        
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.user_id = user_id
        self.update_account_details()
        self.btn_refresh.clicked.connect(self.update_account_details)
        self.Handle_Buttons()
        self.db= DBHandler()
        self.lbl_account_name.setText(self.db.select(table_name="customers",columns="name",condition="custmer_id="+str(self.user_id))[0][0])

    def Handle_Buttons(self):
        self.btn_cash_received.clicked.connect(self.openCashReceivedWindow)

    def openCashReceivedWindow(self):
        self.window = CashReceivedWindow(self.user_id)
        self.window.show()

    def update_account_details(self):
        db= DBHandler()
        # get sales record where customer id = self.customer_id
        data=db.select(table_name="customer_cash_received",columns="date,description,quantity,rate,amount,cash_paid,cash_received,remaining",condition="customer_id="+str(self.user_id))
        name=db.select(table_name="customers",columns="name",condition="custmer_id="+str(self.user_id))[0][0]

        # data = db.conn.execute(f"SELECT sales.date,customers.name,sales.quantity,sales.rate,sales.total_amount,sales.cash_paid,sales.cash_received,sales.sub_total FROM sales LEFT JOIN customers ON sales.customer_id=customers.custmer_id WHERE customers.custmer_id = {self.user_id}").fetchall()
        self.roznamcha_table.setRowCount(0)
        quantity=0
        amount=0
        cash_paid=0
        cash_received=0
        remaining=0
        opening=0
        for index,row in enumerate(data):
            quantity+=row[2]
            amount+=row[4]
            cash_paid+=row[5]
            cash_received+=row[6]
            if index==0:
                opening=row[7]
            elif index==len(data)-1:
                remaining=row[7]
            # sub_total+=row[7]
            self.roznamcha_table.insertRow(index)
            for idx,i in enumerate(row):
                self.roznamcha_table.setItem(index,idx,QTableWidgetItem(str(i)))
            # if row[1]=="Cash Received":
            self.roznamcha_table.item(index,6).setForeground(QColor(255,0,0))
    
        self.label_2.setText(str(quantity))
        self.label_6.setText(str(amount))
        self.txt_total_cash_paid.setText(str(cash_paid))
        self.txt_total_cash_received.setText(str(cash_received))
        self.txt_remaining.setText(str(remaining))
        self.label_4.setText(str(opening))

        # balace = db.conn.execute(f"SELECT balance FROM customers WHERE custmer_id = {self.user_id}").fetchone()[0]
        # self.label_4.setText(str(balace))


def main():
    app = QApplication(sys.argv)
    window = AccountDetailsWindow(1)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()


