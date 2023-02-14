
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

FORM_MAIN, _ = loadUiType('ui/update_roznamcha.ui')


class UpdateNamchaWindow(QMainWindow, FORM_MAIN):
    def __init__(self, id):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()
        self.db=DBHandler()
        self.id = id
        self.select_product.addItems([i[0] for i in self.db.select_all('products','product_name')])
        self.select_customer.addItems([i[0] for i in self.db.select_all('customers','name')])
        self.txt_date.setDate(QDate.currentDate())
        self.update()

    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.update_roznamcha)
        self.btn_delete.clicked.connect(self.delete_roznamcha)
        self.txt_rate.textChanged.connect(self.calculate_total_amount)
        # self.btn_cancel.clicked.connect(self.close)

    def update(self):
        data = self.db.select(
            table_name='roznamcha',
            columns="date,product_id,quantity,rate,total_amount,customer_id,cash_paid,cash_received,description",
            condition="roznamcha_id={}".format(self.id)
        )
        self.txt_date.setDate(data[0][0])
        self.select_product.setCurrentText(self.db.select(table_name='products',columns='product_name',condition="product_id={}".format(data[0][1]))[0][0])
        self.txt_quantity.setText(str(data[0][2]))
        self.txt_rate.setText(str(data[0][3]))
        self.txt_total_amount.setText(str(data[0][4]))
        self.select_customer.setCurrentText(self.db.select(table_name='customers',columns='name',condition="custmer_id={}".format(data[0][5]))[0][0])
        self.txt_cash_paid.setText(str(data[0][6]))
        self.txt_cash_received.setText(str(data[0][7]))
        self.txt_description.setText(data[0][8])





    def calculate_total_amount(self):
        quantity = int(self.txt_quantity.text())
        rate = int(self.txt_rate.text())
        total_amount = quantity * rate
        self.txt_total_amount.setText(str(total_amount))

    def get_product_id(self,db,product_name):
        return db.conn.execute("SELECT product_id FROM products WHERE product_name='{}'".format(product_name)).fetchone()[0]
    
    def get_customer_id(self,db,customer_name):
        return db.conn.execute("SELECT custmer_id FROM customers WHERE name='{}'".format(customer_name)).fetchone()[0]



    def calculate_paid(self,paid,recieved):
        if paid and recieved:
            cash= float(recieved)+float(paid)
            return cash

    def calculate_recieved(self,paid,total_amount,recieved):
        total=float(paid)+float(total_amount)
        if total and recieved:
            cash= float(total)-float(recieved)
            return cash

    def delete_roznamcha(self):
        try:
            confirm=QMessageBox.question(self, "Confirm Delete", "Are you sure you want to delete this expense?", QMessageBox.Yes | QMessageBox.No)
            if confirm == QMessageBox.Yes:
                self.db.conn.execute("DELETE FROM roznamcha WHERE roznamcha_id={}".format(self.id))
                self.db.conn.commit()
        
    
    def update_roznamcha(self):
        db=DBHandler()
        prodcut_id = self.get_product_id(db,self.select_product.currentText())
        customer_id = self.get_customer_id(db,self.select_customer.currentText())
        date = self.txt_date.text()
        quantity = float(self.txt_quantity.text())
        rate = float(self.txt_rate.text())
        total_amount = float(self.txt_total_amount.text())
        cash_paid = float(self.txt_cash_paid.text())
        cash_received = float(self.txt_cash_received.text())
        sub_total= (total_amount)+(cash_paid)-(cash_received)


        if prodcut_id != '' and customer_id != '' and date != '' and quantity != '' and rate != '' and total_amount != '' and cash_paid != '' and cash_received != '':
            db.conn.execute('INSERT INTO roznamcha (product_id, customer_id, date, quantity, rate, total_amount, cash_paid, cash_received) VALUES (?,?,?,?,?,?,?,?)',(prodcut_id,customer_id,date,quantity,rate,total_amount,cash_paid,cash_received))
            customer_remaining = float(db.conn.execute("SELECT balance FROM customers WHERE custmer_id='{}'".format(customer_id)).fetchone()[0])

            if customer_remaining>=0 and sub_total>=0:
                customer_remaining+=sub_total
            elif customer_remaining<0 and sub_total>=0:
                customer_remaining=customer_remaining+sub_total
            elif customer_remaining>=0 and sub_total<0:
                customer_remaining=customer_remaining+sub_total
            elif customer_remaining<0 and sub_total<0:
                customer_remaining=customer_remaining+sub_total

            db.conn.execute("UPDATE customers SET balance=? WHERE custmer_id=?",(customer_remaining,customer_id))
            db.conn.execute(f"INSERT INTO customer_cash_received (customer_id,date,description,quantity,rate,amount,cash_paid,cash_received,remaining) VALUES (?,?,?,?,?,?,?,?,?)",(customer_id,date,'roznamcha',quantity,rate,total_amount,cash_paid,cash_received,customer_remaining))
            db.conn.commit()
            QMessageBox.information(self,'Success','Roznamcha Added Successfully')
            db.close()
            self.close()
        else:
            QMessageBox.information(self,'Error','Please Fill All The Fields')



def main():
    app = QApplication(sys.argv)
    window = UpdateNamchaWindow(1)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()


