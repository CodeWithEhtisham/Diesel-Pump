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
from cash_paid import CashPaidWindow
FORM_MAIN, _ = loadUiType('ui/supplier_account_details.ui')


class SupplierAccountDetailsWindow(QMainWindow, FORM_MAIN):
    def __init__(self,id):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.user_id=id
        self.btn_cash_paid.clicked.connect(self.cash_paids)
        self.fill_table()
        # self.Handle_Buttons()
        
    def fill_table(self):
        self.supplier_account_table.setRowCount(0)
        db=DBHandler()
        data=db.select(table_name="supplier_cash_paid",columns="date,description,quantity,rate,amount,cash_paid,remaining",condition="supplier_id="+str(self.user_id))
        for row_number,row_data in enumerate(data):
            self.supplier_account_table.insertRow(row_number)
            for column_number,data in enumerate(row_data):
                self.supplier_account_table.setItem(row_number,column_number,QTableWidgetItem(str(data)))

    def cash_paids(self):
        self.cash_paid_window=CashPaidWindow(1)
        self.cash_paid_window.show()
        # self.cash_paid_window.exec_()
        # self.fill_table()

def main():
    app = QApplication(sys.argv)
    window = SupplierAccountDetailsWindow(0)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()









# # -*- coding: utf-8 -*-

# ################################################################################
# ## Form generated from reading UI file 'supplier_account_details.ui'
# ##
# ## Created by: Qt User Interface Compiler version 5.15.2
# ##
# ## WARNING! All changes made in this file will be lost when recompiling UI file!
# ################################################################################

# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *

# import resources_rc

# class Ui_AccountDetailsWindow(object):
#     def setupUi(self, AccountDetailsWindow):
#         if not AccountDetailsWindow.objectName():
#             AccountDetailsWindow.setObjectName(u"AccountDetailsWindow")
#         AccountDetailsWindow.resize(1193, 720)
#         AccountDetailsWindow.setMinimumSize(QSize(0, 720))
#         AccountDetailsWindow.setMaximumSize(QSize(16777215, 16777215))
#         icon = QIcon()
#         icon.addFile(u":/icons/assets/icons/logo.png", QSize(), QIcon.Normal, QIcon.Off)
#         AccountDetailsWindow.setWindowIcon(icon)
#         AccountDetailsWindow.setIconSize(QSize(32, 32))
#         AccountDetailsWindow.setTabShape(QTabWidget.Rounded)
#         self.centralwidget = QWidget(AccountDetailsWindow)
#         self.centralwidget.setObjectName(u"centralwidget")
#         self.centralwidget.setStyleSheet(u"* {\n"
# "	background-color: #e0f2f1;\n"
# "}\n"
# "#header_frame {\n"
# "	background-color: #80cbc4;\n"
# "}\n"
# "\n"
# "#lbl_account_name {\n"
# "	background-color: #80cbc4;\n"
# "	color: #00bcd4;\n"
# "}\n"
# "\n"
# "#lbl_accounts {\n"
# "	background-color: #80cbc4;\n"
# "}\n"
# "\n"
# "#accounts_upper_widget {\n"
# "	background-color: #4dd0e1;\n"
# "}\n"
# "\n"
# "QPushButton {\n"
# "	background-color: #fff;\n"
# "	border-radius: 5px;\n"
# "}\n"
# "\n"
# "QDateEdit {\n"
# "	background-color: #fff;\n"
# "	border-radius: 5px;\n"
# "}\n"
# "\n"
# "QLineEdit {\n"
# "	background-color: #fff;\n"
# "	border-radius: 5px;\n"
# "}\n"
# "")
#         self.verticalLayout = QVBoxLayout(self.centralwidget)
#         self.verticalLayout.setSpacing(0)
#         self.verticalLayout.setObjectName(u"verticalLayout")
#         self.verticalLayout.setContentsMargins(0, 0, 0, 0)
#         self.header_frame = QFrame(self.centralwidget)
#         self.header_frame.setObjectName(u"header_frame")
#         self.header_frame.setFrameShape(QFrame.StyledPanel)
#         self.header_frame.setFrameShadow(QFrame.Raised)
#         self.horizontalLayout_4 = QHBoxLayout(self.header_frame)
#         self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
#         self.lbl_account_name = QLabel(self.header_frame)
#         self.lbl_account_name.setObjectName(u"lbl_account_name")
#         font = QFont()
#         font.setFamily(u"Calibri")
#         font.setPointSize(22)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_account_name.setFont(font)
#         self.lbl_account_name.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

#         self.horizontalLayout_4.addWidget(self.lbl_account_name)

#         self.lbl_accounts = QLabel(self.header_frame)
#         self.lbl_accounts.setObjectName(u"lbl_accounts")
#         font1 = QFont()
#         font1.setFamily(u"Calibri")
#         font1.setPointSize(18)
#         font1.setBold(True)
#         font1.setWeight(75)
#         self.lbl_accounts.setFont(font1)
#         self.lbl_accounts.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

#         self.horizontalLayout_4.addWidget(self.lbl_accounts)


#         self.verticalLayout.addWidget(self.header_frame)

#         self.widget = QWidget(self.centralwidget)
#         self.widget.setObjectName(u"widget")
#         self.widget.setLayoutDirection(Qt.LeftToRight)
#         self.horizontalLayout_3 = QHBoxLayout(self.widget)
#         self.horizontalLayout_3.setSpacing(0)
#         self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
#         self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
#         self.frame_2 = QFrame(self.widget)
#         self.frame_2.setObjectName(u"frame_2")
#         self.frame_2.setFrameShape(QFrame.StyledPanel)
#         self.frame_2.setFrameShadow(QFrame.Raised)

#         self.horizontalLayout_3.addWidget(self.frame_2)

#         self.frame = QFrame(self.widget)
#         self.frame.setObjectName(u"frame")
#         self.frame.setFrameShape(QFrame.StyledPanel)
#         self.frame.setFrameShadow(QFrame.Raised)
#         self.horizontalLayout_2 = QHBoxLayout(self.frame)
#         self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
#         self.label_3 = QLabel(self.frame)
#         self.label_3.setObjectName(u"label_3")
#         font2 = QFont()
#         font2.setFamily(u"Calibri")
#         font2.setPointSize(16)
#         self.label_3.setFont(font2)
#         self.label_3.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

#         self.horizontalLayout_2.addWidget(self.label_3)

#         self.label_4 = QLabel(self.frame)
#         self.label_4.setObjectName(u"label_4")
#         self.label_4.setFont(font1)
#         self.label_4.setFrameShape(QFrame.Box)
#         self.label_4.setFrameShadow(QFrame.Raised)

#         self.horizontalLayout_2.addWidget(self.label_4)


#         self.horizontalLayout_3.addWidget(self.frame)


#         self.verticalLayout.addWidget(self.widget)

#         self.accounts_upper_widget = QWidget(self.centralwidget)
#         self.accounts_upper_widget.setObjectName(u"accounts_upper_widget")
#         self.horizontalLayout = QHBoxLayout(self.accounts_upper_widget)
#         self.horizontalLayout.setObjectName(u"horizontalLayout")
#         self.btn_cash_paid = QPushButton(self.accounts_upper_widget)
#         self.btn_cash_paid.setObjectName(u"btn_cash_paid")
#         self.btn_cash_paid.setMinimumSize(QSize(0, 40))
#         self.btn_cash_paid.setMaximumSize(QSize(16777215, 40))
#         font3 = QFont()
#         font3.setFamily(u"Calibri")
#         font3.setPointSize(14)
#         font3.setBold(True)
#         font3.setWeight(75)
#         self.btn_cash_paid.setFont(font3)
#         icon1 = QIcon()
#         icon1.addFile(u":/icons/assets/icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
#         self.btn_cash_paid.setIcon(icon1)
#         self.btn_cash_paid.setIconSize(QSize(32, 32))

#         self.horizontalLayout.addWidget(self.btn_cash_paid)

#         self.txt_search = QLineEdit(self.accounts_upper_widget)
#         self.txt_search.setObjectName(u"txt_search")
#         self.txt_search.setMinimumSize(QSize(400, 40))
#         self.txt_search.setMaximumSize(QSize(400, 40))
#         font4 = QFont()
#         font4.setFamily(u"Calibri")
#         font4.setPointSize(14)
#         self.txt_search.setFont(font4)

#         self.horizontalLayout.addWidget(self.txt_search)

#         self.txt_search_date = QDateEdit(self.accounts_upper_widget)
#         self.txt_search_date.setObjectName(u"txt_search_date")
#         self.txt_search_date.setMinimumSize(QSize(150, 40))
#         self.txt_search_date.setMaximumSize(QSize(150, 40))
#         font5 = QFont()
#         font5.setFamily(u"Calibri")
#         font5.setPointSize(14)
#         font5.setBold(False)
#         font5.setWeight(50)
#         self.txt_search_date.setFont(font5)
#         self.txt_search_date.setDateTime(QDateTime(QDate(2022, 1, 1), QTime(0, 0, 0)))
#         self.txt_search_date.setCurrentSection(QDateTimeEdit.DaySection)
#         self.txt_search_date.setCalendarPopup(True)

#         self.horizontalLayout.addWidget(self.txt_search_date)

#         self.btn_search = QPushButton(self.accounts_upper_widget)
#         self.btn_search.setObjectName(u"btn_search")
#         self.btn_search.setMinimumSize(QSize(50, 40))
#         self.btn_search.setMaximumSize(QSize(50, 40))
#         self.btn_search.setCursor(QCursor(Qt.OpenHandCursor))
#         icon2 = QIcon()
#         icon2.addFile(u":/icons/assets/icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
#         self.btn_search.setIcon(icon2)
#         self.btn_search.setIconSize(QSize(32, 32))

#         self.horizontalLayout.addWidget(self.btn_search)

#         self.btn_print = QPushButton(self.accounts_upper_widget)
#         self.btn_print.setObjectName(u"btn_print")
#         self.btn_print.setMinimumSize(QSize(40, 40))
#         self.btn_print.setMaximumSize(QSize(40, 40))
#         self.btn_print.setCursor(QCursor(Qt.OpenHandCursor))
#         icon3 = QIcon()
#         icon3.addFile(u":/icons/assets/icons/print.png", QSize(), QIcon.Normal, QIcon.Off)
#         self.btn_print.setIcon(icon3)
#         self.btn_print.setIconSize(QSize(32, 32))

#         self.horizontalLayout.addWidget(self.btn_print, 0, Qt.AlignRight)

#         self.btn_refresh = QPushButton(self.accounts_upper_widget)
#         self.btn_refresh.setObjectName(u"btn_refresh")
#         self.btn_refresh.setMinimumSize(QSize(40, 40))
#         self.btn_refresh.setMaximumSize(QSize(40, 40))
#         self.btn_refresh.setCursor(QCursor(Qt.OpenHandCursor))
#         icon4 = QIcon()
#         icon4.addFile(u":/icons/assets/icons/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
#         self.btn_refresh.setIcon(icon4)
#         self.btn_refresh.setIconSize(QSize(32, 32))

#         self.horizontalLayout.addWidget(self.btn_refresh)


#         self.verticalLayout.addWidget(self.accounts_upper_widget)

#         self.roznamcha_table = QTableWidget(self.centralwidget)
#         if (self.roznamcha_table.columnCount() < 7):
#             self.roznamcha_table.setColumnCount(7)
#         __qtablewidgetitem = QTableWidgetItem()
#         __qtablewidgetitem.setFont(font3);
#         self.roznamcha_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
#         __qtablewidgetitem1 = QTableWidgetItem()
#         __qtablewidgetitem1.setFont(font3);
#         self.roznamcha_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
#         __qtablewidgetitem2 = QTableWidgetItem()
#         __qtablewidgetitem2.setFont(font3);
#         self.roznamcha_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
#         __qtablewidgetitem3 = QTableWidgetItem()
#         __qtablewidgetitem3.setFont(font3);
#         self.roznamcha_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
#         __qtablewidgetitem4 = QTableWidgetItem()
#         __qtablewidgetitem4.setFont(font3);
#         self.roznamcha_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
#         brush = QBrush(QColor(0, 0, 0, 255))
#         brush.setStyle(Qt.SolidPattern)
#         __qtablewidgetitem5 = QTableWidgetItem()
#         __qtablewidgetitem5.setFont(font3);
#         __qtablewidgetitem5.setForeground(brush);
#         self.roznamcha_table.setHorizontalHeaderItem(5, __qtablewidgetitem5)
#         __qtablewidgetitem6 = QTableWidgetItem()
#         __qtablewidgetitem6.setFont(font3);
#         self.roznamcha_table.setHorizontalHeaderItem(6, __qtablewidgetitem6)
#         if (self.roznamcha_table.rowCount() < 15):
#             self.roznamcha_table.setRowCount(15)
#         self.roznamcha_table.setObjectName(u"roznamcha_table")
#         self.roznamcha_table.setMinimumSize(QSize(0, 0))
#         self.roznamcha_table.setFont(font4)
#         self.roznamcha_table.setLayoutDirection(Qt.LeftToRight)
#         self.roznamcha_table.setAutoFillBackground(False)
#         self.roznamcha_table.setFrameShape(QFrame.NoFrame)
#         self.roznamcha_table.setMidLineWidth(0)
#         self.roznamcha_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
#         self.roznamcha_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
#         self.roznamcha_table.setAlternatingRowColors(False)
#         self.roznamcha_table.setSelectionMode(QAbstractItemView.SingleSelection)
#         self.roznamcha_table.setSelectionBehavior(QAbstractItemView.SelectRows)
#         self.roznamcha_table.setSortingEnabled(True)
#         self.roznamcha_table.setCornerButtonEnabled(True)
#         self.roznamcha_table.setRowCount(15)
#         self.roznamcha_table.horizontalHeader().setVisible(True)
#         self.roznamcha_table.horizontalHeader().setCascadingSectionResizes(False)
#         self.roznamcha_table.horizontalHeader().setMinimumSectionSize(30)
#         self.roznamcha_table.horizontalHeader().setDefaultSectionSize(150)
#         self.roznamcha_table.horizontalHeader().setHighlightSections(True)
#         self.roznamcha_table.horizontalHeader().setProperty("showSortIndicator", True)
#         self.roznamcha_table.horizontalHeader().setStretchLastSection(False)
#         self.roznamcha_table.verticalHeader().setVisible(True)
#         self.roznamcha_table.verticalHeader().setCascadingSectionResizes(False)
#         self.roznamcha_table.verticalHeader().setMinimumSectionSize(30)
#         self.roznamcha_table.verticalHeader().setDefaultSectionSize(30)
#         self.roznamcha_table.verticalHeader().setProperty("showSortIndicator", True)
#         self.roznamcha_table.verticalHeader().setStretchLastSection(False)

#         self.verticalLayout.addWidget(self.roznamcha_table)

#         self.bottom_widget = QWidget(self.centralwidget)
#         self.bottom_widget.setObjectName(u"bottom_widget")
#         self.verticalLayout_3 = QVBoxLayout(self.bottom_widget)
#         self.verticalLayout_3.setSpacing(1)
#         self.verticalLayout_3.setObjectName(u"verticalLayout_3")
#         self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
#         self.totals_frame = QFrame(self.bottom_widget)
#         self.totals_frame.setObjectName(u"totals_frame")
#         self.totals_frame.setFrameShape(QFrame.StyledPanel)
#         self.totals_frame.setFrameShadow(QFrame.Raised)
#         self.horizontalLayout_9 = QHBoxLayout(self.totals_frame)
#         self.horizontalLayout_9.setSpacing(20)
#         self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
#         self.lbl_total = QLabel(self.totals_frame)
#         self.lbl_total.setObjectName(u"lbl_total")
#         font6 = QFont()
#         font6.setFamily(u"Calibri")
#         font6.setPointSize(16)
#         font6.setBold(True)
#         font6.setWeight(75)
#         self.lbl_total.setFont(font6)

#         self.horizontalLayout_9.addWidget(self.lbl_total)

#         self.label = QLabel(self.totals_frame)
#         self.label.setObjectName(u"label")
#         font7 = QFont()
#         font7.setFamily(u"Calibri Light")
#         font7.setPointSize(16)
#         font7.setBold(True)
#         font7.setWeight(75)
#         self.label.setFont(font7)

#         self.horizontalLayout_9.addWidget(self.label, 0, Qt.AlignRight)

#         self.label_2 = QLabel(self.totals_frame)
#         self.label_2.setObjectName(u"label_2")
#         self.label_2.setFont(font6)
#         self.label_2.setFrameShape(QFrame.Box)
#         self.label_2.setFrameShadow(QFrame.Raised)
#         self.label_2.setMargin(0)

#         self.horizontalLayout_9.addWidget(self.label_2, 0, Qt.AlignLeft)

#         self.label_5 = QLabel(self.totals_frame)
#         self.label_5.setObjectName(u"label_5")
#         self.label_5.setFont(font7)

#         self.horizontalLayout_9.addWidget(self.label_5, 0, Qt.AlignRight)

#         self.label_6 = QLabel(self.totals_frame)
#         self.label_6.setObjectName(u"label_6")
#         self.label_6.setFont(font6)
#         self.label_6.setFrameShape(QFrame.Box)
#         self.label_6.setFrameShadow(QFrame.Raised)

#         self.horizontalLayout_9.addWidget(self.label_6, 0, Qt.AlignLeft)

#         self.lbl_cash_paid = QLabel(self.totals_frame)
#         self.lbl_cash_paid.setObjectName(u"lbl_cash_paid")
#         self.lbl_cash_paid.setFont(font7)

#         self.horizontalLayout_9.addWidget(self.lbl_cash_paid, 0, Qt.AlignRight)

#         self.txt_total_cash_paid = QLabel(self.totals_frame)
#         self.txt_total_cash_paid.setObjectName(u"txt_total_cash_paid")
#         self.txt_total_cash_paid.setFont(font6)
#         self.txt_total_cash_paid.setFrameShape(QFrame.Box)
#         self.txt_total_cash_paid.setFrameShadow(QFrame.Raised)

#         self.horizontalLayout_9.addWidget(self.txt_total_cash_paid, 0, Qt.AlignLeft)

#         self.lbl_cash_received = QLabel(self.totals_frame)
#         self.lbl_cash_received.setObjectName(u"lbl_cash_received")
#         self.lbl_cash_received.setFont(font7)

#         self.horizontalLayout_9.addWidget(self.lbl_cash_received, 0, Qt.AlignRight)

#         self.txt_total_cash_received = QLabel(self.totals_frame)
#         self.txt_total_cash_received.setObjectName(u"txt_total_cash_received")
#         self.txt_total_cash_received.setFont(font6)
#         self.txt_total_cash_received.setFrameShape(QFrame.Box)
#         self.txt_total_cash_received.setFrameShadow(QFrame.Raised)

#         self.horizontalLayout_9.addWidget(self.txt_total_cash_received, 0, Qt.AlignLeft)

#         self.lbl_remaining = QLabel(self.totals_frame)
#         self.lbl_remaining.setObjectName(u"lbl_remaining")
#         self.lbl_remaining.setFont(font7)

#         self.horizontalLayout_9.addWidget(self.lbl_remaining, 0, Qt.AlignRight)

#         self.txt_remaining = QLabel(self.totals_frame)
#         self.txt_remaining.setObjectName(u"txt_remaining")
#         self.txt_remaining.setFont(font6)
#         self.txt_remaining.setFrameShape(QFrame.Box)
#         self.txt_remaining.setFrameShadow(QFrame.Raised)

#         self.horizontalLayout_9.addWidget(self.txt_remaining, 0, Qt.AlignLeft)


#         self.verticalLayout_3.addWidget(self.totals_frame)


#         self.verticalLayout.addWidget(self.bottom_widget)

#         AccountDetailsWindow.setCentralWidget(self.centralwidget)
#         self.statusbar = QStatusBar(AccountDetailsWindow)
#         self.statusbar.setObjectName(u"statusbar")
#         AccountDetailsWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(AccountDetailsWindow)

#         QMetaObject.connectSlotsByName(AccountDetailsWindow)
#     # setupUi

#     def retranslateUi(self, AccountDetailsWindow):
#         AccountDetailsWindow.setWindowTitle(QCoreApplication.translate("AccountDetailsWindow", u"Account Details", None))
#         self.lbl_account_name.setText(QCoreApplication.translate("AccountDetailsWindow", u"Name", None))
#         self.lbl_accounts.setText(QCoreApplication.translate("AccountDetailsWindow", u"Accounts", None))
#         self.label_3.setText(QCoreApplication.translate("AccountDetailsWindow", u"Opening Balance", None))
#         self.label_4.setText(QCoreApplication.translate("AccountDetailsWindow", u"00", None))
#         self.btn_cash_paid.setText(QCoreApplication.translate("AccountDetailsWindow", u"Cash Paid", None))
#         self.btn_search.setText("")
#         self.btn_print.setText("")
#         self.btn_refresh.setText("")
#         ___qtablewidgetitem = self.roznamcha_table.horizontalHeaderItem(0)
#         ___qtablewidgetitem.setText(QCoreApplication.translate("AccountDetailsWindow", u"Date", None));
#         ___qtablewidgetitem1 = self.roznamcha_table.horizontalHeaderItem(1)
#         ___qtablewidgetitem1.setText(QCoreApplication.translate("AccountDetailsWindow", u"Description", None));
#         ___qtablewidgetitem2 = self.roznamcha_table.horizontalHeaderItem(2)
#         ___qtablewidgetitem2.setText(QCoreApplication.translate("AccountDetailsWindow", u"Quantity", None));
#         ___qtablewidgetitem3 = self.roznamcha_table.horizontalHeaderItem(3)
#         ___qtablewidgetitem3.setText(QCoreApplication.translate("AccountDetailsWindow", u"Rate", None));
#         ___qtablewidgetitem4 = self.roznamcha_table.horizontalHeaderItem(4)
#         ___qtablewidgetitem4.setText(QCoreApplication.translate("AccountDetailsWindow", u"Total Amount", None));
#         ___qtablewidgetitem5 = self.roznamcha_table.horizontalHeaderItem(5)
#         ___qtablewidgetitem5.setText(QCoreApplication.translate("AccountDetailsWindow", u"Cash Paid", None));
#         ___qtablewidgetitem6 = self.roznamcha_table.horizontalHeaderItem(6)
#         ___qtablewidgetitem6.setText(QCoreApplication.translate("AccountDetailsWindow", u"Remaining", None));
#         self.lbl_total.setText(QCoreApplication.translate("AccountDetailsWindow", u"Total", None))
#         self.label.setText(QCoreApplication.translate("AccountDetailsWindow", u"Quantity :", None))
#         self.label_2.setText(QCoreApplication.translate("AccountDetailsWindow", u"00", None))
#         self.label_5.setText(QCoreApplication.translate("AccountDetailsWindow", u"Amount :", None))
#         self.label_6.setText(QCoreApplication.translate("AccountDetailsWindow", u"00", None))
#         self.lbl_cash_paid.setText(QCoreApplication.translate("AccountDetailsWindow", u"Cash Paid :", None))
#         self.txt_total_cash_paid.setText(QCoreApplication.translate("AccountDetailsWindow", u"00", None))
#         self.lbl_cash_received.setText(QCoreApplication.translate("AccountDetailsWindow", u"Cash Received :", None))
#         self.txt_total_cash_received.setText(QCoreApplication.translate("AccountDetailsWindow", u"00", None))
#         self.lbl_remaining.setText(QCoreApplication.translate("AccountDetailsWindow", u"Remaining :", None))
#         self.txt_remaining.setText(QCoreApplication.translate("AccountDetailsWindow", u"00", None))
#     # retranslateUi

