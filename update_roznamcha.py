# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'update_roznamcha.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_UpdateRozNamchaWindow(object):
    def setupUi(self, UpdateRozNamchaWindow):
        UpdateRozNamchaWindow.setObjectName("UpdateRozNamchaWindow")
        UpdateRozNamchaWindow.resize(500, 600)
        UpdateRozNamchaWindow.setMinimumSize(QtCore.QSize(500, 600))
        UpdateRozNamchaWindow.setMaximumSize(QtCore.QSize(500, 600))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/assets/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UpdateRozNamchaWindow.setWindowIcon(icon)
        UpdateRozNamchaWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(UpdateRozNamchaWindow)
        self.centralwidget.setStyleSheet("#lbl_add_roz {\n"
"    background-color: #80cbc4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"#btn_update {\n"
"    background-color: #26a69a;\n"
"    border-radius: 5px;\n"
"    padding: 5px 0px;\n"
"    color: white;\n"
"}\n"
"\n"
"#btn_clear {\n"
"    background-color: #81d4fa;\n"
"    border-radius: 5px;\n"
"    padding: 5px 0px;\n"
"    color: white;\n"
"}\n"
"\n"
"#btn_cancel {\n"
"    background-color: #b0bec5;\n"
"    border-radius: 5px;\n"
"    padding: 5px 0px;\n"
"    color: white;\n"
"}\n"
"\n"
"QLineEdit, QDateEdit, QComboBox {\n"
"    border-radius: 5px;\n"
"    padding: 5px 5px;\n"
"    border: 1px solid #81d4fa;\n"
"}\n"
"\n"
"#txt_total_amount {\n"
"    background-color: #eceff1;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_add_roz = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_add_roz.setFont(font)
        self.lbl_add_roz.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_add_roz.setObjectName("lbl_add_roz")
        self.verticalLayout_3.addWidget(self.lbl_add_roz, 0, QtCore.Qt.AlignTop)
        self.details_widget = QtWidgets.QWidget(self.centralwidget)
        self.details_widget.setObjectName("details_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.details_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_frame = QtWidgets.QFrame(self.details_widget)
        self.lbl_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lbl_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lbl_frame.setObjectName("lbl_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.lbl_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_date = QtWidgets.QLabel(self.lbl_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lbl_date.setFont(font)
        self.lbl_date.setObjectName("lbl_date")
        self.verticalLayout.addWidget(self.lbl_date)
        self.lbl_product = QtWidgets.QLabel(self.lbl_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lbl_product.setFont(font)
        self.lbl_product.setObjectName("lbl_product")
        self.verticalLayout.addWidget(self.lbl_product)
        self.lbl_quantity = QtWidgets.QLabel(self.lbl_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lbl_quantity.setFont(font)
        self.lbl_quantity.setObjectName("lbl_quantity")
        self.verticalLayout.addWidget(self.lbl_quantity)
        self.lbl_rate = QtWidgets.QLabel(self.lbl_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lbl_rate.setFont(font)
        self.lbl_rate.setObjectName("lbl_rate")
        self.verticalLayout.addWidget(self.lbl_rate)
        self.lbl_amount = QtWidgets.QLabel(self.lbl_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lbl_amount.setFont(font)
        self.lbl_amount.setObjectName("lbl_amount")
        self.verticalLayout.addWidget(self.lbl_amount)
        self.lbl_customer = QtWidgets.QLabel(self.lbl_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lbl_customer.setFont(font)
        self.lbl_customer.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_customer.setObjectName("lbl_customer")
        self.verticalLayout.addWidget(self.lbl_customer)
        self.lbl_cash_paid = QtWidgets.QLabel(self.lbl_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lbl_cash_paid.setFont(font)
        self.lbl_cash_paid.setObjectName("lbl_cash_paid")
        self.verticalLayout.addWidget(self.lbl_cash_paid)
        self.lbl_cash_received = QtWidgets.QLabel(self.lbl_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lbl_cash_received.setFont(font)
        self.lbl_cash_received.setObjectName("lbl_cash_received")
        self.verticalLayout.addWidget(self.lbl_cash_received)
        self.horizontalLayout.addWidget(self.lbl_frame)
        self.lbl_inputs = QtWidgets.QFrame(self.details_widget)
        self.lbl_inputs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lbl_inputs.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lbl_inputs.setObjectName("lbl_inputs")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.lbl_inputs)
        self.verticalLayout_2.setContentsMargins(10, -1, 10, -1)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txt_date = QtWidgets.QDateEdit(self.lbl_inputs)
        self.txt_date.setMinimumSize(QtCore.QSize(0, 0))
        self.txt_date.setMaximumSize(QtCore.QSize(1000, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.txt_date.setFont(font)
        self.txt_date.setMinimumDate(QtCore.QDate(2000, 9, 14))
        self.txt_date.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.txt_date.setCalendarPopup(True)
        self.txt_date.setTimeSpec(QtCore.Qt.LocalTime)
        self.txt_date.setObjectName("txt_date")
        self.verticalLayout_2.addWidget(self.txt_date)
        self.select_product = QtWidgets.QComboBox(self.lbl_inputs)
        self.select_product.setMinimumSize(QtCore.QSize(0, 0))
        self.select_product.setMaximumSize(QtCore.QSize(1000, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.select_product.setFont(font)
        self.select_product.setObjectName("select_product")
        self.select_product.addItem("")
        self.verticalLayout_2.addWidget(self.select_product)
        self.txt_quantity = QtWidgets.QLineEdit(self.lbl_inputs)
        self.txt_quantity.setMinimumSize(QtCore.QSize(0, 0))
        self.txt_quantity.setMaximumSize(QtCore.QSize(1000, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.txt_quantity.setFont(font)
        self.txt_quantity.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt_quantity.setObjectName("txt_quantity")
        self.verticalLayout_2.addWidget(self.txt_quantity)
        self.txt_rate = QtWidgets.QLineEdit(self.lbl_inputs)
        self.txt_rate.setMinimumSize(QtCore.QSize(0, 0))
        self.txt_rate.setMaximumSize(QtCore.QSize(1000, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.txt_rate.setFont(font)
        self.txt_rate.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt_rate.setObjectName("txt_rate")
        self.verticalLayout_2.addWidget(self.txt_rate)
        self.txt_total_amount = QtWidgets.QLineEdit(self.lbl_inputs)
        self.txt_total_amount.setMinimumSize(QtCore.QSize(0, 40))
        self.txt_total_amount.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt_total_amount.setObjectName("txt_total_amount")
        self.verticalLayout_2.addWidget(self.txt_total_amount)
        self.select_customer = QtWidgets.QComboBox(self.lbl_inputs)
        self.select_customer.setMinimumSize(QtCore.QSize(0, 0))
        self.select_customer.setMaximumSize(QtCore.QSize(1000, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.select_customer.setFont(font)
        self.select_customer.setObjectName("select_customer")
        self.select_customer.addItem("")
        self.verticalLayout_2.addWidget(self.select_customer)
        self.txt_cash_paid = QtWidgets.QLineEdit(self.lbl_inputs)
        self.txt_cash_paid.setMinimumSize(QtCore.QSize(0, 40))
        self.txt_cash_paid.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt_cash_paid.setObjectName("txt_cash_paid")
        self.verticalLayout_2.addWidget(self.txt_cash_paid)
        self.txt_cash_received = QtWidgets.QLineEdit(self.lbl_inputs)
        self.txt_cash_received.setMinimumSize(QtCore.QSize(0, 40))
        self.txt_cash_received.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt_cash_received.setObjectName("txt_cash_received")
        self.verticalLayout_2.addWidget(self.txt_cash_received)
        self.horizontalLayout.addWidget(self.lbl_inputs)
        self.verticalLayout_3.addWidget(self.details_widget)
        self.bottom_widget = QtWidgets.QWidget(self.centralwidget)
        self.bottom_widget.setObjectName("bottom_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bottom_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_update = QtWidgets.QPushButton(self.bottom_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_update.setFont(font)
        self.btn_update.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/assets/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_update.setIcon(icon1)
        self.btn_update.setIconSize(QtCore.QSize(32, 32))
        self.btn_update.setObjectName("btn_update")
        self.horizontalLayout_2.addWidget(self.btn_update)
        self.btn_clear = QtWidgets.QPushButton(self.bottom_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_clear.setFont(font)
        self.btn_clear.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/assets/icons/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_clear.setIcon(icon2)
        self.btn_clear.setIconSize(QtCore.QSize(32, 32))
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout_2.addWidget(self.btn_clear)
        self.btn_cancel = QtWidgets.QPushButton(self.bottom_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cancel.setFont(font)
        self.btn_cancel.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/assets/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon3)
        self.btn_cancel.setIconSize(QtCore.QSize(32, 32))
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_2.addWidget(self.btn_cancel)
        self.verticalLayout_3.addWidget(self.bottom_widget)
        UpdateRozNamchaWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(UpdateRozNamchaWindow)
        self.statusbar.setObjectName("statusbar")
        UpdateRozNamchaWindow.setStatusBar(self.statusbar)

        self.retranslateUi(UpdateRozNamchaWindow)
        QtCore.QMetaObject.connectSlotsByName(UpdateRozNamchaWindow)

    def retranslateUi(self, UpdateRozNamchaWindow):
        _translate = QtCore.QCoreApplication.translate
        UpdateRozNamchaWindow.setWindowTitle(_translate("UpdateRozNamchaWindow", "Update Roz Namcha"))
        self.lbl_add_roz.setText(_translate("UpdateRozNamchaWindow", "Update RozNamcha"))
        self.lbl_date.setText(_translate("UpdateRozNamchaWindow", "Date"))
        self.lbl_product.setText(_translate("UpdateRozNamchaWindow", "Product"))
        self.lbl_quantity.setText(_translate("UpdateRozNamchaWindow", "Quantity"))
        self.lbl_rate.setText(_translate("UpdateRozNamchaWindow", "Rate"))
        self.lbl_amount.setText(_translate("UpdateRozNamchaWindow", "Amount"))
        self.lbl_customer.setText(_translate("UpdateRozNamchaWindow", "Customer"))
        self.lbl_cash_paid.setText(_translate("UpdateRozNamchaWindow", "Cash Paid"))
        self.lbl_cash_received.setText(_translate("UpdateRozNamchaWindow", "Cash Received"))
        self.select_product.setItemText(0, _translate("UpdateRozNamchaWindow", "Select Product"))
        self.select_customer.setItemText(0, _translate("UpdateRozNamchaWindow", "Select Customer"))
        self.btn_update.setText(_translate("UpdateRozNamchaWindow", "UPDATE"))
        self.btn_clear.setText(_translate("UpdateRozNamchaWindow", "CLEAR"))
        self.btn_cancel.setText(_translate("UpdateRozNamchaWindow", "CANCEL"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UpdateRozNamchaWindow = QtWidgets.QMainWindow()
    ui = Ui_UpdateRozNamchaWindow()
    ui.setupUi(UpdateRozNamchaWindow)
    UpdateRozNamchaWindow.show()
    sys.exit(app.exec_())
