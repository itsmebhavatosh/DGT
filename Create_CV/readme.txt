   self.home = QtWidgets.QPushButton(self.top_menubar)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.home.sizePolicy().hasHeightForWidth())
        self.home.setSizePolicy(sizePolicy)
        self.home.setMinimumSize(QtCore.QSize(60, 0))
        self.home.setMaximumSize(QtCore.QSize(100, 16777215))
        font = QtGui.QFont()
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.home.setFont(font)
        self.home.setStyleSheet("QPushButton#home{\n"
"background-color: rgb(2, 47, 88);\n"
"color: rgb(169, 169, 169);\n"
"}\n"
"\n"
"QPushButton#home:pressed{\n"
"background-color: rgb(143, 143, 143);\n"
"\n"
"\n"
"}\n"
"QPushButton#home:hover{\n"
"background-color: rgb(63, 126, 167);\n"
"color: rgb(255, 255, 255);\n"
"}\n"
"")
        self.home.setObjectName("home")
        self.hor_cv_pd_pe.addWidget(self.home)
