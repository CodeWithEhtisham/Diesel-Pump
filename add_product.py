from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2 import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

class Ui_AddProductWindow(object):
    def setupUi(self, AddProductWindow):
        AddProductWindow.setObjectName("AddProductWindow")
        AddProductWindow.resize(500, 300)
        AddProductWindow.setMinimumSize(QtCore.QSize(500, 300))
        AddProductWindow.setMaximumSize(QtCore.QSize(500, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/assets/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        AddProductWindow.setWindowIcon(icon)
        AddProductWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(AddProductWindow)
        self.centralwidget.setStyleSheet("#label_widget {\n"
"    background-color: #80cbc4;\n"
"}\n"
"\n"
"#label_5 {\n"
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
"QLineEdit {\n"
"    border-radius: 5px;\n"
"    padding: 5px 5px;\n"
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
        self.label_5 = QtWidgets.QLabel(self.label_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_4.addWidget(self.label_widget, 0, QtCore.Qt.AlignTop)
        self.details_widget = QtWidgets.QWidget(self.centralwidget)
        self.details_widget.setObjectName("details_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.details_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_frame = QtWidgets.QFrame(self.details_widget)
        self.lbl_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lbl_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lbl_frame.setObjectName("lbl_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.lbl_frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_name = QtWidgets.QLabel(self.lbl_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lbl_name.setFont(font)
        self.lbl_name.setObjectName("lbl_name")
        self.verticalLayout_2.addWidget(self.lbl_name)
        self.lbl_uom = QtWidgets.QLabel(self.lbl_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lbl_uom.setFont(font)
        self.lbl_uom.setObjectName("lbl_uom")
        self.verticalLayout_2.addWidget(self.lbl_uom)
        self.horizontalLayout.addWidget(self.lbl_frame)
        self.lbl_inputs = QtWidgets.QFrame(self.details_widget)
        self.lbl_inputs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lbl_inputs.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lbl_inputs.setObjectName("lbl_inputs")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.lbl_inputs)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txt_product_name = QtWidgets.QLineEdit(self.lbl_inputs)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.txt_product_name.setFont(font)
        self.txt_product_name.setObjectName("txt_product_name")
        self.verticalLayout.addWidget(self.txt_product_name)
        self.txt_uom = QtWidgets.QLineEdit(self.lbl_inputs)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.txt_uom.setFont(font)
        self.txt_uom.setObjectName("txt_uom")
        self.verticalLayout.addWidget(self.txt_uom)
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
        AddProductWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(AddProductWindow)
        self.statusbar.setObjectName("statusbar")
        AddProductWindow.setStatusBar(self.statusbar)

        self.retranslateUi(AddProductWindow)
        QtCore.QMetaObject.connectSlotsByName(AddProductWindow)

    def retranslateUi(self, AddProductWindow):
        _translate = QtCore.QCoreApplication.translate
        AddProductWindow.setWindowTitle(_translate("AddProductWindow", "Add Product"))
        self.label_5.setText(_translate("AddProductWindow", "Add New Product"))
        self.lbl_name.setText(_translate("AddProductWindow", "Product Name"))
        self.lbl_uom.setText(_translate("AddProductWindow", "Unit of Measurement"))
        self.btn_save.setText(_translate("AddProductWindow", "SAVE"))
        self.btn_clear.setText(_translate("AddProductWindow", "CLEAR"))
        self.btn_cancel.setText(_translate("AddProductWindow", "CANCEL"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    AddProductWindow = QtWidgets.QMainWindow()
    ui = Ui_AddProductWindow()
    ui.setupUi(AddProductWindow)
    AddProductWindow.show()
    sys.exit(app.exec_())
