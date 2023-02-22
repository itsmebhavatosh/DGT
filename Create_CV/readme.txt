
    def menu_click(self,button_clicked,button1,button2,clicked_page):
        button_clicked.setStyleSheet()
        button1.setStyleSheet()
        button2.setStyleSheet()
        self.ui.main_stack.setCurrentWidget(clicked_page)
        
        self.ui.CV.clicked.connect(self.menu_click(self.ui.CV,self.ui.PD,self.ui.PE,self.ui.CV_Page))
        self.ui.PD.clicked.connect(self.menu_click(self.ui.PD, self.ui.CV, self.ui.PE))
        self.ui.PE.clicked.connect(self.menu_click(self.ui.PE, self.ui.CV, self.ui.PD))
