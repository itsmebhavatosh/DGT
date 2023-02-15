import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                          QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                         QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from data2 import Ui_MainWindow


class MainWindow(QMainWindow):

    def popup(self):
        error = QMessageBox()
        error.setWindowTitle("error")
        error.setText("Invalid Login")
        error.exec_()

    def button_click1(self):
        input=self.ui.lineEdit.text()
        if input=="aaa":
            self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)
        else:
            self.popup()


    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
        self.ui.b1.clicked.connect(self.button_click1)



        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
