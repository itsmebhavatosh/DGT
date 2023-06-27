# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\bhavatoshr\Desktop\DGT\Finals\Homepage_PE.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(486, 342)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Home_main = QtWidgets.QWidget(self.centralwidget)
        self.Home_main.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Home_main.setObjectName("Home_main")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Home_main)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Home_main_1 = QtWidgets.QLabel(self.Home_main)
        self.Home_main_1.setMinimumSize(QtCore.QSize(0, 80))
        font = QtGui.QFont()
        font.setPointSize(24)
        font.setBold(True)
        font.setWeight(75)
        self.Home_main_1.setFont(font)
        self.Home_main_1.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.Home_main_1.setObjectName("Home_main_1")
        self.verticalLayout.addWidget(self.Home_main_1, 0, QtCore.Qt.AlignHCenter)
        self.textBrowser = QtWidgets.QTextBrowser(self.Home_main)
        self.textBrowser.setMinimumSize(QtCore.QSize(0, 150))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.textBrowser.setFont(font)
        self.textBrowser.setObjectName("textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)
        self.horizontalLayout.addWidget(self.Home_main)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Home_main_1.setText(_translate("MainWindow", "Planning Execution"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri 53\'; font-size:16pt; color:#1f1f1f;\">Planning Execution(PE) Stage of the tool will focus more on Data Quality, Data Lineage &amp; Data Classification.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri 53\'; font-size:16pt; color:#1f1f1f;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri 53\'; font-size:16pt; color:#1f1f1f;\">This phase of the tool is driven by the JIRA ID of the initiative. Details captured in this stage will be at the </span><span style=\" font-family:\'Calibri 53\'; font-size:16pt; font-weight:600; color:#1f1f1f;\">most granular </span><span style=\" font-family:\'Calibri 53\'; font-size:16pt; color:#1f1f1f;\">level of data impact.</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Calibri 53\'; font-size:16pt; color:#1f1f1f;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri 53\'; font-size:16pt; color:#1f1f1f;\">The data changes (new &amp; existing) will be captured using the templates </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:16pt; color:#1f1f1f;\">• </span><span style=\" font-family:\'Calibri 53\'; font-size:16pt; font-weight:600; color:#1f1f1f;\">Technical Dataset Registry: </span><span style=\" font-family:\'Calibri 53\'; font-size:16pt; color:#1f1f1f;\">Documents the data changes down to table, file and column level. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:16pt; color:#1f1f1f;\">• </span><span style=\" font-family:\'Calibri 53\'; font-size:16pt; font-weight:600; color:#1f1f1f;\">Enterprise Data Glossary: </span><span style=\" font-family:\'Calibri 53\'; font-size:16pt; color:#1f1f1f;\">Defines the business terms and ownership for the data changes. </span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:16pt; color:#1f1f1f;\">• </span><span style=\" font-family:\'Calibri 53\'; font-size:16pt; font-weight:600; color:#1f1f1f;\">Data Quality Rules: </span><span style=\" font-family:\'Calibri 53\'; font-size:16pt; color:#1f1f1f;\">Documents data quality rules to be implement for Critical Data Elements(CDEs).</span><span style=\" font-size:16pt;\"> </span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Calibri 53\'; font-size:16pt; color:#000000;\">As a part of workflow, Business, BT architects, Cross Functional teams, BT DNA will have an option to approve/acknowledge.</span><span style=\" font-size:16pt;\"> </span></p></body></html>"))
