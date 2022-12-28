
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from db_handler import DBHandler
from create_user import Ui_CreateUserWindow

from main_window import Ui_MainWindow
from splash_screen import Ui_SplashScreen

## ==> GLOBALS
counter = 0

class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # HOME PAGE BUTTON
        self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home_page))

        # HOME PAGE BUTTON
        self.ui.btn_product.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.product_page))

        # HOME PAGE BUTTON
        self.ui.btn_sales.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sales_page))

        # CUSTOMER PAGE BUTTON
        self.ui.btn_customer.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.customer_page))

        # ROZNAMCHA PAGE BUTTON
        self.ui.btn_roznamcha.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.roznamcha_page))

        # SETTINGS PAGE BUTTON
        self.ui.btn_settings.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settings_page))

        # ## SHOW ==> MAIN WINDOW
        # ########################################################################
        self.show

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            self.main = MainWindow()
            self.main.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1




if __name__ == "__main__":
    db= DBHandler()
    app = QApplication(sys.argv)
    if not db.select_all("users", "*"):
        # open create user window
        CreateUserWindow = QtWidgets.QMainWindow()
        ui = Ui_CreateUserWindow()
        ui.setupUi(CreateUserWindow)
        CreateUserWindow.show()
        sys.exit(app.exec_())
    else:
        window = SplashScreen()
        sys.exit(app.exec_())