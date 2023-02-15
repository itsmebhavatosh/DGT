

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 600)
        ############################################
        self.menu_main = QtWidgets.QWidget(MainWindow)
        self.menu_main.setObjectName("menu_main")
        self.menu_ver_lay = QtWidgets.QVBoxLayout(self.menu_main)
        self.menu_ver_lay.setObjectName("menu_ver_lay")
        self.title_widg = QtWidgets.QWidget(self.menu_main)
        self.title_widg.setMinimumSize(QtCore.QSize(0, 100))
        self.title_widg.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.title_widg.setObjectName("title_widg")
        self.grid_title_lay = QtWidgets.QGridLayout(self.title_widg)
        self.grid_title_lay.setObjectName("grid_title_lay")
        self.label_title = QtWidgets.QLabel(self.title_widg)
        font = QtGui.QFont()
        font.setPointSize(26)
        font.setBold(True)
        font.setWeight(75)
        self.label_title.setFont(font)
        self.label_title.setAlignment(QtCore.Qt.AlignCenter)
        self.label_title.setObjectName("label_title")
        self.grid_title_lay.addWidget(self.label_title, 0, 0, 1, 1)
        self.menu_ver_lay.addWidget(self.title_widg)
        self.widget_body = QtWidgets.QWidget(self.menu_main)
        self.widget_body.setMinimumSize(QtCore.QSize(0, 250))
        self.widget_body.setObjectName("widget_body")
        self.body_ver_lay = QtWidgets.QVBoxLayout(self.widget_body)
        self.body_ver_lay.setContentsMargins(0, 0, 0, 0)
        self.body_ver_lay.setSpacing(0)
        self.body_ver_lay.setObjectName("body_ver_lay")
        self.top_menubar = QtWidgets.QWidget(self.widget_body)
        self.top_menubar.setMinimumSize(QtCore.QSize(0, 40))
        self.top_menubar.setMaximumSize(QtCore.QSize(16777215, 80))
        self.top_menubar.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.top_menubar.setObjectName("top_menubar")
        self.hor_cv_pd_pe = QtWidgets.QHBoxLayout(self.top_menubar)
        self.hor_cv_pd_pe.setContentsMargins(6, 0, 6, 0)
        self.hor_cv_pd_pe.setSpacing(0)
        self.hor_cv_pd_pe.setObjectName("hor_cv_pd_pe")
        self.blankframe = QtWidgets.QFrame(self.top_menubar)
        self.blankframe.setMinimumSize(QtCore.QSize(40, 0))
        self.blankframe.setMaximumSize(QtCore.QSize(70, 16777215))
        self.blankframe.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.blankframe.setFrameShadow(QtWidgets.QFrame.Raised)
        self.blankframe.setObjectName("blankframe")
        self.hor_cv_pd_pe.addWidget(self.blankframe)
        self.CV = QtWidgets.QPushButton(self.top_menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.CV.sizePolicy().hasHeightForWidth())
        self.CV.setSizePolicy(sizePolicy)
        self.CV.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.CV.setFont(font)
        self.CV.setStyleSheet("QPushButton#CV{\n"
"background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton#CV:pressed{\n"
"background-color: rgb(143, 143, 143);\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"QPushButton#CV:hover{\n"
"background-color: rgb(143, 143, 143);\n"
"\n"
"}")
        self.CV.setCheckable(False)
        self.CV.setChecked(False)
        self.CV.setAutoRepeat(False)
        self.CV.setObjectName("CV")
        self.hor_cv_pd_pe.addWidget(self.CV)
        self.PD = QtWidgets.QPushButton(self.top_menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PD.sizePolicy().hasHeightForWidth())
        self.PD.setSizePolicy(sizePolicy)
        self.PD.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PD.setFont(font)
        self.PD.setStyleSheet("QPushButton#PD{\n"
"background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton#PD:pressed{\n"
"background-color: rgb(143, 143, 143);\n"
"\n"
"}\n"
"QPushButton#PD:hover{\n"
"background-color: rgb(143, 143, 143);\n"
"\n"
"}")
        self.PD.setObjectName("PD")
        self.hor_cv_pd_pe.addWidget(self.PD)
        self.PE = QtWidgets.QPushButton(self.top_menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.PE.sizePolicy().hasHeightForWidth())
        self.PE.setSizePolicy(sizePolicy)
        self.PE.setMinimumSize(QtCore.QSize(0, 40))
        self.PE.setMaximumSize(QtCore.QSize(16777215, 16777215))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.PE.setFont(font)
        self.PE.setStyleSheet("QPushButton#PE{\n"
"background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton#PE:pressed{\n"
"background-color: rgb(143, 143, 143);\n"
"}\n"
"QPushButton#PE:hover{\n"
"background-color: rgb(143, 143, 143);\n"
"\n"
"}")
        self.PE.setCheckable(False)
        self.PE.setObjectName("PE")
        self.hor_cv_pd_pe.addWidget(self.PE)
        self.body_ver_lay.addWidget(self.top_menubar)
        self.widget_body_inner = QtWidgets.QWidget(self.widget_body)
        self.widget_body_inner.setMinimumSize(QtCore.QSize(0, 250))
        self.widget_body_inner.setObjectName("widget_body_inner")
        self.verticalLayout_wbi = QtWidgets.QVBoxLayout(self.widget_body_inner)
        self.verticalLayout_wbi.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_wbi.setSpacing(0)
        self.verticalLayout_wbi.setObjectName("verticalLayout_wbi")
        self.main_stack = QtWidgets.QStackedWidget(self.widget_body_inner)
        self.main_stack.setObjectName("main_stack")
        self.CV_Page = QtWidgets.QWidget()
        self.CV_Page.setStyleSheet("background-color: rgb(143, 143, 143);\n"
"")
        self.CV_Page.setObjectName("CV_Page")
        self.CV_page_VER_lay = QtWidgets.QVBoxLayout(self.CV_Page)
        self.CV_page_VER_lay.setContentsMargins(-1, 0, -1, 0)
        self.CV_page_VER_lay.setSpacing(0)
        self.CV_page_VER_lay.setObjectName("CV_page_VER_lay")
        self.cv_main = QtWidgets.QWidget(self.CV_Page)
        self.cv_main.setObjectName("cv_main")
        self.cv_main_hor_lay = QtWidgets.QHBoxLayout(self.cv_main)
        self.cv_main_hor_lay.setContentsMargins(0, -1, 0, -1)
        self.cv_main_hor_lay.setSpacing(0)
        self.cv_main_hor_lay.setObjectName("cv_main_hor_lay")
        self.cv_menu_side = QtWidgets.QWidget(self.cv_main)
        self.cv_menu_side.setMinimumSize(QtCore.QSize(50, 0))
        self.cv_menu_side.setMaximumSize(QtCore.QSize(100, 16777215))
        self.cv_menu_side.setStyleSheet("background-color: rgb(0,0,0);")
        self.cv_menu_side.setObjectName("cv_menu_side")
        self.cv_menu_side_ver_lay = QtWidgets.QVBoxLayout(self.cv_menu_side)
        self.cv_menu_side_ver_lay.setContentsMargins(0, 0, 0, 0)
        self.cv_menu_side_ver_lay.setSpacing(0)
        self.cv_menu_side_ver_lay.setObjectName("cv_menu_side_ver_lay")
        self.cv_buttons = QtWidgets.QFrame(self.cv_menu_side)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cv_buttons.sizePolicy().hasHeightForWidth())
        self.cv_buttons.setSizePolicy(sizePolicy)
        self.cv_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.cv_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.cv_buttons.setObjectName("cv_buttons")
        self.cv_butt_ver_lay = QtWidgets.QVBoxLayout(self.cv_buttons)
        self.cv_butt_ver_lay.setContentsMargins(0, 0, 0, 0)
        self.cv_butt_ver_lay.setSpacing(0)
        self.cv_butt_ver_lay.setObjectName("cv_butt_ver_lay")
        self.create = QtWidgets.QPushButton(self.cv_buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.create.sizePolicy().hasHeightForWidth())
        self.create.setSizePolicy(sizePolicy)
        self.create.setMinimumSize(QtCore.QSize(0, 30))
        self.create.setStyleSheet("QPushButton#create{\n"
"background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton#create:pressed{\n"
"background-color: rgb(143, 143, 143);\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"QPushButton#create:hover{\n"
"background-color: rgb(143, 143, 143);\n"
"\n"
"}")
        self.create.setObjectName("create")
        self.cv_butt_ver_lay.addWidget(self.create)
        self.edit = QtWidgets.QPushButton(self.cv_buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.edit.sizePolicy().hasHeightForWidth())
        self.edit.setSizePolicy(sizePolicy)
        self.edit.setMinimumSize(QtCore.QSize(0, 30))
        self.edit.setStyleSheet("QPushButton#edit{\n"
"background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton#edit:pressed{\n"
"background-color: rgb(143, 143, 143);\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"QPushButton#edit:hover{\n"
"background-color: rgb(143, 143, 143);\n"
"\n"
"}")
        self.edit.setObjectName("edit")
        self.cv_butt_ver_lay.addWidget(self.edit)
        self.delete_2 = QtWidgets.QPushButton(self.cv_buttons)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.delete_2.sizePolicy().hasHeightForWidth())
        self.delete_2.setSizePolicy(sizePolicy)
        self.delete_2.setMinimumSize(QtCore.QSize(0, 30))
        self.delete_2.setStyleSheet("QPushButton#delete_2{\n"
"background-color: rgb(0, 0, 0);\n"
"color:rgb(255, 255, 255);\n"
"}\n"
"QPushButton#delete_2:pressed{\n"
"background-color: rgb(143, 143, 143);\n"
"    font: 75 10pt \"MS Shell Dlg 2\";\n"
"\n"
"}\n"
"QPushButton#delete_2:hover{\n"
"background-color: rgb(143, 143, 143);\n"
"\n"
"}")
        self.delete_2.setObjectName("delete_2")
        self.cv_butt_ver_lay.addWidget(self.delete_2)
        self.cv_menu_side_ver_lay.addWidget(self.cv_buttons, 0, QtCore.Qt.AlignTop)
        self.cv_main_hor_lay.addWidget(self.cv_menu_side)
        self.ced_widget = QtWidgets.QWidget(self.cv_main)
        self.ced_widget.setMinimumSize(QtCore.QSize(400, 0))
        self.ced_widget.setObjectName("ced_widget")
        self.gridLayout_ced = QtWidgets.QGridLayout(self.ced_widget)
        self.gridLayout_ced.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_ced.setSpacing(0)
        self.gridLayout_ced.setObjectName("gridLayout_ced")
        self.CV_Stack = QtWidgets.QStackedWidget(self.ced_widget)
        self.CV_Stack.setObjectName("CV_Stack")
        self.CV_CREATE_PG = QtWidgets.QWidget()
        self.CV_CREATE_PG.setStyleSheet("background-color: rgb(255,255,255);")
        self.CV_CREATE_PG.setObjectName("CV_CREATE_PG")
        self.ver_laycv_create = QtWidgets.QVBoxLayout(self.CV_CREATE_PG)
        self.ver_laycv_create.setObjectName("ver_laycv_create")
        self.scrollArea = QtWidgets.QScrollArea(self.CV_CREATE_PG)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrol_cv_create = QtWidgets.QWidget()
        self.scrol_cv_create.setGeometry(QtCore.QRect(0, -27, 433, 273))
        self.scrol_cv_create.setObjectName("scrol_cv_create")
        self.scroll_cv_c_grid = QtWidgets.QGridLayout(self.scrol_cv_create)
        self.scroll_cv_c_grid.setContentsMargins(6, -1, 10, 10)
        self.scroll_cv_c_grid.setObjectName("scroll_cv_c_grid")
        self.cv_c3 = QtWidgets.QWidget(self.scrol_cv_create)
        self.cv_c3.setObjectName("cv_c3")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.cv_c3)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.DNDCIIND = QtWidgets.QLabel(self.cv_c3)
        self.DNDCIIND.setObjectName("DNDCIIND")
        self.horizontalLayout.addWidget(self.DNDCIIND)
        self.radioButton_3 = QtWidgets.QRadioButton(self.cv_c3)
        self.radioButton_3.setObjectName("radioButton_3")
        self.horizontalLayout.addWidget(self.radioButton_3)
        self.radioButton_2 = QtWidgets.QRadioButton(self.cv_c3)
        self.radioButton_2.setObjectName("radioButton_2")
        self.horizontalLayout.addWidget(self.radioButton_2)
        self.radioButton = QtWidgets.QRadioButton(self.cv_c3)
        self.radioButton.setObjectName("radioButton")
        self.horizontalLayout.addWidget(self.radioButton)
        self.scroll_cv_c_grid.addWidget(self.cv_c3, 2, 0, 1, 1)
        self.cv_c5 = QtWidgets.QWidget(self.scrol_cv_create)
        self.cv_c5.setObjectName("cv_c5")
        self.cv_c_form = QtWidgets.QFormLayout(self.cv_c5)
        self.cv_c_form.setObjectName("cv_c_form")
        self.label_11 = QtWidgets.QLabel(self.cv_c5)
        self.label_11.setObjectName("label_11")
        self.cv_c_form.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_11)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(self.cv_c5)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.cv_c_form.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.plainTextEdit)
        self.scroll_cv_c_grid.addWidget(self.cv_c5, 1, 0, 1, 2)
        self.submit_wid = QtWidgets.QWidget(self.scrol_cv_create)
        self.submit_wid.setObjectName("submit_wid")
        self.submit_lay = QtWidgets.QGridLayout(self.submit_wid)
        self.submit_lay.setObjectName("submit_lay")
        self.sbmit_CV_C = QtWidgets.QPushButton(self.submit_wid)
        self.sbmit_CV_C.setObjectName("sbmit_CV_C")
        self.submit_lay.addWidget(self.sbmit_CV_C, 0, 1, 1, 1)
        self.s_frame = QtWidgets.QFrame(self.submit_wid)
        self.s_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.s_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.s_frame.setObjectName("s_frame")
        self.submit_lay.addWidget(self.s_frame, 0, 0, 1, 1)
        self.s_frane = QtWidgets.QFrame(self.submit_wid)
        self.s_frane.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.s_frane.setFrameShadow(QtWidgets.QFrame.Raised)
        self.s_frane.setObjectName("s_frane")
        self.submit_lay.addWidget(self.s_frane, 0, 2, 1, 1)
        self.scroll_cv_c_grid.addWidget(self.submit_wid, 4, 0, 1, 2)
        self.cv_c2 = QtWidgets.QWidget(self.scrol_cv_create)
        self.cv_c2.setObjectName("cv_c2")
        self.formLayout_2 = QtWidgets.QFormLayout(self.cv_c2)
        self.formLayout_2.setObjectName("formLayout_2")
        self.Approval_date = QtWidgets.QLabel(self.cv_c2)
        self.Approval_date.setObjectName("Approval_date")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Approval_date)
        self.lineEdit_5 = QtWidgets.QLineEdit(self.cv_c2)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.lineEdit_5)
        self.label_8 = QtWidgets.QLabel(self.cv_c2)
        self.label_8.setObjectName("label_8")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.lineEdit_6 = QtWidgets.QLineEdit(self.cv_c2)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_6)
        self.label_9 = QtWidgets.QLabel(self.cv_c2)
        self.label_9.setObjectName("label_9")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.cv_c2)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.formLayout_2.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_7)
        self.label_10 = QtWidgets.QLabel(self.cv_c2)
        self.label_10.setObjectName("label_10")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_10)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.cv_c2)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.formLayout_2.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_8)
        self.scroll_cv_c_grid.addWidget(self.cv_c2, 0, 1, 1, 1)
        self.cv_c1 = QtWidgets.QWidget(self.scrol_cv_create)
        self.cv_c1.setObjectName("cv_c1")
        self.C = QtWidgets.QFormLayout(self.cv_c1)
        self.C.setObjectName("C")
        self.label_5 = QtWidgets.QLabel(self.cv_c1)
        self.label_5.setObjectName("label_5")
        self.C.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.cv_c1)
        self.label_6.setObjectName("label_6")
        self.C.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.gna_cv_e = QtWidgets.QLineEdit(self.cv_c1)
        self.gna_cv_e.setObjectName("gna_cv_e")
        self.C.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.gna_cv_e)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.cv_c1)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.C.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.cv_c1)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.C.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.lineEdit_3)
        self.label_7 = QtWidgets.QLabel(self.cv_c1)
        self.label_7.setObjectName("label_7")
        self.C.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.cv_c1)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.C.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.lineEdit_4)
        self.Gna_cv_ID = QtWidgets.QLabel(self.cv_c1)
        self.Gna_cv_ID.setObjectName("Gna_cv_ID")
        self.C.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.Gna_cv_ID)
        self.scroll_cv_c_grid.addWidget(self.cv_c1, 0, 0, 1, 1)
        self.cv_c4 = QtWidgets.QWidget(self.scrol_cv_create)
        self.cv_c4.setObjectName("cv_c4")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.cv_c4)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_4 = QtWidgets.QLabel(self.cv_c4)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_2.addWidget(self.label_4)
        self.radioButton_5 = QtWidgets.QRadioButton(self.cv_c4)
        self.radioButton_5.setObjectName("radioButton_5")
        self.horizontalLayout_2.addWidget(self.radioButton_5)
        self.radioButton_4 = QtWidgets.QRadioButton(self.cv_c4)
        self.radioButton_4.setObjectName("radioButton_4")
        self.horizontalLayout_2.addWidget(self.radioButton_4)
        self.scroll_cv_c_grid.addWidget(self.cv_c4, 2, 1, 1, 1)
        self.spacer = QtWidgets.QFrame(self.scrol_cv_create)
        self.spacer.setMinimumSize(QtCore.QSize(0, 20))
        self.spacer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.spacer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.spacer.setObjectName("spacer")
        self.scroll_cv_c_grid.addWidget(self.spacer, 3, 0, 1, 2)
        self.scrollArea.setWidget(self.scrol_cv_create)
        self.ver_laycv_create.addWidget(self.scrollArea)
        self.CV_Stack.addWidget(self.CV_CREATE_PG)
        self.CV_EDIT_PG = QtWidgets.QWidget()
        self.CV_EDIT_PG.setObjectName("CV_EDIT_PG")
        self.CV_Stack.addWidget(self.CV_EDIT_PG)
        self.CV_DELETE_PG = QtWidgets.QWidget()
        self.CV_DELETE_PG.setObjectName("CV_DELETE_PG")
        self.CV_Stack.addWidget(self.CV_DELETE_PG)
        self.gridLayout_ced.addWidget(self.CV_Stack, 0, 0, 1, 1)
        self.cv_main_hor_lay.addWidget(self.ced_widget)
        self.CV_page_VER_lay.addWidget(self.cv_main)
        self.main_stack.addWidget(self.CV_Page)
        self.PD_PAGE = QtWidgets.QWidget()
        self.PD_PAGE.setObjectName("PD_PAGE")
        self.gridLayout = QtWidgets.QGridLayout(self.PD_PAGE)
        self.gridLayout.setObjectName("gridLayout")
        self.main_stack.addWidget(self.PD_PAGE)
        self.PE_PAGE = QtWidgets.QWidget()
        self.PE_PAGE.setObjectName("PE_PAGE")
        self.main_stack.addWidget(self.PE_PAGE)
        self.verticalLayout_wbi.addWidget(self.main_stack)
        self.footer = QtWidgets.QFrame(self.widget_body_inner)
        self.footer.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.footer.setFrameShadow(QtWidgets.QFrame.Raised)
        self.footer.setObjectName("footer")
        self.verticalLayout_wbi.addWidget(self.footer)
        self.body_ver_lay.addWidget(self.widget_body_inner)
        self.menu_ver_lay.addWidget(self.widget_body)
        MainWindow.setCentralWidget(self.menu_main)

        self.retranslateUi(MainWindow)
        self.main_stack.setCurrentIndex(0)
        self.CV_Stack.setCurrentIndex(0)

        ##############################################
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label_title.setText(_translate("MainWindow", "Data Governance Tool"))
        self.CV.setText(_translate("MainWindow", "CV"))
        self.PD.setText(_translate("MainWindow", "PD"))
        self.PE.setText(_translate("MainWindow", "PE"))
        self.create.setText(_translate("MainWindow", "Create"))
        self.edit.setText(_translate("MainWindow", "Edit"))
        self.delete_2.setText(_translate("MainWindow", "Delete"))
        self.DNDCIIND.setText(_translate("MainWindow", "DN/DCI Indicator"))
        self.radioButton_3.setText(_translate("MainWindow", "DN"))
        self.radioButton_2.setText(_translate("MainWindow", "DCI"))
        self.radioButton.setText(_translate("MainWindow", "Both"))
        self.label_11.setText(_translate("MainWindow", "CV Description"))
        self.sbmit_CV_C.setText(_translate("MainWindow", "Submit"))
        self.Approval_date.setText(_translate("MainWindow", "Approval Date"))
        self.label_8.setText(_translate("MainWindow", "Date Submitted"))
        self.label_9.setText(_translate("MainWindow", "XF Team"))
        self.label_10.setText(_translate("MainWindow", "PMO Contact"))
        self.label_5.setText(_translate("MainWindow", "CV Initiator Owner"))
        self.label_6.setText(_translate("MainWindow", "XF Lead"))
        self.label_7.setText(_translate("MainWindow", "Priority No"))
        self.Gna_cv_ID.setText(_translate("MainWindow", "Gna CV ID"))
        self.label_4.setText(_translate("MainWindow", "Data Impact"))
        self.radioButton_5.setText(_translate("MainWindow", "Yes"))
        self.radioButton_4.setText(_translate("MainWindow", "No"))