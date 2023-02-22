
    def menu_click(self,button_clicked,button1,button2,clicked_page):
        button_clicked.setStyleSheet()
        button1.setStyleSheet()
        button2.setStyleSheet()
        self.ui.main_stack.setCurrentWidget(clicked_page)
