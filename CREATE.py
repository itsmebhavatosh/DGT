# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\bhavatoshr\Desktop\DGT\CREATE.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(538, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.widget_4 = QtWidgets.QWidget(self.tab)
        self.widget_4.setObjectName("widget_4")
        self.formLayout_6 = QtWidgets.QFormLayout(self.widget_4)
        self.formLayout_6.setObjectName("formLayout_6")
        self.label_7 = QtWidgets.QLabel(self.widget_4)
        self.label_7.setObjectName("label_7")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.plainTextEdit_9 = QtWidgets.QPlainTextEdit(self.widget_4)
        self.plainTextEdit_9.setObjectName("plainTextEdit_9")
        self.formLayout_6.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit_9)
        self.label_15 = QtWidgets.QLabel(self.widget_4)
        self.label_15.setObjectName("label_15")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_15)
        self.checkBox = QtWidgets.QCheckBox(self.widget_4)
        self.checkBox.setTristate(True)
        self.checkBox.setObjectName("checkBox")
        self.formLayout_6.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.checkBox)
        self.label_16 = QtWidgets.QLabel(self.widget_4)
        self.label_16.setObjectName("label_16")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_16)
        self.plainTextEdit_10 = QtWidgets.QPlainTextEdit(self.widget_4)
        self.plainTextEdit_10.setObjectName("plainTextEdit_10")
        self.formLayout_6.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit_10)
        self.gridLayout_2.addWidget(self.widget_4, 2, 1, 1, 1)
        self.widget = QtWidgets.QWidget(self.tab)
        self.widget.setObjectName("widget")
        self.formLayout_4 = QtWidgets.QFormLayout(self.widget)
        self.formLayout_4.setObjectName("formLayout_4")
        self.label_4 = QtWidgets.QLabel(self.widget)
        self.label_4.setObjectName("label_4")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.plainTextEdit_3 = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit_3.setObjectName("plainTextEdit_3")
        self.formLayout_4.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit_3)
        self.label_10 = QtWidgets.QLabel(self.widget)
        self.label_10.setObjectName("label_10")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.plainTextEdit_4 = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit_4.setObjectName("plainTextEdit_4")
        self.formLayout_4.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit_4)
        self.label_11 = QtWidgets.QLabel(self.widget)
        self.label_11.setObjectName("label_11")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.plainTextEdit_5 = QtWidgets.QPlainTextEdit(self.widget)
        self.plainTextEdit_5.setObjectName("plainTextEdit_5")
        self.formLayout_4.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit_5)
        self.gridLayout_2.addWidget(self.widget, 0, 1, 1, 1)
        self.frame_2 = QtWidgets.QFrame(self.tab)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.formLayout_3 = QtWidgets.QFormLayout(self.frame_2)
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setObjectName("label_3")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.frame_2)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit)
        self.label_8 = QtWidgets.QLabel(self.frame_2)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.plainTextEdit_2 = QtWidgets.QPlainTextEdit(self.frame_2)
        self.plainTextEdit_2.setObjectName("plainTextEdit_2")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit_2)
        self.label_9 = QtWidgets.QLabel(self.frame_2)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.textEdit = QtWidgets.QTextEdit(self.frame_2)
        self.textEdit.setObjectName("textEdit")
        self.formLayout_3.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.textEdit)
        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 1)
        self.widget_2 = QtWidgets.QWidget(self.tab)
        self.widget_2.setObjectName("widget_2")
        self.formLayout_7 = QtWidgets.QFormLayout(self.widget_2)
        self.formLayout_7.setObjectName("formLayout_7")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setObjectName("label_5")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.plainTextEdit_6 = QtWidgets.QPlainTextEdit(self.widget_2)
        self.plainTextEdit_6.setObjectName("plainTextEdit_6")
        self.formLayout_7.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit_6)
        self.label_12 = QtWidgets.QLabel(self.widget_2)
        self.label_12.setObjectName("label_12")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_12)
        self.textEdit_2 = QtWidgets.QTextEdit(self.widget_2)
        self.textEdit_2.setObjectName("textEdit_2")
        self.formLayout_7.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.textEdit_2)
        self.gridLayout_2.addWidget(self.widget_2, 1, 0, 1, 2)
        self.widget_3 = QtWidgets.QWidget(self.tab)
        self.widget_3.setObjectName("widget_3")
        self.formLayout_5 = QtWidgets.QFormLayout(self.widget_3)
        self.formLayout_5.setObjectName("formLayout_5")
        self.label_6 = QtWidgets.QLabel(self.widget_3)
        self.label_6.setObjectName("label_6")
        self.formLayout_5.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_13 = QtWidgets.QLabel(self.widget_3)
        self.label_13.setObjectName("label_13")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_13)
        self.plainTextEdit_7 = QtWidgets.QPlainTextEdit(self.widget_3)
        self.plainTextEdit_7.setObjectName("plainTextEdit_7")
        self.formLayout_5.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit_7)
        self.label_14 = QtWidgets.QLabel(self.widget_3)
        self.label_14.setObjectName("label_14")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_14)
        self.plainTextEdit_8 = QtWidgets.QPlainTextEdit(self.widget_3)
        self.plainTextEdit_8.setObjectName("plainTextEdit_8")
        self.formLayout_5.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit_8)
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.radioButton = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton.setObjectName("radioButton")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.radioButton)
        self.radioButton_2 = QtWidgets.QRadioButton(self.widget_3)
        self.radioButton_2.setObjectName("radioButton_2")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.radioButton_2)
        self.formLayout_5.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.formLayout)
        self.gridLayout_2.addWidget(self.widget_3, 2, 0, 1, 1)
        self.pushButton = QtWidgets.QPushButton(self.tab)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout_2.addWidget(self.pushButton, 3, 0, 1, 2)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.tabWidget.addTab(self.tab_2, "")
        self.gridLayout.addWidget(self.tabWidget, 3, 0, 1, 4)
        self.frame_6 = QtWidgets.QFrame(self.centralwidget)
        self.frame_6.setMinimumSize(QtCore.QSize(0, 50))
        self.frame_6.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_6.setObjectName("frame_6")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_2 = QtWidgets.QLabel(self.frame_6)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.gridLayout.addWidget(self.frame_6, 1, 1, 1, 3)
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout.addWidget(self.frame, 0, 1, 1, 1)
        self.frame_5 = QtWidgets.QFrame(self.centralwidget)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 20))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.gridLayout.addWidget(self.frame_5, 2, 0, 1, 4)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setMinimumSize(QtCore.QSize(20, 40))
        self.label.setMaximumSize(QtCore.QSize(100, 16777215))
        self.label.setStyleSheet("image: url(:/newPrefix/discover.png);\n"
"background-color: rgb(255, 255, 255);\n"
"")
        self.label.setText("")
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 2, 1)
        self.frame_3 = QtWidgets.QFrame(self.centralwidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.gridLayout.addWidget(self.frame_3, 4, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_7.setText(_translate("MainWindow", "TextLabel"))
        self.label_15.setText(_translate("MainWindow", "Has this CV been acknowledged by GNA"))
        self.checkBox.setText(_translate("MainWindow", "CheckBox"))
        self.label_16.setText(_translate("MainWindow", "TextLabel"))
        self.label_4.setText(_translate("MainWindow", "Approval Date"))
        self.label_10.setText(_translate("MainWindow", "Date Submitted"))
        self.label_11.setText(_translate("MainWindow", "CV ID"))
        self.label_3.setText(_translate("MainWindow", "GNA CV ID"))
        self.label_8.setText(_translate("MainWindow", "CV Initiator Owner"))
        self.label_9.setText(_translate("MainWindow", "XF Lead"))
        self.label_5.setText(_translate("MainWindow", "CV Description"))
        self.label_12.setText(_translate("MainWindow", "Priority Number"))
        self.label_6.setText(_translate("MainWindow", "DN/DCI Indicator"))
        self.label_13.setText(_translate("MainWindow", "TextLabel"))
        self.label_14.setText(_translate("MainWindow", "TextLabel"))
        self.radioButton.setText(_translate("MainWindow", "DN"))
        self.radioButton_2.setText(_translate("MainWindow", "DCI"))
        self.pushButton.setText(_translate("MainWindow", "Submit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "CREATE"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "EDIT"))
        self.label_2.setText(_translate("MainWindow", "Data Governance Tool"))
import logo_rc