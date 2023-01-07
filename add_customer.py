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

FORM_MAIN, _ = loadUiType('ui/add_customer.ui')


class AddCustomerWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()

    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.Add_Customer)
        self.btn_clear.clicked.connect(self.Clear_Fields)
        self.btn_cancel.clicked.connect(self.close)

    def Add_Customer(self):
        name = self.txt_name.text()
        phone = self.txt_phone.text()
        vehicle = self.txt_vehicle.text()
        address = self.txt_address.text()
        balance_type = self.balance_type.currentText()
        balance = self.txt_balance.text()
        if name and phone and vehicle and address and balance != "":
            try:
                db=DBHandler()
                if balance_type == 'Cash In':
                    balance = balance
                else:
                    balance = -balance

                db.insert(table_name="Customers", columns="name, phone, vehicle, address, balance_type, balance",
                    values=f"'{name}', '{phone}', '{vehicle}', '{address}', '{balance_type}', '{balance}'")

                        # self.conn.execute(f"CREATE TABLE IF NOT EXISTS customer_cash_received (id INTEGER PRIMARY KEY AUTOINCREMENT,customer_id INTEGER,date TEXT,payment_method TEXT,cash_received REAL,remaining REAL,description TEXT DEFAULT 'Cash Received',quantity INTEGER DEFAULT 0,rate REAL DEFAULT 0,amount REAL DEFAULT 0,FOREIGN KEY(customer_id) REFERENCES customers(customer_id))")
                db.conn.execute(f"INSERT INTO customer_cash_received (customer_id,date,payment_method,cash_received,remaining,description,quantity,rate,amount) VALUES ((SELECT customer_id FROM customers WHERE name='{name}'),'{datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}','Cash','{balance}','{balance}','Cash Received',0,0,0)")
                db.conn.commit()
                QMessageBox.information(self, "Success", "Customer has been added")
                db.close()
                self.close()
            except Exception as e:
                QMessageBox.warning(self, "Error", f"Customer has not been added {e}")
        else:
            QMessageBox.warning(self, "Error", "Fields cannot be empty")

    def Clear_Fields(self):
        self.txt_name.setText("")
        self.txt_phone.setText("")
        self.txt_vehicle.setText("")
        self.txt_address.setText("")
        self.txt_balance.setText("")

        

def main():
    app = QApplication(sys.argv)
    window = AddCustomerWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

# from PyQt5 import QtCore, QtGui, QtWidgets
# from PySide2 import *
# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *


# class Ui_AddCustomerWindow(object):
#     def setupUi(self, AddCustomerWindow):
#         AddCustomerWindow.setObjectName("AddCustomerWindow")
#         AddCustomerWindow.resize(500, 500)
#         AddCustomerWindow.setMinimumSize(QtCore.QSize(500, 500))
#         AddCustomerWindow.setMaximumSize(QtCore.QSize(500, 500))
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap(":/icons/assets/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         AddCustomerWindow.setWindowIcon(icon)
#         AddCustomerWindow.setIconSize(QtCore.QSize(32, 32))
#         self.centralwidget = QtWidgets.QWidget(AddCustomerWindow)
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
# "QLineEdit {\n"
# "    border-radius: 5px;\n"
# "    padding: 5px 5px;\n"
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
#         self.label_5 = QtWidgets.QLabel(self.label_widget)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.label_5.setFont(font)
#         self.label_5.setAlignment(QtCore.Qt.AlignCenter)
#         self.label_5.setObjectName("label_5")
#         self.verticalLayout_3.addWidget(self.label_5, 0, QtCore.Qt.AlignTop)
#         self.verticalLayout_4.addWidget(self.label_widget, 0, QtCore.Qt.AlignTop)
#         self.details_widget = QtWidgets.QWidget(self.centralwidget)
#         self.details_widget.setObjectName("details_widget")
#         self.horizontalLayout = QtWidgets.QHBoxLayout(self.details_widget)
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         self.lbl_frame = QtWidgets.QFrame(self.details_widget)
#         self.lbl_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.lbl_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.lbl_frame.setObjectName("lbl_frame")
#         self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.lbl_frame)
#         self.verticalLayout_2.setObjectName("verticalLayout_2")
#         self.lbl_name = QtWidgets.QLabel(self.lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_name.setFont(font)
#         self.lbl_name.setObjectName("lbl_name")
#         self.verticalLayout_2.addWidget(self.lbl_name)
#         self.lbl_mobile = QtWidgets.QLabel(self.lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_mobile.setFont(font)
#         self.lbl_mobile.setObjectName("lbl_mobile")
#         self.verticalLayout_2.addWidget(self.lbl_mobile)
#         self.lbl_vehicle = QtWidgets.QLabel(self.lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_vehicle.setFont(font)
#         self.lbl_vehicle.setObjectName("lbl_vehicle")
#         self.verticalLayout_2.addWidget(self.lbl_vehicle)
#         self.lbl_address = QtWidgets.QLabel(self.lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_address.setFont(font)
#         self.lbl_address.setObjectName("lbl_address")
#         self.verticalLayout_2.addWidget(self.lbl_address)
#         self.lbl_balance = QtWidgets.QLabel(self.lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_balance.setFont(font)
#         self.lbl_balance.setObjectName("lbl_balance")
#         self.verticalLayout_2.addWidget(self.lbl_balance)
#         self.horizontalLayout.addWidget(self.lbl_frame)
#         self.lbl_inputs = QtWidgets.QFrame(self.details_widget)
#         self.lbl_inputs.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.lbl_inputs.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.lbl_inputs.setObjectName("lbl_inputs")
#         self.verticalLayout = QtWidgets.QVBoxLayout(self.lbl_inputs)
#         self.verticalLayout.setObjectName("verticalLayout")
#         self.txt_name = QtWidgets.QLineEdit(self.lbl_inputs)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_name.setFont(font)
#         self.txt_name.setObjectName("txt_name")
#         self.verticalLayout.addWidget(self.txt_name)
#         self.txt_mobile = QtWidgets.QLineEdit(self.lbl_inputs)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_mobile.setFont(font)
#         self.txt_mobile.setObjectName("txt_mobile")
#         self.verticalLayout.addWidget(self.txt_mobile)
#         self.txt_vehicle = QtWidgets.QLineEdit(self.lbl_inputs)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_vehicle.setFont(font)
#         self.txt_vehicle.setObjectName("txt_vehicle")
#         self.verticalLayout.addWidget(self.txt_vehicle)
#         self.txt_address = QtWidgets.QLineEdit(self.lbl_inputs)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_address.setFont(font)
#         self.txt_address.setObjectName("txt_address")
#         self.verticalLayout.addWidget(self.txt_address)
#         self.txt_balance = QtWidgets.QLineEdit(self.lbl_inputs)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_balance.setFont(font)
#         self.txt_balance.setObjectName("txt_balance")
#         self.verticalLayout.addWidget(self.txt_balance)
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
#         AddCustomerWindow.setCentralWidget(self.centralwidget)
#         self.statusbar = QtWidgets.QStatusBar(AddCustomerWindow)
#         self.statusbar.setObjectName("statusbar")
#         AddCustomerWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(AddCustomerWindow)
#         QtCore.QMetaObject.connectSlotsByName(AddCustomerWindow)

#     def retranslateUi(self, AddCustomerWindow):
#         _translate = QtCore.QCoreApplication.translate
#         AddCustomerWindow.setWindowTitle(_translate("AddCustomerWindow", "Add Customer"))
#         self.label_5.setText(_translate("AddCustomerWindow", "Add New Customer"))
#         self.lbl_name.setText(_translate("AddCustomerWindow", "Name"))
#         self.lbl_mobile.setText(_translate("AddCustomerWindow", "Mobile"))
#         self.lbl_vehicle.setText(_translate("AddCustomerWindow", "Vehicle No."))
#         self.lbl_address.setText(_translate("AddCustomerWindow", "Address"))
#         self.lbl_balance.setText(_translate("AddCustomerWindow", "Opening Balance"))
#         self.btn_save.setText(_translate("AddCustomerWindow", "SAVE"))
#         self.btn_clear.setText(_translate("AddCustomerWindow", "CLEAR"))
#         self.btn_cancel.setText(_translate("AddCustomerWindow", "CANCEL"))
# import resources_rc


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     AddCustomerWindow = QtWidgets.QMainWindow()
#     ui = Ui_AddCustomerWindow()
#     ui.setupUi(AddCustomerWindow)
#     AddCustomerWindow.show()
#     sys.exit(app.exec_())
