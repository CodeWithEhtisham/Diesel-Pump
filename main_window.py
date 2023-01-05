
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from db_handler import DBHandler
import sys
from create_business import NewBusinessWindow
from update_business_details import UpdateBusinessWindow
from update_user_details import UpdateUserWindow
from update_password import ChangePasswordWindow
from add_customer import AddCustomerWindow
from add_product import AddProductWindow
from add_stock import AddStockWindow
from add_sale import SalesWindow
from add_roznamcha import RozNamchaWindow
from account_details import AccountDetailsWindow
from supplier_account_details import SupplierAccountDetailsWindow
from add_supplier import AddSupplierWindow
from cash_paid import CashPaidWindow
from PyQt5.uic import loadUiType

FORM_MAIN, _ = loadUiType('ui/main_window.ui')


class MainWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.showMaximized()
        self.update()
        # home page show when window open on load
        self.Handle_Buttons()
    
    def Handle_Buttons(self):
        self.btn_home.clicked.connect(self.home)
        self.btn_product.clicked.connect(self.product)
        self.btn_sales.clicked.connect(self.sales)
        self.btn_customer.clicked.connect(self.customer)
        self.btn_roznamcha.clicked.connect(self.roznamcha)
        self.btn_settings.clicked.connect(self.settings)
        self.btn_supplier.clicked.connect(self.supplier)
        self.btn_add_product.clicked.connect(self.add_product)
        self.btn_add_stock.clicked.connect(self.add_stock)
        self.btn_add_customer.clicked.connect(self.add_customer)
        self.btn_add_sale.clicked.connect(self.add_sales)
        self.btn_add_roznamcha.clicked.connect(self.add_roznamcha)
        self.btn_add_supplier.clicked.connect(self.add_supplier)
        # self.search_option_sale.activated.connect(self.)
        self.txt_search_sale.textChanged.connect(self.sale_search_by_option)
        self.btn_search_sale.clicked.connect(self.sale_search_by_date)
        self.btn_logout.clicked.connect(self.logout)
        self.customer_table.doubleClicked.connect(self.customer_detail_widget)
        self.supplier_table.doubleClicked.connect(self.supplier_account_details)

        # business btns
        self.btn_business_details.clicked.connect(self.business_details)
        self.btn_change_business_details.clicked.connect(self.edit_business)

        # edit user details btns
        self.btn_change_user_details.clicked.connect(self.change_user_details)
        self.btn_change_pwd.clicked.connect(self.change_password)

        self.btn_refresh_customer.clicked.connect(self.update_customer_widget)
        self.btn_search_customer.clicked.connect(self.customer_search)

        self.txt_search_supplier.textChanged.connect(self.supplier_search)
        self.btn_refresh_supplier.clicked.connect(self.update)
        
        
        # product qcombobox select value
        self.select_product.activated.connect(self.stock_search)
        self.txt_date.setDate(QDate.currentDate())
        # on date change event
        self.txt_date.dateChanged.connect(self.stock_search_by_date)
        self.txt_search_rn.textChanged.connect(self.search_roznamcha_by_name)
        self.btn_search_rn.clicked.connect(self.search_roznamcha_by_date)
        self.btn_refresh_rn.clicked.connect(self.update)
        
    def supplier_search(self):
        option = self.search_option_supplier.currentText()
        search = self.txt_search_supplier.text()
        db=DBHandler()
        if option == "By Name":
            data=db.select(table_name='suppliers',columns='supplier_id,name,phone,address,balance',condition=f"name LIKE '%{search}%'")
            self.update_table(data,self.supplier_table)
        elif option=="By Contact":
            data = db.select(table_name='suppliers',columns='supplier_id,name,phone,address,balance',condition=f"phone LIKE '%{search}%'")
            self.update_table(data,self.supplier_table)
        elif option == "By Address":
            data = db.select(table_name='suppliers',columns='supplier_id,name,phone,address,balance',condition=f"address LIKE '%{search}%'")
            self.update_table(data,self.supplier_table)
        else:
            # please select option 
            QMessageBox.information(self,"Error","Please select option")

    def supplier_account_details(self):
        row=self.supplier_table.currentRow()
        id=self.supplier_table.item(row,0).text()
        self.window= SupplierAccountDetailsWindow(id)
        self.window.show()

    def add_supplier(self):
        self.window = AddSupplierWindow()
        self.window.show()

    def logout(self):
        from login_page import LoginWindow
        self.login = LoginWindow()
        self.login.show()
        self.close()

    def customer_detail_widget(self):
        # get row number and its value
        row=self.customer_table.currentRow()
        id=self.customer_table.item(row,0).text()
        self.window = AccountDetailsWindow(id)
        self.window.show()

    def search_roznamcha_by_date(self):
        from_date=self.txt_date_from_rn.date().toString("dd/MM/yyyy")
        to_date=self.txt_date_to_rn.date().toString("dd/MM/yyyy")
        db=DBHandler()
        data=db.conn.execute(f"SELECT products.product_name,customers.name,date,quantity,rate,total_amount,cash_paid,cash_received FROM roznamcha LEFT JOIN customers ON roznamcha.customer_id=customers.custmer_id LEFT JOIN products ON roznamcha.product_id=products.product_id WHERE roznamcha.date BETWEEN '{from_date}' AND '{to_date}'").fetchall()
        self.roznamcha_table.setRowCount(0)
        for index,row in enumerate(data):
                self.roznamcha_table.insertRow(index)
                for idx,i in enumerate(row):
                    self.roznamcha_table.setItem(index,idx,QTableWidgetItem(str(i)))



    def search_roznamcha_by_name(self):
        option=self.search_option_rn.currentText()
        if option=="Select Option":
            QMessageBox.warning(self,"Error","Please Select Search Option")
        else:
            value=self.txt_search_rn.text()
            db=DBHandler()
            data=db.conn.execute(f"SELECT products.product_name,customers.name,date,quantity,rate,total_amount,cash_paid,cash_received FROM roznamcha LEFT JOIN customers ON roznamcha.customer_id=customers.custmer_id LEFT JOIN products ON roznamcha.product_id=products.product_id Where customers.name LIKE '%{value}%'").fetchall()
            self.roznamcha_table.setRowCount(0)
            for index,row in enumerate(data):
                self.roznamcha_table.insertRow(index)
                for idx,i in enumerate(row):
                    self.roznamcha_table.setItem(index,idx,QTableWidgetItem(str(i)))


    def add_roznamcha(self):
        self.roznamcha_window=RozNamchaWindow()
        self.roznamcha_window.show()

    def sale_search_by_date(self):
        from_date=self.txt_date_from_sale.date().toString("dd/MM/yyyy")
        to_date=self.txt_date_to_sale.date().toString("dd/MM/yyyy")
        db=DBHandler()
        data=db.conn.execute(f"SELECT sales.date,customers.name,sales.quantity,sales.rate,sales.total_amount,sales.cash_paid,sales.cash_received,sales.sub_total FROM sales LEFT JOIN customers ON sales.customer_id=customers.custmer_id WHERE sales.date BETWEEN '{from_date}' AND '{to_date}'").fetchall()
        self.sales_table.setRowCount(0)
        for index,row in enumerate(data):
            self.sales_table.insertRow(index)
            for idx,i in enumerate(row):
                self.sales_table.setItem(index,idx,QTableWidgetItem(str(i)))


    def sale_search_by_option(self):
        option=self.search_option_sale.currentText()
        value=self.txt_search_sale.text()
        if option=="Select Option":
            QMessageBox.warning(self,"Error","Please Select Search Option")
        elif option=="By Name":
            db=DBHandler()
            data=db.conn.execute(f"SELECT sales.date,customers.name,sales.quantity,sales.rate,sales.total_amount,sales.cash_paid,sales.cash_received,sales.sub_total FROM sales LEFT JOIN customers ON sales.customer_id=customers.custmer_id WHERE customers.name LIKE '%{value}%'").fetchall()
            self.sales_table.setRowCount(0)
            for index,row in enumerate(data):
                self.sales_table.insertRow(index)
                for idx,i in enumerate(row):
                    self.sales_table.setItem(index,idx,QTableWidgetItem(str(i)))
        elif option=="By Contact":
            db=DBHandler()
            data=db.conn.execute(f"SELECT sales.date,customers.name,sales.quantity,sales.rate,sales.total_amount,sales.cash_paid,sales.cash_received,sales.sub_total FROM sales LEFT JOIN customers ON sales.customer_id=customers.custmer_id WHERE customers.phone LIKE '%{value}%'").fetchall()
            self.sales_table.setRowCount(0)
            for index,row in enumerate(data):
                self.sales_table.insertRow(index)
                for idx,i in enumerate(row):
                    self.sales_table.setItem(index,idx,QTableWidgetItem(str(i)))


    def add_sales(self):
        self.sale_window= SalesWindow()
        self.sale_window.show()

    def customer_search(self):
        option=self.search_option_customer.currentText()
        value=self.txt_search_customer.text()
        if option=="Select Option":
            QMessageBox.warning(self,"Error","Please Select Search Option")
        else:
            db=DBHandler()
            if option=="By Name":
                data=db.conn.execute(f"SELECT * FROM customers WHERE name LIKE '%{value}%'").fetchall()
            elif option=="By Contact":
                data=db.conn.execute(f"SELECT * FROM customers WHERE phone LIKE '%{value}%'").fetchall()
            elif option=="By Vehicle":
                data=db.conn.execute(f"SELECT * FROM customers WHERE vehicle LIKE '%{value}%'").fetchall()
            self.customer_table.setRowCount(0)
            for index,row in enumerate(data):
                self.customer_table.insertRow(index)
                for idx,i in enumerate(row):
                    self.customer_table.setItem(index,idx,QTableWidgetItem(str(i)))

    def add_customer(self):
        self.add_customer_window= AddCustomerWindow()
        self.add_customer_window.show()

    def stock_search_by_date(self):
        date=self.txt_date.date().toString("dd/MM/yyyy")
        product=self.select_product.currentText()
        # empty stock table
        self.stock_table.setRowCount(0)
        db=DBHandler()
        if product=="Select Product":
            print(date)
            data = db.conn.execute(f'SELECT date,supplier,stock,rate,amount FROM stock WHERE date="{date}"').fetchall()
            print('if',data)
            for index,row in enumerate(data):
                self.stock_table.insertRow(index)
                for idx,i in enumerate(row):
                    print(i)
                    self.stock_table.setItem(index,idx,QTableWidgetItem(str(i)))
        else:
            product_id=db.conn.execute(f"SELECT product_id FROM products WHERE product_name='{product}'").fetchone()[0]
            data = db.conn.execute(f"SELECT date,supplier,stock,rate,amount FROM stock WHERE date='{date}' and product_id={product_id}").fetchall()
            print('else')
            for index,row in enumerate(data):
                self.stock_table.insertRow(index)
                for idx,i in enumerate(row):
                    print(i)
                    self.stock_table.setItem(index,idx,QTableWidgetItem(str(i)))

        
    def update_table(self,data,obj):
        obj.setRowCount(0)
        for index,row in enumerate(data):
            obj.insertRow(index)
            for idx,i in enumerate(row):
                obj.setItem(index,idx,QTableWidgetItem(str(i)))
        # main page
    def update(self):

        db= DBHandler()
        data= db.select_all('products',"*")
        self.select_product.clear()
        self.select_product.addItem("Select Product")
        if data:
            for row in data:
                # print(row)
                self.select_product.addItem(row[1])
        data=db.select(table_name='business',columns="*",condition="id=1")
        if data:
            self.lbl_business_name.setText(data[0][1])
            self.lbl_business_contact.setText(data[0][4])
            self.lbl_business_address.setText(data[0][3])

        
        # clean qcombo box
        

        # get all products with total stock if not exit return 0
        data=db.conn.execute("SELECT products.product_name, SUM(stock.stock),products.uom FROM products LEFT JOIN stock ON products.product_id = stock.product_id GROUP BY products.product_id ORDER BY products.product_id and ifnull(stock.stock,0)").fetchall()
        # print(data)
        self.product_table.setRowCount(0)
        for index,row in enumerate(data):
            self.product_table.insertRow(index)
            for i in row:
                self.product_table.setItem(index,row.index(i),QTableWidgetItem(str(i)))

        data = db.conn.execute("SELECT date,supplier,stock,rate,amount FROM stock").fetchall()
        # print(data)
        self.stock_table.setRowCount(0)
        for index,row in enumerate(data):
            self.stock_table.insertRow(index)
            # print(row)
            for idx,i in enumerate(row):
                # print(i)
                self.stock_table.setItem(index,idx,QTableWidgetItem(str(i)))
        # calculate today avg rate of stock
        current_date=QDate.currentDate().toString("dd/MM/yyyy")
        data=db.conn.execute(f"SELECT AVG(rate) FROM stock WHERE date='{current_date}'").fetchone()[0]
        self.txt_average_price.setText(str(data))

        # search all sales information with customer name
        data= db.conn.execute("SELECT sales.date,customers.name,sales.quantity,sales.rate,sales.total_amount,sales.cash_paid,sales.cash_received,sales.sub_total FROM sales LEFT JOIN customers ON sales.customer_id=customers.custmer_id").fetchall()
        # print(f"sales {data}")
        self.sales_table.setRowCount(0)
        total=0
        cash_paid=0
        cash_received=0
        for index,row in enumerate(data):
            self.sales_table.insertRow(index)
            # print(row)
            total+=row[4]
            cash_paid+=row[5]
            cash_received+=row[6]
            for idx,i in enumerate(row):
                # print(i)
                self.sales_table.setItem(index,idx,QTableWidgetItem(str(i)))
        
        self.txt_total_sales.setText(str(total))
        self.txt_total_cash_paid.setText(str(cash_paid))
        self.txt_total_cash_received.setText(str(cash_received))
        self.txt_date_from_sale.setDate(QDate.currentDate())
        self.txt_date_to_sale.setDate(QDate.currentDate())

        data = db.conn.execute(f"SELECT products.product_name,customers.name,date,quantity,rate,total_amount,cash_paid,cash_received FROM roznamcha LEFT JOIN customers ON roznamcha.customer_id=customers.custmer_id LEFT JOIN products ON roznamcha.product_id=products.product_id ").fetchall()
        self.roznamcha_table.setRowCount(0)
        # print(data)
        cash_paid=0
        cash_received=0
        for index,row in enumerate(data):
            self.roznamcha_table.insertRow(index)
            cash_paid+=row[-2]
            cash_received+=row[-1]
            for idx,i in enumerate(row):
                self.roznamcha_table.setItem(index,idx,QTableWidgetItem(str(i)))
        self.txt_date_to_rn.setDate(QDate.currentDate())
        self.txt_date_from_rn.setDate(QDate.currentDate())
        self.txt_total_cash_in.setText(str(cash_received))
        self.txt_total_cash_out.setText(str(cash_paid))

        # get supplier data
        data = db.select_all(table_name="suppliers",columns="supplier_id,name,phone,address,balance")
        self.update_table(data,self.supplier_table)
        self.txt_total_supplier.setText(str(len(data)))
        self.txt_supplier_total_rem_balance.setText(str(sum([float(i[-1]) for i in data])))




    

    def update_customer_widget(self):
        db=DBHandler()
        data=db.select_all('customers','custmer_id,name,phone,vehicle,address,balance')
        print(data)
        self.customer_table.setRowCount(0)
        balance=[]
        for index,row in enumerate(data):
            balance.append(row[-1])
            self.customer_table.insertRow(index)
            print(row)
            for idx,i in enumerate(row):
                # print(i)
                self.customer_table.setItem(index,idx,QTableWidgetItem(str(i)))
        self.txt_total_customers.setText(str(len(data)))
        self.txt_total_rem_balance.setText(str(sum(balance)))


    def stock_search(self):
        product=self.select_product.currentText()
        # empty stock table 
        self.stock_table.setRowCount(0)
        db=DBHandler()
        if product=="Select Product":
            data = db.conn.execute("SELECT date,supplier,stock,rate,amount FROM stock").fetchall()
            print('if')
            for index,row in enumerate(data):
                self.stock_table.insertRow(index)
                for idx,i in enumerate(row):
                    print(i)
                    self.stock_table.setItem(index,idx,QTableWidgetItem(str(i)))
        else:
            product_id=db.conn.execute(f"SELECT product_id FROM products WHERE product_name='{product}'").fetchone()[0]
            data = db.conn.execute(f"SELECT date,supplier,stock,rate,amount FROM stock WHERE product_id={product_id}").fetchall()
            print('else')
            for index,row in enumerate(data):
                self.stock_table.insertRow(index)
                for idx,i in enumerate(row):
                    print(i)
                    self.stock_table.setItem(index,idx,QTableWidgetItem(str(i)))


    def add_product(self):
        self.add_product_window = AddProductWindow()
        self.add_product_window.show()
        

    def add_stock(self):
        self.add_stock_window = AddStockWindow()
        self.add_stock_window.show()

    
    def change_user_details(self):
        self.changeuserdetaisls = UpdateUserWindow()
        self.changeuserdetaisls.show()

    def change_password(self):
        self.changepassword= ChangePasswordWindow()
        self.changepassword.show()

    def business_details(self):
        self.business_details = NewBusinessWindow()
        self.business_details.show()

    def edit_business(self):
        self.edit_business = UpdateBusinessWindow()
        self.edit_business.show()


    def home(self):
        self.stackedWidget.setCurrentWidget(self.home_page)
        self.update()
        
    def product(self):
        self.stackedWidget.setCurrentWidget(self.product_page)
        self.update()

    def sales(self):
        self.stackedWidget.setCurrentWidget(self.sales_page)
        self.update()
        

    def customer(self):
        self.stackedWidget.setCurrentWidget(self.customer_page)
        self.update_customer_widget()
        self.update()
    
    def supplier(self):
        self.stackedWidget.setCurrentWidget(self.supplier_page)
        self.update()

    def roznamcha(self):
        self.stackedWidget.setCurrentWidget(self.roznamcha_page)
        self.update()

    def settings(self):
        self.stackedWidget.setCurrentWidget(self.settings_page)
        self.update()
        db=DBHandler()
        data=db.select_all('users',"*")[0]
        print(data)
        self.txt_user_name.setText(data[1])
        self.txt_user_email.setText(data[2])
        self.txt_user_contact.setText(data[3])
        self.txt_user_username.setText(data[4])

        data = db.select_all('business',"*")[0]
        if data:
            self.txt_business_name.setText(data[1])
            self.txt_business_email.setText(data[2])
            self.txt_business_contact.setText(data[4])
            self.txt_business_address.setText(data[3])
            self.txt_business_owner.setText(data[5])
            self.btn_business_details.hide()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()


# from PyQt5 import QtCore, QtGui, QtWidgets
# from PySide2 import *
# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *

# from add_product import Ui_AddProductWindow
# from add_stock import Ui_AddStockWindow
# from add_sale import Ui_SalesWindow
# from add_customer import Ui_AddCustomerWindow
# from add_roznamcha import Ui_RozNamchaWindow

# from create_business import Ui_NewBusinessWindow
# from update_business_details import Ui_UpdateBusinessWindow
# from update_user_details import Ui_UpdateUserWindow
# from update_password import Ui_ChangePasswordWindow


# class Ui_MainWindow(object):

#     # Add PRODUCTS
#     def openAddProductWindow(self):
#         self.window = QtWidgets.QMainWindow()
#         self.ui = Ui_AddProductWindow()
#         self.ui.setupUi(self.window)
#         self.window.show()

#     # Add STOCK
#     def openAddStockWindow(self):
#         self.window = QtWidgets.QMainWindow()
#         self.ui = Ui_AddStockWindow()
#         self.ui.setupUi(self.window)
#         self.window.show()


#     # Add SALE
#     def openAddSaleWindow(self):
#         self.window = QtWidgets.QMainWindow()
#         self.ui = Ui_SalesWindow()
#         self.ui.setupUi(self.window)
#         self.window.show()

#     # Add CUSTOMER
#     def openAddCustomerWindow(self):
#         self.window = QtWidgets.QMainWindow()
#         self.ui = Ui_AddCustomerWindow()
#         self.ui.setupUi(self.window)
#         self.window.show()

#     # Add ROZNAMCHA
#     def openAddRozNamchaWindow(self):
#         self.window = QtWidgets.QMainWindow()
#         self.ui = Ui_RozNamchaWindow()
#         self.ui.setupUi(self.window)
#         self.window.show()

#     # Create Business
#     def openCreateBusinessWindow(self):
#         self.window = QtWidgets.QMainWindow()
#         self.ui = Ui_NewBusinessWindow()
#         self.ui.setupUi(self.window)
#         self.window.show()

#     # Update Business Details
#     def openUpdateBusinessWindow(self):
#         self.window = QtWidgets.QMainWindow()
#         self.ui = Ui_UpdateBusinessWindow()
#         self.ui.setupUi(self.window)
#         self.window.show()

#     # Update User Details
#     def openUpdateUserWindow(self):
#         self.window = QtWidgets.QMainWindow()
#         self.ui = Ui_UpdateUserWindow()
#         self.ui.setupUi(self.window)
#         self.window.show()

#     # Update Password
#     def openChangePwdWindow(self):
#         self.window = QtWidgets.QMainWindow()
#         self.ui = Ui_ChangePasswordWindow()
#         self.ui.setupUi(self.window)
#         self.window.show()



#     def setupUi(self, MainWindow):
#         MainWindow.setObjectName("MainWindow")
#         MainWindow.resize(1309, 961)
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap(":/icons/assets/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         MainWindow.setWindowIcon(icon)
#         MainWindow.setIconSize(QtCore.QSize(40, 40))
#         self.centralwidget = QtWidgets.QWidget(MainWindow)
#         self.centralwidget.setStyleSheet("* {\n"
# "    background-color: #eceff1;\n"
# "}\n"
# "\n"
# "#upper_widget {\n"
# "    background-color: #80cbc4;\n"
# "}\n"
# "\n"
# "#stackedWidget {\n"
# "    background-color: #e0f2f1;\n"
# "}\n"
# "\n"
# "#btn_accounts {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#btn_home {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#btn_product {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#btn_sales {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#btn_customer {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#btn_roznamcha {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#btn_settings {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#btn_logout {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#user_frame {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "")
#         self.centralwidget.setObjectName("centralwidget")
#         self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.centralwidget)
#         self.verticalLayout_15.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_15.setSpacing(0)
#         self.verticalLayout_15.setObjectName("verticalLayout_15")
#         self.upper_widget = QtWidgets.QWidget(self.centralwidget)
#         self.upper_widget.setObjectName("upper_widget")
#         self.horizontalLayout_10 = QtWidgets.QHBoxLayout(self.upper_widget)
#         self.horizontalLayout_10.setObjectName("horizontalLayout_10")
#         self.btn_home = QtWidgets.QPushButton(self.upper_widget)
#         self.btn_home.setMinimumSize(QtCore.QSize(120, 40))
#         self.btn_home.setMaximumSize(QtCore.QSize(200, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_home.setFont(font)
#         self.btn_home.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         icon1 = QtGui.QIcon()
#         icon1.addPixmap(QtGui.QPixmap(":/icons/assets/icons/home.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_home.setIcon(icon1)
#         self.btn_home.setIconSize(QtCore.QSize(32, 32))
#         self.btn_home.setObjectName("btn_home")
#         self.horizontalLayout_10.addWidget(self.btn_home)
#         self.btn_product = QtWidgets.QPushButton(self.upper_widget)
#         self.btn_product.setMinimumSize(QtCore.QSize(130, 40))
#         self.btn_product.setMaximumSize(QtCore.QSize(200, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_product.setFont(font)
#         self.btn_product.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         icon2 = QtGui.QIcon()
#         icon2.addPixmap(QtGui.QPixmap(":/icons/assets/icons/products.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_product.setIcon(icon2)
#         self.btn_product.setIconSize(QtCore.QSize(32, 32))
#         self.btn_product.setObjectName("btn_product")
#         self.horizontalLayout_10.addWidget(self.btn_product)
#         self.btn_sales = QtWidgets.QPushButton(self.upper_widget)
#         self.btn_sales.setMinimumSize(QtCore.QSize(120, 40))
#         self.btn_sales.setMaximumSize(QtCore.QSize(200, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_sales.setFont(font)
#         self.btn_sales.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         icon3 = QtGui.QIcon()
#         icon3.addPixmap(QtGui.QPixmap(":/icons/assets/icons/sales.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_sales.setIcon(icon3)
#         self.btn_sales.setIconSize(QtCore.QSize(32, 32))
#         self.btn_sales.setObjectName("btn_sales")
#         self.horizontalLayout_10.addWidget(self.btn_sales)
#         self.btn_customer = QtWidgets.QPushButton(self.upper_widget)
#         self.btn_customer.setMinimumSize(QtCore.QSize(150, 40))
#         self.btn_customer.setMaximumSize(QtCore.QSize(200, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_customer.setFont(font)
#         self.btn_customer.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         self.btn_customer.setLayoutDirection(QtCore.Qt.LeftToRight)
#         icon4 = QtGui.QIcon()
#         icon4.addPixmap(QtGui.QPixmap(":/icons/assets/icons/customers_blue.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_customer.setIcon(icon4)
#         self.btn_customer.setIconSize(QtCore.QSize(32, 32))
#         self.btn_customer.setObjectName("btn_customer")
#         self.horizontalLayout_10.addWidget(self.btn_customer)
#         self.btn_roznamcha = QtWidgets.QPushButton(self.upper_widget)
#         self.btn_roznamcha.setMinimumSize(QtCore.QSize(200, 40))
#         self.btn_roznamcha.setMaximumSize(QtCore.QSize(200, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_roznamcha.setFont(font)
#         self.btn_roznamcha.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         icon5 = QtGui.QIcon()
#         icon5.addPixmap(QtGui.QPixmap(":/icons/assets/icons/menu.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_roznamcha.setIcon(icon5)
#         self.btn_roznamcha.setIconSize(QtCore.QSize(32, 32))
#         self.btn_roznamcha.setObjectName("btn_roznamcha")
#         self.horizontalLayout_10.addWidget(self.btn_roznamcha)
#         self.btn_settings = QtWidgets.QPushButton(self.upper_widget)
#         self.btn_settings.setMinimumSize(QtCore.QSize(150, 40))
#         self.btn_settings.setMaximumSize(QtCore.QSize(200, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_settings.setFont(font)
#         self.btn_settings.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         icon6 = QtGui.QIcon()
#         icon6.addPixmap(QtGui.QPixmap(":/icons/assets/icons/settings.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_settings.setIcon(icon6)
#         self.btn_settings.setIconSize(QtCore.QSize(32, 32))
#         self.btn_settings.setObjectName("btn_settings")
#         self.horizontalLayout_10.addWidget(self.btn_settings)
#         self.btn_logout = QtWidgets.QPushButton(self.upper_widget)
#         self.btn_logout.setMinimumSize(QtCore.QSize(120, 40))
#         self.btn_logout.setMaximumSize(QtCore.QSize(150, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_logout.setFont(font)
#         self.btn_logout.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         icon7 = QtGui.QIcon()
#         icon7.addPixmap(QtGui.QPixmap(":/icons/assets/icons/logout.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_logout.setIcon(icon7)
#         self.btn_logout.setIconSize(QtCore.QSize(32, 32))
#         self.btn_logout.setObjectName("btn_logout")
#         self.horizontalLayout_10.addWidget(self.btn_logout, 0, QtCore.Qt.AlignRight)
#         self.verticalLayout_15.addWidget(self.upper_widget)
#         self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
#         self.stackedWidget.setStyleSheet("* {\n"
# "    background-color: #e1f5fe;\n"
# "}")
#         self.stackedWidget.setObjectName("stackedWidget")
#         self.home_page = QtWidgets.QWidget()
#         self.home_page.setStyleSheet("#lbl_home {\n"
# "        background-color: #00b8d4;\n"
# "        color: white;\n"
# "}")
#         self.home_page.setObjectName("home_page")
#         self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.home_page)
#         self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_6.setSpacing(0)
#         self.verticalLayout_6.setObjectName("verticalLayout_6")
#         self.lbl_home = QtWidgets.QLabel(self.home_page)
#         self.lbl_home.setMinimumSize(QtCore.QSize(0, 50))
#         self.lbl_home.setMaximumSize(QtCore.QSize(16777215, 50))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(20)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_home.setFont(font)
#         self.lbl_home.setAlignment(QtCore.Qt.AlignCenter)
#         self.lbl_home.setObjectName("lbl_home")
#         self.verticalLayout_6.addWidget(self.lbl_home)
#         self.business_details_widget = QtWidgets.QWidget(self.home_page)
#         self.business_details_widget.setObjectName("business_details_widget")
#         self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.business_details_widget)
#         self.verticalLayout_5.setObjectName("verticalLayout_5")
#         self.b_details_frame = QtWidgets.QFrame(self.business_details_widget)
#         self.b_details_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.b_details_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.b_details_frame.setObjectName("b_details_frame")
#         self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.b_details_frame)
#         self.verticalLayout_4.setObjectName("verticalLayout_4")
#         self.lbl_business_name = QtWidgets.QLabel(self.b_details_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(20)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_business_name.setFont(font)
#         self.lbl_business_name.setAlignment(QtCore.Qt.AlignCenter)
#         self.lbl_business_name.setObjectName("lbl_business_name")
#         self.verticalLayout_4.addWidget(self.lbl_business_name, 0, QtCore.Qt.AlignBottom)
#         self.lbl_business_contact = QtWidgets.QLabel(self.b_details_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(18)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_business_contact.setFont(font)
#         self.lbl_business_contact.setAlignment(QtCore.Qt.AlignCenter)
#         self.lbl_business_contact.setObjectName("lbl_business_contact")
#         self.verticalLayout_4.addWidget(self.lbl_business_contact, 0, QtCore.Qt.AlignBottom)
#         self.lbl_business_address = QtWidgets.QLabel(self.b_details_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(18)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_business_address.setFont(font)
#         self.lbl_business_address.setAlignment(QtCore.Qt.AlignCenter)
#         self.lbl_business_address.setObjectName("lbl_business_address")
#         self.verticalLayout_4.addWidget(self.lbl_business_address, 0, QtCore.Qt.AlignTop)
#         self.verticalLayout_5.addWidget(self.b_details_frame, 0, QtCore.Qt.AlignVCenter)
#         self.verticalLayout_6.addWidget(self.business_details_widget)
#         self.conpany_details_frame = QtWidgets.QFrame(self.home_page)
#         self.conpany_details_frame.setLayoutDirection(QtCore.Qt.LeftToRight)
#         self.conpany_details_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.conpany_details_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.conpany_details_frame.setObjectName("conpany_details_frame")
#         self.horizontalLayout_17 = QtWidgets.QHBoxLayout(self.conpany_details_frame)
#         self.horizontalLayout_17.setObjectName("horizontalLayout_17")
#         self.lbl_contact = QtWidgets.QLabel(self.conpany_details_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_contact.setFont(font)
#         self.lbl_contact.setObjectName("lbl_contact")
#         self.horizontalLayout_17.addWidget(self.lbl_contact, 0, QtCore.Qt.AlignLeft)
#         self.lbl_description = QtWidgets.QLabel(self.conpany_details_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         self.lbl_description.setFont(font)
#         self.lbl_description.setObjectName("lbl_description")
#         self.horizontalLayout_17.addWidget(self.lbl_description, 0, QtCore.Qt.AlignRight)
#         self.lbl_company = QtWidgets.QLabel(self.conpany_details_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_company.setFont(font)
#         self.lbl_company.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
#         self.lbl_company.setObjectName("lbl_company")
#         self.horizontalLayout_17.addWidget(self.lbl_company)
#         self.verticalLayout_6.addWidget(self.conpany_details_frame, 0, QtCore.Qt.AlignBottom)
#         self.stackedWidget.addWidget(self.home_page)
#         self.product_page = QtWidgets.QWidget()
#         self.product_page.setStyleSheet("* {\n"
# "    background-color: #e3f2fd;\n"
# "}\n"
# "\n"
# "#lbl_product {\n"
# "    background-color: #00b8d4;\n"
# "    color: white;\n"
# "}\n"
# "\n"
# "#product_upper_widget {\n"
# "    background-color: #bbdefb;\n"
# "}\n"
# "\n"
# "#btn_add_product {\n"
# "    background-color: white;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#btn_add_stock {\n"
# "    background-color: white;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#select_product {\n"
# "    background-color: white;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#txt_date {\n"
# "    background-color: white;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#lbl_average_price {\n"
# "    background-color: #bbdefb;\n"
# "}\n"
# "\n"
# "#txt_average_price {\n"
# "    background-color: #bbdefb;\n"
# "}\n"
# "\n"
# "#lbl_products {\n"
# "    background-color: #00b8d4;\n"
# "}\n"
# "\n"
# "#lbl_stock {\n"
# "    background-color: #00b8d4;\n"
# "}")
#         self.product_page.setObjectName("product_page")
#         self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.product_page)
#         self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_12.setSpacing(0)
#         self.verticalLayout_12.setObjectName("verticalLayout_12")
#         self.lbl_product = QtWidgets.QLabel(self.product_page)
#         self.lbl_product.setMinimumSize(QtCore.QSize(0, 50))
#         self.lbl_product.setMaximumSize(QtCore.QSize(16777215, 50))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(20)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_product.setFont(font)
#         self.lbl_product.setAlignment(QtCore.Qt.AlignCenter)
#         self.lbl_product.setObjectName("lbl_product")
#         self.verticalLayout_12.addWidget(self.lbl_product)
#         self.product_upper_widget = QtWidgets.QWidget(self.product_page)
#         self.product_upper_widget.setObjectName("product_upper_widget")
#         self.horizontalLayout = QtWidgets.QHBoxLayout(self.product_upper_widget)
#         self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
#         self.horizontalLayout.setSpacing(10)
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         self.btn_add_product = QtWidgets.QPushButton(
#             self.product_upper_widget, clicked=lambda: self.openAddProductWindow())
#         self.btn_add_product.setMinimumSize(QtCore.QSize(150, 40))
#         self.btn_add_product.setMaximumSize(QtCore.QSize(200, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_add_product.setFont(font)
#         self.btn_add_product.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         icon8 = QtGui.QIcon()
#         icon8.addPixmap(QtGui.QPixmap(":/icons/assets/icons/plus.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_add_product.setIcon(icon8)
#         self.btn_add_product.setIconSize(QtCore.QSize(32, 32))
#         self.btn_add_product.setObjectName("btn_add_product")
#         self.horizontalLayout.addWidget(self.btn_add_product)
#         self.btn_add_stock = QtWidgets.QPushButton(self.product_upper_widget, clicked = lambda: self.openAddStockWindow())
#         self.btn_add_stock.setMinimumSize(QtCore.QSize(140, 40))
#         self.btn_add_stock.setMaximumSize(QtCore.QSize(200, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_add_stock.setFont(font)
#         self.btn_add_stock.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         icon9 = QtGui.QIcon()
#         icon9.addPixmap(QtGui.QPixmap(":/icons/assets/icons/product.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_add_stock.setIcon(icon9)
#         self.btn_add_stock.setIconSize(QtCore.QSize(32, 32))
#         self.btn_add_stock.setObjectName("btn_add_stock")
#         self.horizontalLayout.addWidget(self.btn_add_stock)
#         self.select_product = QtWidgets.QComboBox(self.product_upper_widget)
#         self.select_product.setMinimumSize(QtCore.QSize(200, 40))
#         self.select_product.setMaximumSize(QtCore.QSize(200, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         self.select_product.setFont(font)
#         self.select_product.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         self.select_product.setObjectName("select_product")
#         self.select_product.addItem("")
#         self.horizontalLayout.addWidget(self.select_product)
#         self.txt_date = QtWidgets.QDateEdit(self.product_upper_widget)
#         self.txt_date.setMinimumSize(QtCore.QSize(140, 40))
#         self.txt_date.setMaximumSize(QtCore.QSize(200, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_date.setFont(font)
#         self.txt_date.setObjectName("txt_date")
#         self.horizontalLayout.addWidget(self.txt_date)
#         self.lbl_average_price = QtWidgets.QLabel(self.product_upper_widget)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         self.lbl_average_price.setFont(font)
#         self.lbl_average_price.setObjectName("lbl_average_price")
#         self.horizontalLayout.addWidget(self.lbl_average_price, 0, QtCore.Qt.AlignRight)
#         self.txt_average_price = QtWidgets.QLabel(self.product_upper_widget)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(18)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_average_price.setFont(font)
#         self.txt_average_price.setObjectName("txt_average_price")
#         self.horizontalLayout.addWidget(self.txt_average_price, 0, QtCore.Qt.AlignLeft)
#         self.verticalLayout_12.addWidget(self.product_upper_widget)
#         self.product_stock_widget = QtWidgets.QWidget(self.product_page)
#         self.product_stock_widget.setObjectName("product_stock_widget")
#         self.horizontalLayout_9 = QtWidgets.QHBoxLayout(self.product_stock_widget)
#         self.horizontalLayout_9.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_9.setSpacing(0)
#         self.horizontalLayout_9.setObjectName("horizontalLayout_9")
#         self.product_frame = QtWidgets.QFrame(self.product_stock_widget)
#         self.product_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.product_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.product_frame.setObjectName("product_frame")
#         self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.product_frame)
#         self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_3.setSpacing(0)
#         self.verticalLayout_3.setObjectName("verticalLayout_3")
#         self.lbl_products = QtWidgets.QLabel(self.product_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_products.setFont(font)
#         self.lbl_products.setAlignment(QtCore.Qt.AlignCenter)
#         self.lbl_products.setObjectName("lbl_products")
#         self.verticalLayout_3.addWidget(self.lbl_products)
#         self.product_table = QtWidgets.QTableWidget(self.product_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.product_table.setFont(font)
#         self.product_table.setFrameShape(QtWidgets.QFrame.Box)
#         self.product_table.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.product_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
#         self.product_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
#         self.product_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
#         self.product_table.setRowCount(20)
#         self.product_table.setObjectName("product_table")
#         self.product_table.setColumnCount(3)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.product_table.setHorizontalHeaderItem(0, item)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.product_table.setHorizontalHeaderItem(1, item)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.product_table.setHorizontalHeaderItem(2, item)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(12)
#         item.setFont(font)
#         self.product_table.setItem(0, 0, item)
#         item = QtWidgets.QTableWidgetItem()
#         self.product_table.setItem(0, 1, item)
#         self.product_table.horizontalHeader().setDefaultSectionSize(160)
#         self.product_table.verticalHeader().setVisible(True)
#         self.product_table.verticalHeader().setCascadingSectionResizes(False)
#         self.verticalLayout_3.addWidget(self.product_table)
#         self.horizontalLayout_9.addWidget(self.product_frame)
#         self.stock_frame = QtWidgets.QFrame(self.product_stock_widget)
#         self.stock_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.stock_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.stock_frame.setObjectName("stock_frame")
#         self.verticalLayout = QtWidgets.QVBoxLayout(self.stock_frame)
#         self.verticalLayout.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout.setSpacing(0)
#         self.verticalLayout.setObjectName("verticalLayout")
#         self.lbl_stock = QtWidgets.QLabel(self.stock_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_stock.setFont(font)
#         self.lbl_stock.setLineWidth(1)
#         self.lbl_stock.setAlignment(QtCore.Qt.AlignCenter)
#         self.lbl_stock.setObjectName("lbl_stock")
#         self.verticalLayout.addWidget(self.lbl_stock)
#         self.stock_table = QtWidgets.QTableWidget(self.stock_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.stock_table.setFont(font)
#         self.stock_table.setFrameShape(QtWidgets.QFrame.Box)
#         self.stock_table.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.stock_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
#         self.stock_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
#         self.stock_table.setProperty("showDropIndicator", False)
#         self.stock_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
#         self.stock_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
#         self.stock_table.setTextElideMode(QtCore.Qt.ElideLeft)
#         self.stock_table.setRowCount(20)
#         self.stock_table.setObjectName("stock_table")
#         self.stock_table.setColumnCount(5)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.stock_table.setHorizontalHeaderItem(0, item)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.stock_table.setHorizontalHeaderItem(1, item)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.stock_table.setHorizontalHeaderItem(2, item)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.stock_table.setHorizontalHeaderItem(3, item)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.stock_table.setHorizontalHeaderItem(4, item)
#         self.stock_table.horizontalHeader().setDefaultSectionSize(120)
#         self.stock_table.horizontalHeader().setSortIndicatorShown(True)
#         self.verticalLayout.addWidget(self.stock_table)
#         self.horizontalLayout_9.addWidget(self.stock_frame)
#         self.verticalLayout_12.addWidget(self.product_stock_widget)
#         self.stackedWidget.addWidget(self.product_page)
#         self.sales_page = QtWidgets.QWidget()
#         self.sales_page.setStyleSheet("\n"
# "*{\n"
# "    background-color: #e3f2fd;\n"
# "}\n"
# "\n"
# "#lbl_sales {\n"
# "    background-color: #00b8d4;\n"
# "    color: white;\n"
# "}\n"
# "\n"
# "#sales_upper_widget {\n"
# "    background-color: #bbdefb;\n"
# "}\n"
# "\n"
# "\n"
# "#sales_bottom_widget, #total_cash_recv_frame, #total_cash_paid_frame, \n"
# "#total_sales_frame, #lbl_total_cash_paid, #lbl_total_cash_recv, #lbl_total_sales {\n"
# "    background-color: #bbdefb;\n"
# "}\n"
# "\n"
# "#lbl_from_sale {\n"
# "    background-color: #bbdefb;\n"
# "}\n"
# "#lbl_to_sale {\n"
# "    background-color: #bbdefb;\n"
# "}\n"
# "\n"
# "#btn_add_sale {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#search_option_sale {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#txt_search_sale {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#txt_date_from_sale {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#txt_date_to_sale {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "\n"
# "#btn_search_sale {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#btn_refresh_sale {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#btn_print_sale {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "")
#         self.sales_page.setObjectName("sales_page")
#         self.verticalLayout_13 = QtWidgets.QVBoxLayout(self.sales_page)
#         self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_13.setSpacing(0)
#         self.verticalLayout_13.setObjectName("verticalLayout_13")
#         self.lbl_sales = QtWidgets.QLabel(self.sales_page)
#         self.lbl_sales.setMinimumSize(QtCore.QSize(0, 50))
#         self.lbl_sales.setMaximumSize(QtCore.QSize(16777215, 50))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(20)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_sales.setFont(font)
#         self.lbl_sales.setAlignment(QtCore.Qt.AlignCenter)
#         self.lbl_sales.setObjectName("lbl_sales")
#         self.verticalLayout_13.addWidget(self.lbl_sales)
#         self.sales_upper_widget = QtWidgets.QWidget(self.sales_page)
#         self.sales_upper_widget.setObjectName("sales_upper_widget")
#         self.horizontalLayout_4 = QtWidgets.QHBoxLayout(self.sales_upper_widget)
#         self.horizontalLayout_4.setContentsMargins(10, 10, 10, 10)
#         self.horizontalLayout_4.setSpacing(5)
#         self.horizontalLayout_4.setObjectName("horizontalLayout_4")
#         self.btn_add_sale = QtWidgets.QPushButton(self.sales_upper_widget, clicked = lambda: self.openAddSaleWindow())
#         self.btn_add_sale.setMinimumSize(QtCore.QSize(180, 40))
#         self.btn_add_sale.setMaximumSize(QtCore.QSize(200, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_add_sale.setFont(font)
#         self.btn_add_sale.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         self.btn_add_sale.setIcon(icon8)
#         self.btn_add_sale.setIconSize(QtCore.QSize(32, 32))
#         self.btn_add_sale.setObjectName("btn_add_sale")
#         self.horizontalLayout_4.addWidget(self.btn_add_sale)
#         self.search_option_sale = QtWidgets.QComboBox(self.sales_upper_widget)
#         self.search_option_sale.setMinimumSize(QtCore.QSize(150, 40))
#         self.search_option_sale.setMaximumSize(QtCore.QSize(200, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.search_option_sale.setFont(font)
#         self.search_option_sale.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         self.search_option_sale.setObjectName("search_option_sale")
#         self.search_option_sale.addItem("")
#         self.search_option_sale.addItem("")
#         self.search_option_sale.addItem("")
#         self.horizontalLayout_4.addWidget(self.search_option_sale)
#         self.txt_search_sale = QtWidgets.QLineEdit(self.sales_upper_widget)
#         self.txt_search_sale.setMinimumSize(QtCore.QSize(300, 40))
#         self.txt_search_sale.setMaximumSize(QtCore.QSize(500, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_search_sale.setFont(font)
#         self.txt_search_sale.setObjectName("txt_search_sale")
#         self.horizontalLayout_4.addWidget(self.txt_search_sale)
#         self.lbl_from_sale = QtWidgets.QLabel(self.sales_upper_widget)
#         self.lbl_from_sale.setMaximumSize(QtCore.QSize(100, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_from_sale.setFont(font)
#         self.lbl_from_sale.setObjectName("lbl_from_sale")
#         self.horizontalLayout_4.addWidget(self.lbl_from_sale)
#         self.txt_date_from_sale = QtWidgets.QDateEdit(self.sales_upper_widget)
#         self.txt_date_from_sale.setMinimumSize(QtCore.QSize(130, 40))
#         self.txt_date_from_sale.setMaximumSize(QtCore.QSize(200, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(False)
#         font.setWeight(50)
#         self.txt_date_from_sale.setFont(font)
#         self.txt_date_from_sale.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         self.txt_date_from_sale.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 1), QtCore.QTime(0, 0, 0)))
#         self.txt_date_from_sale.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
#         self.txt_date_from_sale.setCalendarPopup(True)
#         self.txt_date_from_sale.setObjectName("txt_date_from_sale")
#         self.horizontalLayout_4.addWidget(self.txt_date_from_sale)
#         self.lbl_to_sale = QtWidgets.QLabel(self.sales_upper_widget)
#         self.lbl_to_sale.setMaximumSize(QtCore.QSize(100, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_to_sale.setFont(font)
#         self.lbl_to_sale.setObjectName("lbl_to_sale")
#         self.horizontalLayout_4.addWidget(self.lbl_to_sale)
#         self.txt_date_to_sale = QtWidgets.QDateEdit(self.sales_upper_widget)
#         self.txt_date_to_sale.setMinimumSize(QtCore.QSize(130, 40))
#         self.txt_date_to_sale.setMaximumSize(QtCore.QSize(200, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_date_to_sale.setFont(font)
#         self.txt_date_to_sale.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         self.txt_date_to_sale.setCalendarPopup(True)
#         self.txt_date_to_sale.setDate(QtCore.QDate(2022, 12, 15))
#         self.txt_date_to_sale.setObjectName("txt_date_to_sale")
#         self.horizontalLayout_4.addWidget(self.txt_date_to_sale)
#         self.btn_search_sale = QtWidgets.QPushButton(self.sales_upper_widget)
#         self.btn_search_sale.setMinimumSize(QtCore.QSize(50, 40))
#         self.btn_search_sale.setMaximumSize(QtCore.QSize(40, 40))
#         self.btn_search_sale.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         self.btn_search_sale.setText("")
#         icon10 = QtGui.QIcon()
#         icon10.addPixmap(QtGui.QPixmap(":/icons/assets/icons/search.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_search_sale.setIcon(icon10)
#         self.btn_search_sale.setIconSize(QtCore.QSize(32, 32))
#         self.btn_search_sale.setObjectName("btn_search_sale")
#         self.horizontalLayout_4.addWidget(self.btn_search_sale)
#         self.btn_print_sale = QtWidgets.QPushButton(self.sales_upper_widget)
#         self.btn_print_sale.setMinimumSize(QtCore.QSize(40, 40))
#         self.btn_print_sale.setMaximumSize(QtCore.QSize(40, 40))
#         self.btn_print_sale.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         self.btn_print_sale.setText("")
#         icon11 = QtGui.QIcon()
#         icon11.addPixmap(QtGui.QPixmap(":/icons/assets/icons/print.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_print_sale.setIcon(icon11)
#         self.btn_print_sale.setIconSize(QtCore.QSize(32, 32))
#         self.btn_print_sale.setObjectName("btn_print_sale")
#         self.horizontalLayout_4.addWidget(self.btn_print_sale)
#         self.btn_refresh_sale = QtWidgets.QPushButton(self.sales_upper_widget)
#         self.btn_refresh_sale.setMinimumSize(QtCore.QSize(50, 40))
#         self.btn_refresh_sale.setMaximumSize(QtCore.QSize(40, 40))
#         self.btn_refresh_sale.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         self.btn_refresh_sale.setText("")
#         icon12 = QtGui.QIcon()
#         icon12.addPixmap(QtGui.QPixmap(":/icons/assets/icons/refresh.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_refresh_sale.setIcon(icon12)
#         self.btn_refresh_sale.setIconSize(QtCore.QSize(32, 32))
#         self.btn_refresh_sale.setObjectName("btn_refresh_sale")
#         self.horizontalLayout_4.addWidget(self.btn_refresh_sale, 0, QtCore.Qt.AlignRight)
#         self.verticalLayout_13.addWidget(self.sales_upper_widget)
#         self.tableWidget_3 = QtWidgets.QTableWidget(self.sales_page)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.tableWidget_3.setFont(font)
#         self.tableWidget_3.setFrameShape(QtWidgets.QFrame.Box)
#         self.tableWidget_3.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.tableWidget_3.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
#         self.tableWidget_3.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
#         self.tableWidget_3.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
#         self.tableWidget_3.setRowCount(20)
#         self.tableWidget_3.setObjectName("tableWidget_3")
#         self.tableWidget_3.setColumnCount(8)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.tableWidget_3.setHorizontalHeaderItem(0, item)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.tableWidget_3.setHorizontalHeaderItem(1, item)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.tableWidget_3.setHorizontalHeaderItem(2, item)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.tableWidget_3.setHorizontalHeaderItem(3, item)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.tableWidget_3.setHorizontalHeaderItem(4, item)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.tableWidget_3.setHorizontalHeaderItem(5, item)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.tableWidget_3.setHorizontalHeaderItem(6, item)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.tableWidget_3.setHorizontalHeaderItem(7, item)
#         self.tableWidget_3.horizontalHeader().setDefaultSectionSize(145)
#         self.verticalLayout_13.addWidget(self.tableWidget_3)
#         self.sales_bottom_widget = QtWidgets.QWidget(self.sales_page)
#         self.sales_bottom_widget.setObjectName("sales_bottom_widget")
#         self.horizontalLayout_14 = QtWidgets.QHBoxLayout(self.sales_bottom_widget)
#         self.horizontalLayout_14.setObjectName("horizontalLayout_14")
#         self.total_sales_frame = QtWidgets.QFrame(self.sales_bottom_widget)
#         self.total_sales_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.total_sales_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.total_sales_frame.setObjectName("total_sales_frame")
#         self.horizontalLayout_15 = QtWidgets.QHBoxLayout(self.total_sales_frame)
#         self.horizontalLayout_15.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_15.setSpacing(20)
#         self.horizontalLayout_15.setObjectName("horizontalLayout_15")
#         self.lbl_total_sales = QtWidgets.QLabel(self.total_sales_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         self.lbl_total_sales.setFont(font)
#         self.lbl_total_sales.setObjectName("lbl_total_sales")
#         self.horizontalLayout_15.addWidget(self.lbl_total_sales, 0, QtCore.Qt.AlignRight)
#         self.txt_total_sales = QtWidgets.QLabel(self.total_sales_frame)
#         self.txt_total_sales.setMinimumSize(QtCore.QSize(0, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_total_sales.setFont(font)
#         self.txt_total_sales.setFrameShape(QtWidgets.QFrame.Box)
#         self.txt_total_sales.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.txt_total_sales.setObjectName("txt_total_sales")
#         self.horizontalLayout_15.addWidget(self.txt_total_sales)
#         self.horizontalLayout_14.addWidget(self.total_sales_frame)
#         self.total_cash_paid_frame = QtWidgets.QFrame(self.sales_bottom_widget)
#         self.total_cash_paid_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.total_cash_paid_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.total_cash_paid_frame.setObjectName("total_cash_paid_frame")
#         self.horizontalLayout_18 = QtWidgets.QHBoxLayout(self.total_cash_paid_frame)
#         self.horizontalLayout_18.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_18.setSpacing(20)
#         self.horizontalLayout_18.setObjectName("horizontalLayout_18")
#         self.lbl_total_cash_paid = QtWidgets.QLabel(self.total_cash_paid_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         self.lbl_total_cash_paid.setFont(font)
#         self.lbl_total_cash_paid.setObjectName("lbl_total_cash_paid")
#         self.horizontalLayout_18.addWidget(self.lbl_total_cash_paid, 0, QtCore.Qt.AlignRight)
#         self.txt_total_cash_paid = QtWidgets.QLabel(self.total_cash_paid_frame)
#         self.txt_total_cash_paid.setMinimumSize(QtCore.QSize(0, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_total_cash_paid.setFont(font)
#         self.txt_total_cash_paid.setFrameShape(QtWidgets.QFrame.Box)
#         self.txt_total_cash_paid.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.txt_total_cash_paid.setTextFormat(QtCore.Qt.AutoText)
#         self.txt_total_cash_paid.setObjectName("txt_total_cash_paid")
#         self.horizontalLayout_18.addWidget(self.txt_total_cash_paid)
#         self.horizontalLayout_14.addWidget(self.total_cash_paid_frame)
#         self.total_cash_recv_frame = QtWidgets.QFrame(self.sales_bottom_widget)
#         self.total_cash_recv_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.total_cash_recv_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.total_cash_recv_frame.setObjectName("total_cash_recv_frame")
#         self.horizontalLayout_16 = QtWidgets.QHBoxLayout(self.total_cash_recv_frame)
#         self.horizontalLayout_16.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_16.setSpacing(20)
#         self.horizontalLayout_16.setObjectName("horizontalLayout_16")
#         self.lbl_total_cash_recv = QtWidgets.QLabel(self.total_cash_recv_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         self.lbl_total_cash_recv.setFont(font)
#         self.lbl_total_cash_recv.setObjectName("lbl_total_cash_recv")
#         self.horizontalLayout_16.addWidget(self.lbl_total_cash_recv, 0, QtCore.Qt.AlignRight)
#         self.txt_total_cash_received = QtWidgets.QLabel(self.total_cash_recv_frame)
#         self.txt_total_cash_received.setMinimumSize(QtCore.QSize(0, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_total_cash_received.setFont(font)
#         self.txt_total_cash_received.setFrameShape(QtWidgets.QFrame.Box)
#         self.txt_total_cash_received.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.txt_total_cash_received.setTextFormat(QtCore.Qt.AutoText)
#         self.txt_total_cash_received.setObjectName("txt_total_cash_received")
#         self.horizontalLayout_16.addWidget(self.txt_total_cash_received)
#         self.horizontalLayout_14.addWidget(self.total_cash_recv_frame)
#         self.verticalLayout_13.addWidget(self.sales_bottom_widget)
#         self.stackedWidget.addWidget(self.sales_page)
#         self.customer_page = QtWidgets.QWidget()
#         self.customer_page.setStyleSheet("*{\n"
# "    background-color: #e3f2fd;\n"
# "}\n"
# "\n"
# "#lbl_customer {\n"
# "    background-color: #00b8d4;\n"
# "    color: white;\n"
# "}\n"
# "\n"
# "#customer_upper_widget {\n"
# "    background-color: #bbdefb;\n"
# "}\n"
# "\n"
# "#cust_bottom_widget {\n"
# "    background-color: #bbdefb;\n"
# "}\n"
# "\n"
# "#total_cust_frame {\n"
# "    background-color: #bbdefb;\n"
# "}\n"
# "\n"
# "#total_rem_bal_frame {\n"
# "    background-color: #bbdefb;\n"
# "}\n"
# "\n"
# "#lbl_total_customers {\n"
# "    background-color: #bbdefb;\n"
# "}\n"
# "\n"
# "#lbl_total_remaining {\n"
# "    background-color: #bbdefb;\n"
# "}\n"
# "\n"
# "#btn_add_customer {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#search_option_customer {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#txt_search_customer {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#btn_search_customer {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#btn_refresh_customer {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}")
#         self.customer_page.setObjectName("customer_page")
#         self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.customer_page)
#         self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_2.setSpacing(0)
#         self.verticalLayout_2.setObjectName("verticalLayout_2")
#         self.lbl_customer = QtWidgets.QLabel(self.customer_page)
#         self.lbl_customer.setMinimumSize(QtCore.QSize(0, 50))
#         self.lbl_customer.setMaximumSize(QtCore.QSize(16777215, 50))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(18)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_customer.setFont(font)
#         self.lbl_customer.setAlignment(QtCore.Qt.AlignCenter)
#         self.lbl_customer.setObjectName("lbl_customer")
#         self.verticalLayout_2.addWidget(self.lbl_customer)
#         self.customer_upper_widget = QtWidgets.QWidget(self.customer_page)
#         self.customer_upper_widget.setObjectName("customer_upper_widget")
#         self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.customer_upper_widget)
#         self.horizontalLayout_2.setObjectName("horizontalLayout_2")
#         self.btn_add_customer = QtWidgets.QPushButton(self.customer_upper_widget, clicked = lambda: self.openAddCustomerWindow())
#         self.btn_add_customer.setMinimumSize(QtCore.QSize(200, 40))
#         self.btn_add_customer.setMaximumSize(QtCore.QSize(300, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_add_customer.setFont(font)
#         self.btn_add_customer.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         self.btn_add_customer.setIcon(icon8)
#         self.btn_add_customer.setIconSize(QtCore.QSize(32, 32))
#         self.btn_add_customer.setObjectName("btn_add_customer")
#         self.horizontalLayout_2.addWidget(self.btn_add_customer)
#         self.search_option_customer = QtWidgets.QComboBox(self.customer_upper_widget)
#         self.search_option_customer.setMinimumSize(QtCore.QSize(150, 40))
#         self.search_option_customer.setMaximumSize(QtCore.QSize(200, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.search_option_customer.setFont(font)
#         self.search_option_customer.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         self.search_option_customer.setObjectName("search_option_customer")
#         self.search_option_customer.addItem("")
#         self.search_option_customer.addItem("")
#         self.search_option_customer.addItem("")
#         self.search_option_customer.addItem("")
#         self.horizontalLayout_2.addWidget(self.search_option_customer)
#         self.txt_search_customer = QtWidgets.QLineEdit(self.customer_upper_widget)
#         self.txt_search_customer.setMinimumSize(QtCore.QSize(400, 40))
#         self.txt_search_customer.setMaximumSize(QtCore.QSize(500, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_search_customer.setFont(font)
#         self.txt_search_customer.setObjectName("txt_search_customer")
#         self.horizontalLayout_2.addWidget(self.txt_search_customer)
#         self.btn_search_customer = QtWidgets.QPushButton(self.customer_upper_widget)
#         self.btn_search_customer.setMinimumSize(QtCore.QSize(50, 40))
#         self.btn_search_customer.setMaximumSize(QtCore.QSize(50, 40))
#         self.btn_search_customer.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         self.btn_search_customer.setText("")
#         self.btn_search_customer.setIcon(icon10)
#         self.btn_search_customer.setIconSize(QtCore.QSize(32, 32))
#         self.btn_search_customer.setObjectName("btn_search_customer")
#         self.horizontalLayout_2.addWidget(self.btn_search_customer)
#         self.btn_refresh_customer = QtWidgets.QPushButton(self.customer_upper_widget)
#         self.btn_refresh_customer.setMinimumSize(QtCore.QSize(50, 40))
#         self.btn_refresh_customer.setMaximumSize(QtCore.QSize(50, 40))
#         self.btn_refresh_customer.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         self.btn_refresh_customer.setText("")
#         self.btn_refresh_customer.setIcon(icon12)
#         self.btn_refresh_customer.setIconSize(QtCore.QSize(32, 32))
#         self.btn_refresh_customer.setObjectName("btn_refresh_customer")
#         self.horizontalLayout_2.addWidget(self.btn_refresh_customer, 0, QtCore.Qt.AlignRight)
#         self.verticalLayout_2.addWidget(self.customer_upper_widget)
#         self.customer_table = QtWidgets.QTableWidget(self.customer_page)
#         self.customer_table.setFrameShape(QtWidgets.QFrame.Box)
#         self.customer_table.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.customer_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
#         self.customer_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
#         self.customer_table.setDragDropOverwriteMode(True)
#         self.customer_table.setAlternatingRowColors(False)
#         self.customer_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
#         self.customer_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
#         self.customer_table.setTextElideMode(QtCore.Qt.ElideRight)
#         self.customer_table.setShowGrid(True)
#         self.customer_table.setGridStyle(QtCore.Qt.SolidLine)
#         self.customer_table.setCornerButtonEnabled(True)
#         self.customer_table.setRowCount(20)
#         self.customer_table.setObjectName("customer_table")
#         self.customer_table.setColumnCount(5)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.customer_table.setHorizontalHeaderItem(0, item)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.customer_table.setHorizontalHeaderItem(1, item)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.customer_table.setHorizontalHeaderItem(2, item)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.customer_table.setHorizontalHeaderItem(3, item)
#         item = QtWidgets.QTableWidgetItem()
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         item.setFont(font)
#         self.customer_table.setHorizontalHeaderItem(4, item)
#         self.customer_table.horizontalHeader().setVisible(True)
#         self.customer_table.horizontalHeader().setCascadingSectionResizes(True)
#         self.customer_table.horizontalHeader().setDefaultSectionSize(150)
#         self.customer_table.horizontalHeader().setSortIndicatorShown(True)
#         self.customer_table.verticalHeader().setVisible(True)
#         self.customer_table.verticalHeader().setHighlightSections(True)
#         self.customer_table.verticalHeader().setMinimumSectionSize(30)
#         self.customer_table.verticalHeader().setSortIndicatorShown(False)
#         self.verticalLayout_2.addWidget(self.customer_table)
#         self.cust_bottom_widget = QtWidgets.QWidget(self.customer_page)
#         self.cust_bottom_widget.setObjectName("cust_bottom_widget")
#         self.horizontalLayout_13 = QtWidgets.QHBoxLayout(self.cust_bottom_widget)
#         self.horizontalLayout_13.setObjectName("horizontalLayout_13")
#         self.total_cust_frame = QtWidgets.QFrame(self.cust_bottom_widget)
#         self.total_cust_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.total_cust_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.total_cust_frame.setObjectName("total_cust_frame")
#         self.horizontalLayout_12 = QtWidgets.QHBoxLayout(self.total_cust_frame)
#         self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_12.setSpacing(20)
#         self.horizontalLayout_12.setObjectName("horizontalLayout_12")
#         self.lbl_total_customers = QtWidgets.QLabel(self.total_cust_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         self.lbl_total_customers.setFont(font)
#         self.lbl_total_customers.setObjectName("lbl_total_customers")
#         self.horizontalLayout_12.addWidget(self.lbl_total_customers, 0, QtCore.Qt.AlignRight)
#         self.txt_total_customers = QtWidgets.QLabel(self.total_cust_frame)
#         self.txt_total_customers.setMinimumSize(QtCore.QSize(0, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_total_customers.setFont(font)
#         self.txt_total_customers.setFrameShape(QtWidgets.QFrame.Box)
#         self.txt_total_customers.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.txt_total_customers.setObjectName("txt_total_customers")
#         self.horizontalLayout_12.addWidget(self.txt_total_customers)
#         self.horizontalLayout_13.addWidget(self.total_cust_frame)
#         self.total_rem_bal_frame = QtWidgets.QFrame(self.cust_bottom_widget)
#         self.total_rem_bal_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.total_rem_bal_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.total_rem_bal_frame.setObjectName("total_rem_bal_frame")
#         self.horizontalLayout_11 = QtWidgets.QHBoxLayout(self.total_rem_bal_frame)
#         self.horizontalLayout_11.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_11.setSpacing(20)
#         self.horizontalLayout_11.setObjectName("horizontalLayout_11")
#         self.lbl_total_remaining = QtWidgets.QLabel(self.total_rem_bal_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         self.lbl_total_remaining.setFont(font)
#         self.lbl_total_remaining.setObjectName("lbl_total_remaining")
#         self.horizontalLayout_11.addWidget(self.lbl_total_remaining, 0, QtCore.Qt.AlignRight)
#         self.txt_total_rem_balance = QtWidgets.QLabel(self.total_rem_bal_frame)
#         self.txt_total_rem_balance.setMinimumSize(QtCore.QSize(0, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_total_rem_balance.setFont(font)
#         self.txt_total_rem_balance.setFrameShape(QtWidgets.QFrame.Box)
#         self.txt_total_rem_balance.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.txt_total_rem_balance.setTextFormat(QtCore.Qt.AutoText)
#         self.txt_total_rem_balance.setObjectName("txt_total_rem_balance")
#         self.horizontalLayout_11.addWidget(self.txt_total_rem_balance)
#         self.horizontalLayout_13.addWidget(self.total_rem_bal_frame)
#         self.verticalLayout_2.addWidget(self.cust_bottom_widget)
#         self.stackedWidget.addWidget(self.customer_page)
#         self.roznamcha_page = QtWidgets.QWidget()
#         self.roznamcha_page.setStyleSheet("\n"
# "*{\n"
# "    background-color: #e3f2fd;\n"
# "}\n"
# "\n"
# "#lbl_roznamcha {\n"
# "    background-color: #00b8d4;\n"
# "    color: white;\n"
# "}\n"
# "\n"
# "#roznamcha_upper_widget, #lbl_from, #rn_bottom_widget, #total_cash_in_frame, #total_cash_out_frame, #lbl_total_cashIn, #lbl_total_cash_out, #lbl_from_rn, #lbl_to_rn {\n"
# "    background-color: #bbdefb;\n"
# "}\n"
# "\n"
# "QPushButton, QComboBox, QDateEdit {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "#txt_search_rn {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "\n"
# "")
#         self.roznamcha_page.setObjectName("roznamcha_page")
#         self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.roznamcha_page)
#         self.verticalLayout_14.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_14.setSpacing(0)
#         self.verticalLayout_14.setObjectName("verticalLayout_14")
#         self.lbl_roznamcha = QtWidgets.QLabel(self.roznamcha_page)
#         self.lbl_roznamcha.setMinimumSize(QtCore.QSize(0, 50))
#         self.lbl_roznamcha.setMaximumSize(QtCore.QSize(16777215, 50))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(18)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_roznamcha.setFont(font)
#         self.lbl_roznamcha.setAlignment(QtCore.Qt.AlignCenter)
#         self.lbl_roznamcha.setObjectName("lbl_roznamcha")
#         self.verticalLayout_14.addWidget(self.lbl_roznamcha)
#         self.roznamcha_upper_widget = QtWidgets.QWidget(self.roznamcha_page)
#         self.roznamcha_upper_widget.setObjectName("roznamcha_upper_widget")
#         self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.roznamcha_upper_widget)
#         self.horizontalLayout_3.setContentsMargins(5, 5, 5, 10)
#         self.horizontalLayout_3.setSpacing(5)
#         self.horizontalLayout_3.setObjectName("horizontalLayout_3")
#         self.btn_add_roznamcha = QtWidgets.QPushButton(self.roznamcha_upper_widget, clicked = lambda: self.openAddRozNamchaWindow())
#         self.btn_add_roznamcha.setMinimumSize(QtCore.QSize(180, 40))
#         self.btn_add_roznamcha.setMaximumSize(QtCore.QSize(300, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_add_roznamcha.setFont(font)
#         self.btn_add_roznamcha.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         self.btn_add_roznamcha.setIcon(icon8)
#         self.btn_add_roznamcha.setIconSize(QtCore.QSize(32, 32))
#         self.btn_add_roznamcha.setObjectName("btn_add_roznamcha")
#         self.horizontalLayout_3.addWidget(self.btn_add_roznamcha)
#         self.search_option_rn = QtWidgets.QComboBox(self.roznamcha_upper_widget)
#         self.search_option_rn.setMinimumSize(QtCore.QSize(150, 40))
#         self.search_option_rn.setMaximumSize(QtCore.QSize(200, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.search_option_rn.setFont(font)
#         self.search_option_rn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         self.search_option_rn.setObjectName("search_option_rn")
#         self.search_option_rn.addItem("")
#         self.search_option_rn.addItem("")
#         self.horizontalLayout_3.addWidget(self.search_option_rn)
#         self.txt_search_rn = QtWidgets.QLineEdit(self.roznamcha_upper_widget)
#         self.txt_search_rn.setMinimumSize(QtCore.QSize(300, 40))
#         self.txt_search_rn.setMaximumSize(QtCore.QSize(400, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_search_rn.setFont(font)
#         self.txt_search_rn.setObjectName("txt_search_rn")
#         self.horizontalLayout_3.addWidget(self.txt_search_rn)
#         self.lbl_from_rn = QtWidgets.QLabel(self.roznamcha_upper_widget)
#         self.lbl_from_rn.setMaximumSize(QtCore.QSize(16777215, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_from_rn.setFont(font)
#         self.lbl_from_rn.setObjectName("lbl_from_rn")
#         self.horizontalLayout_3.addWidget(self.lbl_from_rn)
#         self.txt_date_from_rn = QtWidgets.QDateEdit(self.roznamcha_upper_widget)
#         self.txt_date_from_rn.setMinimumSize(QtCore.QSize(130, 40))
#         self.txt_date_from_rn.setMaximumSize(QtCore.QSize(130, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(False)
#         font.setWeight(50)
#         self.txt_date_from_rn.setFont(font)
#         self.txt_date_from_rn.setDateTime(QtCore.QDateTime(QtCore.QDate(2022, 1, 1), QtCore.QTime(0, 0, 0)))
#         self.txt_date_from_rn.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
#         self.txt_date_from_rn.setCalendarPopup(True)
#         self.txt_date_from_rn.setObjectName("txt_date_from_rn")
#         self.horizontalLayout_3.addWidget(self.txt_date_from_rn)
#         self.lbl_to_rn = QtWidgets.QLabel(self.roznamcha_upper_widget)
#         self.lbl_to_rn.setMaximumSize(QtCore.QSize(16777215, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_to_rn.setFont(font)
#         self.lbl_to_rn.setObjectName("lbl_to_rn")
#         self.horizontalLayout_3.addWidget(self.lbl_to_rn)
#         self.txt_date_to_rn = QtWidgets.QDateEdit(self.roznamcha_upper_widget)
#         self.txt_date_to_rn.setMinimumSize(QtCore.QSize(130, 40))
#         self.txt_date_to_rn.setMaximumSize(QtCore.QSize(130, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_date_to_rn.setFont(font)
#         self.txt_date_to_rn.setCalendarPopup(True)
#         self.txt_date_to_rn.setDate(QtCore.QDate(2022, 12, 15))
#         self.txt_date_to_rn.setObjectName("txt_date_to_rn")
#         self.horizontalLayout_3.addWidget(self.txt_date_to_rn)
#         self.btn_search_rn = QtWidgets.QPushButton(self.roznamcha_upper_widget)
#         self.btn_search_rn.setMinimumSize(QtCore.QSize(50, 40))
#         self.btn_search_rn.setMaximumSize(QtCore.QSize(50, 40))
#         self.btn_search_rn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         self.btn_search_rn.setText("")
#         self.btn_search_rn.setIcon(icon10)
#         self.btn_search_rn.setIconSize(QtCore.QSize(32, 32))
#         self.btn_search_rn.setObjectName("btn_search_rn")
#         self.horizontalLayout_3.addWidget(self.btn_search_rn, 0, QtCore.Qt.AlignLeft)
#         self.btn_print_rn = QtWidgets.QPushButton(self.roznamcha_upper_widget)
#         self.btn_print_rn.setMinimumSize(QtCore.QSize(40, 40))
#         self.btn_print_rn.setMaximumSize(QtCore.QSize(40, 40))
#         self.btn_print_rn.setText("")
#         self.btn_print_rn.setIcon(icon11)
#         self.btn_print_rn.setIconSize(QtCore.QSize(32, 32))
#         self.btn_print_rn.setObjectName("btn_print_rn")
#         self.horizontalLayout_3.addWidget(self.btn_print_rn, 0, QtCore.Qt.AlignLeft)
#         self.btn_refresh_rn = QtWidgets.QPushButton(self.roznamcha_upper_widget)
#         self.btn_refresh_rn.setMinimumSize(QtCore.QSize(50, 40))
#         self.btn_refresh_rn.setMaximumSize(QtCore.QSize(50, 40))
#         self.btn_refresh_rn.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         self.btn_refresh_rn.setText("")
#         self.btn_refresh_rn.setIcon(icon12)
#         self.btn_refresh_rn.setIconSize(QtCore.QSize(32, 32))
#         self.btn_refresh_rn.setObjectName("btn_refresh_rn")
#         self.horizontalLayout_3.addWidget(self.btn_refresh_rn, 0, QtCore.Qt.AlignRight)
#         self.verticalLayout_14.addWidget(self.roznamcha_upper_widget)
#         self.roznamcha_table = QtWidgets.QTableWidget(self.roznamcha_page)
#         self.roznamcha_table.setMinimumSize(QtCore.QSize(0, 0))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.roznamcha_table.setFont(font)
#         self.roznamcha_table.setLayoutDirection(QtCore.Qt.LeftToRight)
#         self.roznamcha_table.setAutoFillBackground(False)
#         self.roznamcha_table.setFrameShape(QtWidgets.QFrame.Box)
#         self.roznamcha_table.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.roznamcha_table.setMidLineWidth(0)
#         self.roznamcha_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
#         self.roznamcha_table.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
#         self.roznamcha_table.setAlternatingRowColors(False)
#         self.roznamcha_table.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
#         self.roznamcha_table.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
#         self.roznamcha_table.setCornerButtonEnabled(True)
#         self.roznamcha_table.setRowCount(20)
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
#         brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
#         brush.setStyle(QtCore.Qt.SolidPattern)
#         item.setForeground(brush)
#         self.roznamcha_table.setHorizontalHeaderItem(7, item)
#         item = QtWidgets.QTableWidgetItem()
#         item.setFlags(QtCore.Qt.ItemIsSelectable|QtCore.Qt.ItemIsEnabled)
#         self.roznamcha_table.setItem(0, 1, item)
#         self.roznamcha_table.horizontalHeader().setVisible(True)
#         self.roznamcha_table.horizontalHeader().setCascadingSectionResizes(False)
#         self.roznamcha_table.horizontalHeader().setDefaultSectionSize(150)
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
#         self.verticalLayout_14.addWidget(self.roznamcha_table)
#         self.rn_bottom_widget = QtWidgets.QWidget(self.roznamcha_page)
#         self.rn_bottom_widget.setObjectName("rn_bottom_widget")
#         self.horizontalLayout_19 = QtWidgets.QHBoxLayout(self.rn_bottom_widget)
#         self.horizontalLayout_19.setObjectName("horizontalLayout_19")
#         self.total_cash_in_frame = QtWidgets.QFrame(self.rn_bottom_widget)
#         self.total_cash_in_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.total_cash_in_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.total_cash_in_frame.setObjectName("total_cash_in_frame")
#         self.horizontalLayout_20 = QtWidgets.QHBoxLayout(self.total_cash_in_frame)
#         self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_20.setSpacing(20)
#         self.horizontalLayout_20.setObjectName("horizontalLayout_20")
#         self.lbl_total_cashIn = QtWidgets.QLabel(self.total_cash_in_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         self.lbl_total_cashIn.setFont(font)
#         self.lbl_total_cashIn.setObjectName("lbl_total_cashIn")
#         self.horizontalLayout_20.addWidget(self.lbl_total_cashIn, 0, QtCore.Qt.AlignRight)
#         self.txt_total_cash_in = QtWidgets.QLabel(self.total_cash_in_frame)
#         self.txt_total_cash_in.setMinimumSize(QtCore.QSize(0, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_total_cash_in.setFont(font)
#         self.txt_total_cash_in.setFrameShape(QtWidgets.QFrame.Box)
#         self.txt_total_cash_in.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.txt_total_cash_in.setObjectName("txt_total_cash_in")
#         self.horizontalLayout_20.addWidget(self.txt_total_cash_in)
#         self.horizontalLayout_19.addWidget(self.total_cash_in_frame)
#         self.total_cash_out_frame = QtWidgets.QFrame(self.rn_bottom_widget)
#         self.total_cash_out_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.total_cash_out_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.total_cash_out_frame.setObjectName("total_cash_out_frame")
#         self.horizontalLayout_21 = QtWidgets.QHBoxLayout(self.total_cash_out_frame)
#         self.horizontalLayout_21.setContentsMargins(0, 0, 0, 0)
#         self.horizontalLayout_21.setSpacing(20)
#         self.horizontalLayout_21.setObjectName("horizontalLayout_21")
#         self.lbl_total_cash_out = QtWidgets.QLabel(self.total_cash_out_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         self.lbl_total_cash_out.setFont(font)
#         self.lbl_total_cash_out.setObjectName("lbl_total_cash_out")
#         self.horizontalLayout_21.addWidget(self.lbl_total_cash_out, 0, QtCore.Qt.AlignRight)
#         self.txt_total_cash_out = QtWidgets.QLabel(self.total_cash_out_frame)
#         self.txt_total_cash_out.setMinimumSize(QtCore.QSize(0, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri Light")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_total_cash_out.setFont(font)
#         self.txt_total_cash_out.setFrameShape(QtWidgets.QFrame.Box)
#         self.txt_total_cash_out.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.txt_total_cash_out.setTextFormat(QtCore.Qt.AutoText)
#         self.txt_total_cash_out.setObjectName("txt_total_cash_out")
#         self.horizontalLayout_21.addWidget(self.txt_total_cash_out)
#         self.horizontalLayout_19.addWidget(self.total_cash_out_frame)
#         self.verticalLayout_14.addWidget(self.rn_bottom_widget)
#         self.stackedWidget.addWidget(self.roznamcha_page)
#         self.settings_page = QtWidgets.QWidget()
#         self.settings_page.setStyleSheet("*{\n"
# "    background-color: #e3f2fd;\n"
# "}\n"
# "\n"
# "#lbl_settings {\n"
# "    background-color: #00b8d4;\n"
# "    color: white;\n"
# "}\n"
# "\n"
# "QPushButton {\n"
# "    background-color: #fff;\n"
# "    border-radius: 5px;\n"
# "}\n"
# "\n"
# "QFrame {\n"
# "    background-color: #eceff1;\n"
# "}\n"
# "\n"
# "#create_widget {\n"
# "    background-color: #bbdefb;\n"
# "}")
#         self.settings_page.setObjectName("settings_page")
#         self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.settings_page)
#         self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_11.setSpacing(0)
#         self.verticalLayout_11.setObjectName("verticalLayout_11")
#         self.lbl_settings = QtWidgets.QLabel(self.settings_page)
#         self.lbl_settings.setMinimumSize(QtCore.QSize(0, 50))
#         self.lbl_settings.setMaximumSize(QtCore.QSize(16777215, 50))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(18)
#         font.setBold(True)
#         font.setWeight(75)
#         self.lbl_settings.setFont(font)
#         self.lbl_settings.setAlignment(QtCore.Qt.AlignCenter)
#         self.lbl_settings.setObjectName("lbl_settings")
#         self.verticalLayout_11.addWidget(self.lbl_settings)
#         self.create_widget = QtWidgets.QWidget(self.settings_page)
#         self.create_widget.setMinimumSize(QtCore.QSize(0, 0))
#         self.create_widget.setMaximumSize(QtCore.QSize(16777215, 60))
#         self.create_widget.setObjectName("create_widget")
#         self.horizontalLayout_8 = QtWidgets.QHBoxLayout(self.create_widget)
#         self.horizontalLayout_8.setObjectName("horizontalLayout_8")
#         self.btn_business_details = QtWidgets.QPushButton(self.create_widget, clicked=lambda: self.openCreateBusinessWindow())
#         self.btn_business_details.setMinimumSize(QtCore.QSize(300, 40))
#         self.btn_business_details.setMaximumSize(QtCore.QSize(300, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(18)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_business_details.setFont(font)
#         self.btn_business_details.setIcon(icon8)
#         self.btn_business_details.setIconSize(QtCore.QSize(32, 32))
#         self.btn_business_details.setObjectName("btn_business_details")
#         self.horizontalLayout_8.addWidget(self.btn_business_details, 0, QtCore.Qt.AlignLeft)
#         self.btn_change_business_details = QtWidgets.QPushButton(self.create_widget, clicked = lambda: self.openUpdateBusinessWindow())
#         self.btn_change_business_details.setMinimumSize(QtCore.QSize(300, 40))
#         self.btn_change_business_details.setMaximumSize(QtCore.QSize(300, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_change_business_details.setFont(font)
#         self.btn_change_business_details.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         icon13 = QtGui.QIcon()
#         icon13.addPixmap(QtGui.QPixmap(":/icons/assets/icons/edit.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_change_business_details.setIcon(icon13)
#         self.btn_change_business_details.setIconSize(QtCore.QSize(32, 32))
#         self.btn_change_business_details.setObjectName("btn_change_business_details")
#         self.horizontalLayout_8.addWidget(self.btn_change_business_details)
#         self.btn_change_user_details = QtWidgets.QPushButton(self.create_widget, clicked = lambda: self.openUpdateUserWindow())
#         self.btn_change_user_details.setMinimumSize(QtCore.QSize(250, 40))
#         self.btn_change_user_details.setMaximumSize(QtCore.QSize(250, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_change_user_details.setFont(font)
#         self.btn_change_user_details.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         self.btn_change_user_details.setIcon(icon13)
#         self.btn_change_user_details.setIconSize(QtCore.QSize(32, 32))
#         self.btn_change_user_details.setObjectName("btn_change_user_details")
#         self.horizontalLayout_8.addWidget(self.btn_change_user_details)
#         self.btn_change_pwd = QtWidgets.QPushButton(self.create_widget, clicked = lambda: self.openChangePwdWindow())
#         self.btn_change_pwd.setMinimumSize(QtCore.QSize(200, 40))
#         self.btn_change_pwd.setMaximumSize(QtCore.QSize(200, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_change_pwd.setFont(font)
#         self.btn_change_pwd.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         self.btn_change_pwd.setIcon(icon13)
#         self.btn_change_pwd.setIconSize(QtCore.QSize(32, 32))
#         self.btn_change_pwd.setObjectName("btn_change_pwd")
#         self.horizontalLayout_8.addWidget(self.btn_change_pwd)
#         self.verticalLayout_11.addWidget(self.create_widget)
#         self.details_widget = QtWidgets.QWidget(self.settings_page)
#         self.details_widget.setMinimumSize(QtCore.QSize(0, 0))
#         self.details_widget.setMaximumSize(QtCore.QSize(16777215, 200))
#         self.details_widget.setObjectName("details_widget")
#         self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.details_widget)
#         self.horizontalLayout_7.setSpacing(70)
#         self.horizontalLayout_7.setObjectName("horizontalLayout_7")
#         self.business_frame = QtWidgets.QFrame(self.details_widget)
#         self.business_frame.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         self.business_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.business_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.business_frame.setObjectName("business_frame")
#         self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.business_frame)
#         self.horizontalLayout_6.setSpacing(0)
#         self.horizontalLayout_6.setObjectName("horizontalLayout_6")
#         self.b_lbl_frame = QtWidgets.QFrame(self.business_frame)
#         self.b_lbl_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.b_lbl_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.b_lbl_frame.setObjectName("b_lbl_frame")
#         self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.b_lbl_frame)
#         self.verticalLayout_9.setObjectName("verticalLayout_9")
#         self.lbl_b_name = QtWidgets.QLabel(self.b_lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_b_name.setFont(font)
#         self.lbl_b_name.setObjectName("lbl_b_name")
#         self.verticalLayout_9.addWidget(self.lbl_b_name)
#         self.lbl_b_email = QtWidgets.QLabel(self.b_lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_b_email.setFont(font)
#         self.lbl_b_email.setObjectName("lbl_b_email")
#         self.verticalLayout_9.addWidget(self.lbl_b_email)
#         self.lbl_b_contact = QtWidgets.QLabel(self.b_lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_b_contact.setFont(font)
#         self.lbl_b_contact.setObjectName("lbl_b_contact")
#         self.verticalLayout_9.addWidget(self.lbl_b_contact)
#         self.lbl_b_address = QtWidgets.QLabel(self.b_lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_b_address.setFont(font)
#         self.lbl_b_address.setObjectName("lbl_b_address")
#         self.verticalLayout_9.addWidget(self.lbl_b_address)
#         self.lbl_b_owner = QtWidgets.QLabel(self.b_lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_b_owner.setFont(font)
#         self.lbl_b_owner.setObjectName("lbl_b_owner")
#         self.verticalLayout_9.addWidget(self.lbl_b_owner)
#         self.horizontalLayout_6.addWidget(self.b_lbl_frame)
#         self.b_inputs_frame = QtWidgets.QFrame(self.business_frame)
#         self.b_inputs_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.b_inputs_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.b_inputs_frame.setObjectName("b_inputs_frame")
#         self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.b_inputs_frame)
#         self.verticalLayout_10.setObjectName("verticalLayout_10")
#         self.txt_business_name = QtWidgets.QLabel(self.b_inputs_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_business_name.setFont(font)
#         self.txt_business_name.setObjectName("txt_business_name")
#         self.verticalLayout_10.addWidget(self.txt_business_name)
#         self.txt_business_email = QtWidgets.QLabel(self.b_inputs_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_business_email.setFont(font)
#         self.txt_business_email.setObjectName("txt_business_email")
#         self.verticalLayout_10.addWidget(self.txt_business_email)
#         self.txt_business_contact = QtWidgets.QLabel(self.b_inputs_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_business_contact.setFont(font)
#         self.txt_business_contact.setObjectName("txt_business_contact")
#         self.verticalLayout_10.addWidget(self.txt_business_contact)
#         self.txt_business_address = QtWidgets.QLabel(self.b_inputs_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_business_address.setFont(font)
#         self.txt_business_address.setObjectName("txt_business_address")
#         self.verticalLayout_10.addWidget(self.txt_business_address)
#         self.txt_business_owner = QtWidgets.QLabel(self.b_inputs_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_business_owner.setFont(font)
#         self.txt_business_owner.setObjectName("txt_business_owner")
#         self.verticalLayout_10.addWidget(self.txt_business_owner)
#         self.horizontalLayout_6.addWidget(self.b_inputs_frame)
#         self.horizontalLayout_7.addWidget(self.business_frame)
#         self.user_detail_frame = QtWidgets.QFrame(self.details_widget)
#         self.user_detail_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.user_detail_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.user_detail_frame.setObjectName("user_detail_frame")
#         self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.user_detail_frame)
#         self.horizontalLayout_5.setSpacing(0)
#         self.horizontalLayout_5.setObjectName("horizontalLayout_5")
#         self.u_lbl_frame = QtWidgets.QFrame(self.user_detail_frame)
#         self.u_lbl_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.u_lbl_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.u_lbl_frame.setObjectName("u_lbl_frame")
#         self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.u_lbl_frame)
#         self.verticalLayout_8.setObjectName("verticalLayout_8")
#         self.lbl_u_name = QtWidgets.QLabel(self.u_lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_u_name.setFont(font)
#         self.lbl_u_name.setObjectName("lbl_u_name")
#         self.verticalLayout_8.addWidget(self.lbl_u_name)
#         self.lbl_u_email = QtWidgets.QLabel(self.u_lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_u_email.setFont(font)
#         self.lbl_u_email.setObjectName("lbl_u_email")
#         self.verticalLayout_8.addWidget(self.lbl_u_email)
#         self.lbl_u_contact = QtWidgets.QLabel(self.u_lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_u_contact.setFont(font)
#         self.lbl_u_contact.setObjectName("lbl_u_contact")
#         self.verticalLayout_8.addWidget(self.lbl_u_contact)
#         self.lbl_u_username = QtWidgets.QLabel(self.u_lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_u_username.setFont(font)
#         self.lbl_u_username.setObjectName("lbl_u_username")
#         self.verticalLayout_8.addWidget(self.lbl_u_username)
#         self.horizontalLayout_5.addWidget(self.u_lbl_frame)
#         self.u_inputs_frame = QtWidgets.QFrame(self.user_detail_frame)
#         self.u_inputs_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.u_inputs_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.u_inputs_frame.setObjectName("u_inputs_frame")
#         self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.u_inputs_frame)
#         self.verticalLayout_7.setObjectName("verticalLayout_7")
#         self.txt_user_name = QtWidgets.QLabel(self.u_inputs_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_user_name.setFont(font)
#         self.txt_user_name.setObjectName("txt_user_name")
#         self.verticalLayout_7.addWidget(self.txt_user_name)
#         self.txt_user_email = QtWidgets.QLabel(self.u_inputs_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_user_email.setFont(font)
#         self.txt_user_email.setObjectName("txt_user_email")
#         self.verticalLayout_7.addWidget(self.txt_user_email)
#         self.txt_user_contact = QtWidgets.QLabel(self.u_inputs_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_user_contact.setFont(font)
#         self.txt_user_contact.setObjectName("txt_user_contact")
#         self.verticalLayout_7.addWidget(self.txt_user_contact)
#         self.txt_user_username = QtWidgets.QLabel(self.u_inputs_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.txt_user_username.setFont(font)
#         self.txt_user_username.setObjectName("txt_user_username")
#         self.verticalLayout_7.addWidget(self.txt_user_username)
#         self.horizontalLayout_5.addWidget(self.u_inputs_frame)
#         self.horizontalLayout_7.addWidget(self.user_detail_frame)
#         self.verticalLayout_11.addWidget(self.details_widget)
#         self.free_widget = QtWidgets.QWidget(self.settings_page)
#         self.free_widget.setObjectName("free_widget")
#         self.verticalLayout_11.addWidget(self.free_widget)
#         self.stackedWidget.addWidget(self.settings_page)
#         self.verticalLayout_15.addWidget(self.stackedWidget)
#         MainWindow.setCentralWidget(self.centralwidget)

#         self.retranslateUi(MainWindow)
#         self.stackedWidget.setCurrentIndex(0)
#         QtCore.QMetaObject.connectSlotsByName(MainWindow)

#     def retranslateUi(self, MainWindow):
#         _translate = QtCore.QCoreApplication.translate
#         MainWindow.setWindowTitle(_translate("MainWindow", "SAM & SHAMI"))
#         self.btn_home.setText(_translate("MainWindow", "Home"))
#         self.btn_product.setText(_translate("MainWindow", "Product"))
#         self.btn_sales.setText(_translate("MainWindow", "Sales"))
#         self.btn_customer.setText(_translate("MainWindow", "Customer"))
#         self.btn_roznamcha.setText(_translate("MainWindow", "Roz Namcha"))
#         self.btn_settings.setText(_translate("MainWindow", "Settings"))
#         self.btn_logout.setText(_translate("MainWindow", "Logout"))
#         self.lbl_home.setText(_translate("MainWindow", "Home"))
#         self.lbl_business_name.setText(_translate("MainWindow", "Business Name"))
#         self.lbl_business_contact.setText(_translate("MainWindow", "Business Contact"))
#         self.lbl_business_address.setText(_translate("MainWindow", "Business Address"))
#         self.lbl_contact.setText(_translate("MainWindow", "+92 335 2321360"))
#         self.lbl_description.setText(_translate("MainWindow", "Software Developed By:"))
#         self.lbl_company.setText(_translate("MainWindow", "SAM & SHAMI Coding Hub"))
#         self.lbl_product.setText(_translate("MainWindow", "Product"))
#         self.btn_add_product.setText(_translate("MainWindow", "Add Product"))
#         self.btn_add_stock.setText(_translate("MainWindow", "Add Stock"))
#         self.select_product.setItemText(0, _translate("MainWindow", "Select Product"))
#         self.lbl_average_price.setText(_translate("MainWindow", "Average Price"))
#         self.txt_average_price.setText(_translate("MainWindow", "00"))
#         self.lbl_products.setText(_translate("MainWindow", "Products"))
#         self.product_table.setSortingEnabled(True)
#         item = self.product_table.horizontalHeaderItem(0)
#         item.setText(_translate("MainWindow", "Product Name"))
#         item = self.product_table.horizontalHeaderItem(1)
#         item.setText(_translate("MainWindow", "Available Stock"))
#         item = self.product_table.horizontalHeaderItem(2)
#         item.setText(_translate("MainWindow", "UoM"))
#         __sortingEnabled = self.product_table.isSortingEnabled()
#         self.product_table.setSortingEnabled(False)
#         self.product_table.setSortingEnabled(__sortingEnabled)
#         self.lbl_stock.setText(_translate("MainWindow", "Stock"))
#         item = self.stock_table.horizontalHeaderItem(0)
#         item.setText(_translate("MainWindow", "Date"))
#         item = self.stock_table.horizontalHeaderItem(1)
#         item.setText(_translate("MainWindow", "Supplier"))
#         item = self.stock_table.horizontalHeaderItem(2)
#         item.setText(_translate("MainWindow", "Stock"))
#         item = self.stock_table.horizontalHeaderItem(3)
#         item.setText(_translate("MainWindow", "Rate"))
#         item = self.stock_table.horizontalHeaderItem(4)
#         item.setText(_translate("MainWindow", "Amount"))
#         self.lbl_sales.setText(_translate("MainWindow", "Sales"))
#         self.btn_add_sale.setText(_translate("MainWindow", "Create Sale"))
#         self.search_option_sale.setItemText(0, _translate("MainWindow", "Select Option"))
#         self.search_option_sale.setItemText(1, _translate("MainWindow", "By Name"))
#         self.search_option_sale.setItemText(2, _translate("MainWindow", "By Contact"))
#         self.lbl_from_sale.setText(_translate("MainWindow", "From"))
#         self.lbl_to_sale.setText(_translate("MainWindow", "To"))
#         self.tableWidget_3.setSortingEnabled(True)
#         item = self.tableWidget_3.horizontalHeaderItem(0)
#         item.setText(_translate("MainWindow", "Date"))
#         item = self.tableWidget_3.horizontalHeaderItem(1)
#         item.setText(_translate("MainWindow", "Customer"))
#         item = self.tableWidget_3.horizontalHeaderItem(2)
#         item.setText(_translate("MainWindow", "Quantity"))
#         item = self.tableWidget_3.horizontalHeaderItem(3)
#         item.setText(_translate("MainWindow", "Rate"))
#         item = self.tableWidget_3.horizontalHeaderItem(4)
#         item.setText(_translate("MainWindow", "Amount"))
#         item = self.tableWidget_3.horizontalHeaderItem(5)
#         item.setText(_translate("MainWindow", "Cash Paid"))
#         item = self.tableWidget_3.horizontalHeaderItem(6)
#         item.setText(_translate("MainWindow", "Cash Received"))
#         item = self.tableWidget_3.horizontalHeaderItem(7)
#         item.setText(_translate("MainWindow", "Remaining"))
#         self.lbl_total_sales.setText(_translate("MainWindow", "Total Sales Amount:"))
#         self.txt_total_sales.setText(_translate("MainWindow", "00"))
#         self.lbl_total_cash_paid.setText(_translate("MainWindow", "Total Cash Paid :"))
#         self.txt_total_cash_paid.setText(_translate("MainWindow", "00"))
#         self.lbl_total_cash_recv.setText(_translate("MainWindow", "Total Cash Received :"))
#         self.txt_total_cash_received.setText(_translate("MainWindow", "00"))
#         self.lbl_customer.setText(_translate("MainWindow", "Customers"))
#         self.btn_add_customer.setText(_translate("MainWindow", "Add Customer"))
#         self.search_option_customer.setItemText(0, _translate("MainWindow", "Select Option"))
#         self.search_option_customer.setItemText(1, _translate("MainWindow", "By Name"))
#         self.search_option_customer.setItemText(2, _translate("MainWindow", "By Contact"))
#         self.search_option_customer.setItemText(3, _translate("MainWindow", "By Vehicle"))
#         self.customer_table.setSortingEnabled(True)
#         item = self.customer_table.horizontalHeaderItem(0)
#         item.setText(_translate("MainWindow", "Customer Name"))
#         item = self.customer_table.horizontalHeaderItem(1)
#         item.setText(_translate("MainWindow", "Vehicle No."))
#         item = self.customer_table.horizontalHeaderItem(2)
#         item.setText(_translate("MainWindow", "Mobile"))
#         item = self.customer_table.horizontalHeaderItem(3)
#         item.setText(_translate("MainWindow", "Address"))
#         item = self.customer_table.horizontalHeaderItem(4)
#         item.setText(_translate("MainWindow", "R Balance"))
#         self.lbl_total_customers.setText(_translate("MainWindow", "Total Customers :"))
#         self.txt_total_customers.setText(_translate("MainWindow", "00"))
#         self.lbl_total_remaining.setText(_translate("MainWindow", "Total Balance Remaining :"))
#         self.txt_total_rem_balance.setText(_translate("MainWindow", "00"))
#         self.lbl_roznamcha.setText(_translate("MainWindow", "Roz Namcha"))
#         self.btn_add_roznamcha.setText(_translate("MainWindow", "Add RozNamcha"))
#         self.search_option_rn.setItemText(0, _translate("MainWindow", "Select Option"))
#         self.search_option_rn.setItemText(1, _translate("MainWindow", "By Name"))
#         self.lbl_from_rn.setText(_translate("MainWindow", "From"))
#         self.lbl_to_rn.setText(_translate("MainWindow", "To"))
#         self.roznamcha_table.setSortingEnabled(True)
#         item = self.roznamcha_table.horizontalHeaderItem(0)
#         item.setText(_translate("MainWindow", "Date"))
#         item = self.roznamcha_table.horizontalHeaderItem(1)
#         item.setText(_translate("MainWindow", "Product"))
#         item = self.roznamcha_table.horizontalHeaderItem(2)
#         item.setText(_translate("MainWindow", "Quantity"))
#         item = self.roznamcha_table.horizontalHeaderItem(3)
#         item.setText(_translate("MainWindow", "Rate"))
#         item = self.roznamcha_table.horizontalHeaderItem(4)
#         item.setText(_translate("MainWindow", "Amount"))
#         item = self.roznamcha_table.horizontalHeaderItem(5)
#         item.setText(_translate("MainWindow", "Customer"))
#         item = self.roznamcha_table.horizontalHeaderItem(6)
#         item.setText(_translate("MainWindow", "Cash Paid"))
#         item = self.roznamcha_table.horizontalHeaderItem(7)
#         item.setText(_translate("MainWindow", "Cash Received"))
#         __sortingEnabled = self.roznamcha_table.isSortingEnabled()
#         self.roznamcha_table.setSortingEnabled(False)
#         self.roznamcha_table.setSortingEnabled(__sortingEnabled)
#         self.lbl_total_cashIn.setText(_translate("MainWindow", "Total Cash In Amount :"))
#         self.txt_total_cash_in.setText(_translate("MainWindow", "00"))
#         self.lbl_total_cash_out.setText(_translate("MainWindow", "Total Cash Out Amount :"))
#         self.txt_total_cash_out.setText(_translate("MainWindow", "00"))
#         self.lbl_settings.setText(_translate("MainWindow", "Settings"))
#         self.btn_business_details.setText(_translate("MainWindow", "Business Details"))
#         self.btn_change_business_details.setText(_translate("MainWindow", "Change Business Details"))
#         self.btn_change_user_details.setText(_translate("MainWindow", "Change User Deatils"))
#         self.btn_change_pwd.setText(_translate("MainWindow", "Change Password"))
#         self.lbl_b_name.setText(_translate("MainWindow", "Business Name"))
#         self.lbl_b_email.setText(_translate("MainWindow", "Business Email"))
#         self.lbl_b_contact.setText(_translate("MainWindow", "Business Contact"))
#         self.lbl_b_address.setText(_translate("MainWindow", "Business Address"))
#         self.lbl_b_owner.setText(_translate("MainWindow", "Business Owner"))
#         self.txt_business_name.setText(_translate("MainWindow", "Business Name"))
#         self.txt_business_email.setText(_translate("MainWindow", "Business Email"))
#         self.txt_business_contact.setText(_translate("MainWindow", "Business Contact"))
#         self.txt_business_address.setText(_translate("MainWindow", "Business Address"))
#         self.txt_business_owner.setText(_translate("MainWindow", "Business Owner"))
#         self.lbl_u_name.setText(_translate("MainWindow", "Name"))
#         self.lbl_u_email.setText(_translate("MainWindow", "Email"))
#         self.lbl_u_contact.setText(_translate("MainWindow", "Contact"))
#         self.lbl_u_username.setText(_translate("MainWindow", "Username"))
#         self.txt_user_name.setText(_translate("MainWindow", "Name"))
#         self.txt_user_email.setText(_translate("MainWindow", "Email"))
#         self.txt_user_contact.setText(_translate("MainWindow", "Contact"))
#         self.txt_user_username.setText(_translate("MainWindow", "Username"))



# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     MainWindow = QtWidgets.QMainWindow()
#     ui = Ui_MainWindow()
#     ui.setupUi(MainWindow)
#     MainWindow.show()
#     sys.exit(app.exec_())
