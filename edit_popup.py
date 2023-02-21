
from PyQt5 import QtCore, QtGui, QtWidgets


class popup(object):
    def edit_popup(self, Form):
        Form.setObjectName("Form")
        Form.resize(159, 83)
        Form.setMaximumSize(QtCore.QSize(200, 100))
        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")
        self.form_main = QtWidgets.QFrame(Form)
        self.form_main.setMaximumSize(QtCore.QSize(200, 100))
        self.form_main.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.form_main.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.form_main.setFrameShadow(QtWidgets.QFrame.Raised)
        self.form_main.setObjectName("form_main")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.form_main)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.form_name = QtWidgets.QLabel(self.form_main)
        self.form_name.setMaximumSize(QtCore.QSize(200, 100))
        self.form_name.setAlignment(QtCore.Qt.AlignCenter)
        self.form_name.setObjectName("form_name")
        self.gridLayout_2.addWidget(self.form_name, 0, 0, 1, 2)
        self.form_yes = QtWidgets.QPushButton(self.form_main)
        self.form_yes.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.form_yes.setObjectName("form_yes")
        self.gridLayout_2.addWidget(self.form_yes, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.form_main)
        self.pushButton_2.setStyleSheet("background-color: rgb(197, 197, 197);")
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_2.addWidget(self.pushButton_2, 1, 1, 1, 1)
        self.gridLayout.addWidget(self.form_main, 0, 0, 1, 1)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.form_name.setText(_translate("Form", "Please Confirm to Delete the Reocord"))
        self.form_yes.setText(_translate("Form", "YES"))
        self.pushButton_2.setText(_translate("Form", "NO"))
