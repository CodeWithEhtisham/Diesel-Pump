import datetime
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from cash_received import CashReceivedWindow
from db_handler import DBHandler
import sys
from os import path
from PyQt5.uic import loadUiType

FORM_MAIN, _ = loadUiType('ui/account_details.ui')


class AccountDetailsWindow(QMainWindow, FORM_MAIN):
    def __init__(self,user_id):
        
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.user_id = user_id
        self.update_account_details()
        self.btn_refresh.clicked.connect(self.update_account_details)
        self.Handle_Buttons()
        self.db= DBHandler()
        self.lbl_account_name.setText(self.db.select(table_name="customers",columns="name",condition="custmer_id="+str(self.user_id))[0][0])

    def Handle_Buttons(self):
        self.btn_cash_received.clicked.connect(self.openCashReceivedWindow)

    def openCashReceivedWindow(self):
        self.window = CashReceivedWindow(self.user_id)
        self.window.show()

    def update_account_details(self):
        db= DBHandler()
        # get sales record where customer id = self.customer_id
        data=db.select(table_name="customer_cash_received",columns="date,description,quantity,rate,amount,cash_paid,cash_received,remaining",condition="customer_id="+str(self.user_id))
        name=db.select(table_name="customers",columns="name",condition="custmer_id="+str(self.user_id))[0][0]

        # data = db.conn.execute(f"SELECT sales.date,customers.name,sales.quantity,sales.rate,sales.total_amount,sales.cash_paid,sales.cash_received,sales.sub_total FROM sales LEFT JOIN customers ON sales.customer_id=customers.custmer_id WHERE customers.custmer_id = {self.user_id}").fetchall()
        self.roznamcha_table.setRowCount(0)
        quantity=0
        amount=0
        cash_paid=0
        cash_received=0
        remaining=0
        opening=0
        for index,row in enumerate(data):
            quantity+=row[2]
            amount+=row[4]
            cash_paid+=row[5]
            cash_received+=row[6]
            if index==0:
                opening=row[7]
            elif index==len(data)-1:
                remaining=row[7]
            # sub_total+=row[7]
            self.roznamcha_table.insertRow(index)
            for idx,i in enumerate(row):
                self.roznamcha_table.setItem(index,idx,QTableWidgetItem(str(i)))
            # if row[1]=="Cash Received":
            self.roznamcha_table.item(index,6).setForeground(QColor(255,0,0))
    
        self.label_2.setText(str(quantity))
        self.label_6.setText(str(amount))
        self.txt_total_cash_paid.setText(str(cash_paid))
        self.txt_total_cash_received.setText(str(cash_received))
        self.txt_remaining.setText(str(remaining))
        self.label_4.setText(str(opening))

        # balace = db.conn.execute(f"SELECT balance FROM customers WHERE custmer_id = {self.user_id}").fetchone()[0]
        # self.label_4.setText(str(balace))


def main():
    app = QApplication(sys.argv)
    window = AccountDetailsWindow(1)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()


# from PyQt5 import QtCore, QtGui, QtWidgets
# from PySide2 import *
# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *

# from cash_received import Ui_CashReceivedWindow


# class Ui_AccountDetailsWindow(object):

#     # Add CASH
#     def openCashReceivedWindow(self):
#         self.window = QtWidgets.QMainWindow()
#         self.ui = Ui_CashReceivedWindow()
#         self.ui.setupUi(self.window)
#         self.window.show()


#     def setupUi(self, AccountDetailsWindow):
#         AccountDetailsWindow.setObjectName("AccountDetailsWindow")
#         AccountDetailsWindow.resize(1080, 800)
#         AccountDetailsWindow.setMinimumSize(QtCore.QSize(1080, 720))
#         AccountDetailsWindow.setMaximumSize(QtCore.QSize(1080, 800))
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap(":/icons/assets/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         AccountDetailsWindow.setWindowIcon(icon)
#         AccountDetailsWindow.setIconSize(QtCore.QSize(32, 32))
#         AccountDetailsWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
#         self.centralwidget = QtWidgets.QWidget(AccountDetailsWindow)
#         self.centralwidget.setStyleSheet("* {\n"
# "    background-color: #e0f2f1;\n"
# "}\n"
# "#header_frame {\n"
# "    background-color: #80cbc4;\n"
# "}\n"
# "\n"
# "#lbl_account_name {\n"
# "    background-color: #80cbc4;\n"
# "    color: #00bcd4;\n"
# "}\n"
# "\n"
# "#lbl_accounts {\n"
# "    background-color: #80cbc4;\n"
# "}\n"
# "\n"
# "#accounts_upper_widget {\n"
# "    background-color: #4dd0e1;\n"
# "}\n"
# "\n"
# "QPushButton {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "QDateEdit {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "QLineEdit {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "")
#         self.centralwidget.setObjectName("centralwidget")
#         self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
#         self.verticalLayout.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout.setSpacing(0)
#         self.verticalLayout.setObjectName("verticalLayout")
#         self.header_frame = QtWidgets.QFrame(self.centralwidget)
#         self.header_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.header_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.header_frame.setObjectName("header_frame")
#         self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.header_frame)
#         self.horizontalLayout_4.setObjectName("horizontalLayout_4")
#         self.lbl_account_name = QtWidgets.QLabel(self.header_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(22)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_account_name.setFont(font)
#         self.lbl_account_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
#         self.lbl_account_name.setObjectName("lbl_account_name")
#         self.horizontalLayout_4.addWidget(self.lbl_account_name)
#         self.lbl_accounts = QtWidgets.QLabel(self.header_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(18)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_accounts.setFont(font)
#         self.lbl_accounts.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
#         self.lbl_accounts.setObjectName("lbl_accounts")
#         self.horizontalLayout_4.addWidget(self.lbl_accounts)
#         self.verticalLayout.addWidget(self.header_frame)
#         self.widget = QtWidgets.QWidget(self.centralwidget)
#         self.widget.setLayoutDirection(QtCore.Qt.LeftToRight)
#         self.widget.setObjectName("widget")
#         self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget)
#         self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_3.setSpacing(0)
#         self.horizontalLayout_3.setObjectName("horizontalLayout_3")
#         self.frame_2 = QtWidgets.QFrame(self.widget)
#         self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame_2.setObjectName("frame_2")
#         self.horizontalLayout_3.addWidget(self.frame_2)
#         self.frame = QtWidgets.QFrame(self.widget)
#         self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame.setObjectName("frame")
#         self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame)
#         self.horizontalLayout_2.setObjectName("horizontalLayout_2")
#         self.label_3 = QtWidgets.QLabel(self.frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         self.label_3.setFont(font)
#         self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
#         self.label_3.setObjectName("label_3")
#         self.horizontalLayout_2.addWidget(self.label_3)
#         self.label_4 = QtWidgets.QLabel(self.frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(18)
#         font.setBold(True)
#         font.setWeight(75)
#         self.label_4.setFont(font)
#         self.label_4.setFrameShape(QtWidgets.QFrame.Box)
#         self.label_4.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.label_4.setObjectName("label_4")
#         self.horizontalLayout_2.addWidget(self.label_4)
#         self.horizontalLayout_3.addWidget(self.frame)
#         self.verticalLayout.addWidget(self.widget)
#         self.accounts_upper_widget = QtWidgets.QWidget(self.centralwidget)
#         self.accounts_upper_widget.setObjectName("accounts_upper_widget")
#         self.horizontalLayout = QtWidgets.QHBoxLayout(self.accounts_upper_widget)
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         self.btn_cash_received = QtWidgets.QPushButton(self.accounts_upper_widget, clicked = lambda: self.openCashReceivedWindow())
#         self.btn_cash_received.setMinimumSize(QtCore.QSize(0, 40))
#         self.btn_cash_received.setMaximumSize(QtCore.QSize(16777215, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_cash_received.setFont(font)
#         icon1 = QtGui.QIcon()
#         icon1.addPixmap(QtGui.QPixmap(":/icons/assets/icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_cash_received.setIcon(icon1)
#         self.btn_cash_received.setIconSize(QtCore.QSize(32, 32))
#         self.btn_cash_received.setObjectName("btn_cash_received")
#         self.horizontalLayout.addWidget(self.btn_cash_received)
#         self.txt_search = QtWidgets.QLineEdit(self.accounts_upper_widget)
#         self.txt_search.setMinimumSize(QtCore.QSize(400, 40))
#         self.txt_search.setMaximumSize(QtCore.QSize(400, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_search.setFont(font)
#         self.txt_search.setObjectName("txt_search")
#         self.horizontalLayout.addWidget(self.txt_search)
#         self.txt_search_date = QtWidgets.QDateEdit(self.accounts_upper_widget)
#         self.txt_search_date.setMinimumSize(QtCore.QSize(150, 40))
#         self.txt_search_date.setMaximumSize(QtCore.QSize(150, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(False)
#         font.setWeight(50)
#         self.txt_search_date.setFont(font)
#         self.txt_search_date.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 1), QtCore.QTime(0, 0, 0)))
#         self.txt_search_date.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
#         self.txt_search_date.setCalendarPopup(True)
#         self.txt_search_date.setObjectName("txt_search_date")
#         self.horizontalLayout.addWidget(self.txt_search_date)
#         self.btn_search = QtWidgets.QPushButton(self.accounts_upper_widget)
#         self.btn_search.setMinimumSize(QtCore.QSize(50, 40))
#         self.btn_search.setMaximumSize(QtCore.QSize(50, 40))
#         self.btn_search.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         self.btn_search.setText("")
#         icon2 = QtGui.QIcon()
#         icon2.addPixmap(QtGui.QPixmap(":/icons/assets/icons/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_search.setIcon(icon2)
#         self.btn_search.setIconSize(QtCore.QSize(32, 32))
#         self.btn_search.setObjectName("btn_search")
#         self.horizontalLayout.addWidget(self.btn_search)
#         self.btn_print = QtWidgets.QPushButton(self.accounts_upper_widget)
#         self.btn_print.setMinimumSize(QtCore.QSize(40, 40))
#         self.btn_print.setMaximumSize(QtCore.QSize(40, 40))
#         self.btn_print.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         self.btn_print.setText("")
#         icon3 = QtGui.QIcon()
#         icon3.addPixmap(QtGui.QPixmap(":/icons/assets/icons/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_print.setIcon(icon3)
#         self.btn_print.setIconSize(QtCore.QSize(32, 32))
#         self.btn_print.setObjectName("btn_print")
#         self.horizontalLayout.addWidget(self.btn_print, 0, QtCore.Qt.AlignRight)
#         self.btn_refresh = QtWidgets.QPushButton(self.accounts_upper_widget)
#         self.btn_refresh.setMinimumSize(QtCore.QSize(40, 40))
#         self.btn_refresh.setMaximumSize(QtCore.QSize(40, 40))
#         self.btn_refresh.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         self.btn_refresh.setText("")
#         icon4 = QtGui.QIcon()
#         icon4.addPixmap(QtGui.QPixmap(":/icons/assets/icons/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_refresh.setIcon(icon4)
#         self.btn_refresh.setIconSize(QtCore.QSize(32, 32))
#         self.btn_refresh.setObjectName("btn_refresh")
#         self.horizontalLayout.addWidget(self.btn_refresh)
#         self.verticalLayout.addWidget(self.accounts_upper_widget)
#         self.roznamcha_table = QtWidgets.QTableWidget(self.centralwidget)
#         self.roznamcha_table.setMinimumSize(QtCore.QSize(0, 0))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.roznamcha_table.setFont(font)
#         self.roznamcha_table.setLayoutDirection(QtCore.Qt.LeftToRight)
#         self.roznamcha_table.setAutoFillBackground(False)
#         self.roznamcha_table.setFrameShape(QtWidgets.QFrame.NoFrame)
#         self.roznamcha_table.setMidLineWidth(0)
#         self.roznamcha_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
#         self.roznamcha_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
#         self.roznamcha_table.setAlternatingRowColors(False)
#         self.roznamcha_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
#         self.roznamcha_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
#         self.roznamcha_table.setCornerButtonEnabled(True)
#         self.roznamcha_table.setRowCount(15)
#         self.roznamcha_table.setObjectName("roznamcha_table")
#         self.roznamcha_table.setColumnCount(8)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.roznamcha_table.setHorizontalHeaderItem(0, item)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.roznamcha_table.setHorizontalHeaderItem(1, item)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.roznamcha_table.setHorizontalHeaderItem(2, item)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.roznamcha_table.setHorizontalHeaderItem(3, item)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.roznamcha_table.setHorizontalHeaderItem(4, item)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         item.setForeground(brush)
#         self.roznamcha_table.setHorizontalHeaderItem(5, item)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.roznamcha_table.setHorizontalHeaderItem(6, item)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.roznamcha_table.setHorizontalHeaderItem(7, item)
#         self.roznamcha_table.horizontalHeader().setVisible(True)
#         self.roznamcha_table.horizontalHeader().setCascadingSectionResizes(False)
#         self.roznamcha_table.horizontalHeader().setDefaultSectionSize(120)
#         self.roznamcha_table.horizontalHeader().setHighlightSections(True)
#         self.roznamcha_table.horizontalHeader().setMinimumSectionSize(30)
#         self.roznamcha_table.horizontalHeader().setSortIndicatorShown(True)
#         self.roznamcha_table.horizontalHeader().setStretchLastSection(False)
#         self.roznamcha_table.verticalHeader().setVisible(True)
#         self.roznamcha_table.verticalHeader().setCascadingSectionResizes(False)
#         self.roznamcha_table.verticalHeader().setDefaultSectionSize(30)
#         self.roznamcha_table.verticalHeader().setMinimumSectionSize(30)
#         self.roznamcha_table.verticalHeader().setSortIndicatorShown(True)
#         self.roznamcha_table.verticalHeader().setStretchLastSection(False)
#         self.verticalLayout.addWidget(self.roznamcha_table)
#         self.bottom_widget = QtWidgets.QWidget(self.centralwidget)
#         self.bottom_widget.setObjectName("bottom_widget")
#         self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.bottom_widget)
#         self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_3.setSpacing(1)
#         self.verticalLayout_3.setObjectName("verticalLayout_3")
#         self.totals_frame = QtWidgets.QFrame(self.bottom_widget)
#         self.totals_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.totals_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.totals_frame.setObjectName("totals_frame")
#         self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.totals_frame)
#         self.horizontalLayout_9.setSpacing(20)
#         self.horizontalLayout_9.setObjectName("horizontalLayout_9")
#         self.lbl_total = QtWidgets.QLabel(self.totals_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_total.setFont(font)
#         self.lbl_total.setObjectName("lbl_total")
#         self.horizontalLayout_9.addWidget(self.lbl_total)
#         self.label = QtWidgets.QLabel(self.totals_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.label.setFont(font)
#         self.label.setObjectName("label")
#         self.horizontalLayout_9.addWidget(self.label, 0, QtCore.Qt.AlignRight)
#         self.label_2 = QtWidgets.QLabel(self.totals_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.label_2.setFont(font)
#         self.label_2.setFrameShape(QtWidgets.QFrame.Box)
#         self.label_2.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.label_2.setObjectName("label_2")
#         self.horizontalLayout_9.addWidget(self.label_2, 0, QtCore.Qt.AlignLeft)
#         self.label_5 = QtWidgets.QLabel(self.totals_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.label_5.setFont(font)
#         self.label_5.setObjectName("label_5")
#         self.horizontalLayout_9.addWidget(self.label_5, 0, QtCore.Qt.AlignRight)
#         self.label_6 = QtWidgets.QLabel(self.totals_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.label_6.setFont(font)
#         self.label_6.setFrameShape(QtWidgets.QFrame.Box)
#         self.label_6.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.label_6.setObjectName("label_6")
#         self.horizontalLayout_9.addWidget(self.label_6, 0, QtCore.Qt.AlignLeft)
#         self.lbl_cash_paid = QtWidgets.QLabel(self.totals_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_cash_paid.setFont(font)
#         self.lbl_cash_paid.setObjectName("lbl_cash_paid")
#         self.horizontalLayout_9.addWidget(self.lbl_cash_paid, 0, QtCore.Qt.AlignRight)
#         self.txt_total_cash_paid = QtWidgets.QLabel(self.totals_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_total_cash_paid.setFont(font)
#         self.txt_total_cash_paid.setFrameShape(QtWidgets.QFrame.Box)
#         self.txt_total_cash_paid.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.txt_total_cash_paid.setObjectName("txt_total_cash_paid")
#         self.horizontalLayout_9.addWidget(self.txt_total_cash_paid, 0, QtCore.Qt.AlignLeft)
#         self.lbl_cash_received = QtWidgets.QLabel(self.totals_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_cash_received.setFont(font)
#         self.lbl_cash_received.setObjectName("lbl_cash_received")
#         self.horizontalLayout_9.addWidget(self.lbl_cash_received, 0, QtCore.Qt.AlignRight)
#         self.txt_total_cash_received = QtWidgets.QLabel(self.totals_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_total_cash_received.setFont(font)
#         self.txt_total_cash_received.setFrameShape(QtWidgets.QFrame.Box)
#         self.txt_total_cash_received.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.txt_total_cash_received.setObjectName("txt_total_cash_received")
#         self.horizontalLayout_9.addWidget(self.txt_total_cash_received, 0, QtCore.Qt.AlignLeft)
#         self.lbl_remaining = QtWidgets.QLabel(self.totals_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_remaining.setFont(font)
#         self.lbl_remaining.setObjectName("lbl_remaining")
#         self.horizontalLayout_9.addWidget(self.lbl_remaining, 0, QtCore.Qt.AlignRight)
#         self.txt_remaining = QtWidgets.QLabel(self.totals_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_remaining.setFont(font)
#         self.txt_remaining.setFrameShape(QtWidgets.QFrame.Box)
#         self.txt_remaining.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.txt_remaining.setObjectName("txt_remaining")
#         self.horizontalLayout_9.addWidget(self.txt_remaining, 0, QtCore.Qt.AlignLeft)
#         self.verticalLayout_3.addWidget(self.totals_frame)
#         self.verticalLayout.addWidget(self.bottom_widget)
#         AccountDetailsWindow.setCentralWidget(self.centralwidget)
#         self.statusbar = QtWidgets.QStatusBar(AccountDetailsWindow)
#         self.statusbar.setObjectName("statusbar")
#         AccountDetailsWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(AccountDetailsWindow)
#         QtCore.QMetaObject.connectSlotsByName(AccountDetailsWindow)

#     def retranslateUi(self, AccountDetailsWindow):
#         _translate = QtCore.QCoreApplication.translate
#         AccountDetailsWindow.setWindowTitle(_translate("AccountDetailsWindow", "Account Details"))
#         self.lbl_account_name.setText(_translate("AccountDetailsWindow", "Name"))
#         self.lbl_accounts.setText(_translate("AccountDetailsWindow", "Accounts"))
#         self.label_3.setText(_translate("AccountDetailsWindow", "Opening Balance"))
#         self.label_4.setText(_translate("AccountDetailsWindow", "00"))
#         self.btn_cash_received.setText(_translate("AccountDetailsWindow", "Cash Received"))
#         self.roznamcha_table.setSortingEnabled(True)
#         item = self.roznamcha_table.horizontalHeaderItem(0)
#         item.setText(_translate("AccountDetailsWindow", "Date"))
#         item = self.roznamcha_table.horizontalHeaderItem(1)
#         item.setText(_translate("AccountDetailsWindow", "Description"))
#         item = self.roznamcha_table.horizontalHeaderItem(2)
#         item.setText(_translate("AccountDetailsWindow", "Quantity"))
#         item = self.roznamcha_table.horizontalHeaderItem(3)
#         item.setText(_translate("AccountDetailsWindow", "Rate"))
#         item = self.roznamcha_table.horizontalHeaderItem(4)
#         item.setText(_translate("AccountDetailsWindow", "Total Amount"))
#         item = self.roznamcha_table.horizontalHeaderItem(5)
#         item.setText(_translate("AccountDetailsWindow", "Cash Paid"))
#         item = self.roznamcha_table.horizontalHeaderItem(6)
#         item.setText(_translate("AccountDetailsWindow", "Cash Received"))
#         item = self.roznamcha_table.horizontalHeaderItem(7)
#         item.setText(_translate("AccountDetailsWindow", "Remaining"))
#         self.lbl_total.setText(_translate("AccountDetailsWindow", "Total"))
#         self.label.setText(_translate("AccountDetailsWindow", "Quantity :"))
#         self.label_2.setText(_translate("AccountDetailsWindow", "00"))
#         self.label_5.setText(_translate("AccountDetailsWindow", "Amount :"))
#         self.label_6.setText(_translate("AccountDetailsWindow", "00"))
#         self.lbl_cash_paid.setText(_translate("AccountDetailsWindow", "Cash Paid :"))
#         self.txt_total_cash_paid.setText(_translate("AccountDetailsWindow", "00"))
#         self.lbl_cash_received.setText(_translate("AccountDetailsWindow", "Cash Received :"))
#         self.txt_total_cash_received.setText(_translate("AccountDetailsWindow", "00"))
#         self.lbl_remaining.setText(_translate("AccountDetailsWindow", "Remaining :"))
#         self.txt_remaining.setText(_translate("AccountDetailsWindow", "00"))
# import resources_rc


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     AccountDetailsWindow = QtWidgets.QMainWindow()
#     ui = Ui_AccountDetailsWindow()
#     ui.setupUi(AccountDetailsWindow)
#     AccountDetailsWindow.show()
#     sys.exit(app.exec_())
