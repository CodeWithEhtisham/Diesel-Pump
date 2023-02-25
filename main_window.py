
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
from resources_rc import *
from expenses import ExpensesWindow
from expense_type import ExpenseTypeWindow
from update_expense import UpdateExpensesWindow
from update_roznamcha import UpdateNamchaWindow
from update_customer import UpdateCustomerWindow
from update_supplier import UpdateSupplierWindow

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
        self.txt_date_from_sale.setDate(QDate.currentDate())
        self.txt_date_to_sale.setDate(QDate.currentDate())
        self.txt_date_to_rn.setDate(QDate.currentDate())
        self.txt_date_from_rn.setDate(QDate.currentDate())
        self.from_date_expense.setDate(QDate.currentDate())
        self.to_date_expense.setDate(QDate.currentDate())
        self.btn_home.clicked.connect(self.home)
        self.btn_product.clicked.connect(self.product)
        self.btn_sales.clicked.connect(self.sales)
        self.btn_customer.clicked.connect(self.customer)
        self.btn_roznamcha.clicked.connect(self.roznamcha)
        self.btn_settings.clicked.connect(self.settings)
        self.btn_supplier.clicked.connect(self.supplier)
        self.btn_reports.clicked.connect(self.reports)
        self.btn_expense.clicked.connect(self.expense)

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
        self.supplier_table.doubleClicked.connect(
            self.supplier_account_details)

        # business btns
        self.btn_business_details.clicked.connect(self.business_details)
        self.btn_change_business_details.clicked.connect(self.edit_business)

        # edit user details btns
        self.btn_change_user_details.clicked.connect(self.change_user_details)
        self.btn_change_pwd.clicked.connect(self.change_password)

        self.btn_refresh_customer.clicked.connect(self.update_customer_table)
        # self.btn_search_customer.clicked.connect(self.customer_search)
        self.txt_search_customer.textChanged.connect(self.customer_search)

        self.txt_search_supplier.textChanged.connect(self.supplier_search)
        self.btn_refresh_supplier.clicked.connect(self.update_supplier_table)

        # product qcombobox select value
        self.select_product.activated.connect(self.stock_search)
        self.txt_date.setDate(QDate.currentDate())
        # on date change event
        self.txt_date.dateChanged.connect(self.stock_search_by_date)
        self.txt_search_rn.textChanged.connect(self.search_roznamcha_by_name)
        self.btn_search_rn.clicked.connect(self.search_roznamcha_by_date)
        self.btn_refresh_rn.clicked.connect(self.update_roznamcha_table)
        self.btn_refresh_sale.clicked.connect(self.update_sales_table)

        self.btn_add_expense.clicked.connect(self.add_expense)
        self.btn_expense_refresh.clicked.connect(self.update_expense_table)
        self.btn_search_expense.clicked.connect(self.expense_search_by_date)
        self.txt_expense_search.textChanged.connect(self.search_expense)
        self.btn_expense_type.clicked.connect(self.open_expense_type_window)

        self.btn_edit_expense.clicked.connect(self.edit_expense)
        self.btn_edit_rn.clicked.connect(self.edit_roznamcha)
        self.btn_edit_customer.clicked.connect(self.edit_customer)
        self.btn_edit_supplier.clicked.connect(self.edit_supplier)

    def edit_supplier(self):
        row = self.supplier_table.currentRow()
        try:
            id = self.supplier_table.item(row, 0).text()
            self.edit_supplier_window = UpdateSupplierWindow(int(id))
            self.edit_supplier_window.show()
            self.edit_supplier_window.btn_save.clicked.connect(self.update_supplier_table)
        except:
            QMessageBox.warning(self, "Error", "Please select a supplier")

    def edit_customer(self):
        row = self.customer_table.currentRow()
        print(row)
        try:
            id = self.customer_table.item(row, 0).text()
            self.edit_customer_window = UpdateCustomerWindow(int(id))
            self.edit_customer_window.show()
            self.edit_customer_window.btn_save.clicked.connect(self.update_customer_table)
        except:
            QMessageBox.warning(self, "Error", "Please select a customer")

    def edit_roznamcha(self):
        db=DBHandler()
        row = self.roznamcha_table.currentRow()
        date = self.roznamcha_table.item(row, 0).text()
        quantity = self.roznamcha_table.item(row, 2).text()
        rate= self.roznamcha_table.item(row, 3).text()
        total_amount = self.roznamcha_table.item(row, 4).text()
        cash_paid = self.roznamcha_table.item(row, 6).text()
        cash_received = self.roznamcha_table.item(row, 7).text()
        # date,quantity,rate,total_amount,cash_paid,cash_received
        id = db.select(table_name='roznamcha', columns='roznamcha_id', condition=f"date='{date}' AND quantity='{quantity}' AND rate='{rate}' AND total_amount='{total_amount}' AND cash_paid='{cash_paid}' AND cash_received='{cash_received}'")[0][0]
        self.edit_roznamcha = UpdateNamchaWindow(id)
        self.edit_roznamcha.show()
        self.edit_roznamcha.btn_delete.clicked.connect(self.update_roznamcha_table)
    def edit_expense(self):
        db=DBHandler()
        row = self.expense_table.currentRow()
        date = self.expense_table.item(row, 0).text()
        hoa = self.expense_table.item(row, 1).text()
        amount = self.expense_table.item(row, 2).text()
        payment_type = self.expense_table.item(row, 3).text()
        recipient_name = self.expense_table.item(row, 4).text()
        comment = self.expense_table.item(row, 5).text()
        id = db.select(table_name='expenses', columns='id', condition=f"date='{date}' AND hoa='{hoa}' AND amount='{amount}' AND payment_type='{payment_type}' AND recipient_name='{recipient_name}' AND comment='{comment}'")[0][0]
        if id:
            self.expense_window = UpdateExpensesWindow(id)
            self.expense_window.show()
            self.expense_window.btn_save.clicked.connect(self.update_expense_table)
            self.expense_window.btn_delete.clicked.connect(self.update_expense_table)
        else:
            QMessageBox.warning(self, "Error", "Please select an expense")
            return
    
    def expense_search_by_date(self):
        from_date = self.from_date_expense.date().toString('dd/MM/yyyy')
        to_date = self.to_date_expense.date().toString('dd/MM/yyyy')

        db = DBHandler()
        data = db.select(
            table_name='expenses',
            columns="date,hoa,amount,payment_type,recipient_name,comment",
            condition=f"date BETWEEN '{from_date}' AND '{to_date}'")
        if data:
            self.update_expense_table(data)
        else:
            self.expense_table.setRowCount(0)
            self.total_expense.setText('0')

    def open_expense_type_window(self):
        self.expense_type_window=ExpenseTypeWindow()
        self.expense_type_window.show()
    
    def search_expense(self):
        db=DBHandler()
        search = self.txt_expense_search.text()
        data = db.select(
            table_name='expenses',
            columns="date,hoa,amount,payment_type,recipient_name,comment",
            condition=f"date LIKE '%{search}%' OR hoa LIKE '%{search}%' OR amount LIKE '%{search}%' OR payment_type LIKE '%{search}%' OR recipient_name LIKE '%{search}%' OR comment LIKE '%{search}%'")
        if data:
            self.update_expense_table(data)
        else:
            self.expense_table.setRowCount(0)
            self.total_expense.setText('0')
        
    def add_expense(self):
        self.add_expense_window = ExpensesWindow()
        self.add_expense_window.show()
        self.add_expense_window.btn_save.clicked.connect(self.update_expense_table)

    def update_expense_table(self,expense=None):
        db=DBHandler()
        if expense is None or expense==False:
            expense = db.select_all(
                table_name='expenses',
                columns="date,hoa,amount,payment_type,recipient_name,comment",
            )
        if expense:
            amount = 0
            self.expense_table.setRowCount(0)
            for row, form in enumerate(expense):
                self.expense_table.insertRow(row)
                amount += int(form[2])
                for column, item in enumerate(form):
                    self.expense_table.setItem(
                        row, column, QTableWidgetItem(str(item)))
            self.total_expense.setText(str(amount))
        else:
            self.expense_table.setRowCount(0)
            self.total_expense.setText('0')


    def update_supplier_table(self,data=None):
        db=DBHandler()
        if data is None or data is False:
            data=db.select_all(table_name='suppliers',columns='supplier_id,name,phone,address,balance')
        if data:
            self.supplier_table.setRowCount(0)
            for index,row in enumerate(data):
                self.supplier_table.insertRow(index)
                for idx,i in enumerate(row):
                    self.supplier_table.setItem(index,idx,QTableWidgetItem(str(i)))
            self.txt_total_supplier.setText(str(len(data)))
            self.txt_supplier_total_rem_balance.setText(
                str(sum([float(i[-1]) for i in data])))
        else:
            self.supplier_table.setRowCount(0)
            self.txt_total_supplier.setText('0')
            self.txt_supplier_total_rem_balance.setText('0')

    def supplier_search(self):
        # option = self.search_option_supplier.currentText()
        search = self.txt_search_supplier.text()
        db = DBHandler()
        data = db.conn.execute(
            f"SELECT supplier_id,name,phone,address,balance FROM suppliers WHERE name LIKE '%{search}%' OR phone LIKE '%{search}%' OR address LIKE '%{search}%'").fetchall()
        if data:
            self.update_supplier_table(data)
        else:
            self.supplier_table.setRowCount(0)
            self.txt_total_supplier.setText('0')
            self.txt_supplier_total_rem_balance.setText('0')


    def supplier_account_details(self):
        row = self.supplier_table.currentRow()
        id = self.supplier_table.item(row, 0).text()
        self.window = SupplierAccountDetailsWindow(id)
        self.window.show()

    def add_supplier(self):
        self.window = AddSupplierWindow()
        self.window.show()
        self.window.btn_save.clicked.connect(self.update_supplier_table)

    def logout(self):
        from login_page import LoginWindow
        self.login = LoginWindow()
        self.login.show()
        self.close()

    def customer_detail_widget(self):
        # get row number and its value
        row = self.customer_table.currentRow()
        id = self.customer_table.item(row, 0).text()
        self.window = AccountDetailsWindow(id)
        self.window.show()

    def search_roznamcha_by_date(self):
        from_date = self.txt_date_from_rn.date().toString("dd/MM/yyyy")
        to_date = self.txt_date_to_rn.date().toString("dd/MM/yyyy")
        db = DBHandler()
        data = db.conn.execute(
            f"SELECT date,products.product_name,quantity,rate,total_amount,customers.name,cash_paid,cash_received FROM roznamcha LEFT JOIN customers ON roznamcha.customer_id=customers.custmer_id LEFT JOIN products ON roznamcha.product_id=products.product_id WHERE roznamcha.date BETWEEN '{from_date}' AND '{to_date}'").fetchall()
        if data:
            self.update_roznamcha_table(data)
        else:
            self.roznamcha_table.setRowCount(0)
            self.txt_total_cash_in.setText('0')
            self.txt_total_cash_out.setText('0')

    def search_roznamcha_by_name(self):
            search = self.txt_search_rn.text()
            db = DBHandler()
            data = db.conn.execute(
                f"SELECT date,products.product_name,quantity,rate,total_amount,customers.name,cash_paid,cash_received FROM roznamcha LEFT JOIN customers ON roznamcha.customer_id=customers.custmer_id LEFT JOIN products ON roznamcha.product_id=products.product_id Where customers.name LIKE '%{search}%' or products.product_name LIKE '%{search}%'").fetchall()
            if data:
                self.update_roznamcha_table(data)
            else:
                self.roznamcha_table.setRowCount(0)
                self.txt_total_cash_in.setText('0')
                self.txt_total_cash_out.setText('0')

    def update_roznamcha_table(self,data=None):
        db=DBHandler()
        if data is None or data is False:
            data = db.conn.execute(f"SELECT date,products.product_name,quantity,rate,total_amount,customers.name,cash_paid,cash_received FROM roznamcha LEFT JOIN customers ON roznamcha.customer_id=customers.custmer_id LEFT JOIN products ON roznamcha.product_id=products.product_id ").fetchall()
        if data:
            self.roznamcha_table.setRowCount(0)
            cash_paid = 0
            cash_received = 0
            for index, row in enumerate(data):
                self.roznamcha_table.insertRow(index)
                cash_paid += row[-2]
                cash_received += row[-1]
                for idx, i in enumerate(row):
                    self.roznamcha_table.setItem(
                        index, idx, QTableWidgetItem(str(i)))
            self.txt_total_cash_in.setText(str(cash_received))
            self.txt_total_cash_out.setText(str(cash_paid))
        else:
            self.roznamcha_table.setRowCount(0)
            self.txt_total_cash_in.setText('0')
            self.txt_total_cash_out.setText('0')

    def add_roznamcha(self):
        self.roznamcha_window = RozNamchaWindow()
        self.roznamcha_window.show()
        self.roznamcha_window.btn_save.clicked.connect(self.update_roznamcha_table)

    def sale_search_by_date(self):
        from_date = self.txt_date_from_sale.date().toString("dd/MM/yyyy")
        to_date = self.txt_date_to_sale.date().toString("dd/MM/yyyy")
        db = DBHandler()
        data = db.conn.execute(
            f"SELECT sales.date,customers.name,sales.quantity,sales.rate,sales.total_amount,sales.cash_paid,sales.cash_received,sales.sub_total FROM sales LEFT JOIN customers ON sales.customer_id=customers.custmer_id WHERE sales.date BETWEEN '{from_date}' AND '{to_date}'").fetchall()
        if data:
            self.update_sales_table(data)
        else:
            self.sales_table.setRowCount(0)
            self.txt_total_sales.setText("0")
            self.txt_total_cash_paid.setText("0")
            self.txt_total_cash_received.setText("0")

    def sale_search_by_option(self):
        # option = self.search_option_sale.currentText()
        search = self.txt_search_sale.text()
        db = DBHandler()
        data = db.conn.execute(
            f"SELECT sales.date,customers.name,sales.quantity,sales.rate,sales.total_amount,sales.cash_paid,sales.cash_received,sales.sub_total FROM sales LEFT JOIN customers ON sales.customer_id=customers.custmer_id WHERE customers.name LIKE '%{search}%' OR customers.phone LIKE '%{search}%'").fetchall()
        if data:
            self.update_sales_table(data)
        else:
            self.sales_table.setRowCount(0)
            self.txt_total_sales.setText("0")
            self.txt_total_cash_paid.setText("0")
            self.txt_total_cash_received.setText("0")

    def update_sales_table(self, data=None):
        db=DBHandler()
        if data is None or data is False:
            data = db.conn.execute(
            "SELECT sales.date,customers.name,sales.quantity,sales.rate,sales.total_amount,sales.cash_paid,sales.cash_received,sales.sub_total FROM sales LEFT JOIN customers ON sales.customer_id=customers.custmer_id").fetchall()
        # print(f"sales {data}")
        if data:
            self.sales_table.setRowCount(0)
            total = 0
            cash_paid = 0
            cash_received = 0
            for index, row in enumerate(data):
                self.sales_table.insertRow(index)
                total += row[4]
                cash_paid += row[5]
                cash_received += row[6]
                for idx, i in enumerate(row):
                    self.sales_table.setItem(index, idx, QTableWidgetItem(str(i)))

            self.txt_total_sales.setText(str(total))
            self.txt_total_cash_paid.setText(str(cash_paid))
            self.txt_total_cash_received.setText(str(cash_received))
        else:
            self.sales_table.setRowCount(0)
            self.txt_total_sales.setText("0")
            self.txt_total_cash_paid.setText("0")
            self.txt_total_cash_received.setText("0")

    def add_sales(self):
        self.sale_window = SalesWindow()
        self.sale_window.show()
        self.sale_window.btn_sale.clicked.connect(self.update_sales_table)
        self.sale_window.btn_sale_print.clicked.connect(self.update_sales_table)

    def customer_search(self):
        search=self.txt_search_customer.text()
        db=DBHandler()
        data=db.conn.execute(f"SELECT * FROM customers WHERE name LIKE '%{search}%' OR phone LIKE '%{search}%' OR address LIKE '%{search}%' OR vehicle LIKE '%{search}%' OR balance_type LIKE '%{search}%'").fetchall()
        if data:
            self.update_customer_table(data)
        else:
            self.customer_table.setRowCount(0)
            self.txt_total_customers.setText("0")
            self.txt_total_rem_balance.setText("0")

    def update_customer_table(self,data=None):
        print("customer data ",data)
        db = DBHandler()
        if data is None or data is False:
            print("data is none")
            data = db.select_all(
                'customers', 'custmer_id,name,phone,vehicle,address,balance')
        if data:
            self.customer_table.setRowCount(0)
            balance = []
            for index, row in enumerate(data):
                balance.append(float(row[-1]))
                self.customer_table.insertRow(index)
                print(row)
                for idx, i in enumerate(row):
                    # print(i)
                    self.customer_table.setItem(
                        index, idx, QTableWidgetItem(str(i)))
            self.txt_total_customers.setText(str(len(data)))
            self.txt_total_rem_balance.setText(str(sum(balance)))
        else:
            self.customer_table.setRowCount(0)
            self.txt_total_customers.setText("0")
            self.txt_total_rem_balance.setText("0")

    def add_customer(self):
        self.add_customer_window = AddCustomerWindow()
        self.add_customer_window.show()
        self.add_customer_window.btn_save.clicked.connect(self.update_customer_table)

    def update_table(self,data,obj):
        obj.setRowCount(0)
        for index,row in enumerate(data):
            obj.insertRow(index)
            for idx,i in enumerate(row):
                obj.setItem(index,idx,QTableWidgetItem(str(i)))

    def update_product_table(self):
        db=DBHandler()
        data= db.select_all('products',"product_name")
        self.select_product.clear()
        self.select_product.addItem("Select Product")
        if data: 
            for i in data: self.select_product.addItem(i[0])
        data=db.conn.execute("SELECT products.product_name,product_stock,products.uom FROM products").fetchall()
        if data:
            self.product_table.setRowCount(0)
            for index,row in enumerate(data):
                self.product_table.insertRow(index)
                for i in row:
                    self.product_table.setItem(index,row.index(i),QTableWidgetItem(str(i)))

    def update_stock_table(self,data=None,option=None):
        db=DBHandler()
        if not data or False:
            data = db.conn.execute("SELECT stock.date,suppliers.name,stock.stock,stock.rate,stock.amount from stock LEFT JOIN suppliers ON stock.supplier_id=suppliers.supplier_id").fetchall()
        if data:
            self.stock_table.setRowCount(0)
            for index,row in enumerate(data):
                self.stock_table.insertRow(index)
                for idx,i in enumerate(row):
                    self.stock_table.setItem(index,idx,QTableWidgetItem(str(i)))
            current_date=QDate.currentDate().toString("dd/MM/yyyy")
            previous_date=QDate.currentDate().addDays(-2).toString("dd/MM/yyyy")
            if option==None:
                data=db.conn.execute(f"SELECT AVG(rate) FROM stock WHERE date BETWEEN '{previous_date}' AND '{current_date}'").fetchone()[0]
            else:
                data=db.conn.execute(f"SELECT AVG(rate) FROM stock WHERE date BETWEEN '{previous_date}' AND '{current_date}' AND product_id={option}").fetchone()[0]
            self.txt_average_price.setText(str(data))
        else:
            self.stock_table.setRowCount(0)
            self.txt_average_price.setText("0")
    
    def stock_search_by_date(self):
        date=self.txt_date.date().toString("dd/MM/yyyy")
        product=self.select_product.currentText()
        db=DBHandler()
        if product=="Select Product":
            print(date)
            data = db.conn.execute(f"SELECT stock.date,suppliers.name,stock.stock,stock.rate,stock.amount from stock LEFT JOIN suppliers ON stock.supplier_id=suppliers.supplier_id WHERE date='{date}'").fetchall()
            if data:
                self.update_stock_table(data)
            else:
                self.stock_table.setRowCount(0)
                self.txt_average_price.setText("0")
        else:
            product_id=db.conn.execute(f"SELECT product_id FROM products WHERE product_name='{product}'").fetchone()[0]
            data = db.conn.execute(f"SELECT stock.date,suppliers.name,stock.stock,stock.rate,stock.amount from stock LEFT JOIN suppliers ON stock.supplier_id=suppliers.supplier_id  WHERE date='{date}' and product_id={product_id}").fetchall()
            if data:
                self.update_stock_table(data=data,option=product_id)
            else:
                self.stock_table.setRowCount(0)
                self.txt_average_price.setText("0")
            
    def stock_search(self):
        db=DBHandler()
        product=self.select_product.currentText()
        self.stock_table.setRowCount(0)
        if product=="Select Product":
            self.update_stock_table()
        else:
            product_id=db.conn.execute(f"SELECT product_id FROM products WHERE product_name='{product}'").fetchone()[0]
            data = db.conn.execute(f"SELECT stock.date,suppliers.name,stock.stock,stock.rate,stock.amount from stock LEFT JOIN suppliers ON stock.supplier_id=suppliers.supplier_id  WHERE product_id={product_id}").fetchall()
            if data:
                self.update_stock_table(data=data,option=product_id)
            else:
                self.stock_table.setRowCount(0)
                self.txt_average_price.setText("0")

    def update_report_table(self):
        db=DBHandler()
        total_stoack_amount=db.conn.execute("SELECT SUM(amount) FROM stock").fetchone()[0]
        if not total_stoack_amount:
            # total_stoack_amount=total_stoack_amount[0]
            total_stoack_amount=0
        # else:
        self.total_stock_amount.setText(str(f"{total_stoack_amount:,}"))
        
        total_apyable=db.conn.execute("SELECT SUM(balance) FROM customers").fetchone()[0]
        if not total_apyable:
            # total_apyable=total_apyable[0]
            total_apyable=0
        # else:
        self.total_payable.setText("0")
        
        total_receivable=db.conn.execute("SELECT SUM(balance) FROM suppliers").fetchone()[0]
        if not total_receivable:
            # total_receivable=total_receivable[0]
            total_receivable=0
        # else:
        self.total_receivable.setText(str(f"{total_receivable:,}"))
        
        total_sales=db.conn.execute("SELECT SUM(sub_total) FROM sales").fetchone()[0]
        if not total_sales:
            # total_sales=total_sales[0]
            total_sales=0
        # else:
        self.total_sales.setText(str(f"{total_sales:,}"))

        total_purchase=db.conn.execute("SELECT SUM(amount) FROM stock").fetchone()[0]
        if not total_purchase:
            # total_purchase=total_purchase[0]
            total_purchase=0
        # else:
        self.total_stock_purchase.setText(str(f"{total_purchase:,}"))
        
        total_expenses=db.conn.execute("SELECT SUM(amount) FROM expenses").fetchone()[0]
        if not total_expenses:
            # total_expenses=total_expenses[0]
            total_expenses=0
        # else:
        self.total_expenses.setText(str(f"{total_expenses:,}"))
        
        total_amount=db.conn.execute("SELECT SUM(total_amount) FROM sales").fetchone()[0]
        if not total_amount:
            # total_amount=total_amount[0]
            total_amount=0
        # else:
            
        total_expenses=db.conn.execute("SELECT SUM(amount) FROM expenses").fetchone()[0]
        print(total_amount,total_expenses)
        if not total_expenses:
            total_expenses=0
            # total_expenses=total_expenses[0]
        # else:
        print(total_amount,total_expenses)
        total_profit=total_amount-total_expenses
        self.net_balance.setText(
            str(f"{total_profit:,}")
        )

    

    def update(self):
        db = DBHandler()
        data = db.select_all('products', "*")
        self.select_product.clear()
        self.select_product.addItem("Select Product")
        if data: 
            for i in data: self.select_product.addItem(i[1])

        data=db.select(table_name='business',columns="*",condition="id=1")
        if data:
            self.lbl_business_name.setText(data[0][1])
            self.lbl_business_contact.setText(data[0][4])
            self.lbl_business_address.setText(data[0][3])


    def add_product(self):
        self.add_product_window = AddProductWindow()
        self.add_product_window.show()
        self.add_product_window.btn_save.clicked.connect(self.update_product_table)
        

    def add_stock(self):
        self.add_stock_window = AddStockWindow()
        self.add_stock_window.show()
        self.add_stock_window.btn_save.clicked.connect(self.update_stock_table)
        self.add_stock_window.btn_save.clicked.connect(self.update_product_table)

    def change_user_details(self):
        self.changeuserdetaisls = UpdateUserWindow()
        self.changeuserdetaisls.show()

    def change_password(self):
        self.changepassword = ChangePasswordWindow()
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
        self.update_product_table()
        self.update_stock_table()

    def sales(self):
        self.stackedWidget.setCurrentWidget(self.sales_page)
        self.update_sales_table()

    def customer(self):
        self.stackedWidget.setCurrentWidget(self.customer_page)
        self.update_customer_table()
        # self.update()

    def supplier(self):
        self.stackedWidget.setCurrentWidget(self.supplier_page)
        self.update_supplier_table()

    def roznamcha(self):
        self.stackedWidget.setCurrentWidget(self.roznamcha_page)
        self.update_roznamcha_table()

    def reports(self):
        self.stackedWidget.setCurrentWidget(self.reports_page)
        self.update_report_table()

    def expense(self):
        self.stackedWidget.setCurrentWidget(self.expense_page)
        self.update_expense_table()

    def settings(self):
        self.stackedWidget.setCurrentWidget(self.settings_page)
        self.update()
        db = DBHandler()
        data = db.select_all('users', "*")
        if data:
            self.txt_user_name.setText(data[0][1])
            self.txt_user_email.setText(data[0][2])
            self.txt_user_contact.setText(data[0][3])
            self.txt_user_username.setText(data[0][4])

        data = db.select_all('business', "*")
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
