
import datetime
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore
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
        self.txt_stock.textChanged.connect(self.add_seprator)
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

    def add_seprator(self):
        try:
            stock= self.txt_stock.text().replace(',', '')
            if stock != '':
                self.txt_stock.setText("{:,}".format(int(stock)))
        except:
            QMessageBox.warning(self, 'Error', 'Stock must be integer')
            self.txt_stock.setText('')
            self.txt_stock.setFocus()
            return

    def calculate_amount(self):
        rate= self.txt_rate.text()
        stock= self.txt_stock.text().replace(',', '')
        if rate and stock != '':
            try:
                rate= float(rate)
                stock= int(stock)
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
        stock= int(self.txt_stock.text().replace(',', ''))
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

# from PyQt5 import QtCore, QtGui, QtWidgets
# from PySide2 import *
# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *

# class Ui_AddStockWindow(object):
#     def setupUi(self, AddStockWindow):
#         AddStockWindow.setObjectName("AddStockWindow")
#         AddStockWindow.resize(500, 500)
#         AddStockWindow.setMinimumSize(QtCore.QSize(500, 500))
#         AddStockWindow.setMaximumSize(QtCore.QSize(500, 500))
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap(":/icons/assets/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         AddStockWindow.setWindowIcon(icon)
#         AddStockWindow.setIconSize(QtCore.QSize(32, 32))
#         self.centralwidget = QtWidgets.QWidget(AddStockWindow)
#         self.centralwidget.setStyleSheet("#label_widget {\n"
# "    background-color: #80cbc4;\n"
# "}\n"
# "\n"
# "#label_5 {\n"
# "    color: #fff;\n"
# "}\n"
# "\n"
# "#btn_save {\n"
# "    background-color: #26a69a;\n"
# "    border-radius: 5px;\n"
# "    padding: 5px 0px;\n"
# "    color: white;\n"
# "}\n"
# "\n"
# "#btn_clear {\n"
# "    background-color: #81d4fa;\n"
# "    border-radius: 5px;\n"
# "    padding: 5px 0px;\n"
# "    color: white;\n"
# "}\n"
# "\n"
# "#btn_cancel {\n"
# "    background-color: #b0bec5;\n"
# "    border-radius: 5px;\n"
# "    padding: 5px 0px;\n"
# "    color: white;\n"
# "}\n"
# "\n"
# "QLineEdit, QDateEdit, QComboBox {\n"
# "    border-radius: 5px;\n"
# "    padding: 5px 5px;\n"
# "    border: 1px solid #81d4fa;\n"
# "}\n"
# "\n"
# "#txt_amount {\n"
# "    background-color: #eee;\n"
# "    border: 1px solid #81d4fa;\n"
# "}")
#         self.centralwidget.setObjectName("centralwidget")
#         self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
#         self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_4.setSpacing(0)
#         self.verticalLayout_4.setObjectName("verticalLayout_4")
#         self.label_widget = QtWidgets.QWidget(self.centralwidget)
#         self.label_widget.setObjectName("label_widget")
#         self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.label_widget)
#         self.verticalLayout_3.setObjectName("verticalLayout_3")
#         self.lbl_add_stock = QtWidgets.QLabel(self.label_widget)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(18)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_add_stock.setFont(font)
#         self.lbl_add_stock.setAlignment(QtCore.Qt.AlignCenter)
#         self.lbl_add_stock.setObjectName("lbl_add_stock")
#         self.verticalLayout_3.addWidget(self.lbl_add_stock, 0, QtCore.Qt.AlignTop)
#         self.verticalLayout_4.addWidget(self.label_widget, 0, QtCore.Qt.AlignTop)
#         self.details_widget = QtWidgets.QWidget(self.centralwidget)
#         self.details_widget.setObjectName("details_widget")
#         self.horizontalLayout = QtWidgets.QHBoxLayout(self.details_widget)
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         self.lbl_frame = QtWidgets.QFrame(self.details_widget)
#         self.lbl_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.lbl_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.lbl_frame.setObjectName("lbl_frame")
#         self.verticalLayout = QtWidgets.QVBoxLayout(self.lbl_frame)
#         self.verticalLayout.setObjectName("verticalLayout")
#         self.lbl_name = QtWidgets.QLabel(self.lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         self.lbl_name.setFont(font)
#         self.lbl_name.setObjectName("lbl_name")
#         self.verticalLayout.addWidget(self.lbl_name)
#         self.lbl_date = QtWidgets.QLabel(self.lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         self.lbl_date.setFont(font)
#         self.lbl_date.setObjectName("lbl_date")
#         self.verticalLayout.addWidget(self.lbl_date)
#         self.lbl_supplier = QtWidgets.QLabel(self.lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         self.lbl_supplier.setFont(font)
#         self.lbl_supplier.setObjectName("lbl_supplier")
#         self.verticalLayout.addWidget(self.lbl_supplier)
#         self.lbl_stock = QtWidgets.QLabel(self.lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         self.lbl_stock.setFont(font)
#         self.lbl_stock.setObjectName("lbl_stock")
#         self.verticalLayout.addWidget(self.lbl_stock)
#         self.lbl_rate = QtWidgets.QLabel(self.lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         self.lbl_rate.setFont(font)
#         self.lbl_rate.setObjectName("lbl_rate")
#         self.verticalLayout.addWidget(self.lbl_rate)
#         self.lbl_amount = QtWidgets.QLabel(self.lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         self.lbl_amount.setFont(font)
#         self.lbl_amount.setObjectName("lbl_amount")
#         self.verticalLayout.addWidget(self.lbl_amount)
#         self.horizontalLayout.addWidget(self.lbl_frame)
#         self.lbl_inputs = QtWidgets.QFrame(self.details_widget)
#         self.lbl_inputs.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.lbl_inputs.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.lbl_inputs.setObjectName("lbl_inputs")
#         self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.lbl_inputs)
#         self.verticalLayout_2.setObjectName("verticalLayout_2")
#         self.select_product = QtWidgets.QComboBox(self.lbl_inputs)
#         self.select_product.setMinimumSize(QtCore.QSize(300, 35))
#         self.select_product.setMaximumSize(QtCore.QSize(300, 16777215))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.select_product.setFont(font)
#         self.select_product.setEditable(True)
#         self.select_product.setObjectName("select_product")
#         self.verticalLayout_2.addWidget(self.select_product)
#         self.txt_date = QtWidgets.QDateEdit(self.lbl_inputs)
#         self.txt_date.setMinimumSize(QtCore.QSize(300, 35))
#         self.txt_date.setMaximumSize(QtCore.QSize(300, 16777215))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_date.setFont(font)
#         self.txt_date.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
#         self.txt_date.setCalendarPopup(True)
#         self.txt_date.setObjectName("txt_date")
#         self.verticalLayout_2.addWidget(self.txt_date)
#         self.txt_supplier = QtWidgets.QLineEdit(self.lbl_inputs)
#         self.txt_supplier.setMinimumSize(QtCore.QSize(300, 0))
#         self.txt_supplier.setMaximumSize(QtCore.QSize(300, 16777215))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_supplier.setFont(font)
#         self.txt_supplier.setObjectName("txt_supplier")
#         self.verticalLayout_2.addWidget(self.txt_supplier, 0, QtCore.Qt.AlignRight)
#         self.txt_stock = QtWidgets.QLineEdit(self.lbl_inputs)
#         self.txt_stock.setMinimumSize(QtCore.QSize(300, 0))
#         self.txt_stock.setMaximumSize(QtCore.QSize(300, 16777215))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_stock.setFont(font)
#         self.txt_stock.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
#         self.txt_stock.setObjectName("txt_stock")
#         self.verticalLayout_2.addWidget(self.txt_stock, 0, QtCore.Qt.AlignRight)
#         self.txt_rate = QtWidgets.QLineEdit(self.lbl_inputs)
#         self.txt_rate.setMinimumSize(QtCore.QSize(300, 0))
#         self.txt_rate.setMaximumSize(QtCore.QSize(300, 16777215))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_rate.setFont(font)
#         self.txt_rate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
#         self.txt_rate.setObjectName("txt_rate")
#         self.verticalLayout_2.addWidget(self.txt_rate, 0, QtCore.Qt.AlignRight)
#         self.txt_amount = QtWidgets.QLineEdit(self.lbl_inputs)
#         self.txt_amount.setMinimumSize(QtCore.QSize(300, 0))
#         self.txt_amount.setMaximumSize(QtCore.QSize(300, 16777215))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_amount.setFont(font)
#         self.txt_amount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
#         self.txt_amount.setReadOnly(True)
#         self.txt_amount.setObjectName("txt_amount")
#         self.verticalLayout_2.addWidget(self.txt_amount, 0, QtCore.Qt.AlignRight)
#         self.horizontalLayout.addWidget(self.lbl_inputs)
#         self.verticalLayout_4.addWidget(self.details_widget)
#         self.bottom_widget = QtWidgets.QWidget(self.centralwidget)
#         self.bottom_widget.setObjectName("bottom_widget")
#         self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bottom_widget)
#         self.horizontalLayout_2.setObjectName("horizontalLayout_2")
#         self.btn_save = QtWidgets.QPushButton(self.bottom_widget)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_save.setFont(font)
#         icon1 = QtGui.QIcon()
#         icon1.addPixmap(QtGui.QPixmap(":/icons/assets/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_save.setIcon(icon1)
#         self.btn_save.setIconSize(QtCore.QSize(32, 32))
#         self.btn_save.setObjectName("btn_save")
#         self.horizontalLayout_2.addWidget(self.btn_save)
#         self.btn_clear = QtWidgets.QPushButton(self.bottom_widget)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_clear.setFont(font)
#         icon2 = QtGui.QIcon()
#         icon2.addPixmap(QtGui.QPixmap(":/icons/assets/icons/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_clear.setIcon(icon2)
#         self.btn_clear.setIconSize(QtCore.QSize(32, 32))
#         self.btn_clear.setObjectName("btn_clear")
#         self.horizontalLayout_2.addWidget(self.btn_clear)
#         self.btn_cancel = QtWidgets.QPushButton(self.bottom_widget)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_cancel.setFont(font)
#         icon3 = QtGui.QIcon()
#         icon3.addPixmap(QtGui.QPixmap(":/icons/assets/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_cancel.setIcon(icon3)
#         self.btn_cancel.setIconSize(QtCore.QSize(32, 32))
#         self.btn_cancel.setObjectName("btn_cancel")
#         self.horizontalLayout_2.addWidget(self.btn_cancel)
#         self.verticalLayout_4.addWidget(self.bottom_widget)
#         AddStockWindow.setCentralWidget(self.centralwidget)
#         self.statusbar = QtWidgets.QStatusBar(AddStockWindow)
#         self.statusbar.setObjectName("statusbar")
#         AddStockWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(AddStockWindow)
#         QtCore.QMetaObject.connectSlotsByName(AddStockWindow)

#     def retranslateUi(self, AddStockWindow):
#         _translate = QtCore.QCoreApplication.translate
#         AddStockWindow.setWindowTitle(_translate("AddStockWindow", "Add Stock"))
#         self.lbl_add_stock.setText(_translate("AddStockWindow", "Add Stock"))
#         self.lbl_name.setText(_translate("AddStockWindow", "Name"))
#         self.lbl_date.setText(_translate("AddStockWindow", "Date"))
#         self.lbl_supplier.setText(_translate("AddStockWindow", "Supplier"))
#         self.lbl_stock.setText(_translate("AddStockWindow", "Stock"))
#         self.lbl_rate.setText(_translate("AddStockWindow", "Rate"))
#         self.lbl_amount.setText(_translate("AddStockWindow", "Amount"))
#         self.btn_save.setText(_translate("AddStockWindow", "SAVE"))
#         self.btn_clear.setText(_translate("AddStockWindow", "CLEAR"))
#         self.btn_cancel.setText(_translate("AddStockWindow", "CANCEL"))
# import resources_rc


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     AddStockWindow = QtWidgets.QMainWindow()
#     ui = Ui_AddStockWindow()
#     ui.setupUi(AddStockWindow)
#     AddStockWindow.show()
#     sys.exit(app.exec_())
