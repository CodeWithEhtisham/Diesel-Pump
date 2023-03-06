import datetime
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication

import sys
from os import path
from PyQt5.uic import loadUiType
from resources_rc import *
from db_handler import DBHandler
FORM_MAIN, _ = loadUiType('ui/add_stock.ui')


class AddStockWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()
        self.add_product()
        self.txt_date.setDate(datetime.date.today())

        # on rate change event
        self.txt_rate.textChanged.connect(self.calculate_amount)
        # self.txt_stock.textChanged.connect(self.add_seprator)
        self.txt_paid_amount.textChanged.connect(self.add_seprators)

    def add_seprators(self):
        try:
            paid= self.txt_paid_amount.text().replace(',', '')
            if paid != '':
                self.txt_paid_amount.setText("{:,}".format(int(paid)))
        except:
            QMessageBox.warning(self, 'Error', 'Paid amount must be integer')
            self.txt_paid_amount.setText('')
            self.txt_paid_amount.setFocus()
            return

    # def add_seprator(self):
    #     try:
    #         stock= self.txt_stock.text().replace(',', '')
    #         if stock != '':
    #             self.txt_stock.setText("{:,}".format(int(stock)))
    #     except:
    #         QMessageBox.warning(self, 'Error', 'Stock must be integer')
    #         self.txt_stock.setText('')
    #         self.txt_stock.setFocus()
    #         return

    def calculate_amount(self):
        rate= self.txt_rate.text()
        stock= self.txt_stock.text().replace(',', '')
        if rate and stock != '':
            try:
                rate= float(rate)
                stock= float(stock)
                amount= rate * stock
                self.txt_amount.setText(str(amount))
            except:
                QMessageBox.warning(self, 'Error', 'Rate and Stock must be integers')

    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.add_stock)
        self.btn_clear.clicked.connect(self.clear_fields)
        self.btn_cancel.clicked.connect(self.close)

    def get_product_id(self, product):
        db= DBHandler()
        data= db.select('products','product_id', f"product_name='{product}'")
        if data:
            return data[0][0]

    def get_supplier_id(self, supplier):
        db= DBHandler()
        data= db.select('suppliers', 'supplier_id', f"name='{supplier}'")
        if data:
            return data[0][0]

    def add_stock(self):
        db= DBHandler()
        product= self.select_product.currentText()
        date= self.txt_date.text()
        supplier= self.select_supplier.currentText()
        stock= float(self.txt_stock.text().replace(',', ''))
        rate= float(self.txt_rate.text())
        amount= float(self.txt_amount.text())
        paid_amount= int(self.txt_paid_amount.text().replace(',', ''))
        product_id= self.get_product_id(product)
        supplier_id= self.get_supplier_id(supplier)

        if product and date and supplier and stock and rate and amount and paid_amount != '':
            try:
                db= DBHandler()
                db.conn.execute("UPDATE products SET product_stock=product_stock+? WHERE product_id=?", (stock, product_id))
                db.conn.commit()
                db.insert('stock', f"product_id, date, supplier_id, stock, rate, amount, paid_amount", f"{product_id}, '{date}', {supplier_id}, {stock}, {rate}, {amount}, {paid_amount}")
                # db.conn.execute("UPDATE products SET stock=stock+? WHERE product_id=?", (stock, product_id))
                remaining_amount= db.select('supplier_cash_paid', 'remaining', f"supplier_id={supplier_id}")[-1][0]
                if remaining_amount>=0:
                    remaining_amount=-((float(amount)-float(paid_amount))-float(remaining_amount))
                else:
                    remaining_amount= -(float(amount)+abs(float(remaining_amount))-float(paid_amount))
                    # remaining_amount= float(amount)-float(paid_amount)+float(abs(remaining_amount))
                db.conn.execute("UPDATE suppliers SET balance=? WHERE supplier_id=?", (remaining_amount, supplier_id))
                db.conn.execute(f"INSERT into supplier_cash_paid (supplier_id, date, payment_method,cash_paid,remaining,description,quantity,rate,amount) values ({supplier_id},'{date}','Cash',{paid_amount},{remaining_amount},'Stock Purchase',{stock},{rate},{amount})")
                db.conn.commit()
                QMessageBox.information(self, 'Success', 'Stock added successfully')
                self.close()
            except Exception as e:
                QMessageBox.warning(self, 'Error', f'Stock not added {e}')
        else:
            QMessageBox.warning(self, 'Error', 'All fields are required')

    def add_product(self):
        db= DBHandler()
        data = db.select_all(table_name='products', columns='product_name')
        if data:
            self.select_product.addItems([row[0] for row in data])

        data = db.select_all(table_name='suppliers', columns='name')
        if data:
            self.select_supplier.addItems([row[0] for row in data])


    def clear_fields(self):
        self.add_product()
        self.txt_date.setDate(datetime.date.today())
        self.select_supplier.setCurrentIndex(0)
        self.txt_stock.setText('')
        self.txt_rate.setText('')
        self.txt_amount.setText('')
        self.txt_paid_amount.setText('')

        

def main():
    app = QApplication(sys.argv)
    window = AddStockWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

