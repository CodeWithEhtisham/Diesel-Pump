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
FORM_MAIN, _ = loadUiType('ui/add_supplier.ui')


class UpdateSupplierWindow(QMainWindow, FORM_MAIN):
    def __init__(self,id):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.id=id
        self.db= DBHandler()
        self.Handle_Buttons()
        self.update()

    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.add_supplier)
        # self.btn_clear.clicked.connect(self.clear_fields)
        self.btn_cancel.clicked.connect(self.close)

    def update(self):
        data = self.db.select(
            table_name='suppliers',
            columns="name,phone,address,balance_type,balance",
            condition="supplier_id={}".format(self.id)
        )
        self.txt_name.setText(data[0][0])
        self.txt_phone.setText(data[0][1])
        self.txt_address.setText(data[0][2])
        self.balance_type.setCurrentText(data[0][3])
        self.txt_balance.setText(str(data[0][4]))
        self.txt_balance.setReadOnly(True)
        self.balance_type.setDisabled(True)

    def add_supplier(self):
        name = self.txt_name.text()
        phone = self.txt_phone.text()
        address = self.txt_address.text()
        if not (name and phone and address):
            QMessageBox.warning(self, 'Error', 'All fields are required')
        else:
            try:
                db = DBHandler()
                db.conn.execute(
                    "UPDATE suppliers SET name=?,phone=?,address=? WHERE supplier_id=?",
                    (name, phone, address, self.id)
                )
                db.conn.commit()
                db.close()
                QMessageBox.information(self, 'Success', 'Supplier updated successfully')
                self.close()
            except Exception as e:
                QMessageBox.warning(self, 'Error', f'insertion error supplier: {e}')


    # def clear_fields(self):
    #     self.txt_name.setText('')
    #     self.txt_phone.setText('')
    #     self.txt_address.setText('')
    #     self.txt_balance.setText('')
        


def main():
    app = QApplication(sys.argv)
    window = UpdateSupplierWindow(1)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

