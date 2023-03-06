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
from cash_paid import CashPaidWindow
FORM_MAIN, _ = loadUiType('ui/supplier_account_details.ui')


class SupplierAccountDetailsWindow(QMainWindow, FORM_MAIN):
    def __init__(self,id):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.user_id=id
        self.btn_cash_paid.clicked.connect(self.cash_paids)
        self.btn_refresh.clicked.connect(self.fill_table)
        self.txt_search.textChanged.connect(self.search_table)
        self.btn_search.clicked.connect(self.search_table_date)
        self.txt_search_date.setDate(QDate.currentDate())
        self.fill_table()

        # self.Handle_Buttons()
    def search_table_date(self):
        self.txt_search_date.text()
        db=DBHandler()
        data=db.select(table_name="supplier_cash_paid",columns="date,description,quantity,rate,amount,cash_paid,remaining",condition="supplier_id="+str(self.user_id)+" and date like '%"+self.txt_search_date.text()+"%'")
        self.supplier_account_table.setRowCount(0)
        for row_number,row_data in enumerate(data):
            self.supplier_account_table.insertRow(row_number)
            for column_number,valuess in enumerate(row_data):
                self.supplier_account_table.setItem(row_number,column_number,QTableWidgetItem(str(valuess)))

    def search_table(self):
        description=self.txt_search.text()
        db=DBHandler()
        data=db.select(table_name="supplier_cash_paid",columns="date,description,quantity,rate,amount,cash_paid,remaining",condition="supplier_id="+str(self.user_id)+" and description like '%"+description+"%'")
        self.supplier_account_table.setRowCount(0)
        for row_number,row_data in enumerate(data):
            self.supplier_account_table.insertRow(row_number)
            for column_number,valuess in enumerate(row_data):
                self.supplier_account_table.setItem(row_number,column_number,QTableWidgetItem(str(valuess)))
        
    def fill_table(self):
        self.supplier_account_table.setRowCount(0)
        db=DBHandler()
        data=db.select(table_name="supplier_cash_paid",columns="date,description,quantity,rate,amount,cash_paid,remaining",condition="supplier_id="+str(self.user_id))
        name=db.select(table_name="suppliers",columns="name",condition="supplier_id="+str(self.user_id))[0][0]
        self.lbl_account_name.setText(name)
        quantity=0
        amount=0
        cash_paid=0
        remaining=0
        for row_number,row_data in enumerate(data):
            if row_number==0:
                opening=row_data[-1]
            elif row_number==len(data)-1:
                remaining=row_data[-1]
            quantity+=row_data[2]
            amount+=row_data[4]
            cash_paid+=row_data[5]
            # remaining+=row_data[6]

            self.supplier_account_table.insertRow(row_number)
            for column_number,valuess in enumerate(row_data):
                self.supplier_account_table.setItem(row_number,column_number,QTableWidgetItem(str(valuess)))
                # self.supplier_account_table.item(row_number,column_number).setForeground(QBrush(QColor(0, 255, 0)))
            self.supplier_account_table.item(row_number,5).setForeground(QColor(255,0,0))
        self.txt_total_cash_paid.setText(str(f"{cash_paid:,}"))
        self.txt_remaining.setText(str(f"{remaining:,}"))
        self.label_6.setText(str(f"{amount:,}"))
        self.label_2.setText(str(quantity))
        self.label_4.setText(str(f"{opening:,}"))

    def cash_paids(self):
        self.cash_paid_window=CashPaidWindow(self.user_id)
        self.cash_paid_window.show()
        self.cash_paid_window.btn_save.clicked.connect(self.fill_table)

        # self.cash_paid_window.exec_()
        # self.fill_table()

def main():
    app = QApplication(sys.argv)
    window = SupplierAccountDetailsWindow(0)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()





