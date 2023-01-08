
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

FORM_MAIN, _ = loadUiType('ui/add_sale.ui')


class SalesWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()
        self.update_sales()

        self.select_product.activated.connect(self.get_product_info)
        self.select_customer.activated.connect(self.get_customer_info)
        self.txt_sale_date.setDate(QDate.currentDate())

        self.txt_cash_paid.textChanged.connect(self.calculate_paid)
        self.txt_cash_received.textChanged.connect(self.calculate_recieved)
        # self.btn_save.clicked.connect(self.add_sale)
        self.txt_rate.textChanged.connect(self.calculate_total)


    def calculate_total(self):
        price= self.txt_rate.text()
        quantity= self.txt_quantity.text()
        if price and quantity:
            total= float(price)*float(quantity)
            self.txt_total_amount.setText(str(total))

    def calculate_paid(self):
        paid= self.txt_cash_paid.text()
        recieved= self.txt_total_amount.text()
        if paid and recieved:
            cash= float(recieved)+float(paid)
            self.lbl_sub_total.setText(str(cash))

    def calculate_recieved(self):
        paid= self.txt_cash_paid.text()
        c= self.txt_total_amount.text()
        total=float(paid)+float(c)
        recieved= self.txt_cash_received.text()
        if total and recieved:
            cash= float(total)-float(recieved)
            self.lbl_sub_total.setText(str(cash))

    

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


    def Handle_Buttons(self):
        self.btn_sale.clicked.connect(self.add_sale)
        self.btn_sale_print.clicked.connect(self.add_sale_print)
        self.btn_clear.clicked.connect(self.clear_fields)
        self.btn_cancel.clicked.connect(self.close)

    def add_sale(self):
        db= DBHandler()
        product_name= self.select_product.currentText()
        product_id= db.select('products', 'product_id', f"product_name='{product_name}'")[0][0]
        customer_name= self.select_customer.currentText()
        customer_id= db.select('customers', 'custmer_id', f"name='{customer_name}'")[0][0]
        date= self.txt_sale_date.text()
        quantity= int(self.txt_quantity.text())
        print(quantity)
        rate= int(self.txt_rate.text())
        total_amount= float(self.txt_total_amount.text())
        cash_paid= float(self.txt_cash_paid.text())
        cash_received= float(self.txt_cash_received.text())
        total_sub= float(self.lbl_sub_total.text())

        # stock= db.select('stock', 'stock,stock_id', f"product_id='{product_id}'")
        # if stock:
        #     q=quantity
        #     if sum([i[0] for i in stock]) > q:
        #         for i in stock:
        #             print(f"stock: {i[0]}")
        #             print(f"q: {q}")
        #             if i[0] > q:
        #                 # update stock with respect to index
        #                 db.conn.execute("UPDATE stock SET stock=? WHERE stock_id=?",(i[0]-q, i[1]))
        #                 db.conn.commit()
        #                 break

        #             else:
        #                 q-=i[0]
        #                 db.conn.execute("UPDATE stock SET stock=? WHERE stock_id=?",(0, i[1]))
        #                 db.conn.commit()

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

# from PyQt5 import QtCore, QtGui, QtWidgets
# from PySide2 import *
# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *


# class Ui_SalesWindow(object):
#     def setupUi(self, SalesWindow):
#         SalesWindow.setObjectName("SalesWindow")
#         SalesWindow.resize(1080, 720)
#         SalesWindow.setMinimumSize(QtCore.QSize(1080, 720))
#         SalesWindow.setMaximumSize(QtCore.QSize(1080, 720))
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap(":/icons/assets/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         SalesWindow.setWindowIcon(icon)
#         SalesWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
#         self.centralwidget = QtWidgets.QWidget(SalesWindow)
#         self.centralwidget.setStyleSheet("* {\n"
# "    background-color: #e3f2fd;\n"
# "}\n"
# "\n"
# "#lbl_sales {\n"
# "    background-color: #81d4fa;\n"
# "    color: #fff;\n"
# "}\n"
# "\n"
# "QComboBox {\n"
# "    background-color: white;\n"
# "    border-radius: 5px;\n"
# "    padding: 2px;\n"
# "    border: 1px solid  #81d4fa;\n"
# "}\n"
# "\n"
# "QLineEdit {\n"
# "    background-color: white;\n"
# "    border-radius: 5px;\n"
# "    border: 1px solid  #81d4fa;\n"
# "}\n"
# "\n"
# "QDateEdit {\n"
# "    background-color: white;\n"
# "    border-radius: 5px;\n"
# "    border: 1px solid  #81d4fa;\n"
# "}\n"
# "\n"
# "#txt_name {\n"
# "    color: #01579b;\n"
# "}\n"
# "\n"
# "#txt_stock {\n"
# "    color: #01579b;\n"
# "}\n"
# "\n"
# "#btn_sale {\n"
# "    background-color: #009688;\n"
# "    color: white;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#btn_sale_print {\n"
# "    background-color: #03a9f4;\n"
# "    color: white;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#btn_clear {\n"
# "    background-color: #b0bec5;\n"
# "    color: white;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#btn_cancel {\n"
# "    background-color: #90a4ae;\n"
# "    color: white;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#bottom_widget {\n"
# "    background-color: #b3e5fc;\n"
# "}\n"
# "\n"
# "#lbl_sale {\n"
# "    background-color: #80deea;\n"
# "}\n"
# "\n"
# "#lbl_payment {\n"
# "    background-color: #80deea;\n"
# "}\n"
# "\n"
# "#lbl_product {\n"
# "    background-color: #81d4fa;\n"
# "}\n"
# "\n"
# "#lbl_customer {\n"
# "    background-color: #81d4fa;\n"
# "}")
#         self.centralwidget.setObjectName("centralwidget")
#         self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.centralwidget)
#         self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_11.setSpacing(60)
#         self.verticalLayout_11.setObjectName("verticalLayout_11")
#         self.lbl_sales = QtWidgets.QLabel(self.centralwidget)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(22)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_sales.setFont(font)
#         self.lbl_sales.setAlignment(QtCore.Qt.AlignCenter)
#         self.lbl_sales.setObjectName("lbl_sales")
#         self.verticalLayout_11.addWidget(self.lbl_sales)
#         self.main_widget = QtWidgets.QWidget(self.centralwidget)
#         self.main_widget.setObjectName("main_widget")
#         self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.main_widget)
#         self.horizontalLayout_6.setContentsMargins(1, 1, 1, 1)
#         self.horizontalLayout_6.setSpacing(150)
#         self.horizontalLayout_6.setObjectName("horizontalLayout_6")
#         self.left_widget = QtWidgets.QWidget(self.main_widget)
#         self.left_widget.setObjectName("left_widget")
#         self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.left_widget)
#         self.verticalLayout_5.setContentsMargins(1, 1, 1, 1)
#         self.verticalLayout_5.setSpacing(10)
#         self.verticalLayout_5.setObjectName("verticalLayout_5")
#         self.lbl_product = QtWidgets.QLabel(self.left_widget)
#         self.lbl_product.setMinimumSize(QtCore.QSize(0, 40))
#         self.lbl_product.setMaximumSize(QtCore.QSize(16777215, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(18)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_product.setFont(font)
#         self.lbl_product.setAlignment(QtCore.Qt.AlignCenter)
#         self.lbl_product.setObjectName("lbl_product")
#         self.verticalLayout_5.addWidget(self.lbl_product)
#         self.product_frame = QtWidgets.QFrame(self.left_widget)
#         self.product_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.product_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.product_frame.setObjectName("product_frame")
#         self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.product_frame)
#         self.horizontalLayout_3.setContentsMargins(1, 1, 1, 1)
#         self.horizontalLayout_3.setSpacing(10)
#         self.horizontalLayout_3.setObjectName("horizontalLayout_3")
#         self.product_lbl_frame = QtWidgets.QFrame(self.product_frame)
#         self.product_lbl_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.product_lbl_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.product_lbl_frame.setObjectName("product_lbl_frame")
#         self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.product_lbl_frame)
#         self.verticalLayout_4.setObjectName("verticalLayout_4")
#         self.lbl_product_name = QtWidgets.QLabel(self.product_lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_product_name.setFont(font)
#         self.lbl_product_name.setObjectName("lbl_product_name")
#         self.verticalLayout_4.addWidget(self.lbl_product_name)
#         self.lbl_product_stock = QtWidgets.QLabel(self.product_lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_product_stock.setFont(font)
#         self.lbl_product_stock.setObjectName("lbl_product_stock")
#         self.verticalLayout_4.addWidget(self.lbl_product_stock)
#         self.lbl_product_price = QtWidgets.QLabel(self.product_lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_product_price.setFont(font)
#         self.lbl_product_price.setObjectName("lbl_product_price")
#         self.verticalLayout_4.addWidget(self.lbl_product_price)
#         self.horizontalLayout_3.addWidget(self.product_lbl_frame)
#         self.product_details_frame = QtWidgets.QFrame(self.product_frame)
#         self.product_details_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.product_details_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.product_details_frame.setObjectName("product_details_frame")
#         self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.product_details_frame)
#         self.verticalLayout_3.setObjectName("verticalLayout_3")
#         self.select_product = QtWidgets.QComboBox(self.product_details_frame)
#         self.select_product.setMinimumSize(QtCore.QSize(200, 35))
#         self.select_product.setMaximumSize(QtCore.QSize(200, 35))
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.select_product.setFont(font)
#         self.select_product.setToolTip("")
#         self.select_product.setToolTipDuration(0)
#         self.select_product.setEditable(True)
#         self.select_product.setObjectName("select_product")
#         self.verticalLayout_3.addWidget(self.select_product)
#         self.txt_stock = QtWidgets.QLabel(self.product_details_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_stock.setFont(font)
#         self.txt_stock.setObjectName("txt_stock")
#         self.verticalLayout_3.addWidget(self.txt_stock, 0, QtCore.Qt.AlignRight)
#         self.txt_price = QtWidgets.QLabel(self.product_details_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_price.setFont(font)
#         self.txt_price.setObjectName("txt_price")
#         self.verticalLayout_3.addWidget(self.txt_price, 0, QtCore.Qt.AlignRight)
#         self.horizontalLayout_3.addWidget(self.product_details_frame)
#         self.verticalLayout_5.addWidget(self.product_frame)
#         self.lbl_customer = QtWidgets.QLabel(self.left_widget)
#         self.lbl_customer.setMinimumSize(QtCore.QSize(0, 40))
#         self.lbl_customer.setMaximumSize(QtCore.QSize(16777215, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(18)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_customer.setFont(font)
#         self.lbl_customer.setAlignment(QtCore.Qt.AlignCenter)
#         self.lbl_customer.setObjectName("lbl_customer")
#         self.verticalLayout_5.addWidget(self.lbl_customer)
#         self.customer_frame = QtWidgets.QFrame(self.left_widget)
#         self.customer_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.customer_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.customer_frame.setObjectName("customer_frame")
#         self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.customer_frame)
#         self.horizontalLayout_2.setContentsMargins(1, 1, 1, 1)
#         self.horizontalLayout_2.setSpacing(10)
#         self.horizontalLayout_2.setObjectName("horizontalLayout_2")
#         self.cust_lbl_frame = QtWidgets.QFrame(self.customer_frame)
#         self.cust_lbl_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.cust_lbl_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.cust_lbl_frame.setObjectName("cust_lbl_frame")
#         self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.cust_lbl_frame)
#         self.verticalLayout_2.setObjectName("verticalLayout_2")
#         self.lbl_name = QtWidgets.QLabel(self.cust_lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_name.setFont(font)
#         self.lbl_name.setObjectName("lbl_name")
#         self.verticalLayout_2.addWidget(self.lbl_name)
#         self.lbl_vehicle = QtWidgets.QLabel(self.cust_lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_vehicle.setFont(font)
#         self.lbl_vehicle.setObjectName("lbl_vehicle")
#         self.verticalLayout_2.addWidget(self.lbl_vehicle)
#         self.lbl_contact = QtWidgets.QLabel(self.cust_lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_contact.setFont(font)
#         self.lbl_contact.setObjectName("lbl_contact")
#         self.verticalLayout_2.addWidget(self.lbl_contact)
#         self.lbl_balance = QtWidgets.QLabel(self.cust_lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_balance.setFont(font)
#         self.lbl_balance.setObjectName("lbl_balance")
#         self.verticalLayout_2.addWidget(self.lbl_balance)
#         self.horizontalLayout_2.addWidget(self.cust_lbl_frame)
#         self.cust_details_frame = QtWidgets.QFrame(self.customer_frame)
#         self.cust_details_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.cust_details_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.cust_details_frame.setObjectName("cust_details_frame")
#         self.verticalLayout = QtWidgets.QVBoxLayout(self.cust_details_frame)
#         self.verticalLayout.setObjectName("verticalLayout")
#         self.txt_name = QtWidgets.QLabel(self.cust_details_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_name.setFont(font)
#         self.txt_name.setObjectName("txt_name")
#         self.verticalLayout.addWidget(self.txt_name)
#         self.txt_vehicle = QtWidgets.QLabel(self.cust_details_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_vehicle.setFont(font)
#         self.txt_vehicle.setObjectName("txt_vehicle")
#         self.verticalLayout.addWidget(self.txt_vehicle)
#         self.txt_contact = QtWidgets.QLabel(self.cust_details_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_contact.setFont(font)
#         self.txt_contact.setObjectName("txt_contact")
#         self.verticalLayout.addWidget(self.txt_contact)
#         self.txt_balance = QtWidgets.QLabel(self.cust_details_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_balance.setFont(font)
#         self.txt_balance.setObjectName("txt_balance")
#         self.verticalLayout.addWidget(self.txt_balance)
#         self.horizontalLayout_2.addWidget(self.cust_details_frame)
#         self.verticalLayout_5.addWidget(self.customer_frame)
#         self.horizontalLayout_6.addWidget(self.left_widget)
#         self.right_widget = QtWidgets.QWidget(self.main_widget)
#         self.right_widget.setObjectName("right_widget")
#         self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.right_widget)
#         self.verticalLayout_10.setContentsMargins(1, 1, 1, 1)
#         self.verticalLayout_10.setSpacing(10)
#         self.verticalLayout_10.setObjectName("verticalLayout_10")
#         self.lbl_sale = QtWidgets.QLabel(self.right_widget)
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(18)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_sale.setFont(font)
#         self.lbl_sale.setAlignment(QtCore.Qt.AlignCenter)
#         self.lbl_sale.setObjectName("lbl_sale")
#         self.verticalLayout_10.addWidget(self.lbl_sale)
#         self.sale_frame = QtWidgets.QFrame(self.right_widget)
#         self.sale_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.sale_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.sale_frame.setObjectName("sale_frame")
#         self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.sale_frame)
#         self.horizontalLayout_5.setContentsMargins(1, 1, -1, -1)
#         self.horizontalLayout_5.setObjectName("horizontalLayout_5")
#         self.sale_lbl_frame = QtWidgets.QFrame(self.sale_frame)
#         self.sale_lbl_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.sale_lbl_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.sale_lbl_frame.setObjectName("sale_lbl_frame")
#         self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.sale_lbl_frame)
#         self.verticalLayout_9.setSpacing(10)
#         self.verticalLayout_9.setObjectName("verticalLayout_9")
#         self.lbl_sale_date = QtWidgets.QLabel(self.sale_lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_sale_date.setFont(font)
#         self.lbl_sale_date.setObjectName("lbl_sale_date")
#         self.verticalLayout_9.addWidget(self.lbl_sale_date, 0, QtCore.Qt.AlignRight)
#         self.lbl_quantity = QtWidgets.QLabel(self.sale_lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_quantity.setFont(font)
#         self.lbl_quantity.setObjectName("lbl_quantity")
#         self.verticalLayout_9.addWidget(self.lbl_quantity, 0, QtCore.Qt.AlignRight)
#         self.lbl_rate = QtWidgets.QLabel(self.sale_lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_rate.setFont(font)
#         self.lbl_rate.setObjectName("lbl_rate")
#         self.verticalLayout_9.addWidget(self.lbl_rate, 0, QtCore.Qt.AlignRight)
#         self.lbl_customer_name = QtWidgets.QLabel(self.sale_lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_customer_name.setFont(font)
#         self.lbl_customer_name.setObjectName("lbl_customer_name")
#         self.verticalLayout_9.addWidget(self.lbl_customer_name, 0, QtCore.Qt.AlignRight)
#         self.horizontalLayout_5.addWidget(self.sale_lbl_frame)
#         self.sale_details_frame = QtWidgets.QFrame(self.sale_frame)
#         self.sale_details_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.sale_details_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.sale_details_frame.setObjectName("sale_details_frame")
#         self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.sale_details_frame)
#         self.verticalLayout_8.setSpacing(10)
#         self.verticalLayout_8.setObjectName("verticalLayout_8")
#         self.txt_sale_date = QtWidgets.QDateEdit(self.sale_details_frame)
#         self.txt_sale_date.setMinimumSize(QtCore.QSize(250, 35))
#         self.txt_sale_date.setMaximumSize(QtCore.QSize(250, 35))
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_sale_date.setFont(font)
#         self.txt_sale_date.setCalendarPopup(True)
#         self.txt_sale_date.setObjectName("txt_sale_date")
#         self.verticalLayout_8.addWidget(self.txt_sale_date, 0, QtCore.Qt.AlignRight)
#         self.txt_quantity = QtWidgets.QLineEdit(self.sale_details_frame)
#         self.txt_quantity.setMinimumSize(QtCore.QSize(250, 35))
#         self.txt_quantity.setMaximumSize(QtCore.QSize(250, 35))
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_quantity.setFont(font)
#         self.txt_quantity.setText("")
#         self.txt_quantity.setObjectName("txt_quantity")
#         self.verticalLayout_8.addWidget(self.txt_quantity, 0, QtCore.Qt.AlignRight)
#         self.txt_rate = QtWidgets.QLineEdit(self.sale_details_frame)
#         self.txt_rate.setMinimumSize(QtCore.QSize(250, 35))
#         self.txt_rate.setMaximumSize(QtCore.QSize(250, 35))
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_rate.setFont(font)
#         self.txt_rate.setObjectName("txt_rate")
#         self.verticalLayout_8.addWidget(self.txt_rate, 0, QtCore.Qt.AlignRight)
#         self.select_customer = QtWidgets.QComboBox(self.sale_details_frame)
#         self.select_customer.setMinimumSize(QtCore.QSize(250, 35))
#         self.select_customer.setMaximumSize(QtCore.QSize(250, 35))
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.select_customer.setFont(font)
#         self.select_customer.setEditable(True)
#         self.select_customer.setObjectName("select_customer")
#         self.verticalLayout_8.addWidget(self.select_customer, 0, QtCore.Qt.AlignRight)
#         self.horizontalLayout_5.addWidget(self.sale_details_frame)
#         self.verticalLayout_10.addWidget(self.sale_frame)
#         self.lbl_payment = QtWidgets.QLabel(self.right_widget)
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(18)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_payment.setFont(font)
#         self.lbl_payment.setAlignment(QtCore.Qt.AlignCenter)
#         self.lbl_payment.setObjectName("lbl_payment")
#         self.verticalLayout_10.addWidget(self.lbl_payment)
#         self.payment_frame = QtWidgets.QFrame(self.right_widget)
#         self.payment_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.payment_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.payment_frame.setObjectName("payment_frame")
#         self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.payment_frame)
#         self.horizontalLayout_4.setContentsMargins(1, 1, 1, 1)
#         self.horizontalLayout_4.setSpacing(10)
#         self.horizontalLayout_4.setObjectName("horizontalLayout_4")
#         self.payment_lbl_frame = QtWidgets.QFrame(self.payment_frame)
#         self.payment_lbl_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.payment_lbl_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.payment_lbl_frame.setObjectName("payment_lbl_frame")
#         self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.payment_lbl_frame)
#         self.verticalLayout_7.setSpacing(20)
#         self.verticalLayout_7.setObjectName("verticalLayout_7")
#         self.lbl_total_amount = QtWidgets.QLabel(self.payment_lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_total_amount.setFont(font)
#         self.lbl_total_amount.setObjectName("lbl_total_amount")
#         self.verticalLayout_7.addWidget(self.lbl_total_amount, 0, QtCore.Qt.AlignRight)
#         self.lbl_cash_paid = QtWidgets.QLabel(self.payment_lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_cash_paid.setFont(font)
#         self.lbl_cash_paid.setObjectName("lbl_cash_paid")
#         self.verticalLayout_7.addWidget(self.lbl_cash_paid, 0, QtCore.Qt.AlignRight)
#         self.lbl_cash_received = QtWidgets.QLabel(self.payment_lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_cash_received.setFont(font)
#         self.lbl_cash_received.setObjectName("lbl_cash_received")
#         self.verticalLayout_7.addWidget(self.lbl_cash_received, 0, QtCore.Qt.AlignRight)
#         self.lbl_sub_total_2 = QtWidgets.QLabel(self.payment_lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_sub_total_2.setFont(font)
#         self.lbl_sub_total_2.setObjectName("lbl_sub_total_2")
#         self.verticalLayout_7.addWidget(self.lbl_sub_total_2, 0, QtCore.Qt.AlignRight)
#         self.horizontalLayout_4.addWidget(self.payment_lbl_frame)
#         self.payment_details_frame = QtWidgets.QFrame(self.payment_frame)
#         self.payment_details_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.payment_details_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.payment_details_frame.setObjectName("payment_details_frame")
#         self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.payment_details_frame)
#         self.verticalLayout_6.setSpacing(20)
#         self.verticalLayout_6.setObjectName("verticalLayout_6")
#         self.txt_total_amount = QtWidgets.QLabel(self.payment_details_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_total_amount.setFont(font)
#         self.txt_total_amount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
#         self.txt_total_amount.setObjectName("txt_total_amount")
#         self.verticalLayout_6.addWidget(self.txt_total_amount, 0, QtCore.Qt.AlignRight)
#         self.txt_cash_paid = QtWidgets.QLineEdit(self.payment_details_frame)
#         self.txt_cash_paid.setMinimumSize(QtCore.QSize(250, 35))
#         self.txt_cash_paid.setMaximumSize(QtCore.QSize(250, 35))
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_cash_paid.setFont(font)
#         self.txt_cash_paid.setWhatsThis("")
#         self.txt_cash_paid.setLayoutDirection(QtCore.Qt.RightToLeft)
#         self.txt_cash_paid.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
#         self.txt_cash_paid.setObjectName("txt_cash_paid")
#         self.verticalLayout_6.addWidget(self.txt_cash_paid, 0, QtCore.Qt.AlignRight)
#         self.txt_cash_received = QtWidgets.QLineEdit(self.payment_details_frame)
#         self.txt_cash_received.setMinimumSize(QtCore.QSize(250, 35))
#         self.txt_cash_received.setMaximumSize(QtCore.QSize(250, 35))
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_cash_received.setFont(font)
#         self.txt_cash_received.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
#         self.txt_cash_received.setClearButtonEnabled(False)
#         self.txt_cash_received.setObjectName("txt_cash_received")
#         self.verticalLayout_6.addWidget(self.txt_cash_received, 0, QtCore.Qt.AlignRight)
#         self.lbl_sub_total = QtWidgets.QLabel(self.payment_details_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_sub_total.setFont(font)
#         self.lbl_sub_total.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
#         self.lbl_sub_total.setObjectName("lbl_sub_total")
#         self.verticalLayout_6.addWidget(self.lbl_sub_total, 0, QtCore.Qt.AlignRight)
#         self.horizontalLayout_4.addWidget(self.payment_details_frame)
#         self.verticalLayout_10.addWidget(self.payment_frame)
#         self.horizontalLayout_6.addWidget(self.right_widget)
#         self.verticalLayout_11.addWidget(self.main_widget)
#         self.bottom_widget = QtWidgets.QWidget(self.centralwidget)
#         self.bottom_widget.setLayoutDirection(QtCore.Qt.LeftToRight)
#         self.bottom_widget.setObjectName("bottom_widget")
#         self.horizontalLayout = QtWidgets.QHBoxLayout(self.bottom_widget)
#         self.horizontalLayout.setContentsMargins(30, -1, 30, -1)
#         self.horizontalLayout.setSpacing(50)
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         self.btn_cancel = QtWidgets.QPushButton(self.bottom_widget)
#         self.btn_cancel.setMinimumSize(QtCore.QSize(120, 40))
#         self.btn_cancel.setMaximumSize(QtCore.QSize(120, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_cancel.setFont(font)
#         self.btn_cancel.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         icon1 = QtGui.QIcon()
#         icon1.addPixmap(QtGui.QPixmap(":/icons/assets/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_cancel.setIcon(icon1)
#         self.btn_cancel.setIconSize(QtCore.QSize(32, 32))
#         self.btn_cancel.setObjectName("btn_cancel")
#         self.horizontalLayout.addWidget(self.btn_cancel, 0, QtCore.Qt.AlignLeft)
#         self.btn_clear = QtWidgets.QPushButton(self.bottom_widget)
#         self.btn_clear.setMinimumSize(QtCore.QSize(120, 40))
#         self.btn_clear.setMaximumSize(QtCore.QSize(120, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_clear.setFont(font)
#         self.btn_clear.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         icon2 = QtGui.QIcon()
#         icon2.addPixmap(QtGui.QPixmap(":/icons/assets/icons/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_clear.setIcon(icon2)
#         self.btn_clear.setIconSize(QtCore.QSize(32, 32))
#         self.btn_clear.setObjectName("btn_clear")
#         self.horizontalLayout.addWidget(self.btn_clear, 0, QtCore.Qt.AlignLeft)
#         self.btn_sale_print = QtWidgets.QPushButton(self.bottom_widget)
#         self.btn_sale_print.setMinimumSize(QtCore.QSize(200, 40))
#         self.btn_sale_print.setMaximumSize(QtCore.QSize(200, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_sale_print.setFont(font)
#         self.btn_sale_print.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         icon3 = QtGui.QIcon()
#         icon3.addPixmap(QtGui.QPixmap(":/icons/assets/icons/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_sale_print.setIcon(icon3)
#         self.btn_sale_print.setIconSize(QtCore.QSize(32, 32))
#         self.btn_sale_print.setObjectName("btn_sale_print")
#         self.horizontalLayout.addWidget(self.btn_sale_print, 0, QtCore.Qt.AlignRight)
#         self.btn_sale = QtWidgets.QPushButton(self.bottom_widget)
#         self.btn_sale.setMinimumSize(QtCore.QSize(120, 40))
#         self.btn_sale.setMaximumSize(QtCore.QSize(120, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_sale.setFont(font)
#         self.btn_sale.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         icon4 = QtGui.QIcon()
#         icon4.addPixmap(QtGui.QPixmap(":/icons/assets/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_sale.setIcon(icon4)
#         self.btn_sale.setIconSize(QtCore.QSize(32, 32))
#         self.btn_sale.setObjectName("btn_sale")
#         self.horizontalLayout.addWidget(self.btn_sale, 0, QtCore.Qt.AlignRight)
#         self.verticalLayout_11.addWidget(self.bottom_widget)
#         SalesWindow.setCentralWidget(self.centralwidget)
#         self.statusbar = QtWidgets.QStatusBar(SalesWindow)
#         self.statusbar.setObjectName("statusbar")
#         SalesWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(SalesWindow)
#         QtCore.QMetaObject.connectSlotsByName(SalesWindow)

#     def retranslateUi(self, SalesWindow):
#         _translate = QtCore.QCoreApplication.translate
#         SalesWindow.setWindowTitle(_translate("SalesWindow", "Sales Terminal"))
#         self.lbl_sales.setText(_translate("SalesWindow", "Sales Terminal"))
#         self.lbl_product.setText(_translate("SalesWindow", "Product"))
#         self.lbl_product_name.setText(_translate("SalesWindow", "Select Product"))
#         self.lbl_product_stock.setText(_translate("SalesWindow", "Product Stock"))
#         self.lbl_product_price.setText(_translate("SalesWindow", "Product Price"))
#         self.txt_stock.setText(_translate("SalesWindow", "56514"))
#         self.txt_price.setText(_translate("SalesWindow", "1546"))
#         self.lbl_customer.setText(_translate("SalesWindow", "Customer"))
#         self.lbl_name.setText(_translate("SalesWindow", "Customer Name"))
#         self.lbl_vehicle.setText(_translate("SalesWindow", "Vehicle No."))
#         self.lbl_contact.setText(_translate("SalesWindow", "Contact No."))
#         self.lbl_balance.setText(_translate("SalesWindow", "Balance"))
#         self.txt_name.setText(_translate("SalesWindow", "Walking-Customer"))
#         self.txt_vehicle.setText(_translate("SalesWindow", "AB01"))
#         self.txt_contact.setText(_translate("SalesWindow", "0000 0000000"))
#         self.txt_balance.setText(_translate("SalesWindow", "0000"))
#         self.lbl_sale.setText(_translate("SalesWindow", "Sale"))
#         self.lbl_sale_date.setText(_translate("SalesWindow", "Sale Date"))
#         self.lbl_quantity.setText(_translate("SalesWindow", "Quantity"))
#         self.lbl_rate.setText(_translate("SalesWindow", "Rate"))
#         self.lbl_customer_name.setText(_translate("SalesWindow", "Customer"))
#         self.lbl_payment.setText(_translate("SalesWindow", "Payment"))
#         self.lbl_total_amount.setText(_translate("SalesWindow", "Total Amount"))
#         self.lbl_cash_paid.setText(_translate("SalesWindow", "Cash Paid"))
#         self.lbl_cash_received.setText(_translate("SalesWindow", "Cash Received"))
#         self.lbl_sub_total_2.setText(_translate("SalesWindow", "Sub Total Amount"))
#         self.txt_total_amount.setText(_translate("SalesWindow", "00"))
#         self.lbl_sub_total.setText(_translate("SalesWindow", "00"))
#         self.btn_cancel.setText(_translate("SalesWindow", "CANCEL"))
#         self.btn_clear.setText(_translate("SalesWindow", "CLEAR"))
#         self.btn_sale_print.setText(_translate("SalesWindow", "SALE and PRINT"))
#         self.btn_sale.setText(_translate("SalesWindow", "SALE"))
# import resources_rc


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     SalesWindow = QtWidgets.QMainWindow()
#     ui = Ui_SalesWindow()
#     ui.setupUi(SalesWindow)
#     SalesWindow.show()
#     sys.exit(app.exec_())
