# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\bhavatoshr\Desktop\DGT\trial_1.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(463, 347)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_MAIN = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_MAIN.setObjectName("gridLayout_MAIN")
        self.stackedWidget = QtWidgets.QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.gridLayout_PAGE1 = QtWidgets.QGridLayout(self.page)
        self.gridLayout_PAGE1.setObjectName("gridLayout_PAGE1")
        self.page_widget = QtWidgets.QWidget(self.page)
        self.page_widget.setObjectName("page_widget")
        self.gridLayout_pw1 = QtWidgets.QGridLayout(self.page_widget)
        self.gridLayout_pw1.setObjectName("gridLayout_pw1")
        self.lineEdit = QtWidgets.QLineEdit(self.page_widget)
        self.lineEdit.setObjectName("lineEdit")
        self.gridLayout_pw1.addWidget(self.lineEdit, 0, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.page_widget)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_pw1.addWidget(self.pushButton, 1, 0, 1, 1)
        self.gridLayout_PAGE1.addWidget(self.page_widget, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.gridLayout_PAGE2 = QtWidgets.QGridLayout(self.page_2)
        self.gridLayout_PAGE2.setObjectName("gridLayout_PAGE2")
        self.page2_widget = QtWidgets.QWidget(self.page_2)
        self.page2_widget.setObjectName("page2_widget")
        self.verticalLayoutpg2 = QtWidgets.QVBoxLayout(self.page2_widget)
        self.verticalLayoutpg2.setObjectName("verticalLayoutpg2")
        self.beta = QtWidgets.QLabel(self.page2_widget)
        font = QtGui.QFont()
        font.setPointSize(48)
        self.beta.setFont(font)
        self.beta.setObjectName("beta")
        self.verticalLayoutpg2.addWidget(self.beta)
        self.gridLayout_PAGE2.addWidget(self.page2_widget, 0, 0, 1, 1)
        self.stackedWidget.addWidget(self.page_2)
        self.gridLayout_MAIN.addWidget(self.stackedWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.stackedWidget.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))
        self.beta.setText(_translate("MainWindow", "Login Successfull"))
