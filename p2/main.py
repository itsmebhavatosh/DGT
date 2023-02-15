import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                          QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                         QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from mainpage import Ui_MainWindow


class MainWindow(QMainWindow):

    def button_click1(self):
        self.ui.CV.setStyleSheet("QPushButton { background-color: rgb(143,143,143);font: 20pt}")
        self.ui.PD.setStyleSheet("QPushButton { background-color: rgb(0, 0, 0); color:rgb(255, 255, 255)}")
        self.ui.PE.setStyleSheet("QPushButton { background-color: rgb(0, 0, 0); color:rgb(255, 255, 255)}")
        self.ui.main_stack.setCurrentWidget(self.ui.CV_Page)
    def button_click2(self):
        self.ui.PD.setStyleSheet("QPushButton { background-color: rgb(143,143,143);font: 20pt}")
        self.ui.CV.setStyleSheet("QPushButton { background-color: rgb(0, 0, 0);color:rgb(255, 255, 255)}")
        self.ui.PE.setStyleSheet("QPushButton { background-color: rgb(0, 0, 0);color:rgb(255, 255, 255)}")
        self.ui.main_stack.setCurrentWidget(self.ui.PD_PAGE)
    def button_click3(self):
        self.ui.PE.setStyleSheet("QPushButton { background-color: rgb(143,143,143);font: 20pt}")
        self.ui.CV.setStyleSheet("QPushButton { background-color: rgb(0, 0, 0);color:rgb(255, 255, 255)}")
        self.ui.PD.setStyleSheet("QPushButton { background-color: rgb(0, 0, 0);color:rgb(255, 255, 255)}")
        self.ui.main_stack.setCurrentWidget(self.ui.PE_PAGE)

    def CV_Create_click(self):
        self.ui.create.setStyleSheet("QPushButton { background-color: rgb(255,255,255);font: 75 10pt;}")
        self.ui.edit.setStyleSheet("QPushButton { background-color: rgb(0,0,0); color:rgb(255, 255, 255)}")
        self.ui.CV_Stack.setCurrentWidget(self.ui.CV_CREATE_PG)

    def CV_Edit_click(self):
        self.ui.edit.setStyleSheet("QPushButton { background-color: rgb(255,255,255)}")
        self.ui.create.setStyleSheet("QPushButton { background-color: rgb(0,0,0); color:rgb(255, 255, 255)}")
        self.ui.CV_Stack.setCurrentWidget(self.ui.CV_EDIT_PG)
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.main_stack.setCurrentWidget(self.ui.PD_PAGE)
        self.ui.CV_Stack.setCurrentWidget(self.ui.CV_EDIT_PG)
        self.ui.CV.clicked.connect(self.button_click1)
        self.ui.PD.clicked.connect(self.button_click2)
        self.ui.PE.clicked.connect(self.button_click3)
        self.ui.create.clicked.connect(self.CV_Create_click)
        self.ui.edit.clicked.connect(self.CV_Edit_click)


        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
