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

FORM_MAIN, _ = loadUiType('ui/cash_received.ui')


class CashReceivedWindow(QMainWindow, FORM_MAIN):
    def __init__(self,user_id):
        
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.user_id = user_id
        self.Handle_Buttons()
        self.txt_date.setDate(QDate.currentDate())
        self.db=DBHandler()
        self.txt_name.setText(self.db.select(table_name='customers',columns='name',condition=f"custmer_id = {self.user_id}")[0][0])
        self.txt_previous.setText(str(self.db.select(table_name='customers',columns='balance',condition=f"custmer_id = {self.user_id}")[0][0]))
        self.txt_amount.textChanged.connect(self.Calculate_Remaining)

    def Calculate_Remaining(self):
        amount = self.txt_amount.text()
        previous = self.txt_previous.text()
        if amount == '' or previous == '':
            self.txt_remaining.setText('')
        else:
            try:
                # if float(previous)>=0:
                #     remaining = float(previous) + float(amount)
                # else:
                #     remaining = float(amount)+float(previous)
                self.txt_remaining.setText(str(round(float(previous) - float(amount),2)))
            except Exception as e:
                print(f"Error: {e}")
                self.txt_remaining.setText('')

    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.Save)
        self.btn_clear.clicked.connect(self.Clear_fileds)
        self.btn_cancel.clicked.connect(self.close)

    def Save(self):
        name = self.txt_name.text()
        date = self.txt_date.text()
        amount = self.txt_amount.text()
        previous = self.txt_previous.text()
        remaining = self.txt_remaining.text()

        if name == '' or date == '' or amount == '' or previous == '' or remaining == '':
            QMessageBox.warning(self, 'Data Error', 'Please Fill All Fields')
            return
        else:
            try:
                amount = float(amount)
                previous = float(previous)
                remaining = float(remaining)
                self.db.conn.execute(f"INSERT INTO customer_cash_received (customer_id, date, cash_received, remaining) VALUES ({self.user_id}, '{date}', {amount},{remaining})")
                self.db.conn.execute(f"UPDATE customers SET balance = {remaining} WHERE custmer_id = {self.user_id}")
                self.db.conn.commit()
                QMessageBox.information(self, 'Data Saved', 'Data Saved Successfully')
                self.close()
            except Exception as e:
                QMessageBox.warning(self, 'Data Error', f'Please Enter Valid Amount {e}')
                return
            
    def Clear_fileds(self):
        # self.txt_name.setText('')
        self.txt_name.setText(self.db.select(table_name='customers',columns='name',condition=f"custmer_id = {self.user_id}")[0][0])
        self.txt_previous.setText(str(self.db.select(table_name='customers',columns='balance',condition=f"custmer_id = {self.user_id}")[0][0]))
        self.txt_date.setDate(QDate.currentDate())
        self.txt_amount.setText('')
        # self.txt_previous.setText('')
        self.txt_remaining.setText('')
    
        

def main():
    app = QApplication(sys.argv)
    window = CashReceivedWindow(1)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

