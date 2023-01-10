
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
FORM_MAIN, _ = loadUiType('ui/add_product.ui')


class AddProductWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()

    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.Save_Product)
        self.btn_clear.clicked.connect(self.Clear_Fields)
        self.btn_cancel.clicked.connect(self.close)

    def Save_Product(self):
        product_name = self.txt_product_name.text()
        uom = self.txt_uom.text()

        if product_name == '' or uom == '':
            QMessageBox.warning(self, "Warning", "All fields are required")
        else:
            try:
                db=DBHandler()
                db.insert(table_name='products',columns='product_name, uom', values=f"'{product_name}', '{uom}'")
                db.close()
                # self.Clear_Fields()
                self.close()
                
            except Exception:
                QMessageBox.warning(self, "Warning", "Product has not been added")
    
    def Clear_Fields(self):
        self.txt_product_name.setText('')
        self.txt_uom.setText('')



def main():
    app = QApplication(sys.argv)
    window = AddProductWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

