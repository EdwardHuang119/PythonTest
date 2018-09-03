#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
import cipsmessageanalys
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtWidgets import QFileDialog
# 如下要求导入
from cipsmodle import Ui_MainWindow


class MyMainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyMainWindow, self).__init__(parent)
        self.setupUi(self)
        self.initUI()

    # 定义槽函数开始
    def initUI(self):
        # 定义打开文件
        self.pussbutton_openfiles.clicked.connect(self.fileschoose)
        # 定义解析文件按钮的槽
        self.pushButton_analys.clicked.connect(self.analys)

    # 打开文件功能确认
    def fileschoose(self):
        filename, _ = QFileDialog.getOpenFileName(self,'Open file','./',"All Files (*);;PDF Files (*.pdf);;Text Files (*.txt)")
        if filename:
            file = open(filename)
            data = file.read()
            self.textEdit.setText(data)
            file.close()

    def analys(self):
        a = cipsmessageanalys.messageanalys(self.textEdit.toPlainText())
        messageafteranalys = a[-1]
        self.textEdit_2.setText(messageafteranalys)

        # print(a[-1])
    # def analys(self):
    #     a = self.textEdit.toPlainText()
    #     b = a +'333'
    #     self.textEdit_2.setText(b)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWin = MyMainWindow()
    myWin.show()
    sys.exit(app.exec_())