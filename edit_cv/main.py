import sys
import platform
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect,
                          QSize, QTime, QUrl, Qt, QEvent)
from PyQt5.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence,
                         QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PyQt5.QtWidgets import *
from CV_EDIT import Ui_MainWindow
from datetime import date
#from edit_popup import popup


class MainWindow(QMainWindow):
    def setlineEdit(self):
        self.ui.CV_E_M_1_W2_L16.hide()
        self.ui.CV_E_M_1_W2_RB.hide()
        self.ui.CV_E_M_1_W2_RB2.hide()

        LE_list = [self.ui.CV_E_M_1_W5_LE4,
               self.ui.CV_E_M_1_W5_LE7,
               self.ui.CV_E_M_1_W5_LE9,
               self.ui.CV_E_M_1_W4_LE5,
               self.ui.CV_E_M_1_W4_LE10,
               self.ui.CV_E_M_1_W4_LE11,
               self.ui.CV_E_M_1_W2_LE14,
               self.ui.CV_E_M_1_W2_LE16,
               self.ui.CV_E_M_1_W2_LE15,
               self.ui.CV_E_M_1_W2_LE17,
               self.ui.CV_E_M_1_W4_LE13,
               self.ui.CV_E_M_1_W4_LE12,
               self.ui.CV_E_M_1_W5_LE8,
               self.ui.CV_E_XF_TEAM_CB,
                   self.ui.CV_E_S_IO_CB,
                   self.ui.CV_E_S_ID_CB]

        for lineEdit in LE_list:
            lineEdit.setMinimumSize(16777215, 40)
    # self.ui.CV_E_XF_TEAM_CB.setMinimumSize(500, 40)
        lst2 = ['Global Network Analytics', 'Global Network Analytics WEB', 'Enterprise Data Governance']
        admin_lst=['Bhavatosh','Vishnu','Harshita','Rishita']
        self.ui.CV_E_XF_TEAM_CB.addItems(lst2)
        self.ui.CV_E_S_IO_CB.addItems(admin_lst)
        self.ui.CV_E_S_IO_CB.setCurrentIndex(-1)
        self.ui.CV_E_XF_TEAM_CB.setCurrentIndex(-1)
    def test(self,rb):
        self.ui.CV_E_DC_STACK.setCurrentWidget(rb)
        self.ui.CV_E_DC_STACK.setMaximumSize(QtCore.QSize(16777215, 200))

    def admin(self):
        master_lst=['Harshita','Rishita']
        if self.ui.CV_E_S_IO_CB.currentText() in master_lst:
            self.ui.CV_E_M_1_W2_L16.show()
            self.ui.CV_E_M_1_W2_RB.show()
            self.ui.CV_E_M_1_W2_RB2.show()

    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.showMaximized()
        self.setlineEdit()
        self.ui.CV_E_M_4_W18_RB21.clicked.connect(lambda: self.test(self.ui.CV_E_DC_EXIST_PG))
        self.ui.CV_E_M_4_W18_RB27.clicked.connect(lambda: self.test(self.ui.CV_E_DC_NEW_PG))
        self.ui.CV_E_M_4_W18_RB33.clicked.connect(lambda: self.test(self.ui.CV_E_DC_BOTH_PG))
        self.ui.CV_E_S_IO_CB.activated.connect(self.admin)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec_())
