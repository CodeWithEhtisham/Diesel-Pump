
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
# from cash_paid import CashPaidWindow
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
        data=db.conn.execute(f"SELECT date,products.product_name,quantity,rate,total_amount,customers.name,cash_paid,cash_received FROM roznamcha LEFT JOIN customers ON roznamcha.customer_id=customers.custmer_id LEFT JOIN products ON roznamcha.product_id=products.product_id WHERE roznamcha.date BETWEEN '{from_date}' AND '{to_date}'").fetchall()
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
            data=db.conn.execute(f"SELECT date,products.product_name,quantity,rate,total_amount,customers.name,cash_paid,cash_received FROM roznamcha LEFT JOIN customers ON roznamcha.customer_id=customers.custmer_id LEFT JOIN products ON roznamcha.product_id=products.product_id Where customers.name LIKE '%{value}%'").fetchall()
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
        data=db.conn.execute("SELECT products.product_name,product_stock,products.uom FROM products").fetchall()
        # print(data)
        self.product_table.setRowCount(0)
        for index,row in enumerate(data):
            self.product_table.insertRow(index)
            for i in row:
                self.product_table.setItem(index,row.index(i),QTableWidgetItem(str(i)))

        data = db.conn.execute("SELECT date,supplier_id,stock,rate,amount FROM stock").fetchall()
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

        data = db.conn.execute(f"SELECT date,products.product_name,quantity,rate,total_amount,customers.name,cash_paid,cash_received FROM roznamcha LEFT JOIN customers ON roznamcha.customer_id=customers.custmer_id LEFT JOIN products ON roznamcha.product_id=products.product_id ").fetchall()
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
            balance.append(float(row[-1]))
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
        data=db.select_all('users',"*")
        if data:
            self.txt_user_name.setText(data[0][1])
            self.txt_user_email.setText(data[0][2])
            self.txt_user_contact.setText(data[0][3])
            self.txt_user_username.setText(data[0][4])

        data = db.select_all('business',"*")
        if data:
            self.txt_business_name.setText(data[0][1])
            self.txt_business_email.setText(data[0][2])
            self.txt_business_contact.setText(data[0][4])
            self.txt_business_address.setText(data[0][3])
            self.txt_business_owner.setText(data[0][5])
            self.btn_business_details.hide()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()


