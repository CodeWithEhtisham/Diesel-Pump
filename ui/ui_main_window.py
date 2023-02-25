# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc
import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1429, 961)
        icon = QIcon()
        icon.addFile(u":/icons/assets/icons/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(40, 40))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"* {\n"
"	background-color: #eceff1;\n"
"}\n"
"\n"
"#upper_widget {\n"
"	background-color: #80cbc4;\n"
"}\n"
"\n"
"#stackedWidget {\n"
"	background-color: #e0f2f1;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#user_frame {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"        ")
        self.verticalLayout_15 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_15.setSpacing(0)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.upper_widget = QWidget(self.centralwidget)
        self.upper_widget.setObjectName(u"upper_widget")
        self.horizontalLayout_10 = QHBoxLayout(self.upper_widget)
        self.horizontalLayout_10.setSpacing(5)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(5, 5, 5, 5)
        self.btn_home = QPushButton(self.upper_widget)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(0, 40))
        self.btn_home.setMaximumSize(QSize(16777215, 16777215))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.OpenHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon1)
        self.btn_home.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.btn_home, 0, Qt.AlignLeft)

        self.btn_product = QPushButton(self.upper_widget)
        self.btn_product.setObjectName(u"btn_product")
        self.btn_product.setMinimumSize(QSize(0, 40))
        self.btn_product.setMaximumSize(QSize(16777215, 16777215))
        self.btn_product.setFont(font)
        self.btn_product.setCursor(QCursor(Qt.OpenHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/icons/products.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_product.setIcon(icon2)
        self.btn_product.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.btn_product)

        self.btn_sales = QPushButton(self.upper_widget)
        self.btn_sales.setObjectName(u"btn_sales")
        self.btn_sales.setMinimumSize(QSize(0, 40))
        self.btn_sales.setMaximumSize(QSize(16777215, 16777215))
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setWeight(75)
        self.btn_sales.setFont(font1)
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/icons/sales.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_sales.setIcon(icon3)
        self.btn_sales.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.btn_sales)

        self.btn_customer = QPushButton(self.upper_widget)
        self.btn_customer.setObjectName(u"btn_customer")
        self.btn_customer.setMinimumSize(QSize(0, 40))
        self.btn_customer.setMaximumSize(QSize(16777215, 16777215))
        self.btn_customer.setFont(font)
        self.btn_customer.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_customer.setLayoutDirection(Qt.LeftToRight)
        icon4 = QIcon()
        icon4.addFile(u":/icons/assets/icons/customers_blue.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_customer.setIcon(icon4)
        self.btn_customer.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.btn_customer)

        self.btn_supplier = QPushButton(self.upper_widget)
        self.btn_supplier.setObjectName(u"btn_supplier")
        self.btn_supplier.setMinimumSize(QSize(0, 40))
        self.btn_supplier.setMaximumSize(QSize(16777215, 16777215))
        self.btn_supplier.setFont(font)
        icon5 = QIcon()
        icon5.addFile(u":/icons/assets/icons/supplier.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_supplier.setIcon(icon5)
        self.btn_supplier.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.btn_supplier)

        self.btn_roznamcha = QPushButton(self.upper_widget)
        self.btn_roznamcha.setObjectName(u"btn_roznamcha")
        self.btn_roznamcha.setMinimumSize(QSize(0, 40))
        self.btn_roznamcha.setMaximumSize(QSize(16777215, 16777215))
        self.btn_roznamcha.setFont(font)
        self.btn_roznamcha.setCursor(QCursor(Qt.OpenHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/assets/icons/menu.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_roznamcha.setIcon(icon6)
        self.btn_roznamcha.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.btn_roznamcha)

        self.btn_settings = QPushButton(self.upper_widget)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMinimumSize(QSize(0, 40))
        self.btn_settings.setMaximumSize(QSize(16777215, 16777215))
        self.btn_settings.setFont(font)
        self.btn_settings.setCursor(QCursor(Qt.OpenHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/assets/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon7)
        self.btn_settings.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.btn_settings)

        self.btn_reports = QPushButton(self.upper_widget)
        self.btn_reports.setObjectName(u"btn_reports")
        self.btn_reports.setMinimumSize(QSize(0, 40))
        self.btn_reports.setMaximumSize(QSize(16777215, 16777215))
        self.btn_reports.setFont(font)
        icon8 = QIcon()
        icon8.addFile(u":/icons/assets/icons/reports.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_reports.setIcon(icon8)
        self.btn_reports.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.btn_reports)

        self.btn_expense = QPushButton(self.upper_widget)
        self.btn_expense.setObjectName(u"btn_expense")
        self.btn_expense.setMinimumSize(QSize(0, 40))
        self.btn_expense.setFont(font1)
        self.btn_expense.setIcon(icon8)
        self.btn_expense.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.btn_expense)

        self.btn_logout = QPushButton(self.upper_widget)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setMinimumSize(QSize(0, 40))
        self.btn_logout.setMaximumSize(QSize(16777215, 16777215))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.OpenHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/assets/icons/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logout.setIcon(icon9)
        self.btn_logout.setIconSize(QSize(32, 32))

        self.horizontalLayout_10.addWidget(self.btn_logout, 0, Qt.AlignRight)


        self.verticalLayout_15.addWidget(self.upper_widget)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"* {\n"
"	background-color: #e1f5fe;\n"
"}")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"#lbl_home {\n"
"		background-color: #00b8d4;\n"
"		color: white;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.home_page)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lbl_home = QLabel(self.home_page)
        self.lbl_home.setObjectName(u"lbl_home")
        self.lbl_home.setMinimumSize(QSize(0, 50))
        self.lbl_home.setMaximumSize(QSize(16777215, 50))
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(20)
        font2.setBold(True)
        font2.setWeight(75)
        self.lbl_home.setFont(font2)
        self.lbl_home.setAlignment(Qt.AlignCenter)
        self.lbl_home.setMargin(10)

        self.verticalLayout_6.addWidget(self.lbl_home)

        self.business_details_widget = QWidget(self.home_page)
        self.business_details_widget.setObjectName(u"business_details_widget")
        self.verticalLayout_5 = QVBoxLayout(self.business_details_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.b_details_frame = QFrame(self.business_details_widget)
        self.b_details_frame.setObjectName(u"b_details_frame")
        self.b_details_frame.setFrameShape(QFrame.StyledPanel)
        self.b_details_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.b_details_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_business_name = QLabel(self.b_details_frame)
        self.lbl_business_name.setObjectName(u"lbl_business_name")
        self.lbl_business_name.setFont(font2)
        self.lbl_business_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_business_name, 0, Qt.AlignBottom)

        self.lbl_business_contact = QLabel(self.b_details_frame)
        self.lbl_business_contact.setObjectName(u"lbl_business_contact")
        font3 = QFont()
        font3.setFamily(u"Calibri")
        font3.setPointSize(18)
        font3.setBold(True)
        font3.setWeight(75)
        self.lbl_business_contact.setFont(font3)
        self.lbl_business_contact.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_business_contact, 0, Qt.AlignBottom)

        self.lbl_business_address = QLabel(self.b_details_frame)
        self.lbl_business_address.setObjectName(u"lbl_business_address")
        self.lbl_business_address.setFont(font3)
        self.lbl_business_address.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_business_address, 0, Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.b_details_frame, 0, Qt.AlignVCenter)


        self.verticalLayout_6.addWidget(self.business_details_widget)

        self.conpany_details_frame = QFrame(self.home_page)
        self.conpany_details_frame.setObjectName(u"conpany_details_frame")
        self.conpany_details_frame.setLayoutDirection(Qt.LeftToRight)
        self.conpany_details_frame.setFrameShape(QFrame.StyledPanel)
        self.conpany_details_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.conpany_details_frame)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lbl_contact = QLabel(self.conpany_details_frame)
        self.lbl_contact.setObjectName(u"lbl_contact")
        self.lbl_contact.setFont(font)

        self.horizontalLayout_17.addWidget(self.lbl_contact, 0, Qt.AlignLeft)

        self.lbl_description = QLabel(self.conpany_details_frame)
        self.lbl_description.setObjectName(u"lbl_description")
        font4 = QFont()
        font4.setFamily(u"Calibri")
        font4.setPointSize(16)
        self.lbl_description.setFont(font4)

        self.horizontalLayout_17.addWidget(self.lbl_description, 0, Qt.AlignRight)

        self.lbl_company = QLabel(self.conpany_details_frame)
        self.lbl_company.setObjectName(u"lbl_company")
        self.lbl_company.setFont(font)
        self.lbl_company.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.lbl_company)


        self.verticalLayout_6.addWidget(self.conpany_details_frame, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.home_page)
        self.product_page = QWidget()
        self.product_page.setObjectName(u"product_page")
        self.product_page.setStyleSheet(u"* {\n"
"	background-color: #e3f2fd;\n"
"}\n"
"\n"
"#lbl_product {\n"
"	background-color: #00b8d4;\n"
"	color: white;\n"
"}\n"
"\n"
"#product_upper_widget {\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"#btn_add_product {\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#btn_add_stock {\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#select_product {\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#txt_date {\n"
"	background-color: white;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#lbl_average_price {\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"#txt_average_price {\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"#lbl_products {\n"
"	background-color: #00b8d4;\n"
"}\n"
"\n"
"#lbl_stock {\n"
"	background-color: #00b8d4;\n"
"}")
        self.verticalLayout_12 = QVBoxLayout(self.product_page)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lbl_product = QLabel(self.product_page)
        self.lbl_product.setObjectName(u"lbl_product")
        self.lbl_product.setMinimumSize(QSize(0, 50))
        self.lbl_product.setMaximumSize(QSize(16777215, 50))
        self.lbl_product.setFont(font2)
        self.lbl_product.setAlignment(Qt.AlignCenter)
        self.lbl_product.setMargin(10)

        self.verticalLayout_12.addWidget(self.lbl_product)

        self.product_upper_widget = QWidget(self.product_page)
        self.product_upper_widget.setObjectName(u"product_upper_widget")
        self.horizontalLayout = QHBoxLayout(self.product_upper_widget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.btn_add_product = QPushButton(self.product_upper_widget)
        self.btn_add_product.setObjectName(u"btn_add_product")
        self.btn_add_product.setMinimumSize(QSize(150, 40))
        self.btn_add_product.setMaximumSize(QSize(200, 40))
        self.btn_add_product.setFont(font1)
        self.btn_add_product.setCursor(QCursor(Qt.OpenHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/assets/icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_product.setIcon(icon10)
        self.btn_add_product.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btn_add_product)

        self.btn_add_stock = QPushButton(self.product_upper_widget)
        self.btn_add_stock.setObjectName(u"btn_add_stock")
        self.btn_add_stock.setMinimumSize(QSize(140, 40))
        self.btn_add_stock.setMaximumSize(QSize(200, 40))
        self.btn_add_stock.setFont(font1)
        self.btn_add_stock.setCursor(QCursor(Qt.OpenHandCursor))
        icon11 = QIcon()
        icon11.addFile(u":/icons/assets/icons/product.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_stock.setIcon(icon11)
        self.btn_add_stock.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btn_add_stock)

        self.select_product = QComboBox(self.product_upper_widget)
        self.select_product.addItem("")
        self.select_product.setObjectName(u"select_product")
        self.select_product.setMinimumSize(QSize(200, 40))
        self.select_product.setMaximumSize(QSize(200, 40))
        self.select_product.setFont(font4)
        self.select_product.setCursor(QCursor(Qt.OpenHandCursor))

        self.horizontalLayout.addWidget(self.select_product)

        self.txt_date = QDateEdit(self.product_upper_widget)
        self.txt_date.setObjectName(u"txt_date")
        self.txt_date.setMinimumSize(QSize(140, 40))
        self.txt_date.setMaximumSize(QSize(200, 40))
        font5 = QFont()
        font5.setFamily(u"Calibri")
        font5.setPointSize(14)
        self.txt_date.setFont(font5)
        self.txt_date.setCalendarPopup(True)

        self.horizontalLayout.addWidget(self.txt_date)

        self.lbl_average_price = QLabel(self.product_upper_widget)
        self.lbl_average_price.setObjectName(u"lbl_average_price")
        self.lbl_average_price.setFont(font4)

        self.horizontalLayout.addWidget(self.lbl_average_price, 0, Qt.AlignRight)

        self.txt_average_price = QLabel(self.product_upper_widget)
        self.txt_average_price.setObjectName(u"txt_average_price")
        self.txt_average_price.setFont(font3)
        self.txt_average_price.setMargin(0)

        self.horizontalLayout.addWidget(self.txt_average_price, 0, Qt.AlignLeft)


        self.verticalLayout_12.addWidget(self.product_upper_widget)

        self.product_stock_widget = QWidget(self.product_page)
        self.product_stock_widget.setObjectName(u"product_stock_widget")
        self.horizontalLayout_9 = QHBoxLayout(self.product_stock_widget)
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
        self.product_frame = QFrame(self.product_stock_widget)
        self.product_frame.setObjectName(u"product_frame")
        self.product_frame.setFrameShape(QFrame.StyledPanel)
        self.product_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.product_frame)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.lbl_products = QLabel(self.product_frame)
        self.lbl_products.setObjectName(u"lbl_products")
        self.lbl_products.setFont(font)
        self.lbl_products.setAlignment(Qt.AlignCenter)
        self.lbl_products.setMargin(10)

        self.verticalLayout_3.addWidget(self.lbl_products)

        self.product_table = QTableWidget(self.product_frame)
        if (self.product_table.columnCount() < 3):
            self.product_table.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font1);
        self.product_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font1);
        self.product_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font1);
        self.product_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        if (self.product_table.rowCount() < 20):
            self.product_table.setRowCount(20)
        font6 = QFont()
        font6.setFamily(u"Calibri")
        font6.setPointSize(12)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font6);
        self.product_table.setItem(0, 0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.product_table.setItem(0, 1, __qtablewidgetitem4)
        self.product_table.setObjectName(u"product_table")
        self.product_table.setFont(font5)
        self.product_table.setFrameShape(QFrame.Box)
        self.product_table.setFrameShadow(QFrame.Raised)
        self.product_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.product_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.product_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.product_table.setSortingEnabled(True)
        self.product_table.setRowCount(20)
        self.product_table.horizontalHeader().setDefaultSectionSize(180)
        self.product_table.verticalHeader().setVisible(False)
        self.product_table.verticalHeader().setCascadingSectionResizes(False)

        self.verticalLayout_3.addWidget(self.product_table)


        self.horizontalLayout_9.addWidget(self.product_frame)

        self.stock_frame = QFrame(self.product_stock_widget)
        self.stock_frame.setObjectName(u"stock_frame")
        self.stock_frame.setFrameShape(QFrame.StyledPanel)
        self.stock_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout = QVBoxLayout(self.stock_frame)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.lbl_stock = QLabel(self.stock_frame)
        self.lbl_stock.setObjectName(u"lbl_stock")
        self.lbl_stock.setFont(font)
        self.lbl_stock.setLineWidth(1)
        self.lbl_stock.setAlignment(Qt.AlignCenter)
        self.lbl_stock.setMargin(10)

        self.verticalLayout.addWidget(self.lbl_stock)

        self.stock_table = QTableWidget(self.stock_frame)
        if (self.stock_table.columnCount() < 5):
            self.stock_table.setColumnCount(5)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font1);
        self.stock_table.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font1);
        self.stock_table.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font1);
        self.stock_table.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font1);
        self.stock_table.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font1);
        self.stock_table.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        if (self.stock_table.rowCount() < 20):
            self.stock_table.setRowCount(20)
        self.stock_table.setObjectName(u"stock_table")
        self.stock_table.setFont(font5)
        self.stock_table.setFrameShape(QFrame.Box)
        self.stock_table.setFrameShadow(QFrame.Raised)
        self.stock_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.stock_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.stock_table.setProperty("showDropIndicator", False)
        self.stock_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.stock_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.stock_table.setTextElideMode(Qt.ElideLeft)
        self.stock_table.setRowCount(20)
        self.stock_table.horizontalHeader().setDefaultSectionSize(130)
        self.stock_table.horizontalHeader().setProperty("showSortIndicator", True)

        self.verticalLayout.addWidget(self.stock_table)


        self.horizontalLayout_9.addWidget(self.stock_frame)


        self.verticalLayout_12.addWidget(self.product_stock_widget)

        self.stackedWidget.addWidget(self.product_page)
        self.sales_page = QWidget()
        self.sales_page.setObjectName(u"sales_page")
        self.sales_page.setStyleSheet(u"\n"
"*{\n"
"	background-color: #e3f2fd;\n"
"}\n"
"\n"
"#lbl_sales {\n"
"	background-color: #00b8d4;\n"
"	color: white;\n"
"}\n"
"\n"
"#sales_upper_widget {\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"#sales_bottom_widget, #total_cash_recv_frame, #total_cash_paid_frame, \n"
"#total_sales_frame, #lbl_total_cash_paid, #lbl_total_cash_recv, #lbl_total_sales {\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"#lbl_from_sale {\n"
"	background-color: #bbdefb;\n"
"}\n"
"#lbl_to_sale {\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"#search_option_sale {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#txt_search_sale {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #00bcd4;\n"
"}\n"
"\n"
"#txt_date_from_sale {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#txt_date_to_sale {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"QPushButton {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"                ")
        self.verticalLayout_13 = QVBoxLayout(self.sales_page)
        self.verticalLayout_13.setSpacing(0)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.lbl_sales = QLabel(self.sales_page)
        self.lbl_sales.setObjectName(u"lbl_sales")
        self.lbl_sales.setMinimumSize(QSize(0, 50))
        self.lbl_sales.setMaximumSize(QSize(16777215, 50))
        self.lbl_sales.setFont(font2)
        self.lbl_sales.setAlignment(Qt.AlignCenter)
        self.lbl_sales.setMargin(10)

        self.verticalLayout_13.addWidget(self.lbl_sales)

        self.sales_upper_widget = QWidget(self.sales_page)
        self.sales_upper_widget.setObjectName(u"sales_upper_widget")
        self.horizontalLayout_4 = QHBoxLayout(self.sales_upper_widget)
        self.horizontalLayout_4.setSpacing(5)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
        self.btn_add_sale = QPushButton(self.sales_upper_widget)
        self.btn_add_sale.setObjectName(u"btn_add_sale")
        self.btn_add_sale.setMinimumSize(QSize(180, 40))
        self.btn_add_sale.setMaximumSize(QSize(200, 40))
        self.btn_add_sale.setFont(font1)
        self.btn_add_sale.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_add_sale.setIcon(icon10)
        self.btn_add_sale.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.btn_add_sale)

        self.txt_search_sale = QLineEdit(self.sales_upper_widget)
        self.txt_search_sale.setObjectName(u"txt_search_sale")
        self.txt_search_sale.setMinimumSize(QSize(400, 40))
        self.txt_search_sale.setMaximumSize(QSize(400, 40))
        self.txt_search_sale.setFont(font5)

        self.horizontalLayout_4.addWidget(self.txt_search_sale)

        self.lbl_from_sale = QLabel(self.sales_upper_widget)
        self.lbl_from_sale.setObjectName(u"lbl_from_sale")
        self.lbl_from_sale.setMaximumSize(QSize(100, 40))
        self.lbl_from_sale.setFont(font5)

        self.horizontalLayout_4.addWidget(self.lbl_from_sale)

        self.txt_date_from_sale = QDateEdit(self.sales_upper_widget)
        self.txt_date_from_sale.setObjectName(u"txt_date_from_sale")
        self.txt_date_from_sale.setMinimumSize(QSize(130, 40))
        self.txt_date_from_sale.setMaximumSize(QSize(16777215, 16777215))
        font7 = QFont()
        font7.setFamily(u"Calibri")
        font7.setPointSize(14)
        font7.setBold(False)
        font7.setWeight(50)
        self.txt_date_from_sale.setFont(font7)
        self.txt_date_from_sale.setCursor(QCursor(Qt.OpenHandCursor))
        self.txt_date_from_sale.setDateTime(QDateTime(QDate(2022, 1, 1), QTime(0, 0, 0)))
        self.txt_date_from_sale.setCurrentSection(QDateTimeEdit.DaySection)
        self.txt_date_from_sale.setCalendarPopup(True)

        self.horizontalLayout_4.addWidget(self.txt_date_from_sale)

        self.lbl_to_sale = QLabel(self.sales_upper_widget)
        self.lbl_to_sale.setObjectName(u"lbl_to_sale")
        self.lbl_to_sale.setMaximumSize(QSize(100, 40))
        self.lbl_to_sale.setFont(font5)

        self.horizontalLayout_4.addWidget(self.lbl_to_sale)

        self.txt_date_to_sale = QDateEdit(self.sales_upper_widget)
        self.txt_date_to_sale.setObjectName(u"txt_date_to_sale")
        self.txt_date_to_sale.setMinimumSize(QSize(130, 40))
        self.txt_date_to_sale.setMaximumSize(QSize(16777215, 16777215))
        self.txt_date_to_sale.setFont(font5)
        self.txt_date_to_sale.setCursor(QCursor(Qt.OpenHandCursor))
        self.txt_date_to_sale.setCalendarPopup(True)
        self.txt_date_to_sale.setDate(QDate(2022, 12, 15))

        self.horizontalLayout_4.addWidget(self.txt_date_to_sale)

        self.btn_search_sale = QPushButton(self.sales_upper_widget)
        self.btn_search_sale.setObjectName(u"btn_search_sale")
        self.btn_search_sale.setMinimumSize(QSize(40, 40))
        self.btn_search_sale.setMaximumSize(QSize(16777215, 16777215))
        self.btn_search_sale.setCursor(QCursor(Qt.OpenHandCursor))
        icon12 = QIcon()
        icon12.addFile(u":/icons/assets/icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search_sale.setIcon(icon12)
        self.btn_search_sale.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.btn_search_sale, 0, Qt.AlignRight)

        self.btn_edit_sales = QPushButton(self.sales_upper_widget)
        self.btn_edit_sales.setObjectName(u"btn_edit_sales")
        self.btn_edit_sales.setMinimumSize(QSize(40, 40))
        icon13 = QIcon()
        icon13.addFile(u":/icons/assets/icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_edit_sales.setIcon(icon13)
        self.btn_edit_sales.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.btn_edit_sales, 0, Qt.AlignRight)

        self.btn_print_sale = QPushButton(self.sales_upper_widget)
        self.btn_print_sale.setObjectName(u"btn_print_sale")
        self.btn_print_sale.setMinimumSize(QSize(40, 40))
        self.btn_print_sale.setMaximumSize(QSize(16777215, 16777215))
        self.btn_print_sale.setCursor(QCursor(Qt.OpenHandCursor))
        icon14 = QIcon()
        icon14.addFile(u":/icons/assets/icons/print.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_print_sale.setIcon(icon14)
        self.btn_print_sale.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.btn_print_sale, 0, Qt.AlignRight)

        self.btn_refresh_sale = QPushButton(self.sales_upper_widget)
        self.btn_refresh_sale.setObjectName(u"btn_refresh_sale")
        self.btn_refresh_sale.setMinimumSize(QSize(40, 40))
        self.btn_refresh_sale.setMaximumSize(QSize(16777215, 16777215))
        self.btn_refresh_sale.setCursor(QCursor(Qt.OpenHandCursor))
        icon15 = QIcon()
        icon15.addFile(u":/icons/assets/icons/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_refresh_sale.setIcon(icon15)
        self.btn_refresh_sale.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.btn_refresh_sale, 0, Qt.AlignRight)


        self.verticalLayout_13.addWidget(self.sales_upper_widget)

        self.sales_table = QTableWidget(self.sales_page)
        if (self.sales_table.columnCount() < 8):
            self.sales_table.setColumnCount(8)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font1);
        self.sales_table.setHorizontalHeaderItem(0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font1);
        self.sales_table.setHorizontalHeaderItem(1, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font1);
        self.sales_table.setHorizontalHeaderItem(2, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font1);
        self.sales_table.setHorizontalHeaderItem(3, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFont(font1);
        self.sales_table.setHorizontalHeaderItem(4, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        __qtablewidgetitem15.setFont(font1);
        self.sales_table.setHorizontalHeaderItem(5, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        __qtablewidgetitem16.setFont(font1);
        self.sales_table.setHorizontalHeaderItem(6, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        __qtablewidgetitem17.setFont(font1);
        self.sales_table.setHorizontalHeaderItem(7, __qtablewidgetitem17)
        if (self.sales_table.rowCount() < 20):
            self.sales_table.setRowCount(20)
        self.sales_table.setObjectName(u"sales_table")
        self.sales_table.setFont(font5)
        self.sales_table.setFrameShape(QFrame.Box)
        self.sales_table.setFrameShadow(QFrame.Raised)
        self.sales_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.sales_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.sales_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.sales_table.setSortingEnabled(True)
        self.sales_table.setRowCount(20)
        self.sales_table.horizontalHeader().setDefaultSectionSize(145)

        self.verticalLayout_13.addWidget(self.sales_table)

        self.sales_bottom_widget = QWidget(self.sales_page)
        self.sales_bottom_widget.setObjectName(u"sales_bottom_widget")
        self.horizontalLayout_14 = QHBoxLayout(self.sales_bottom_widget)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.total_sales_frame = QFrame(self.sales_bottom_widget)
        self.total_sales_frame.setObjectName(u"total_sales_frame")
        self.total_sales_frame.setFrameShape(QFrame.StyledPanel)
        self.total_sales_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.total_sales_frame)
        self.horizontalLayout_15.setSpacing(20)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
        self.lbl_total_sales = QLabel(self.total_sales_frame)
        self.lbl_total_sales.setObjectName(u"lbl_total_sales")
        self.lbl_total_sales.setFont(font4)

        self.horizontalLayout_15.addWidget(self.lbl_total_sales, 0, Qt.AlignRight)

        self.txt_total_sales = QLabel(self.total_sales_frame)
        self.txt_total_sales.setObjectName(u"txt_total_sales")
        self.txt_total_sales.setMinimumSize(QSize(0, 40))
        font8 = QFont()
        font8.setFamily(u"Calibri Light")
        font8.setPointSize(16)
        font8.setBold(True)
        font8.setWeight(75)
        self.txt_total_sales.setFont(font8)
        self.txt_total_sales.setFrameShape(QFrame.Box)
        self.txt_total_sales.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_15.addWidget(self.txt_total_sales)


        self.horizontalLayout_14.addWidget(self.total_sales_frame)

        self.total_cash_paid_frame = QFrame(self.sales_bottom_widget)
        self.total_cash_paid_frame.setObjectName(u"total_cash_paid_frame")
        self.total_cash_paid_frame.setFrameShape(QFrame.StyledPanel)
        self.total_cash_paid_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_18 = QHBoxLayout(self.total_cash_paid_frame)
        self.horizontalLayout_18.setSpacing(20)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
        self.lbl_total_cash_paid = QLabel(self.total_cash_paid_frame)
        self.lbl_total_cash_paid.setObjectName(u"lbl_total_cash_paid")
        self.lbl_total_cash_paid.setFont(font4)

        self.horizontalLayout_18.addWidget(self.lbl_total_cash_paid, 0, Qt.AlignRight)

        self.txt_total_cash_paid = QLabel(self.total_cash_paid_frame)
        self.txt_total_cash_paid.setObjectName(u"txt_total_cash_paid")
        self.txt_total_cash_paid.setMinimumSize(QSize(0, 40))
        self.txt_total_cash_paid.setFont(font8)
        self.txt_total_cash_paid.setFrameShape(QFrame.Box)
        self.txt_total_cash_paid.setFrameShadow(QFrame.Raised)
        self.txt_total_cash_paid.setTextFormat(Qt.AutoText)

        self.horizontalLayout_18.addWidget(self.txt_total_cash_paid)


        self.horizontalLayout_14.addWidget(self.total_cash_paid_frame)

        self.total_cash_recv_frame = QFrame(self.sales_bottom_widget)
        self.total_cash_recv_frame.setObjectName(u"total_cash_recv_frame")
        self.total_cash_recv_frame.setFrameShape(QFrame.StyledPanel)
        self.total_cash_recv_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_16 = QHBoxLayout(self.total_cash_recv_frame)
        self.horizontalLayout_16.setSpacing(20)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.lbl_total_cash_recv = QLabel(self.total_cash_recv_frame)
        self.lbl_total_cash_recv.setObjectName(u"lbl_total_cash_recv")
        self.lbl_total_cash_recv.setFont(font4)

        self.horizontalLayout_16.addWidget(self.lbl_total_cash_recv, 0, Qt.AlignRight)

        self.txt_total_cash_received = QLabel(self.total_cash_recv_frame)
        self.txt_total_cash_received.setObjectName(u"txt_total_cash_received")
        self.txt_total_cash_received.setMinimumSize(QSize(0, 40))
        self.txt_total_cash_received.setFont(font8)
        self.txt_total_cash_received.setFrameShape(QFrame.Box)
        self.txt_total_cash_received.setFrameShadow(QFrame.Raised)
        self.txt_total_cash_received.setTextFormat(Qt.AutoText)

        self.horizontalLayout_16.addWidget(self.txt_total_cash_received)


        self.horizontalLayout_14.addWidget(self.total_cash_recv_frame)


        self.verticalLayout_13.addWidget(self.sales_bottom_widget)

        self.stackedWidget.addWidget(self.sales_page)
        self.customer_page = QWidget()
        self.customer_page.setObjectName(u"customer_page")
        self.customer_page.setStyleSheet(u"*{\n"
"	background-color: #e3f2fd;\n"
"}\n"
"\n"
"#lbl_customer {\n"
"	background-color: #00b8d4;\n"
"	color: white;\n"
"}\n"
"\n"
"#customer_upper_widget, #frame {\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"#cust_bottom_widget {\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"#total_cust_frame {\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"#total_rem_bal_frame {\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"#lbl_total_customers {\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"#lbl_total_remaining {\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"#btn_add_customer {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#search_option_customer {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#txt_search_customer {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #00bcd4;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.customer_page)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbl_customer = QLabel(self.customer_page)
        self.lbl_customer.setObjectName(u"lbl_customer")
        self.lbl_customer.setMinimumSize(QSize(0, 50))
        self.lbl_customer.setMaximumSize(QSize(16777215, 50))
        self.lbl_customer.setFont(font3)
        self.lbl_customer.setAlignment(Qt.AlignCenter)
        self.lbl_customer.setMargin(10)

        self.verticalLayout_2.addWidget(self.lbl_customer)

        self.customer_upper_widget = QWidget(self.customer_page)
        self.customer_upper_widget.setObjectName(u"customer_upper_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.customer_upper_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_add_customer = QPushButton(self.customer_upper_widget)
        self.btn_add_customer.setObjectName(u"btn_add_customer")
        self.btn_add_customer.setMinimumSize(QSize(200, 40))
        self.btn_add_customer.setMaximumSize(QSize(300, 40))
        self.btn_add_customer.setFont(font1)
        self.btn_add_customer.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_add_customer.setIcon(icon10)
        self.btn_add_customer.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_add_customer)

        self.txt_search_customer = QLineEdit(self.customer_upper_widget)
        self.txt_search_customer.setObjectName(u"txt_search_customer")
        self.txt_search_customer.setMinimumSize(QSize(400, 40))
        self.txt_search_customer.setMaximumSize(QSize(400, 40))
        self.txt_search_customer.setFont(font5)

        self.horizontalLayout_2.addWidget(self.txt_search_customer)

        self.frame = QFrame(self.customer_upper_widget)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_28 = QHBoxLayout(self.frame)
        self.horizontalLayout_28.setSpacing(20)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.btn_edit_customer = QPushButton(self.frame)
        self.btn_edit_customer.setObjectName(u"btn_edit_customer")
        self.btn_edit_customer.setMinimumSize(QSize(40, 40))
        self.btn_edit_customer.setIcon(icon13)
        self.btn_edit_customer.setIconSize(QSize(32, 32))

        self.horizontalLayout_28.addWidget(self.btn_edit_customer)

        self.btn_print_customer = QPushButton(self.frame)
        self.btn_print_customer.setObjectName(u"btn_print_customer")
        self.btn_print_customer.setMinimumSize(QSize(40, 40))
        self.btn_print_customer.setIcon(icon14)
        self.btn_print_customer.setIconSize(QSize(32, 32))

        self.horizontalLayout_28.addWidget(self.btn_print_customer)

        self.btn_refresh_customer = QPushButton(self.frame)
        self.btn_refresh_customer.setObjectName(u"btn_refresh_customer")
        self.btn_refresh_customer.setMinimumSize(QSize(40, 40))
        self.btn_refresh_customer.setMaximumSize(QSize(16777215, 16777215))
        self.btn_refresh_customer.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_refresh_customer.setIcon(icon15)
        self.btn_refresh_customer.setIconSize(QSize(32, 32))

        self.horizontalLayout_28.addWidget(self.btn_refresh_customer)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.customer_upper_widget)

        self.customer_table = QTableWidget(self.customer_page)
        if (self.customer_table.columnCount() < 6):
            self.customer_table.setColumnCount(6)
        __qtablewidgetitem18 = QTableWidgetItem()
        __qtablewidgetitem18.setFont(font1);
        self.customer_table.setHorizontalHeaderItem(0, __qtablewidgetitem18)
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setFont(font1);
        self.customer_table.setHorizontalHeaderItem(1, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setFont(font1);
        self.customer_table.setHorizontalHeaderItem(2, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        __qtablewidgetitem21.setFont(font1);
        self.customer_table.setHorizontalHeaderItem(3, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        __qtablewidgetitem22.setFont(font1);
        self.customer_table.setHorizontalHeaderItem(4, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        __qtablewidgetitem23.setFont(font1);
        self.customer_table.setHorizontalHeaderItem(5, __qtablewidgetitem23)
        if (self.customer_table.rowCount() < 20):
            self.customer_table.setRowCount(20)
        self.customer_table.setObjectName(u"customer_table")
        self.customer_table.setFont(font5)
        self.customer_table.setFrameShape(QFrame.Box)
        self.customer_table.setFrameShadow(QFrame.Raised)
        self.customer_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.customer_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.customer_table.setDragDropOverwriteMode(True)
        self.customer_table.setAlternatingRowColors(False)
        self.customer_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.customer_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.customer_table.setTextElideMode(Qt.ElideRight)
        self.customer_table.setShowGrid(True)
        self.customer_table.setGridStyle(Qt.SolidLine)
        self.customer_table.setSortingEnabled(True)
        self.customer_table.setCornerButtonEnabled(True)
        self.customer_table.setRowCount(20)
        self.customer_table.horizontalHeader().setVisible(True)
        self.customer_table.horizontalHeader().setCascadingSectionResizes(True)
        self.customer_table.horizontalHeader().setDefaultSectionSize(150)
        self.customer_table.horizontalHeader().setProperty("showSortIndicator", True)
        self.customer_table.verticalHeader().setVisible(False)
        self.customer_table.verticalHeader().setMinimumSectionSize(30)
        self.customer_table.verticalHeader().setHighlightSections(True)
        self.customer_table.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_2.addWidget(self.customer_table)

        self.cust_bottom_widget = QWidget(self.customer_page)
        self.cust_bottom_widget.setObjectName(u"cust_bottom_widget")
        self.horizontalLayout_13 = QHBoxLayout(self.cust_bottom_widget)
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.total_cust_frame = QFrame(self.cust_bottom_widget)
        self.total_cust_frame.setObjectName(u"total_cust_frame")
        self.total_cust_frame.setFrameShape(QFrame.StyledPanel)
        self.total_cust_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_12 = QHBoxLayout(self.total_cust_frame)
        self.horizontalLayout_12.setSpacing(20)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lbl_total_customers = QLabel(self.total_cust_frame)
        self.lbl_total_customers.setObjectName(u"lbl_total_customers")
        self.lbl_total_customers.setFont(font4)

        self.horizontalLayout_12.addWidget(self.lbl_total_customers, 0, Qt.AlignRight)

        self.txt_total_customers = QLabel(self.total_cust_frame)
        self.txt_total_customers.setObjectName(u"txt_total_customers")
        self.txt_total_customers.setMinimumSize(QSize(0, 40))
        self.txt_total_customers.setFont(font8)
        self.txt_total_customers.setFrameShape(QFrame.Box)
        self.txt_total_customers.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_12.addWidget(self.txt_total_customers)


        self.horizontalLayout_13.addWidget(self.total_cust_frame)

        self.total_rem_bal_frame = QFrame(self.cust_bottom_widget)
        self.total_rem_bal_frame.setObjectName(u"total_rem_bal_frame")
        self.total_rem_bal_frame.setFrameShape(QFrame.StyledPanel)
        self.total_rem_bal_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_11 = QHBoxLayout(self.total_rem_bal_frame)
        self.horizontalLayout_11.setSpacing(20)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lbl_total_remaining = QLabel(self.total_rem_bal_frame)
        self.lbl_total_remaining.setObjectName(u"lbl_total_remaining")
        self.lbl_total_remaining.setFont(font4)

        self.horizontalLayout_11.addWidget(self.lbl_total_remaining, 0, Qt.AlignRight)

        self.txt_total_rem_balance = QLabel(self.total_rem_bal_frame)
        self.txt_total_rem_balance.setObjectName(u"txt_total_rem_balance")
        self.txt_total_rem_balance.setMinimumSize(QSize(0, 40))
        self.txt_total_rem_balance.setFont(font8)
        self.txt_total_rem_balance.setFrameShape(QFrame.Box)
        self.txt_total_rem_balance.setFrameShadow(QFrame.Raised)
        self.txt_total_rem_balance.setTextFormat(Qt.AutoText)

        self.horizontalLayout_11.addWidget(self.txt_total_rem_balance)


        self.horizontalLayout_13.addWidget(self.total_rem_bal_frame)


        self.verticalLayout_2.addWidget(self.cust_bottom_widget)

        self.stackedWidget.addWidget(self.customer_page)
        self.roznamcha_page = QWidget()
        self.roznamcha_page.setObjectName(u"roznamcha_page")
        self.roznamcha_page.setStyleSheet(u"\n"
"*{\n"
"	background-color: #e3f2fd;\n"
"}\n"
"\n"
"#lbl_roznamcha {\n"
"	background-color: #00b8d4;\n"
"	color: white;\n"
"}\n"
"\n"
"#frame_2, #roznamcha_upper_widget, #lbl_from, #rn_bottom_widget, #total_cash_in_frame, #total_cash_out_frame, #lbl_total_cashIn, #lbl_total_cash_out, #lbl_from_rn, #lbl_to_rn {\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"QPushButton, QComboBox, QDateEdit {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#txt_search_rn {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #00bcd4;\n"
"}\n"
"\n"
"\n"
"                ")
        self.verticalLayout_14 = QVBoxLayout(self.roznamcha_page)
        self.verticalLayout_14.setSpacing(0)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
        self.lbl_roznamcha = QLabel(self.roznamcha_page)
        self.lbl_roznamcha.setObjectName(u"lbl_roznamcha")
        self.lbl_roznamcha.setMinimumSize(QSize(0, 50))
        self.lbl_roznamcha.setMaximumSize(QSize(16777215, 50))
        self.lbl_roznamcha.setFont(font3)
        self.lbl_roznamcha.setAlignment(Qt.AlignCenter)
        self.lbl_roznamcha.setMargin(10)

        self.verticalLayout_14.addWidget(self.lbl_roznamcha)

        self.roznamcha_upper_widget = QWidget(self.roznamcha_page)
        self.roznamcha_upper_widget.setObjectName(u"roznamcha_upper_widget")
        self.horizontalLayout_3 = QHBoxLayout(self.roznamcha_upper_widget)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 10)
        self.btn_add_roznamcha = QPushButton(self.roznamcha_upper_widget)
        self.btn_add_roznamcha.setObjectName(u"btn_add_roznamcha")
        self.btn_add_roznamcha.setMinimumSize(QSize(180, 40))
        self.btn_add_roznamcha.setMaximumSize(QSize(300, 40))
        self.btn_add_roznamcha.setFont(font1)
        self.btn_add_roznamcha.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_add_roznamcha.setIcon(icon10)
        self.btn_add_roznamcha.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.btn_add_roznamcha)

        self.txt_search_rn = QLineEdit(self.roznamcha_upper_widget)
        self.txt_search_rn.setObjectName(u"txt_search_rn")
        self.txt_search_rn.setMinimumSize(QSize(300, 40))
        self.txt_search_rn.setMaximumSize(QSize(400, 40))
        self.txt_search_rn.setFont(font5)

        self.horizontalLayout_3.addWidget(self.txt_search_rn)

        self.lbl_from_rn = QLabel(self.roznamcha_upper_widget)
        self.lbl_from_rn.setObjectName(u"lbl_from_rn")
        self.lbl_from_rn.setMaximumSize(QSize(16777215, 40))
        self.lbl_from_rn.setFont(font5)

        self.horizontalLayout_3.addWidget(self.lbl_from_rn)

        self.txt_date_from_rn = QDateEdit(self.roznamcha_upper_widget)
        self.txt_date_from_rn.setObjectName(u"txt_date_from_rn")
        self.txt_date_from_rn.setMinimumSize(QSize(130, 40))
        self.txt_date_from_rn.setMaximumSize(QSize(130, 40))
        self.txt_date_from_rn.setFont(font7)
        self.txt_date_from_rn.setDateTime(QDateTime(QDate(2022, 1, 1), QTime(0, 0, 0)))
        self.txt_date_from_rn.setCurrentSection(QDateTimeEdit.DaySection)
        self.txt_date_from_rn.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.txt_date_from_rn)

        self.lbl_to_rn = QLabel(self.roznamcha_upper_widget)
        self.lbl_to_rn.setObjectName(u"lbl_to_rn")
        self.lbl_to_rn.setMaximumSize(QSize(16777215, 40))
        self.lbl_to_rn.setFont(font5)

        self.horizontalLayout_3.addWidget(self.lbl_to_rn)

        self.txt_date_to_rn = QDateEdit(self.roznamcha_upper_widget)
        self.txt_date_to_rn.setObjectName(u"txt_date_to_rn")
        self.txt_date_to_rn.setMinimumSize(QSize(130, 40))
        self.txt_date_to_rn.setMaximumSize(QSize(130, 40))
        self.txt_date_to_rn.setFont(font5)
        self.txt_date_to_rn.setCalendarPopup(True)
        self.txt_date_to_rn.setDate(QDate(2022, 12, 15))

        self.horizontalLayout_3.addWidget(self.txt_date_to_rn)

        self.btn_search_rn = QPushButton(self.roznamcha_upper_widget)
        self.btn_search_rn.setObjectName(u"btn_search_rn")
        self.btn_search_rn.setMinimumSize(QSize(40, 40))
        self.btn_search_rn.setMaximumSize(QSize(16777215, 16777215))
        self.btn_search_rn.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_search_rn.setIcon(icon12)
        self.btn_search_rn.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.btn_search_rn, 0, Qt.AlignLeft)

        self.frame_2 = QFrame(self.roznamcha_upper_widget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_29 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_29.setSpacing(20)
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalLayout_29.setContentsMargins(0, 0, 0, 0)
        self.btn_edit_rn = QPushButton(self.frame_2)
        self.btn_edit_rn.setObjectName(u"btn_edit_rn")
        self.btn_edit_rn.setMinimumSize(QSize(40, 40))
        self.btn_edit_rn.setIcon(icon13)
        self.btn_edit_rn.setIconSize(QSize(32, 32))

        self.horizontalLayout_29.addWidget(self.btn_edit_rn)

        self.btn_print_rn = QPushButton(self.frame_2)
        self.btn_print_rn.setObjectName(u"btn_print_rn")
        self.btn_print_rn.setMinimumSize(QSize(40, 40))
        self.btn_print_rn.setMaximumSize(QSize(16777215, 16777215))
        self.btn_print_rn.setIcon(icon14)
        self.btn_print_rn.setIconSize(QSize(32, 32))

        self.horizontalLayout_29.addWidget(self.btn_print_rn)

        self.btn_refresh_rn = QPushButton(self.frame_2)
        self.btn_refresh_rn.setObjectName(u"btn_refresh_rn")
        self.btn_refresh_rn.setMinimumSize(QSize(40, 40))
        self.btn_refresh_rn.setMaximumSize(QSize(16777215, 16777215))
        self.btn_refresh_rn.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_refresh_rn.setIcon(icon15)
        self.btn_refresh_rn.setIconSize(QSize(32, 32))

        self.horizontalLayout_29.addWidget(self.btn_refresh_rn)


        self.horizontalLayout_3.addWidget(self.frame_2)


        self.verticalLayout_14.addWidget(self.roznamcha_upper_widget)

        self.roznamcha_table = QTableWidget(self.roznamcha_page)
        if (self.roznamcha_table.columnCount() < 8):
            self.roznamcha_table.setColumnCount(8)
        __qtablewidgetitem24 = QTableWidgetItem()
        __qtablewidgetitem24.setFont(font1);
        self.roznamcha_table.setHorizontalHeaderItem(0, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        __qtablewidgetitem25.setFont(font1);
        self.roznamcha_table.setHorizontalHeaderItem(1, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setFont(font1);
        self.roznamcha_table.setHorizontalHeaderItem(2, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setFont(font1);
        self.roznamcha_table.setHorizontalHeaderItem(3, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        __qtablewidgetitem28.setFont(font1);
        self.roznamcha_table.setHorizontalHeaderItem(4, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        __qtablewidgetitem29.setFont(font1);
        self.roznamcha_table.setHorizontalHeaderItem(5, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        __qtablewidgetitem30.setFont(font1);
        self.roznamcha_table.setHorizontalHeaderItem(6, __qtablewidgetitem30)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem31 = QTableWidgetItem()
        __qtablewidgetitem31.setFont(font1);
        __qtablewidgetitem31.setForeground(brush);
        self.roznamcha_table.setHorizontalHeaderItem(7, __qtablewidgetitem31)
        if (self.roznamcha_table.rowCount() < 20):
            self.roznamcha_table.setRowCount(20)
        __qtablewidgetitem32 = QTableWidgetItem()
        __qtablewidgetitem32.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        self.roznamcha_table.setItem(0, 1, __qtablewidgetitem32)
        self.roznamcha_table.setObjectName(u"roznamcha_table")
        self.roznamcha_table.setMinimumSize(QSize(0, 0))
        self.roznamcha_table.setFont(font5)
        self.roznamcha_table.setLayoutDirection(Qt.LeftToRight)
        self.roznamcha_table.setAutoFillBackground(False)
        self.roznamcha_table.setFrameShape(QFrame.Box)
        self.roznamcha_table.setFrameShadow(QFrame.Raised)
        self.roznamcha_table.setMidLineWidth(0)
        self.roznamcha_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.roznamcha_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.roznamcha_table.setAlternatingRowColors(False)
        self.roznamcha_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.roznamcha_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.roznamcha_table.setSortingEnabled(True)
        self.roznamcha_table.setCornerButtonEnabled(True)
        self.roznamcha_table.setRowCount(20)
        self.roznamcha_table.horizontalHeader().setVisible(True)
        self.roznamcha_table.horizontalHeader().setCascadingSectionResizes(False)
        self.roznamcha_table.horizontalHeader().setMinimumSectionSize(30)
        self.roznamcha_table.horizontalHeader().setDefaultSectionSize(150)
        self.roznamcha_table.horizontalHeader().setHighlightSections(True)
        self.roznamcha_table.horizontalHeader().setProperty("showSortIndicator", True)
        self.roznamcha_table.horizontalHeader().setStretchLastSection(False)
        self.roznamcha_table.verticalHeader().setVisible(False)
        self.roznamcha_table.verticalHeader().setCascadingSectionResizes(False)
        self.roznamcha_table.verticalHeader().setMinimumSectionSize(30)
        self.roznamcha_table.verticalHeader().setDefaultSectionSize(30)
        self.roznamcha_table.verticalHeader().setProperty("showSortIndicator", True)
        self.roznamcha_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_14.addWidget(self.roznamcha_table)

        self.rn_bottom_widget = QWidget(self.roznamcha_page)
        self.rn_bottom_widget.setObjectName(u"rn_bottom_widget")
        self.horizontalLayout_19 = QHBoxLayout(self.rn_bottom_widget)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.total_cash_in_frame = QFrame(self.rn_bottom_widget)
        self.total_cash_in_frame.setObjectName(u"total_cash_in_frame")
        self.total_cash_in_frame.setFrameShape(QFrame.StyledPanel)
        self.total_cash_in_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_20 = QHBoxLayout(self.total_cash_in_frame)
        self.horizontalLayout_20.setSpacing(20)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.lbl_total_cashIn = QLabel(self.total_cash_in_frame)
        self.lbl_total_cashIn.setObjectName(u"lbl_total_cashIn")
        self.lbl_total_cashIn.setFont(font4)

        self.horizontalLayout_20.addWidget(self.lbl_total_cashIn, 0, Qt.AlignRight)

        self.txt_total_cash_in = QLabel(self.total_cash_in_frame)
        self.txt_total_cash_in.setObjectName(u"txt_total_cash_in")
        self.txt_total_cash_in.setMinimumSize(QSize(0, 40))
        self.txt_total_cash_in.setFont(font8)
        self.txt_total_cash_in.setFrameShape(QFrame.Box)
        self.txt_total_cash_in.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_20.addWidget(self.txt_total_cash_in)


        self.horizontalLayout_19.addWidget(self.total_cash_in_frame)

        self.total_cash_out_frame = QFrame(self.rn_bottom_widget)
        self.total_cash_out_frame.setObjectName(u"total_cash_out_frame")
        self.total_cash_out_frame.setFrameShape(QFrame.StyledPanel)
        self.total_cash_out_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.total_cash_out_frame)
        self.horizontalLayout_21.setSpacing(20)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
        self.lbl_total_cash_out = QLabel(self.total_cash_out_frame)
        self.lbl_total_cash_out.setObjectName(u"lbl_total_cash_out")
        self.lbl_total_cash_out.setFont(font4)

        self.horizontalLayout_21.addWidget(self.lbl_total_cash_out, 0, Qt.AlignRight)

        self.txt_total_cash_out = QLabel(self.total_cash_out_frame)
        self.txt_total_cash_out.setObjectName(u"txt_total_cash_out")
        self.txt_total_cash_out.setMinimumSize(QSize(0, 40))
        self.txt_total_cash_out.setFont(font8)
        self.txt_total_cash_out.setFrameShape(QFrame.Box)
        self.txt_total_cash_out.setFrameShadow(QFrame.Raised)
        self.txt_total_cash_out.setTextFormat(Qt.AutoText)

        self.horizontalLayout_21.addWidget(self.txt_total_cash_out)


        self.horizontalLayout_19.addWidget(self.total_cash_out_frame)


        self.verticalLayout_14.addWidget(self.rn_bottom_widget)

        self.stackedWidget.addWidget(self.roznamcha_page)
        self.supplier_page = QWidget()
        self.supplier_page.setObjectName(u"supplier_page")
        self.supplier_page.setStyleSheet(u"*{\n"
"	background-color: #e3f2fd;\n"
"}\n"
"\n"
"#lbl_supplier {\n"
"	background-color: #00b8d4;\n"
"	color: white;\n"
"}\n"
"\n"
"#supplier_upper_widget, #frame_5 {\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"#supplier_bottom_widget {\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"#total_supplier_frame {\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"#total_sup_rem_bal_frame {\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"#lbl_total_suppliers {\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"#lbl_sup_total_rem {\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"#txt_search_supplier {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"	border: 1px solid #00bcd4;\n"
"}\n"
"")
        self.verticalLayout_16 = QVBoxLayout(self.supplier_page)
        self.verticalLayout_16.setSpacing(0)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.lbl_supplier = QLabel(self.supplier_page)
        self.lbl_supplier.setObjectName(u"lbl_supplier")
        self.lbl_supplier.setMinimumSize(QSize(0, 50))
        self.lbl_supplier.setMaximumSize(QSize(16777215, 50))
        self.lbl_supplier.setFont(font3)
        self.lbl_supplier.setAlignment(Qt.AlignCenter)
        self.lbl_supplier.setMargin(10)

        self.verticalLayout_16.addWidget(self.lbl_supplier)

        self.supplier_upper_widget = QWidget(self.supplier_page)
        self.supplier_upper_widget.setObjectName(u"supplier_upper_widget")
        self.horizontalLayout_22 = QHBoxLayout(self.supplier_upper_widget)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.btn_add_supplier = QPushButton(self.supplier_upper_widget)
        self.btn_add_supplier.setObjectName(u"btn_add_supplier")
        self.btn_add_supplier.setMinimumSize(QSize(200, 40))
        self.btn_add_supplier.setMaximumSize(QSize(300, 40))
        self.btn_add_supplier.setFont(font1)
        self.btn_add_supplier.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_add_supplier.setIcon(icon10)
        self.btn_add_supplier.setIconSize(QSize(32, 32))

        self.horizontalLayout_22.addWidget(self.btn_add_supplier)

        self.txt_search_supplier = QLineEdit(self.supplier_upper_widget)
        self.txt_search_supplier.setObjectName(u"txt_search_supplier")
        self.txt_search_supplier.setMinimumSize(QSize(400, 40))
        self.txt_search_supplier.setMaximumSize(QSize(500, 40))
        self.txt_search_supplier.setFont(font5)

        self.horizontalLayout_22.addWidget(self.txt_search_supplier)

        self.frame_5 = QFrame(self.supplier_upper_widget)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_34 = QHBoxLayout(self.frame_5)
        self.horizontalLayout_34.setSpacing(20)
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.horizontalLayout_34.setContentsMargins(0, 0, 0, 0)
        self.btn_edit_supplier = QPushButton(self.frame_5)
        self.btn_edit_supplier.setObjectName(u"btn_edit_supplier")
        self.btn_edit_supplier.setMinimumSize(QSize(40, 40))
        self.btn_edit_supplier.setIcon(icon13)
        self.btn_edit_supplier.setIconSize(QSize(32, 32))

        self.horizontalLayout_34.addWidget(self.btn_edit_supplier, 0, Qt.AlignRight)

        self.btn_print_supplier = QPushButton(self.frame_5)
        self.btn_print_supplier.setObjectName(u"btn_print_supplier")
        self.btn_print_supplier.setMinimumSize(QSize(40, 40))
        self.btn_print_supplier.setIcon(icon14)
        self.btn_print_supplier.setIconSize(QSize(32, 32))

        self.horizontalLayout_34.addWidget(self.btn_print_supplier, 0, Qt.AlignRight)

        self.btn_refresh_supplier = QPushButton(self.frame_5)
        self.btn_refresh_supplier.setObjectName(u"btn_refresh_supplier")
        self.btn_refresh_supplier.setMinimumSize(QSize(40, 40))
        self.btn_refresh_supplier.setMaximumSize(QSize(40, 40))
        self.btn_refresh_supplier.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_refresh_supplier.setIcon(icon15)
        self.btn_refresh_supplier.setIconSize(QSize(32, 32))

        self.horizontalLayout_34.addWidget(self.btn_refresh_supplier)


        self.horizontalLayout_22.addWidget(self.frame_5, 0, Qt.AlignRight)


        self.verticalLayout_16.addWidget(self.supplier_upper_widget)

        self.supplier_table = QTableWidget(self.supplier_page)
        if (self.supplier_table.columnCount() < 5):
            self.supplier_table.setColumnCount(5)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setFont(font1);
        self.supplier_table.setHorizontalHeaderItem(0, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setFont(font1);
        self.supplier_table.setHorizontalHeaderItem(1, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        __qtablewidgetitem35.setFont(font1);
        self.supplier_table.setHorizontalHeaderItem(2, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        __qtablewidgetitem36.setFont(font1);
        self.supplier_table.setHorizontalHeaderItem(3, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        __qtablewidgetitem37.setFont(font1);
        self.supplier_table.setHorizontalHeaderItem(4, __qtablewidgetitem37)
        if (self.supplier_table.rowCount() < 20):
            self.supplier_table.setRowCount(20)
        self.supplier_table.setObjectName(u"supplier_table")
        self.supplier_table.setFont(font5)
        self.supplier_table.setFrameShape(QFrame.Box)
        self.supplier_table.setFrameShadow(QFrame.Raised)
        self.supplier_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.supplier_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.supplier_table.setDragDropOverwriteMode(True)
        self.supplier_table.setAlternatingRowColors(False)
        self.supplier_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.supplier_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.supplier_table.setTextElideMode(Qt.ElideRight)
        self.supplier_table.setShowGrid(True)
        self.supplier_table.setGridStyle(Qt.SolidLine)
        self.supplier_table.setSortingEnabled(True)
        self.supplier_table.setCornerButtonEnabled(True)
        self.supplier_table.setRowCount(20)
        self.supplier_table.horizontalHeader().setVisible(True)
        self.supplier_table.horizontalHeader().setCascadingSectionResizes(True)
        self.supplier_table.horizontalHeader().setDefaultSectionSize(150)
        self.supplier_table.horizontalHeader().setProperty("showSortIndicator", True)
        self.supplier_table.verticalHeader().setVisible(False)
        self.supplier_table.verticalHeader().setMinimumSectionSize(30)
        self.supplier_table.verticalHeader().setHighlightSections(True)
        self.supplier_table.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_16.addWidget(self.supplier_table)

        self.supplier_bottom_widget = QWidget(self.supplier_page)
        self.supplier_bottom_widget.setObjectName(u"supplier_bottom_widget")
        self.horizontalLayout_23 = QHBoxLayout(self.supplier_bottom_widget)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.total_supplier_frame = QFrame(self.supplier_bottom_widget)
        self.total_supplier_frame.setObjectName(u"total_supplier_frame")
        self.total_supplier_frame.setFrameShape(QFrame.StyledPanel)
        self.total_supplier_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_24 = QHBoxLayout(self.total_supplier_frame)
        self.horizontalLayout_24.setSpacing(20)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalLayout_24.setContentsMargins(0, 0, 0, 0)
        self.lbl_total_suppliers = QLabel(self.total_supplier_frame)
        self.lbl_total_suppliers.setObjectName(u"lbl_total_suppliers")
        self.lbl_total_suppliers.setFont(font4)

        self.horizontalLayout_24.addWidget(self.lbl_total_suppliers, 0, Qt.AlignRight)

        self.txt_total_supplier = QLabel(self.total_supplier_frame)
        self.txt_total_supplier.setObjectName(u"txt_total_supplier")
        self.txt_total_supplier.setMinimumSize(QSize(0, 40))
        self.txt_total_supplier.setFont(font8)
        self.txt_total_supplier.setFrameShape(QFrame.Box)
        self.txt_total_supplier.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_24.addWidget(self.txt_total_supplier)


        self.horizontalLayout_23.addWidget(self.total_supplier_frame)

        self.total_sup_rem_bal_frame = QFrame(self.supplier_bottom_widget)
        self.total_sup_rem_bal_frame.setObjectName(u"total_sup_rem_bal_frame")
        self.total_sup_rem_bal_frame.setFrameShape(QFrame.StyledPanel)
        self.total_sup_rem_bal_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.total_sup_rem_bal_frame)
        self.horizontalLayout_25.setSpacing(20)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_25.setContentsMargins(0, 0, 0, 0)
        self.lbl_sup_total_rem = QLabel(self.total_sup_rem_bal_frame)
        self.lbl_sup_total_rem.setObjectName(u"lbl_sup_total_rem")
        self.lbl_sup_total_rem.setFont(font4)

        self.horizontalLayout_25.addWidget(self.lbl_sup_total_rem, 0, Qt.AlignRight)

        self.txt_supplier_total_rem_balance = QLabel(self.total_sup_rem_bal_frame)
        self.txt_supplier_total_rem_balance.setObjectName(u"txt_supplier_total_rem_balance")
        self.txt_supplier_total_rem_balance.setMinimumSize(QSize(0, 40))
        self.txt_supplier_total_rem_balance.setFont(font8)
        self.txt_supplier_total_rem_balance.setFrameShape(QFrame.Box)
        self.txt_supplier_total_rem_balance.setFrameShadow(QFrame.Raised)
        self.txt_supplier_total_rem_balance.setTextFormat(Qt.AutoText)

        self.horizontalLayout_25.addWidget(self.txt_supplier_total_rem_balance)


        self.horizontalLayout_23.addWidget(self.total_sup_rem_bal_frame)


        self.verticalLayout_16.addWidget(self.supplier_bottom_widget)

        self.stackedWidget.addWidget(self.supplier_page)
        self.reports_page = QWidget()
        self.reports_page.setObjectName(u"reports_page")
        self.reports_page.setStyleSheet(u"\n"
"#lbl_reports {\n"
"	background-color: #00b8d4;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #fff;\n"
"}")
        self.verticalLayout_19 = QVBoxLayout(self.reports_page)
        self.verticalLayout_19.setSpacing(0)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_19.setContentsMargins(0, 0, 0, 0)
        self.lbl_reports = QLabel(self.reports_page)
        self.lbl_reports.setObjectName(u"lbl_reports")
        self.lbl_reports.setMinimumSize(QSize(0, 50))
        self.lbl_reports.setMaximumSize(QSize(16777215, 50))
        self.lbl_reports.setFont(font3)
        self.lbl_reports.setAlignment(Qt.AlignCenter)
        self.lbl_reports.setMargin(0)

        self.verticalLayout_19.addWidget(self.lbl_reports)

        self.reports_upper_widget = QWidget(self.reports_page)
        self.reports_upper_widget.setObjectName(u"reports_upper_widget")
        self.horizontalLayout_33 = QHBoxLayout(self.reports_upper_widget)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.btn_print_reports = QPushButton(self.reports_upper_widget)
        self.btn_print_reports.setObjectName(u"btn_print_reports")
        self.btn_print_reports.setMinimumSize(QSize(40, 40))
        self.btn_print_reports.setIcon(icon14)
        self.btn_print_reports.setIconSize(QSize(32, 32))

        self.horizontalLayout_33.addWidget(self.btn_print_reports, 0, Qt.AlignRight)


        self.verticalLayout_19.addWidget(self.reports_upper_widget, 0, Qt.AlignTop)

        self.main_details_widget = QWidget(self.reports_page)
        self.main_details_widget.setObjectName(u"main_details_widget")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.main_details_widget.sizePolicy().hasHeightForWidth())
        self.main_details_widget.setSizePolicy(sizePolicy)
        self.horizontalLayout_32 = QHBoxLayout(self.main_details_widget)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.frame_4 = QFrame(self.main_details_widget)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_31 = QHBoxLayout(self.frame_4)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.lft_frame = QFrame(self.frame_4)
        self.lft_frame.setObjectName(u"lft_frame")
        self.lft_frame.setFrameShape(QFrame.StyledPanel)
        self.lft_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.lft_frame)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label = QLabel(self.lft_frame)
        self.label.setObjectName(u"label")
        self.label.setFont(font4)

        self.verticalLayout_17.addWidget(self.label)

        self.label_2 = QLabel(self.lft_frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font4)

        self.verticalLayout_17.addWidget(self.label_2)

        self.label_3 = QLabel(self.lft_frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setFont(font4)

        self.verticalLayout_17.addWidget(self.label_3)

        self.label_4 = QLabel(self.lft_frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setFont(font4)

        self.verticalLayout_17.addWidget(self.label_4)

        self.label_5 = QLabel(self.lft_frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font4)

        self.verticalLayout_17.addWidget(self.label_5)

        self.label_9 = QLabel(self.lft_frame)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font4)

        self.verticalLayout_17.addWidget(self.label_9)

        self.label_10 = QLabel(self.lft_frame)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font)

        self.verticalLayout_17.addWidget(self.label_10)


        self.horizontalLayout_31.addWidget(self.lft_frame, 0, Qt.AlignTop)

        self.ri8_frame = QFrame(self.frame_4)
        self.ri8_frame.setObjectName(u"ri8_frame")
        self.ri8_frame.setFrameShape(QFrame.StyledPanel)
        self.ri8_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_18 = QVBoxLayout(self.ri8_frame)
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.total_stock_amount = QLabel(self.ri8_frame)
        self.total_stock_amount.setObjectName(u"total_stock_amount")
        self.total_stock_amount.setFont(font4)

        self.verticalLayout_18.addWidget(self.total_stock_amount)

        self.total_payable = QLabel(self.ri8_frame)
        self.total_payable.setObjectName(u"total_payable")
        self.total_payable.setFont(font4)

        self.verticalLayout_18.addWidget(self.total_payable)

        self.total_receivable = QLabel(self.ri8_frame)
        self.total_receivable.setObjectName(u"total_receivable")
        self.total_receivable.setFont(font4)

        self.verticalLayout_18.addWidget(self.total_receivable)

        self.total_sales = QLabel(self.ri8_frame)
        self.total_sales.setObjectName(u"total_sales")
        self.total_sales.setFont(font4)

        self.verticalLayout_18.addWidget(self.total_sales)

        self.total_stock_purchase = QLabel(self.ri8_frame)
        self.total_stock_purchase.setObjectName(u"total_stock_purchase")
        self.total_stock_purchase.setFont(font4)

        self.verticalLayout_18.addWidget(self.total_stock_purchase)

        self.total_expenses = QLabel(self.ri8_frame)
        self.total_expenses.setObjectName(u"total_expenses")
        self.total_expenses.setFont(font4)

        self.verticalLayout_18.addWidget(self.total_expenses)

        self.net_balance = QLabel(self.ri8_frame)
        self.net_balance.setObjectName(u"net_balance")
        self.net_balance.setFont(font)

        self.verticalLayout_18.addWidget(self.net_balance)


        self.horizontalLayout_31.addWidget(self.ri8_frame, 0, Qt.AlignTop)


        self.horizontalLayout_32.addWidget(self.frame_4)


        self.verticalLayout_19.addWidget(self.main_details_widget)

        self.stackedWidget.addWidget(self.reports_page)
        self.expense_page = QWidget()
        self.expense_page.setObjectName(u"expense_page")
        self.expense_page.setStyleSheet(u"\n"
"#lbl_expenses {\n"
"	background-color: #00b8d4;\n"
"	color: #fff;\n"
"	padding: 10px;\n"
"}\n"
"\n"
"#exp_upper_widget, #label_8, #label_7, #frame_3 {\n"
"	background-color: #b3e5fc;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QLineEdit, QDateEdit {\n"
"	background-color: #fff;\n"
"	border: 1px solid #00bcd4;\n"
"	border-radius: 5px;\n"
"}")
        self.verticalLayout_20 = QVBoxLayout(self.expense_page)
        self.verticalLayout_20.setSpacing(0)
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.verticalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.lbl_expenses = QLabel(self.expense_page)
        self.lbl_expenses.setObjectName(u"lbl_expenses")
        self.lbl_expenses.setFont(font3)
        self.lbl_expenses.setAlignment(Qt.AlignCenter)
        self.lbl_expenses.setMargin(0)

        self.verticalLayout_20.addWidget(self.lbl_expenses)

        self.exp_upper_widget = QWidget(self.expense_page)
        self.exp_upper_widget.setObjectName(u"exp_upper_widget")
        self.horizontalLayout_26 = QHBoxLayout(self.exp_upper_widget)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.btn_add_expense = QPushButton(self.exp_upper_widget)
        self.btn_add_expense.setObjectName(u"btn_add_expense")
        self.btn_add_expense.setMinimumSize(QSize(150, 40))
        self.btn_add_expense.setFont(font1)
        self.btn_add_expense.setIcon(icon10)
        self.btn_add_expense.setIconSize(QSize(32, 32))

        self.horizontalLayout_26.addWidget(self.btn_add_expense, 0, Qt.AlignLeft)

        self.txt_expense_search = QLineEdit(self.exp_upper_widget)
        self.txt_expense_search.setObjectName(u"txt_expense_search")
        self.txt_expense_search.setMinimumSize(QSize(400, 40))
        self.txt_expense_search.setFont(font5)

        self.horizontalLayout_26.addWidget(self.txt_expense_search, 0, Qt.AlignLeft)

        self.label_7 = QLabel(self.exp_upper_widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setFont(font5)

        self.horizontalLayout_26.addWidget(self.label_7)

        self.from_date_expense = QDateEdit(self.exp_upper_widget)
        self.from_date_expense.setObjectName(u"from_date_expense")
        self.from_date_expense.setMinimumSize(QSize(140, 40))
        self.from_date_expense.setFont(font5)
        self.from_date_expense.setCalendarPopup(True)

        self.horizontalLayout_26.addWidget(self.from_date_expense)

        self.label_8 = QLabel(self.exp_upper_widget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setFont(font5)

        self.horizontalLayout_26.addWidget(self.label_8)

        self.to_date_expense = QDateEdit(self.exp_upper_widget)
        self.to_date_expense.setObjectName(u"to_date_expense")
        self.to_date_expense.setMinimumSize(QSize(140, 40))
        self.to_date_expense.setFont(font5)
        self.to_date_expense.setCalendarPopup(True)

        self.horizontalLayout_26.addWidget(self.to_date_expense)

        self.btn_search_expense = QPushButton(self.exp_upper_widget)
        self.btn_search_expense.setObjectName(u"btn_search_expense")
        self.btn_search_expense.setMinimumSize(QSize(40, 40))
        self.btn_search_expense.setIcon(icon12)
        self.btn_search_expense.setIconSize(QSize(32, 32))

        self.horizontalLayout_26.addWidget(self.btn_search_expense, 0, Qt.AlignLeft)

        self.btn_expense_type = QPushButton(self.exp_upper_widget)
        self.btn_expense_type.setObjectName(u"btn_expense_type")
        self.btn_expense_type.setMinimumSize(QSize(160, 40))
        self.btn_expense_type.setFont(font4)
        self.btn_expense_type.setIcon(icon3)
        self.btn_expense_type.setIconSize(QSize(30, 30))

        self.horizontalLayout_26.addWidget(self.btn_expense_type, 0, Qt.AlignRight)

        self.frame_3 = QFrame(self.exp_upper_widget)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_30 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_30.setSpacing(20)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(0, 0, 0, 0)
        self.btn_edit_expense = QPushButton(self.frame_3)
        self.btn_edit_expense.setObjectName(u"btn_edit_expense")
        self.btn_edit_expense.setMinimumSize(QSize(40, 40))
        self.btn_edit_expense.setIcon(icon13)
        self.btn_edit_expense.setIconSize(QSize(32, 32))

        self.horizontalLayout_30.addWidget(self.btn_edit_expense)

        self.btn_expense_print = QPushButton(self.frame_3)
        self.btn_expense_print.setObjectName(u"btn_expense_print")
        self.btn_expense_print.setMinimumSize(QSize(40, 40))
        self.btn_expense_print.setIcon(icon14)
        self.btn_expense_print.setIconSize(QSize(32, 32))

        self.horizontalLayout_30.addWidget(self.btn_expense_print)

        self.btn_expense_refresh = QPushButton(self.frame_3)
        self.btn_expense_refresh.setObjectName(u"btn_expense_refresh")
        self.btn_expense_refresh.setMinimumSize(QSize(35, 35))
        self.btn_expense_refresh.setMaximumSize(QSize(16777215, 16777215))
        self.btn_expense_refresh.setIcon(icon15)
        self.btn_expense_refresh.setIconSize(QSize(32, 32))

        self.horizontalLayout_30.addWidget(self.btn_expense_refresh)


        self.horizontalLayout_26.addWidget(self.frame_3, 0, Qt.AlignRight)


        self.verticalLayout_20.addWidget(self.exp_upper_widget)

        self.expense_table = QTableWidget(self.expense_page)
        if (self.expense_table.columnCount() < 6):
            self.expense_table.setColumnCount(6)
        __qtablewidgetitem38 = QTableWidgetItem()
        __qtablewidgetitem38.setFont(font1);
        self.expense_table.setHorizontalHeaderItem(0, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        __qtablewidgetitem39.setFont(font1);
        self.expense_table.setHorizontalHeaderItem(1, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setFont(font1);
        self.expense_table.setHorizontalHeaderItem(2, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setFont(font1);
        self.expense_table.setHorizontalHeaderItem(3, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        __qtablewidgetitem42.setFont(font1);
        self.expense_table.setHorizontalHeaderItem(4, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        __qtablewidgetitem43.setFont(font1);
        self.expense_table.setHorizontalHeaderItem(5, __qtablewidgetitem43)
        if (self.expense_table.rowCount() < 15):
            self.expense_table.setRowCount(15)
        self.expense_table.setObjectName(u"expense_table")
        self.expense_table.setFont(font5)
        self.expense_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.expense_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.expense_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.expense_table.setRowCount(15)
        self.expense_table.horizontalHeader().setDefaultSectionSize(150)

        self.verticalLayout_20.addWidget(self.expense_table)

        self.exp_bottom_widget = QWidget(self.expense_page)
        self.exp_bottom_widget.setObjectName(u"exp_bottom_widget")
        self.horizontalLayout_27 = QHBoxLayout(self.exp_bottom_widget)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.label_6 = QLabel(self.exp_bottom_widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font4)

        self.horizontalLayout_27.addWidget(self.label_6, 0, Qt.AlignRight)

        self.total_expense = QLabel(self.exp_bottom_widget)
        self.total_expense.setObjectName(u"total_expense")
        self.total_expense.setFont(font)
        self.total_expense.setFrameShape(QFrame.Box)
        self.total_expense.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_27.addWidget(self.total_expense, 0, Qt.AlignLeft)


        self.verticalLayout_20.addWidget(self.exp_bottom_widget)

        self.stackedWidget.addWidget(self.expense_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.settings_page.setStyleSheet(u"*{\n"
"	background-color: #e3f2fd;\n"
"}\n"
"\n"
"#lbl_settings {\n"
"	background-color: #00b8d4;\n"
"	color: white;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QFrame {\n"
"	background-color: #eceff1;\n"
"}\n"
"\n"
"#create_widget {\n"
"	background-color: #bbdefb;\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.settings_page)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lbl_settings = QLabel(self.settings_page)
        self.lbl_settings.setObjectName(u"lbl_settings")
        self.lbl_settings.setMinimumSize(QSize(0, 50))
        self.lbl_settings.setMaximumSize(QSize(16777215, 50))
        self.lbl_settings.setFont(font3)
        self.lbl_settings.setAlignment(Qt.AlignCenter)
        self.lbl_settings.setMargin(0)

        self.verticalLayout_11.addWidget(self.lbl_settings)

        self.create_widget = QWidget(self.settings_page)
        self.create_widget.setObjectName(u"create_widget")
        self.create_widget.setMinimumSize(QSize(0, 0))
        self.create_widget.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_8 = QHBoxLayout(self.create_widget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_business_details = QPushButton(self.create_widget)
        self.btn_business_details.setObjectName(u"btn_business_details")
        self.btn_business_details.setMinimumSize(QSize(300, 40))
        self.btn_business_details.setMaximumSize(QSize(300, 40))
        self.btn_business_details.setFont(font3)
        self.btn_business_details.setIcon(icon10)
        self.btn_business_details.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.btn_business_details, 0, Qt.AlignLeft)

        self.btn_change_business_details = QPushButton(self.create_widget)
        self.btn_change_business_details.setObjectName(u"btn_change_business_details")
        self.btn_change_business_details.setMinimumSize(QSize(300, 40))
        self.btn_change_business_details.setMaximumSize(QSize(300, 40))
        self.btn_change_business_details.setFont(font1)
        self.btn_change_business_details.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_change_business_details.setIcon(icon13)
        self.btn_change_business_details.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.btn_change_business_details)

        self.btn_change_user_details = QPushButton(self.create_widget)
        self.btn_change_user_details.setObjectName(u"btn_change_user_details")
        self.btn_change_user_details.setMinimumSize(QSize(250, 40))
        self.btn_change_user_details.setMaximumSize(QSize(250, 40))
        self.btn_change_user_details.setFont(font1)
        self.btn_change_user_details.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_change_user_details.setIcon(icon13)
        self.btn_change_user_details.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.btn_change_user_details)

        self.btn_change_pwd = QPushButton(self.create_widget)
        self.btn_change_pwd.setObjectName(u"btn_change_pwd")
        self.btn_change_pwd.setMinimumSize(QSize(200, 40))
        self.btn_change_pwd.setMaximumSize(QSize(200, 40))
        self.btn_change_pwd.setFont(font1)
        self.btn_change_pwd.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_change_pwd.setIcon(icon13)
        self.btn_change_pwd.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.btn_change_pwd)


        self.verticalLayout_11.addWidget(self.create_widget)

        self.details_widget = QWidget(self.settings_page)
        self.details_widget.setObjectName(u"details_widget")
        self.details_widget.setMinimumSize(QSize(0, 0))
        self.details_widget.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_7 = QHBoxLayout(self.details_widget)
        self.horizontalLayout_7.setSpacing(70)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.business_frame = QFrame(self.details_widget)
        self.business_frame.setObjectName(u"business_frame")
        self.business_frame.setCursor(QCursor(Qt.OpenHandCursor))
        self.business_frame.setFrameShape(QFrame.StyledPanel)
        self.business_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.business_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.b_lbl_frame = QFrame(self.business_frame)
        self.b_lbl_frame.setObjectName(u"b_lbl_frame")
        self.b_lbl_frame.setFrameShape(QFrame.StyledPanel)
        self.b_lbl_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.b_lbl_frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lbl_b_name = QLabel(self.b_lbl_frame)
        self.lbl_b_name.setObjectName(u"lbl_b_name")
        self.lbl_b_name.setFont(font5)

        self.verticalLayout_9.addWidget(self.lbl_b_name)

        self.lbl_b_email = QLabel(self.b_lbl_frame)
        self.lbl_b_email.setObjectName(u"lbl_b_email")
        self.lbl_b_email.setFont(font5)

        self.verticalLayout_9.addWidget(self.lbl_b_email)

        self.lbl_b_contact = QLabel(self.b_lbl_frame)
        self.lbl_b_contact.setObjectName(u"lbl_b_contact")
        self.lbl_b_contact.setFont(font5)

        self.verticalLayout_9.addWidget(self.lbl_b_contact)

        self.lbl_b_address = QLabel(self.b_lbl_frame)
        self.lbl_b_address.setObjectName(u"lbl_b_address")
        self.lbl_b_address.setFont(font5)

        self.verticalLayout_9.addWidget(self.lbl_b_address)

        self.lbl_b_owner = QLabel(self.b_lbl_frame)
        self.lbl_b_owner.setObjectName(u"lbl_b_owner")
        self.lbl_b_owner.setFont(font5)

        self.verticalLayout_9.addWidget(self.lbl_b_owner)


        self.horizontalLayout_6.addWidget(self.b_lbl_frame)

        self.b_inputs_frame = QFrame(self.business_frame)
        self.b_inputs_frame.setObjectName(u"b_inputs_frame")
        self.b_inputs_frame.setFrameShape(QFrame.StyledPanel)
        self.b_inputs_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.b_inputs_frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.txt_business_name = QLabel(self.b_inputs_frame)
        self.txt_business_name.setObjectName(u"txt_business_name")
        self.txt_business_name.setFont(font1)

        self.verticalLayout_10.addWidget(self.txt_business_name)

        self.txt_business_email = QLabel(self.b_inputs_frame)
        self.txt_business_email.setObjectName(u"txt_business_email")
        self.txt_business_email.setFont(font1)

        self.verticalLayout_10.addWidget(self.txt_business_email)

        self.txt_business_contact = QLabel(self.b_inputs_frame)
        self.txt_business_contact.setObjectName(u"txt_business_contact")
        self.txt_business_contact.setFont(font1)

        self.verticalLayout_10.addWidget(self.txt_business_contact)

        self.txt_business_address = QLabel(self.b_inputs_frame)
        self.txt_business_address.setObjectName(u"txt_business_address")
        self.txt_business_address.setFont(font1)

        self.verticalLayout_10.addWidget(self.txt_business_address)

        self.txt_business_owner = QLabel(self.b_inputs_frame)
        self.txt_business_owner.setObjectName(u"txt_business_owner")
        self.txt_business_owner.setFont(font1)

        self.verticalLayout_10.addWidget(self.txt_business_owner)


        self.horizontalLayout_6.addWidget(self.b_inputs_frame)


        self.horizontalLayout_7.addWidget(self.business_frame)

        self.user_detail_frame = QFrame(self.details_widget)
        self.user_detail_frame.setObjectName(u"user_detail_frame")
        self.user_detail_frame.setFrameShape(QFrame.StyledPanel)
        self.user_detail_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.user_detail_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.u_lbl_frame = QFrame(self.user_detail_frame)
        self.u_lbl_frame.setObjectName(u"u_lbl_frame")
        self.u_lbl_frame.setFrameShape(QFrame.StyledPanel)
        self.u_lbl_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.u_lbl_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.lbl_u_name = QLabel(self.u_lbl_frame)
        self.lbl_u_name.setObjectName(u"lbl_u_name")
        self.lbl_u_name.setFont(font5)

        self.verticalLayout_8.addWidget(self.lbl_u_name)

        self.lbl_u_email = QLabel(self.u_lbl_frame)
        self.lbl_u_email.setObjectName(u"lbl_u_email")
        self.lbl_u_email.setFont(font5)

        self.verticalLayout_8.addWidget(self.lbl_u_email)

        self.lbl_u_contact = QLabel(self.u_lbl_frame)
        self.lbl_u_contact.setObjectName(u"lbl_u_contact")
        self.lbl_u_contact.setFont(font5)

        self.verticalLayout_8.addWidget(self.lbl_u_contact)

        self.lbl_u_username = QLabel(self.u_lbl_frame)
        self.lbl_u_username.setObjectName(u"lbl_u_username")
        self.lbl_u_username.setFont(font5)

        self.verticalLayout_8.addWidget(self.lbl_u_username)


        self.horizontalLayout_5.addWidget(self.u_lbl_frame)

        self.u_inputs_frame = QFrame(self.user_detail_frame)
        self.u_inputs_frame.setObjectName(u"u_inputs_frame")
        self.u_inputs_frame.setFrameShape(QFrame.StyledPanel)
        self.u_inputs_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.u_inputs_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.txt_user_name = QLabel(self.u_inputs_frame)
        self.txt_user_name.setObjectName(u"txt_user_name")
        self.txt_user_name.setFont(font1)

        self.verticalLayout_7.addWidget(self.txt_user_name)

        self.txt_user_email = QLabel(self.u_inputs_frame)
        self.txt_user_email.setObjectName(u"txt_user_email")
        self.txt_user_email.setFont(font1)

        self.verticalLayout_7.addWidget(self.txt_user_email)

        self.txt_user_contact = QLabel(self.u_inputs_frame)
        self.txt_user_contact.setObjectName(u"txt_user_contact")
        self.txt_user_contact.setFont(font1)

        self.verticalLayout_7.addWidget(self.txt_user_contact)

        self.txt_user_username = QLabel(self.u_inputs_frame)
        self.txt_user_username.setObjectName(u"txt_user_username")
        self.txt_user_username.setFont(font1)

        self.verticalLayout_7.addWidget(self.txt_user_username)


        self.horizontalLayout_5.addWidget(self.u_inputs_frame)


        self.horizontalLayout_7.addWidget(self.user_detail_frame)


        self.verticalLayout_11.addWidget(self.details_widget)

        self.free_widget = QWidget(self.settings_page)
        self.free_widget.setObjectName(u"free_widget")

        self.verticalLayout_11.addWidget(self.free_widget)

        self.stackedWidget.addWidget(self.settings_page)

        self.verticalLayout_15.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ComPy Softwares", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_product.setText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.btn_sales.setText(QCoreApplication.translate("MainWindow", u"Sales", None))
        self.btn_customer.setText(QCoreApplication.translate("MainWindow", u"Customer", None))
        self.btn_supplier.setText(QCoreApplication.translate("MainWindow", u"Supplier", None))
        self.btn_roznamcha.setText(QCoreApplication.translate("MainWindow", u"Roz Namcha", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btn_reports.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.btn_expense.setText(QCoreApplication.translate("MainWindow", u"Expense", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.lbl_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.lbl_business_name.setText(QCoreApplication.translate("MainWindow", u"Business Name", None))
        self.lbl_business_contact.setText(QCoreApplication.translate("MainWindow", u"Business Contact", None))
        self.lbl_business_address.setText(QCoreApplication.translate("MainWindow", u"Business Address", None))
        self.lbl_contact.setText(QCoreApplication.translate("MainWindow", u"+92 335 2321360", None))
        self.lbl_description.setText(QCoreApplication.translate("MainWindow", u"Software Developed By:", None))
        self.lbl_company.setText(QCoreApplication.translate("MainWindow", u"ComPy Softwares Quetta", None))
        self.lbl_product.setText(QCoreApplication.translate("MainWindow", u"Product", None))
        self.btn_add_product.setText(QCoreApplication.translate("MainWindow", u"Add Product", None))
        self.btn_add_stock.setText(QCoreApplication.translate("MainWindow", u"Add Stock", None))
        self.select_product.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Product", None))

        self.lbl_average_price.setText(QCoreApplication.translate("MainWindow", u"Average Price", None))
        self.txt_average_price.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lbl_products.setText(QCoreApplication.translate("MainWindow", u"Products", None))
        ___qtablewidgetitem = self.product_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Product Name", None));
        ___qtablewidgetitem1 = self.product_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Available Stock", None));
        ___qtablewidgetitem2 = self.product_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"UoM", None));

        __sortingEnabled = self.product_table.isSortingEnabled()
        self.product_table.setSortingEnabled(False)
        self.product_table.setSortingEnabled(__sortingEnabled)

        self.lbl_stock.setText(QCoreApplication.translate("MainWindow", u"Stock", None))
        ___qtablewidgetitem3 = self.stock_table.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem4 = self.stock_table.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Supplier", None));
        ___qtablewidgetitem5 = self.stock_table.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Stock", None));
        ___qtablewidgetitem6 = self.stock_table.horizontalHeaderItem(3)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Rate", None));
        ___qtablewidgetitem7 = self.stock_table.horizontalHeaderItem(4)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        self.lbl_sales.setText(QCoreApplication.translate("MainWindow", u"Sales", None))
        self.btn_add_sale.setText(QCoreApplication.translate("MainWindow", u"Create Sale", None))
        self.txt_search_sale.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search here", None))
        self.lbl_from_sale.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.lbl_to_sale.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.btn_search_sale.setText("")
        self.btn_edit_sales.setText("")
        self.btn_print_sale.setText("")
        self.btn_refresh_sale.setText("")
        ___qtablewidgetitem8 = self.sales_table.horizontalHeaderItem(0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem9 = self.sales_table.horizontalHeaderItem(1)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Customer", None));
        ___qtablewidgetitem10 = self.sales_table.horizontalHeaderItem(2)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem11 = self.sales_table.horizontalHeaderItem(3)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Rate", None));
        ___qtablewidgetitem12 = self.sales_table.horizontalHeaderItem(4)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem13 = self.sales_table.horizontalHeaderItem(5)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Cash Paid", None));
        ___qtablewidgetitem14 = self.sales_table.horizontalHeaderItem(6)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Cash Received", None));
        ___qtablewidgetitem15 = self.sales_table.horizontalHeaderItem(7)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Remaining", None));
        self.lbl_total_sales.setText(QCoreApplication.translate("MainWindow", u"Total Sales Amount:", None))
        self.txt_total_sales.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lbl_total_cash_paid.setText(QCoreApplication.translate("MainWindow", u"Total Cash Paid :", None))
        self.txt_total_cash_paid.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lbl_total_cash_recv.setText(QCoreApplication.translate("MainWindow", u"Total Cash Received :", None))
        self.txt_total_cash_received.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lbl_customer.setText(QCoreApplication.translate("MainWindow", u"Customers", None))
        self.btn_add_customer.setText(QCoreApplication.translate("MainWindow", u"Add Customer", None))
        self.txt_search_customer.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search here", None))
        self.btn_edit_customer.setText("")
        self.btn_print_customer.setText("")
        self.btn_refresh_customer.setText("")
        ___qtablewidgetitem16 = self.customer_table.horizontalHeaderItem(0)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Customer id.", None));
        ___qtablewidgetitem17 = self.customer_table.horizontalHeaderItem(1)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Customer Name", None));
        ___qtablewidgetitem18 = self.customer_table.horizontalHeaderItem(2)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Vehicle No.", None));
        ___qtablewidgetitem19 = self.customer_table.horizontalHeaderItem(3)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Mobile", None));
        ___qtablewidgetitem20 = self.customer_table.horizontalHeaderItem(4)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem21 = self.customer_table.horizontalHeaderItem(5)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"R Balance", None));
        self.lbl_total_customers.setText(QCoreApplication.translate("MainWindow", u"Total Customers :", None))
        self.txt_total_customers.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lbl_total_remaining.setText(QCoreApplication.translate("MainWindow", u"Total Balance Remaining :", None))
        self.txt_total_rem_balance.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lbl_roznamcha.setText(QCoreApplication.translate("MainWindow", u"Roz Namcha", None))
        self.btn_add_roznamcha.setText(QCoreApplication.translate("MainWindow", u"Add RozNamcha", None))
        self.txt_search_rn.setPlaceholderText(QCoreApplication.translate("MainWindow", u"searh here", None))
        self.lbl_from_rn.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.lbl_to_rn.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.btn_search_rn.setText("")
        self.btn_edit_rn.setText("")
        self.btn_print_rn.setText("")
        self.btn_refresh_rn.setText("")
        ___qtablewidgetitem22 = self.roznamcha_table.horizontalHeaderItem(0)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem23 = self.roznamcha_table.horizontalHeaderItem(1)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Product", None));
        ___qtablewidgetitem24 = self.roznamcha_table.horizontalHeaderItem(2)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Quantity", None));
        ___qtablewidgetitem25 = self.roznamcha_table.horizontalHeaderItem(3)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Rate", None));
        ___qtablewidgetitem26 = self.roznamcha_table.horizontalHeaderItem(4)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem27 = self.roznamcha_table.horizontalHeaderItem(5)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Customer", None));
        ___qtablewidgetitem28 = self.roznamcha_table.horizontalHeaderItem(6)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Cash Paid", None));
        ___qtablewidgetitem29 = self.roznamcha_table.horizontalHeaderItem(7)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Cash Received", None));

        __sortingEnabled1 = self.roznamcha_table.isSortingEnabled()
        self.roznamcha_table.setSortingEnabled(False)
        self.roznamcha_table.setSortingEnabled(__sortingEnabled1)

        self.lbl_total_cashIn.setText(QCoreApplication.translate("MainWindow", u"Total Cash In Amount :", None))
        self.txt_total_cash_in.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lbl_total_cash_out.setText(QCoreApplication.translate("MainWindow", u"Total Cash Out Amount :", None))
        self.txt_total_cash_out.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lbl_supplier.setText(QCoreApplication.translate("MainWindow", u"Suppliers", None))
        self.btn_add_supplier.setText(QCoreApplication.translate("MainWindow", u"Add Supplier", None))
        self.txt_search_supplier.setPlaceholderText(QCoreApplication.translate("MainWindow", u"search here", None))
        self.btn_edit_supplier.setText("")
        self.btn_print_supplier.setText("")
        self.btn_refresh_supplier.setText("")
        ___qtablewidgetitem30 = self.supplier_table.horizontalHeaderItem(0)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Supplier id.", None));
        ___qtablewidgetitem31 = self.supplier_table.horizontalHeaderItem(1)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Supplier Name", None));
        ___qtablewidgetitem32 = self.supplier_table.horizontalHeaderItem(2)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Mobile", None));
        ___qtablewidgetitem33 = self.supplier_table.horizontalHeaderItem(3)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem34 = self.supplier_table.horizontalHeaderItem(4)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Opening Balance", None));
        self.lbl_total_suppliers.setText(QCoreApplication.translate("MainWindow", u"Total Suppliers :", None))
        self.txt_total_supplier.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lbl_sup_total_rem.setText(QCoreApplication.translate("MainWindow", u"Total Balance Remaining :", None))
        self.txt_supplier_total_rem_balance.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lbl_reports.setText(QCoreApplication.translate("MainWindow", u"Reports", None))
        self.btn_print_reports.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Total Stock Amount", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Total Payable Amount", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Total Receivable Amount", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Total Sales", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Total Stock Purchase", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Total Expense", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Net Balance", None))
        self.total_stock_amount.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.total_payable.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.total_receivable.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.total_sales.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.total_stock_purchase.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.total_expenses.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.net_balance.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_expenses.setText(QCoreApplication.translate("MainWindow", u"Expenses", None))
        self.btn_add_expense.setText(QCoreApplication.translate("MainWindow", u"Add Expense", None))
        self.txt_expense_search.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Search Here", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.btn_search_expense.setText("")
        self.btn_expense_type.setText(QCoreApplication.translate("MainWindow", u"Expense Type", None))
        self.btn_edit_expense.setText("")
        self.btn_expense_print.setText("")
        self.btn_expense_refresh.setText("")
        ___qtablewidgetitem35 = self.expense_table.horizontalHeaderItem(0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem36 = self.expense_table.horizontalHeaderItem(1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Head of Account", None));
        ___qtablewidgetitem37 = self.expense_table.horizontalHeaderItem(2)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Amount", None));
        ___qtablewidgetitem38 = self.expense_table.horizontalHeaderItem(3)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Payment Type", None));
        ___qtablewidgetitem39 = self.expense_table.horizontalHeaderItem(4)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Recipient name", None));
        ___qtablewidgetitem40 = self.expense_table.horizontalHeaderItem(5)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Comments", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Total Expense:", None))
        self.total_expense.setText(QCoreApplication.translate("MainWindow", u"0", None))
        self.lbl_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btn_business_details.setText(QCoreApplication.translate("MainWindow", u"Business Details", None))
        self.btn_change_business_details.setText(QCoreApplication.translate("MainWindow", u"Change Business Details", None))
        self.btn_change_user_details.setText(QCoreApplication.translate("MainWindow", u"Change User Deatils", None))
        self.btn_change_pwd.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.lbl_b_name.setText(QCoreApplication.translate("MainWindow", u"Business Name", None))
        self.lbl_b_email.setText(QCoreApplication.translate("MainWindow", u"Business Email", None))
        self.lbl_b_contact.setText(QCoreApplication.translate("MainWindow", u"Business Contact", None))
        self.lbl_b_address.setText(QCoreApplication.translate("MainWindow", u"Business Address", None))
        self.lbl_b_owner.setText(QCoreApplication.translate("MainWindow", u"Business Owner", None))
        self.txt_business_name.setText(QCoreApplication.translate("MainWindow", u"Business Name", None))
        self.txt_business_email.setText(QCoreApplication.translate("MainWindow", u"Business Email", None))
        self.txt_business_contact.setText(QCoreApplication.translate("MainWindow", u"Business Contact", None))
        self.txt_business_address.setText(QCoreApplication.translate("MainWindow", u"Business Address", None))
        self.txt_business_owner.setText(QCoreApplication.translate("MainWindow", u"Business Owner", None))
        self.lbl_u_name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.lbl_u_email.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lbl_u_contact.setText(QCoreApplication.translate("MainWindow", u"Contact", None))
        self.lbl_u_username.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.txt_user_name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.txt_user_email.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.txt_user_contact.setText(QCoreApplication.translate("MainWindow", u"Contact", None))
        self.txt_user_username.setText(QCoreApplication.translate("MainWindow", u"Username", None))
    # retranslateUi

