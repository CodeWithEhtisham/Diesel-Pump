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

FORM_MAIN, _ = loadUiType('ui/add_supplier.ui')


class AddSupplierWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()

    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.add_supplier)
        self.btn_clear.clicked.connect(self.clear_fields)
        self.btn_cancel.clicked.connect(self.close)

    def add_supplier(self):
        name = self.txt_name.text()
        phone = self.txt_phone.text()
        address = self.txt_address.text()
        balance_type = self.balance_type.currentText()
        balance = self.txt_balance.text()
        print(f"{name}, {phone}, {address}, {balance_type}, {balance}")
        if not (name and phone and address and balance_type and balance):
            QMessageBox.warning(self, 'Error', 'All fields are required')
        else:
            try:
                balance = float(balance)
            except ValueError:
                QMessageBox.warning(self, 'Error', 'Balance must be a number')
                return
            try:
                db = DBHandler()

                if balance_type == 'Cash In':
                    balance = -balance
                else:
                    balance = balance
                # db.conn.execute("Drop table suppliers")
                # db.conn.execute("Drop table supplier_cash_paid")
                db.insert(table_name='suppliers',columns="name, phone, address, balance_type, balance ", values=f"'{name}', '{phone}', '{address}', '{balance_type}', '{balance}'")
                db.insert(table_name="supplier_cash_paid",columns="supplier_id,date,payment_method,cash_paid,remaining,description,quantity,rate,amount",values=f"'{db.cursor.lastrowid}', '{QDate.currentDate().toString('dd/MM/yyyy')}', 'Cash', '0', '{balance}', 'Opening -{balance_type}', '0', '0', '0'")
                QMessageBox.information(self, 'Success', 'Supplier added successfully')
                self.close()
                db.close()
            except Exception as e:
                QMessageBox.warning(self, 'Error', f'insertion error supplier: {e}')


    def clear_fields(self):
        self.txt_name.setText('')
        self.txt_phone.setText('')
        self.txt_address.setText('')
        self.txt_balance.setText('')
        


def main():
    app = QApplication(sys.argv)
    window = AddSupplierWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()



# # -*- coding: utf-8 -*-

# ################################################################################
# ## Form generated from reading UI file 'add_supplier.ui'
# ##
# ## Created by: Qt User Interface Compiler version 5.15.2
# ##
# ## WARNING! All changes made in this file will be lost when recompiling UI file!
# ################################################################################

# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *

# import resources_rc

# # class Ui_AddSupplierWindow(object):
#     def setupUi(self, AddSupplierWindow):
#         if not AddSupplierWindow.objectName():
#             AddSupplierWindow.setObjectName(u"AddSupplierWindow")
#         AddSupplierWindow.resize(500, 500)
#         AddSupplierWindow.setMinimumSize(QSize(500, 500))
#         AddSupplierWindow.setMaximumSize(QSize(500, 500))
#         icon = QIcon()
#         icon.addFile(u":/icons/assets/icons/logo.png", QSize(), QIcon.Normal, QIcon.Off)
#         AddSupplierWindow.setWindowIcon(icon)
#         AddSupplierWindow.setIconSize(QSize(32, 32))
#         self.centralwidget = QWidget(AddSupplierWindow)
#         self.centralwidget.setObjectName(u"centralwidget")
#         self.centralwidget.setStyleSheet(u"#label_widget {\n"
# "	background-color: #80cbc4;\n"
# "}\n"
# "\n"
# "#label_5 {\n"
# "	color: #fff;\n"
# "}\n"
# "\n"
# "#btn_save {\n"
# "	background-color: #26a69a;\n"
# "	border-radius: 5px;\n"
# "	padding: 5px 0px;\n"
# "	color: white;\n"
# "}\n"
# "\n"
# "#btn_clear {\n"
# "	background-color: #81d4fa;\n"
# "	border-radius: 5px;\n"
# "	padding: 5px 0px;\n"
# "	color: white;\n"
# "}\n"
# "\n"
# "#btn_cancel {\n"
# "	background-color: #b0bec5;\n"
# "	border-radius: 5px;\n"
# "	padding: 5px 0px;\n"
# "	color: white;\n"
# "}\n"
# "\n"
# "QLineEdit {\n"
# "	border-radius: 5px;\n"
# "	padding: 5px 5px;\n"
# "	border: 1px solid #81d4fa;\n"
# "}\n"
# "\n"
# "QComboBox {\n"
# "	border-radius: 5px;\n"
# "	padding: 5px 5px;\n"
# "	border: 1px solid #81d4fa;\n"
# "}")
#         self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
#         self.verticalLayout_4.setSpacing(0)
#         self.verticalLayout_4.setObjectName(u"verticalLayout_4")
#         self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
#         self.label_widget = QWidget(self.centralwidget)
#         self.label_widget.setObjectName(u"label_widget")
#         self.verticalLayout_3 = QVBoxLayout(self.label_widget)
#         self.verticalLayout_3.setObjectName(u"verticalLayout_3")
#         self.label_5 = QLabel(self.label_widget)
#         self.label_5.setObjectName(u"label_5")
#         font = QFont()
#         font.setFamily(u"Calibri")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.label_5.setFont(font)
#         self.label_5.setAlignment(Qt.AlignCenter)

#         self.verticalLayout_3.addWidget(self.label_5, 0, Qt.AlignTop)


#         self.verticalLayout_4.addWidget(self.label_widget, 0, Qt.AlignTop)

#         self.details_widget = QWidget(self.centralwidget)
#         self.details_widget.setObjectName(u"details_widget")
#         self.horizontalLayout = QHBoxLayout(self.details_widget)
#         self.horizontalLayout.setObjectName(u"horizontalLayout")
#         self.lbl_frame = QFrame(self.details_widget)
#         self.lbl_frame.setObjectName(u"lbl_frame")
#         self.lbl_frame.setFrameShape(QFrame.StyledPanel)
#         self.lbl_frame.setFrameShadow(QFrame.Raised)
#         self.verticalLayout_2 = QVBoxLayout(self.lbl_frame)
#         self.verticalLayout_2.setObjectName(u"verticalLayout_2")
#         self.lbl_name = QLabel(self.lbl_frame)
#         self.lbl_name.setObjectName(u"lbl_name")
#         font1 = QFont()
#         font1.setFamily(u"Calibri")
#         font1.setPointSize(14)
#         self.lbl_name.setFont(font1)

#         self.verticalLayout_2.addWidget(self.lbl_name)

#         self.lbl_mobile = QLabel(self.lbl_frame)
#         self.lbl_mobile.setObjectName(u"lbl_mobile")
#         self.lbl_mobile.setFont(font1)

#         self.verticalLayout_2.addWidget(self.lbl_mobile)

#         self.lbl_address = QLabel(self.lbl_frame)
#         self.lbl_address.setObjectName(u"lbl_address")
#         self.lbl_address.setFont(font1)

#         self.verticalLayout_2.addWidget(self.lbl_address)

#         self.lbl_balance_type = QLabel(self.lbl_frame)
#         self.lbl_balance_type.setObjectName(u"lbl_balance_type")
#         self.lbl_balance_type.setFont(font1)

#         self.verticalLayout_2.addWidget(self.lbl_balance_type)

#         self.lbl_balance = QLabel(self.lbl_frame)
#         self.lbl_balance.setObjectName(u"lbl_balance")
#         self.lbl_balance.setFont(font1)

#         self.verticalLayout_2.addWidget(self.lbl_balance)


#         self.horizontalLayout.addWidget(self.lbl_frame)

#         self.lbl_inputs = QFrame(self.details_widget)
#         self.lbl_inputs.setObjectName(u"lbl_inputs")
#         self.lbl_inputs.setFrameShape(QFrame.StyledPanel)
#         self.lbl_inputs.setFrameShadow(QFrame.Raised)
#         self.verticalLayout = QVBoxLayout(self.lbl_inputs)
#         self.verticalLayout.setObjectName(u"verticalLayout")
#         self.txt_name = QLineEdit(self.lbl_inputs)
#         self.txt_name.setObjectName(u"txt_name")
#         self.txt_name.setFont(font1)

#         self.verticalLayout.addWidget(self.txt_name)

#         self.txt_phone = QLineEdit(self.lbl_inputs)
#         self.txt_phone.setObjectName(u"txt_phone")
#         self.txt_phone.setFont(font1)

#         self.verticalLayout.addWidget(self.txt_phone)

#         self.txt_vehicle = QLineEdit(self.lbl_inputs)
#         self.txt_vehicle.setObjectName(u"txt_vehicle")
#         self.txt_vehicle.setFont(font1)

#         self.verticalLayout.addWidget(self.txt_vehicle)

#         self.balance_type = QComboBox(self.lbl_inputs)
#         self.balance_type.addItem("")
#         self.balance_type.addItem("")
#         self.balance_type.setObjectName(u"balance_type")
#         self.balance_type.setFont(font1)

#         self.verticalLayout.addWidget(self.balance_type)

#         self.txt_balance = QLineEdit(self.lbl_inputs)
#         self.txt_balance.setObjectName(u"txt_balance")
#         self.txt_balance.setFont(font1)

#         self.verticalLayout.addWidget(self.txt_balance)


#         self.horizontalLayout.addWidget(self.lbl_inputs)


#         self.verticalLayout_4.addWidget(self.details_widget)

#         self.bottom_widget = QWidget(self.centralwidget)
#         self.bottom_widget.setObjectName(u"bottom_widget")
#         self.horizontalLayout_2 = QHBoxLayout(self.bottom_widget)
#         self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
#         self.btn_save = QPushButton(self.bottom_widget)
#         self.btn_save.setObjectName(u"btn_save")
#         font2 = QFont()
#         font2.setFamily(u"Calibri")
#         font2.setPointSize(14)
#         font2.setBold(True)
#         font2.setWeight(75)
#         self.btn_save.setFont(font2)
#         icon1 = QIcon()
#         icon1.addFile(u":/icons/assets/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
#         self.btn_save.setIcon(icon1)
#         self.btn_save.setIconSize(QSize(32, 32))

#         self.horizontalLayout_2.addWidget(self.btn_save)

#         self.btn_clear = QPushButton(self.bottom_widget)
#         self.btn_clear.setObjectName(u"btn_clear")
#         self.btn_clear.setFont(font2)
#         icon2 = QIcon()
#         icon2.addFile(u":/icons/assets/icons/clear.png", QSize(), QIcon.Normal, QIcon.Off)
#         self.btn_clear.setIcon(icon2)
#         self.btn_clear.setIconSize(QSize(32, 32))

#         self.horizontalLayout_2.addWidget(self.btn_clear)

#         self.btn_cancel = QPushButton(self.bottom_widget)
#         self.btn_cancel.setObjectName(u"btn_cancel")
#         self.btn_cancel.setFont(font2)
#         icon3 = QIcon()
#         icon3.addFile(u":/icons/assets/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
#         self.btn_cancel.setIcon(icon3)
#         self.btn_cancel.setIconSize(QSize(32, 32))

#         self.horizontalLayout_2.addWidget(self.btn_cancel)


#         self.verticalLayout_4.addWidget(self.bottom_widget)

#         AddSupplierWindow.setCentralWidget(self.centralwidget)
#         self.statusbar = QStatusBar(AddSupplierWindow)
#         self.statusbar.setObjectName(u"statusbar")
#         AddSupplierWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(AddSupplierWindow)

#         QMetaObject.connectSlotsByName(AddSupplierWindow)
#     # setupUi

#     def retranslateUi(self, AddSupplierWindow):
#         AddSupplierWindow.setWindowTitle(QCoreApplication.translate("AddSupplierWindow", u"Add Supplier", None))
#         self.label_5.setText(QCoreApplication.translate("AddSupplierWindow", u"Add New Supplier", None))
#         self.lbl_name.setText(QCoreApplication.translate("AddSupplierWindow", u"Name", None))
#         self.lbl_mobile.setText(QCoreApplication.translate("AddSupplierWindow", u"Mobile", None))
#         self.lbl_address.setText(QCoreApplication.translate("AddSupplierWindow", u"Address", None))
#         self.lbl_balance_type.setText(QCoreApplication.translate("AddSupplierWindow", u"Balance Type", None))
#         self.lbl_balance.setText(QCoreApplication.translate("AddSupplierWindow", u"Opening Balance", None))
#         self.balance_type.setItemText(0, QCoreApplication.translate("AddSupplierWindow", u"Cash In", None))
#         self.balance_type.setItemText(1, QCoreApplication.translate("AddSupplierWindow", u"Cash Out", None))

#         self.btn_save.setText(QCoreApplication.translate("AddSupplierWindow", u"SAVE", None))
#         self.btn_clear.setText(QCoreApplication.translate("AddSupplierWindow", u"CLEAR", None))
#         self.btn_cancel.setText(QCoreApplication.translate("AddSupplierWindow", u"CANCEL", None))
#     # retranslateUi

