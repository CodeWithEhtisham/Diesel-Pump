
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

FORM_MAIN, _ = loadUiType('ui/add_roznamcha.ui')


class RozNamchaWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()

        db=DBHandler()
        self.select_product.addItems([i[0] for i in db.select_all('products','product_name')])
        self.select_customer.addItems([i[0] for i in db.select_all('customers','name')])
        self.txt_date.setDate(QDate.currentDate())

        self.txt_rate.textChanged.connect(self.calculate_total_amount)

    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.add_roznamcha)
        self.btn_clear.clicked.connect(self.clear_fields)
        self.btn_cancel.clicked.connect(self.close)


    def calculate_total_amount(self):
        quantity = int(self.txt_quantity.text())
        rate = int(self.txt_rate.text())
        total_amount = quantity * rate
        self.txt_total_amount.setText(str(total_amount))

    def get_product_id(self,db,product_name):
        return db.conn.execute("SELECT product_id FROM products WHERE product_name='{}'".format(product_name)).fetchone()[0]
    
    def get_customer_id(self,db,customer_name):
        return db.conn.execute("SELECT custmer_id FROM customers WHERE name='{}'".format(customer_name)).fetchone()[0]
        
    
    def add_roznamcha(self):
        db=DBHandler()
        prodcut_id = self.get_product_id(db,self.select_product.currentText())
        customer_id = self.get_customer_id(db,self.select_customer.currentText())
        date = self.txt_date.text()
        quantity = int(self.txt_quantity.text())
        rate = int(self.txt_rate.text())
        total_amount = int(self.txt_total_amount.text())
        cash_paid = int(self.txt_cash_paid.text())
        cash_received = int(self.txt_cash_received.text())

        if prodcut_id and customer_id and date and quantity and rate and total_amount and cash_paid and cash_received:
            db.conn.execute('INSERT INTO roznamcha (product_id, customer_id, date, quantity, rate, total_amount, cash_paid, cash_received) VALUES (?,?,?,?,?,?,?,?)',(prodcut_id,customer_id,date,quantity,rate,total_amount,cash_paid,cash_received))
            QMessageBox.information(self,'Success','Roznamcha Added Successfully')
            db.close()
            self.close()

    def clear_fields(self):
        self.txt_date.setDate(datetime.date.today())
        self.select_product.setCurrentIndex(0)
        self.txt_quantity.setText('')
        self.txt_rate.setText('')
        self.txt_total_amount.setText('')
        self.select_customer.setCurrentIndex(0)
        self.txt_cash_paid.setText('')
        self.txt_cash_received.setText('')
        

def main():
    app = QApplication(sys.argv)
    window = RozNamchaWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

# from PyQt5 import QtCore, QtGui, QtWidgets
# from PySide2 import *
# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *


# class Ui_RozNamchaWindow(object):
#     def setupUi(self, RozNamchaWindow):
#         RozNamchaWindow.setObjectName("RozNamchaWindow")
#         RozNamchaWindow.resize(500, 600)
#         RozNamchaWindow.setMinimumSize(QtCore.QSize(500, 600))
#         RozNamchaWindow.setMaximumSize(QtCore.QSize(500, 600))
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap(":/icons/assets/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         RozNamchaWindow.setWindowIcon(icon)
#         RozNamchaWindow.setIconSize(QtCore.QSize(32, 32))
#         self.centralwidget = QtWidgets.QWidget(RozNamchaWindow)
#         self.centralwidget.setStyleSheet("#lbl_add_roz {\n"
# "    background-color: #80cbc4;\n"
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
# "#txt_total_amount {\n"
# "    background-color: #eceff1;\n"
# "}")
#         self.centralwidget.setObjectName("centralwidget")
#         self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
#         self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_3.setSpacing(0)
#         self.verticalLayout_3.setObjectName("verticalLayout_3")
#         self.lbl_add_roz = QtWidgets.QLabel(self.centralwidget)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_add_roz.setFont(font)
#         self.lbl_add_roz.setAlignment(QtCore.Qt.AlignCenter)
#         self.lbl_add_roz.setObjectName("lbl_add_roz")
#         self.verticalLayout_3.addWidget(self.lbl_add_roz, 0, QtCore.Qt.AlignTop)
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
#         self.lbl_date = QtWidgets.QLabel(self.lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_date.setFont(font)
#         self.lbl_date.setObjectName("lbl_date")
#         self.verticalLayout.addWidget(self.lbl_date)
#         self.lbl_product = QtWidgets.QLabel(self.lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_product.setFont(font)
#         self.lbl_product.setObjectName("lbl_product")
#         self.verticalLayout.addWidget(self.lbl_product)
#         self.lbl_quantity = QtWidgets.QLabel(self.lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_quantity.setFont(font)
#         self.lbl_quantity.setObjectName("lbl_quantity")
#         self.verticalLayout.addWidget(self.lbl_quantity)
#         self.lbl_rate = QtWidgets.QLabel(self.lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_rate.setFont(font)
#         self.lbl_rate.setObjectName("lbl_rate")
#         self.verticalLayout.addWidget(self.lbl_rate)
#         self.lbl_amount = QtWidgets.QLabel(self.lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_amount.setFont(font)
#         self.lbl_amount.setObjectName("lbl_amount")
#         self.verticalLayout.addWidget(self.lbl_amount)
#         self.lbl_customer = QtWidgets.QLabel(self.lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_customer.setFont(font)
#         self.lbl_customer.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
#         self.lbl_customer.setObjectName("lbl_customer")
#         self.verticalLayout.addWidget(self.lbl_customer)
#         self.lbl_cash_paid = QtWidgets.QLabel(self.lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_cash_paid.setFont(font)
#         self.lbl_cash_paid.setObjectName("lbl_cash_paid")
#         self.verticalLayout.addWidget(self.lbl_cash_paid)
#         self.lbl_cash_received = QtWidgets.QLabel(self.lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_cash_received.setFont(font)
#         self.lbl_cash_received.setObjectName("lbl_cash_received")
#         self.verticalLayout.addWidget(self.lbl_cash_received)
#         self.horizontalLayout.addWidget(self.lbl_frame)
#         self.lbl_inputs = QtWidgets.QFrame(self.details_widget)
#         self.lbl_inputs.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.lbl_inputs.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.lbl_inputs.setObjectName("lbl_inputs")
#         self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.lbl_inputs)
#         self.verticalLayout_2.setContentsMargins(10, -1, 10, -1)
#         self.verticalLayout_2.setObjectName("verticalLayout_2")
#         self.txt_date = QtWidgets.QDateEdit(self.lbl_inputs)
#         self.txt_date.setMinimumSize(QtCore.QSize(0, 0))
#         self.txt_date.setMaximumSize(QtCore.QSize(1000, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_date.setFont(font)
#         self.txt_date.setMinimumDate(QtCore.QDate(2000, 9, 14))
#         self.txt_date.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
#         self.txt_date.setCalendarPopup(True)
#         self.txt_date.setTimeSpec(QtCore.Qt.LocalTime)
#         self.txt_date.setObjectName("txt_date")
#         self.verticalLayout_2.addWidget(self.txt_date)
#         self.select_product = QtWidgets.QComboBox(self.lbl_inputs)
#         self.select_product.setMinimumSize(QtCore.QSize(0, 0))
#         self.select_product.setMaximumSize(QtCore.QSize(1000, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.select_product.setFont(font)
#         self.select_product.setObjectName("select_product")
#         self.select_product.addItem("")
#         self.verticalLayout_2.addWidget(self.select_product)
#         self.txt_quantity = QtWidgets.QLineEdit(self.lbl_inputs)
#         self.txt_quantity.setMinimumSize(QtCore.QSize(0, 0))
#         self.txt_quantity.setMaximumSize(QtCore.QSize(1000, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_quantity.setFont(font)
#         self.txt_quantity.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
#         self.txt_quantity.setObjectName("txt_quantity")
#         self.verticalLayout_2.addWidget(self.txt_quantity)
#         self.txt_rate = QtWidgets.QLineEdit(self.lbl_inputs)
#         self.txt_rate.setMinimumSize(QtCore.QSize(0, 0))
#         self.txt_rate.setMaximumSize(QtCore.QSize(1000, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_rate.setFont(font)
#         self.txt_rate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
#         self.txt_rate.setObjectName("txt_rate")
#         self.verticalLayout_2.addWidget(self.txt_rate)
#         self.txt_total_amount = QtWidgets.QLineEdit(self.lbl_inputs)
#         self.txt_total_amount.setMinimumSize(QtCore.QSize(0, 40))
#         self.txt_total_amount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
#         self.txt_total_amount.setObjectName("txt_total_amount")
#         self.verticalLayout_2.addWidget(self.txt_total_amount)
#         self.select_customer = QtWidgets.QComboBox(self.lbl_inputs)
#         self.select_customer.setMinimumSize(QtCore.QSize(0, 0))
#         self.select_customer.setMaximumSize(QtCore.QSize(1000, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.select_customer.setFont(font)
#         self.select_customer.setObjectName("select_customer")
#         self.select_customer.addItem("")
#         self.verticalLayout_2.addWidget(self.select_customer)
#         self.txt_cash_paid = QtWidgets.QLineEdit(self.lbl_inputs)
#         self.txt_cash_paid.setMinimumSize(QtCore.QSize(0, 40))
#         self.txt_cash_paid.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
#         self.txt_cash_paid.setObjectName("txt_cash_paid")
#         self.verticalLayout_2.addWidget(self.txt_cash_paid)
#         self.txt_cash_received = QtWidgets.QLineEdit(self.lbl_inputs)
#         self.txt_cash_received.setMinimumSize(QtCore.QSize(0, 40))
#         self.txt_cash_received.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
#         self.txt_cash_received.setObjectName("txt_cash_received")
#         self.verticalLayout_2.addWidget(self.txt_cash_received)
#         self.horizontalLayout.addWidget(self.lbl_inputs)
#         self.verticalLayout_3.addWidget(self.details_widget)
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
#         self.btn_save.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
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
#         self.btn_clear.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
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
#         self.btn_cancel.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         icon3 = QtGui.QIcon()
#         icon3.addPixmap(QtGui.QPixmap(":/icons/assets/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_cancel.setIcon(icon3)
#         self.btn_cancel.setIconSize(QtCore.QSize(32, 32))
#         self.btn_cancel.setObjectName("btn_cancel")
#         self.horizontalLayout_2.addWidget(self.btn_cancel)
#         self.verticalLayout_3.addWidget(self.bottom_widget)
#         RozNamchaWindow.setCentralWidget(self.centralwidget)
#         self.statusbar = QtWidgets.QStatusBar(RozNamchaWindow)
#         self.statusbar.setObjectName("statusbar")
#         RozNamchaWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(RozNamchaWindow)
#         QtCore.QMetaObject.connectSlotsByName(RozNamchaWindow)

#     def retranslateUi(self, RozNamchaWindow):
#         _translate = QtCore.QCoreApplication.translate
#         RozNamchaWindow.setWindowTitle(_translate("RozNamchaWindow", "Roz Namcha"))
#         self.lbl_add_roz.setText(_translate("RozNamchaWindow", "Add New RozNamcha"))
#         self.lbl_date.setText(_translate("RozNamchaWindow", "Date"))
#         self.lbl_product.setText(_translate("RozNamchaWindow", "Product"))
#         self.lbl_quantity.setText(_translate("RozNamchaWindow", "Quantity"))
#         self.lbl_rate.setText(_translate("RozNamchaWindow", "Rate"))
#         self.lbl_amount.setText(_translate("RozNamchaWindow", "Amount"))
#         self.lbl_customer.setText(_translate("RozNamchaWindow", "Customer"))
#         self.lbl_cash_paid.setText(_translate("RozNamchaWindow", "Cash Paid"))
#         self.lbl_cash_received.setText(_translate("RozNamchaWindow", "Cash Received"))
#         self.select_product.setItemText(0, _translate("RozNamchaWindow", "Select Product"))
#         self.select_customer.setItemText(0, _translate("RozNamchaWindow", "Select Customer"))
#         self.btn_save.setText(_translate("RozNamchaWindow", "SAVE"))
#         self.btn_clear.setText(_translate("RozNamchaWindow", "CLEAR"))
#         self.btn_cancel.setText(_translate("RozNamchaWindow", "CANCEL"))
# import resources_rc


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     RozNamchaWindow = QtWidgets.QMainWindow()
#     ui = Ui_RozNamchaWindow()
#     ui.setupUi(RozNamchaWindow)
#     RozNamchaWindow.show()
#     sys.exit(app.exec_())
