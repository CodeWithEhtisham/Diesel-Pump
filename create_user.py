
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from db_handler import DBHandler
import sys
from PyQt5.uic import loadUiType
from login_page import LoginWindow
from resources_rc import *

FORM_MAIN, _ = loadUiType('ui/create_user.ui')


class CreateUserWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()
    
    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.save_user)
        self.btn_cancel.clicked.connect(self.close_window)
        self.btn_clear.clicked.connect(self.clear_text)

    def close_window(self):
        self.close()
    
    def clear_text(self):
        self.txt_name.clear()
        self.txt_email.clear()
        self.txt_contact.clear()
        self.txt_username.clear()
        self.txt_password.clear()

    def save_user(self):
        print("save")
        name = self.txt_name.text()
        email = self.txt_email.text()
        contact = self.txt_contact.text()
        username = self.txt_username.text()
        password = self.txt_password.text()

        if name and email and contact and username and password != "":
            try:
                db=DBHandler()
                db.insert("users", "name, email, contact, username, password", f"'{name}', '{email}', '{contact}', '{username}','{password}'")
                db.close()
                # successfull message box 
                QMessageBox.information(self.centralwidget, "Info", "User has been created")
                # self.clear()
                self.login = LoginWindow()
                self.login.show()
                self.close_window()
            except:
                QMessageBox.information(self.centralwidget, "Info", "User has not been created")
        else:
            QMessageBox.information(self, "Info", "Fields cannot be empty")
        

def main():
    app = QApplication(sys.argv)
    window = CreateUserWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()