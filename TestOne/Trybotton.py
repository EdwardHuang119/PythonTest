# -*- coding: utf-8 -*-
import sys
import buttonTest
from buttonTest import Ui_MainWindow
from PyQt5.QtWidgets import QApplication, QMainWindow

class MyWindow(Ui_MainWindow):
   def __init__(self):
       super(MyWindow,self).__init__()
       self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    MainWindow = QMainWindow()

    ui = buttonTest.Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()
    sys.exit(app.exec_())