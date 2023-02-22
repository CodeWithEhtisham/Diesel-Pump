
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

FORM_MAIN, _ = loadUiType('ui/add_sale.ui')


class SalesWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()
        self.update_sales()

    def Handle_Buttons(self):
        self.btn_sale.clicked.connect(self.add_sale)
        self.btn_sale_print.clicked.connect(self.add_sale_print)
        self.btn_clear.clicked.connect(self.clear_fields)
        self.btn_cancel.clicked.connect(self.close)
        self.txt_quantity.textChanged.connect(self.add_seprator)
        self.select_product.activated.connect(self.get_product_info)
        self.select_customer.activated.connect(self.get_customer_info)
        self.txt_sale_date.setDate(QDate.currentDate())

        self.txt_cash_paid.textChanged.connect(self.calculate_paid)
        self.txt_cash_received.textChanged.connect(self.calculate_recieved)
        # self.btn_save.clicked.connect(self.add_sale)
        self.txt_rate.textChanged.connect(self.calculate_total)


    def calculate_total(self):
        try:
            price= self.txt_rate.text()
            quantity= self.txt_quantity.text().replace(",","")
            if price and quantity:
                total= float(price)*float(quantity)
                self.txt_total_amount.setText(str(total))
        except Exception as e:
            QMessageBox.warning(self, 'Error', 'Please enter valid {}'.format(e))
            self.txt_total_amount.setText('')
            self.txt_rate.setFocus()
            return


    def calculate_paid(self):
        try:
            paid= self.txt_cash_paid.text().replace(",","")
            self.txt_cash_paid.setText("{:,}".format(int(paid.replace(",",""))))
            recieved= self.txt_total_amount.text().replace(",","")
            if paid and recieved:
                cash= float(recieved)+float(paid)
                self.lbl_sub_total.setText(str(cash))
        except Exception as e:
            QMessageBox.warning(self, 'Error', 'Please enter valid {}'.format(e))
            self.txt_cash_paid.setText('')
            self.txt_cash_paid.setFocus()
            return

    def calculate_recieved(self):
        try:
            paid= self.txt_cash_paid.text().replace(",","")
            c= self.txt_total_amount.text()
            total=float(paid)+float(c)
            recieved= self.txt_cash_received.text().replace(",","")
            self.txt_cash_received.setText("{:,}".format(int(recieved.replace(",",""))))
            if total and recieved:
                cash= float(total)-float(recieved)
                self.lbl_sub_total.setText(str(cash))
        except Exception as e:
            QMessageBox.warning(self, 'Error', 'Please enter valid {}'.format(e))
            self.txt_cash_received.setText('')
            self.txt_cash_received.setFocus()
            return

    

    def get_product_info(self):
        db= DBHandler()
        product_name= self.select_product.currentText()
        data,stock= db.select('products', 'product_id,product_stock', f"product_name='{product_name}'")[0]
        print(data,stock)
        if data:
            # get average price and sum of stock
            price=db.conn.execute("SELECT AVG(rate) FROM stock WHERE product_id=?",(data,)).fetchall()[0][0]
            # stock=db.conn.execute("SELECT product_stock from products WHERE product_id=?",(data,)).fetchall()[0]
            if price:
                self.txt_price.setText(str(price))
            else:
                self.txt_price.setText('0')
            if stock:
                self.txt_stock.setText(str(stock))
            else:
                self.txt_stock.setText('0')

    def get_customer_info(self):
        db= DBHandler()
        customer_name= self.select_customer.currentText()
        data= db.select('customers', '*', f"name='{customer_name}'")[0]
        if data:
            self.txt_name.setText(data[1])
            self.txt_vehicle.setText(data[3])
            self.txt_contact.setText(data[2])
            self.txt_balance.setText(str(data[-1]))

        
        

    def update_sales(self):
        db= DBHandler()
        data= db.select_all('products',"*")
        if data:
            for row in data:
                self.select_product.addItem(row[1])
        data= db.select_all("customers","name")
        print(data)
        if data:
            for row in data:
                self.select_customer.addItem(row[0])




    def add_seprator(self):
        try:
            quantity= self.txt_quantity.text()
            if quantity:
                # check quantity is gettting any alphabet
                if not float(quantity):
                    QMessageBox.warning(self, "Warning", "Please enter a valid number")
                    self.txt_quantity.setText('')
                    return
        except Exception as e:
            QMessageBox.warning(self, "Warning", "Please enter a valid number")
            self.txt_quantity.setText('')
            return
        #     quantity= self.txt_quantity.text()
        #     if quantity:
        #         # self.txt_quantity.setText("{:,}".format(int(quantity.replace(",",""))))
        #         self.txt_quantity.setText("{:,}".format(float(quantity.replace(",",""))))
        # except Exception as e:
        #     QMessageBox.warning(self, "Warning", "Please enter a valid number")
        #     self.txt_quantity.setText('')
        #     return
    
    def add_sale(self):
        db= DBHandler()
        product_name= self.select_product.currentText()
        product_id= db.select('products', 'product_id', f"product_name='{product_name}'")[0][0]
        customer_name= self.select_customer.currentText()
        customer_id= db.select('customers', 'custmer_id', f"name='{customer_name}'")[0][0]
        date= self.txt_sale_date.text()
        quantity= float(self.txt_quantity.text().replace(",",""))
        rate= float(self.txt_rate.text().replace(",",""))
        total_amount= float(self.txt_total_amount.text().replace(",",""))
        cash_paid= float(self.txt_cash_paid.text().replace(",",""))
        cash_received= float(self.txt_cash_received.text().replace(",",""))
        total_sub= float(self.lbl_sub_total.text().replace(",",""))

        available_stock= db.select('products', 'product_stock', f"product_id='{product_id}'")[0][0]
        if available_stock < quantity:
            QMessageBox.warning(self, "Warning", "Stock is not available")
            return

        if product_name != '' and customer_name != '' and date != '' and quantity != '' and rate != '' and total_amount != '' and cash_paid != '' and cash_received != '' and total_sub != '':
            db.conn.execute("UPDATE products SET product_stock=product_stock-? WHERE product_id=?",(quantity, product_id))
            db.conn.execute("INSERT INTO sales (product_id, customer_id, date, quantity, rate, total_amount, cash_paid, cash_received, sub_total) VALUES (?,?,?,?,?,?,?,?,?)",(product_id, customer_id, date, quantity, rate, total_amount, cash_paid, cash_received, total_sub))
            customer_remaining=float( db.select(table_name='customers', columns='balance', condition=f"custmer_id={customer_id}")[0][0])
            if customer_remaining>=0 and total_sub>=0:
                customer_remaining+=total_sub
            elif customer_remaining<0 and total_sub>=0:
                customer_remaining=customer_remaining+total_sub
            elif customer_remaining>=0 and total_sub<0:
                customer_remaining=customer_remaining+total_sub
            elif customer_remaining<0 and total_sub<0:
                customer_remaining=customer_remaining+total_sub

            db.conn.execute("UPDATE customers SET balance=? WHERE custmer_id=?",(customer_remaining, customer_id))
            db.conn.execute("INSERT INTO customer_cash_received (customer_id,date,description,quantity,rate,amount,cash_paid,cash_received,remaining) VALUES (?,?,?,?,?,?,?,?,?)",(customer_id, date, "Sale", quantity, rate, total_amount, cash_paid, cash_received, customer_remaining))

            db.conn.commit()
            QMessageBox.information(self, "Success", "Sale added successfully")
            db.close()
            self.close()
        else:
            QMessageBox.warning(self, "Warning", "Fields are empty")

    def clear_fields(self):
        self.select_product.setCurrentIndex(0)
        self.select_customer.setCurrentIndex(0)
        self.txt_sale_date.setDate(QDate.currentDate())
        self.txt_quantity.setText('')
        self.txt_rate.setText('')
        self.txt_total_amount.setText('00.00')
        self.txt_cash_paid.setText('')
        self.txt_cash_received.setText('')
        self.lbl_sub_total.setText('00.00')

    def add_sale_print(self):
        pass

def main():
    app = QApplication(sys.argv)
    window = SalesWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

