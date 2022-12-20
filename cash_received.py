from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2 import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_CashReceivedWindow(object):
    def setupUi(self, CashReceivedWindow):
        CashReceivedWindow.setObjectName("CashReceivedWindow")
        CashReceivedWindow.resize(500, 500)
        CashReceivedWindow.setMinimumSize(QtCore.QSize(500, 500))
        CashReceivedWindow.setMaximumSize(QtCore.QSize(500, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/assets/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        CashReceivedWindow.setWindowIcon(icon)
        CashReceivedWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(CashReceivedWindow)
        self.centralwidget.setStyleSheet("#label_widget {\n"
"    background-color: #80cbc4;\n"
"    color: #fff;\n"
"}\n"
"\n"
"#btn_save {\n"
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
"#txt_name, #txt_previous, #txt_remaining {\n"
"    background-color: #eee;\n"
"    border: 1px solid #81d4fa;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_widget = QtWidgets.QWidget(self.centralwidget)
        self.label_widget.setObjectName("label_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.label_widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.lbl_add_stock = QtWidgets.QLabel(self.label_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lbl_add_stock.setFont(font)
        self.lbl_add_stock.setAlignment(QtCore.Qt.AlignCenter)
        self.lbl_add_stock.setObjectName("lbl_add_stock")
        self.verticalLayout_3.addWidget(self.lbl_add_stock, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_4.addWidget(self.label_widget, 0, QtCore.Qt.AlignTop)
        self.details_widget = QtWidgets.QWidget(self.centralwidget)
        self.details_widget.setObjectName("details_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.details_widget)
        self.horizontalLayout.setContentsMargins(15, 0, 15, 0)
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_frame = QtWidgets.QFrame(self.details_widget)
        self.lbl_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lbl_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lbl_frame.setObjectName("lbl_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.lbl_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_name = QtWidgets.QLabel(self.lbl_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.lbl_name.setFont(font)
        self.lbl_name.setObjectName("lbl_name")
        self.verticalLayout.addWidget(self.lbl_name)
        self.lbl_date = QtWidgets.QLabel(self.lbl_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.lbl_date.setFont(font)
        self.lbl_date.setObjectName("lbl_date")
        self.verticalLayout.addWidget(self.lbl_date)
        self.lbl_supplier = QtWidgets.QLabel(self.lbl_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.lbl_supplier.setFont(font)
        self.lbl_supplier.setObjectName("lbl_supplier")
        self.verticalLayout.addWidget(self.lbl_supplier)
        self.lbl_stock = QtWidgets.QLabel(self.lbl_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.lbl_stock.setFont(font)
        self.lbl_stock.setObjectName("lbl_stock")
        self.verticalLayout.addWidget(self.lbl_stock)
        self.lbl_rate = QtWidgets.QLabel(self.lbl_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        self.lbl_rate.setFont(font)
        self.lbl_rate.setObjectName("lbl_rate")
        self.verticalLayout.addWidget(self.lbl_rate)
        self.horizontalLayout.addWidget(self.lbl_frame)
        self.lbl_inputs = QtWidgets.QFrame(self.details_widget)
        self.lbl_inputs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lbl_inputs.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lbl_inputs.setObjectName("lbl_inputs")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.lbl_inputs)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txt_name = QtWidgets.QLineEdit(self.lbl_inputs)
        self.txt_name.setMinimumSize(QtCore.QSize(300, 0))
        self.txt_name.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.txt_name.setFont(font)
        self.txt_name.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt_name.setReadOnly(True)
        self.txt_name.setObjectName("txt_name")
        self.verticalLayout_2.addWidget(self.txt_name, 0, QtCore.Qt.AlignRight)
        self.txt_date = QtWidgets.QDateEdit(self.lbl_inputs)
        self.txt_date.setMinimumSize(QtCore.QSize(300, 35))
        self.txt_date.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.txt_date.setFont(font)
        self.txt_date.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.txt_date.setCalendarPopup(True)
        self.txt_date.setObjectName("txt_date")
        self.verticalLayout_2.addWidget(self.txt_date, 0, QtCore.Qt.AlignRight)
        self.txt_amount = QtWidgets.QLineEdit(self.lbl_inputs)
        self.txt_amount.setMinimumSize(QtCore.QSize(300, 0))
        self.txt_amount.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.txt_amount.setFont(font)
        self.txt_amount.setAlignment(QtCore.Qt.AlignCenter)
        self.txt_amount.setObjectName("txt_amount")
        self.verticalLayout_2.addWidget(self.txt_amount, 0, QtCore.Qt.AlignRight)
        self.txt_previous = QtWidgets.QLineEdit(self.lbl_inputs)
        self.txt_previous.setMinimumSize(QtCore.QSize(300, 0))
        self.txt_previous.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.txt_previous.setFont(font)
        self.txt_previous.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt_previous.setReadOnly(True)
        self.txt_previous.setObjectName("txt_previous")
        self.verticalLayout_2.addWidget(self.txt_previous, 0, QtCore.Qt.AlignRight)
        self.txt_remaining = QtWidgets.QLineEdit(self.lbl_inputs)
        self.txt_remaining.setMinimumSize(QtCore.QSize(300, 0))
        self.txt_remaining.setMaximumSize(QtCore.QSize(300, 16777215))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.txt_remaining.setFont(font)
        self.txt_remaining.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.txt_remaining.setReadOnly(True)
        self.txt_remaining.setObjectName("txt_remaining")
        self.verticalLayout_2.addWidget(self.txt_remaining, 0, QtCore.Qt.AlignRight)
        self.horizontalLayout.addWidget(self.lbl_inputs)
        self.verticalLayout_4.addWidget(self.details_widget)
        self.bottom_widget = QtWidgets.QWidget(self.centralwidget)
        self.bottom_widget.setObjectName("bottom_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bottom_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_save = QtWidgets.QPushButton(self.bottom_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/assets/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save.setIcon(icon1)
        self.btn_save.setIconSize(QtCore.QSize(32, 32))
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_2.addWidget(self.btn_save)
        self.btn_clear = QtWidgets.QPushButton(self.bottom_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_clear.setFont(font)
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
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/assets/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon3)
        self.btn_cancel.setIconSize(QtCore.QSize(32, 32))
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_2.addWidget(self.btn_cancel)
        self.verticalLayout_4.addWidget(self.bottom_widget)
        CashReceivedWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(CashReceivedWindow)
        self.statusbar.setObjectName("statusbar")
        CashReceivedWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CashReceivedWindow)
        QtCore.QMetaObject.connectSlotsByName(CashReceivedWindow)

    def retranslateUi(self, CashReceivedWindow):
        _translate = QtCore.QCoreApplication.translate
        CashReceivedWindow.setWindowTitle(_translate("CashReceivedWindow", "Cash Received"))
        self.lbl_add_stock.setText(_translate("CashReceivedWindow", "Cash Received"))
        self.lbl_name.setText(_translate("CashReceivedWindow", "Name"))
        self.lbl_date.setText(_translate("CashReceivedWindow", "Date"))
        self.lbl_supplier.setText(_translate("CashReceivedWindow", "Amount"))
        self.lbl_stock.setText(_translate("CashReceivedWindow", "Previous"))
        self.lbl_rate.setText(_translate("CashReceivedWindow", "Remaining"))
        self.btn_save.setText(_translate("CashReceivedWindow", "SAVE"))
        self.btn_clear.setText(_translate("CashReceivedWindow", "CLEAR"))
        self.btn_cancel.setText(_translate("CashReceivedWindow", "CANCEL"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    CashReceivedWindow = QtWidgets.QMainWindow()
    ui = Ui_CashReceivedWindow()
    ui.setupUi(CashReceivedWindow)
    CashReceivedWindow.show()
    sys.exit(app.exec_())
