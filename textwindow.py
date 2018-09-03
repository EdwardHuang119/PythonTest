# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'textwindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import os
from PyQt5.QtWidgets import QFileDialog
# from PyQt5 import *

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.cwd = os.getcwd()  # 获取当前程序文件位置
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(200, 30, 296, 417))
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.gridLayout = QtWidgets.QGridLayout(self.frame)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout.addWidget(self.pushButton_2, 5, 0, 1, 2)
        self.pushButton_4 = QtWidgets.QPushButton(self.frame)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 7, 0, 1, 2)
        self.pushButton_3 = QtWidgets.QPushButton(self.frame)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 6, 0, 1, 2)
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.frame)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 4, 0, 1, 2)
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setObjectName("pushButton")
        self.gridLayout.addWidget(self.pushButton, 3, 0, 1, 2)
        self.textEdit = QtWidgets.QTextEdit(self.frame)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 1, 0, 1, 2)
        self.pushButton_6 = QtWidgets.QPushButton(self.frame)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 2, 0, 1, 2)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        # 逐步开始定义槽相关内容
        self.pushButton_6.clicked.connect(MainWindow.close)
        # 内建槽函数，关闭对话框
        # 如下开始自行书写需要自定义的槽函数
        self.pushButton.clicked.connect(self.showtxt)
        self.pushButton_5.clicked.connect(self.showxml)
        self.pushButton_3.clicked.connect(self.fileschoose)
        self.pushButton_2.clicked.connect(self.cleartxt)
        self.pushButton_4.clicked.connect(self.filesave)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # 定义各种槽函数
    # 定义最基本的展现内容按钮
    def showtxt(self):
        self.textEdit.setPlainText("Hello PyQt5!\n点击按钮")
    # 定义基本展现Xml格式的按钮
    def showxml(self):
        self.textEdit.setHtml("<font color='red' size='6'><red>Hello PyQt5!\n点击按钮。</font>")

    # 展示一个打开文档并展现在某个对话框的按钮
    # 尝试定义起始路径
    def fileschoose(self):
        filename, _ = QFileDialog.getOpenFileName(self,'Open file','C:/Users/Edward & Bella/Documents',"All Files (*);;PDF Files (*.pdf);;Text Files (*.txt)")
        if filename:
            file = open(filename)
            data = file.read()
            self.textEdit.setText(data)
            file.close()
            # 打印内容
            print(data)
            # 打印路径
            print(filename)
            # print(os.path.expandvars('$HOME'))

    # 基本的清空对话框按钮
    def cleartxt(self):
        self.textEdit.setPlainText("")

    def filesave(self):
        filenamesave, _ = QFileDialog.getSaveFileName(self, 'Save file', './',"All Files (*);;Text Files (*.txt)")
        mytest =self.textEdit.toPlainText()
        if filenamesave:
            file = open(filenamesave,"w+")
            file.write(mytest)
            file.close()
            QtWidgets.QMessageBox.information(self, "MessageBox", "保存成功。Oh yeah!!")


    def filesavemyself(self):
        filenamemyself,_ = QFileDialog.getSaveFileName(self, 'Save file', './',"All Files (*);;Text Files (*.txt)")
        mytest =self.textEdit.toPlainText()
        if filenamemyself:
            file = open(filenamemyself,"w+")
            file.write(mytest)
            file.close()
            QtWidgets.QMessageBox.information(self, "MessageBox", "保存成功。Oh yeah!!")


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_2.setText(_translate("MainWindow", "清空内容"))
        self.pushButton_4.setText(_translate("MainWindow", "保存文档"))
        self.pushButton_3.setText(_translate("MainWindow", "打开文档"))
        self.label.setText(_translate("MainWindow", "文档对话框尝试"))
        self.pushButton_5.setText(_translate("MainWindow", "显示Xml"))
        self.pushButton.setText(_translate("MainWindow", "显示文档"))
        self.pushButton_6.setText(_translate("MainWindow", "关闭窗口"))

