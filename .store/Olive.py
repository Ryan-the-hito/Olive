#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
from PyQt6.QtWidgets import (QWidget, QPushButton, QApplication,
                             QLabel, QHBoxLayout, QVBoxLayout,
                             QSystemTrayIcon, QMenu, QDialog, QLineEdit, QMenuBar, QTextEdit)
from PyQt6.QtCore import Qt, QTimer
from PyQt6.QtGui import QAction, QIcon
import PyQt6.QtGui
import subprocess
import applescript
import codecs
import re
import os
from pathlib import Path
import webbrowser
try:
	from AppKit import NSWorkspace
except ImportError:
	print("can't import AppKit -- maybe you're running python from homebrew?")
	print("try running with /usr/bin/python instead")
	exit(1)

app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

# Create the icon
icon = QIcon("olivemenu.icns")

# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Create the menu
menu = QMenu()

action5 = QAction("🫒 Start Olive!")
action5.setCheckable(True)
menu.addAction(action5)

action3 = QAction("📜 Select windows!")
action3.setCheckable(True)
menu.addAction(action3)

action4 = QAction("⚙️ Settings")
menu.addAction(action4)

menu.addSeparator()

action2 = QAction("🆕 Check for Updates")
menu.addAction(action2)

action1 = QAction("ℹ️ About")
menu.addAction(action1)

menu.addSeparator()

# Add a Quit option to the menu.
quit = QAction("Quit")
menu.addAction(quit)

# Add the menu to the tray
tray.setContextMenu(menu)

# create a system menu
button_action = QAction("&Select windows!")
button_action.setCheckable(True)
sysmenu = QMenuBar()
file_menu = sysmenu.addMenu("&Actions")
file_menu.addAction(button_action)


class window_about(QWidget):  # 增加说明页面(About)
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 说明页面内信息
        self.setUpMainWindow()
        self.resize(400, 380)
        self.center()
        self.setWindowTitle('About')
        self.setFocus()
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

    def setUpMainWindow(self):
        widg1 = QWidget()
        l1 = QLabel(self)
        png = PyQt6.QtGui.QPixmap('olivemenu.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
        l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        l1.setMaximumWidth(100)
        l1.setMaximumHeight(100)
        l1.setScaledContents(True)
        blay1 = QHBoxLayout()
        blay1.setContentsMargins(0, 0, 0, 0)
        blay1.addStretch()
        blay1.addWidget(l1)
        blay1.addStretch()
        widg1.setLayout(blay1)

        widg2 = QWidget()
        lbl0 = QLabel('Olive', self)
        font = PyQt6.QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        font.setPointSize(20)
        lbl0.setFont(font)
        blay2 = QHBoxLayout()
        blay2.setContentsMargins(0, 0, 0, 0)
        blay2.addStretch()
        blay2.addWidget(lbl0)
        blay2.addStretch()
        widg2.setLayout(blay2)

        widg3 = QWidget()
        lbl1 = QLabel('Version 0.1.9', self)
        blay3 = QHBoxLayout()
        blay3.setContentsMargins(0, 0, 0, 0)
        blay3.addStretch()
        blay3.addWidget(lbl1)
        blay3.addStretch()
        widg3.setLayout(blay3)

        widg4 = QWidget()
        lbl2 = QLabel('This app is open-sourced.', self)
        blay4 = QHBoxLayout()
        blay4.setContentsMargins(0, 0, 0, 0)
        blay4.addStretch()
        blay4.addWidget(lbl2)
        blay4.addStretch()
        widg4.setLayout(blay4)

        widg5 = QWidget()
        lbl3 = QLabel('本软件开源。', self)
        blay5 = QHBoxLayout()
        blay5.setContentsMargins(0, 0, 0, 0)
        blay5.addStretch()
        blay5.addWidget(lbl3)
        blay5.addStretch()
        widg5.setLayout(blay5)

        widg6 = QWidget()
        lbl4 = QLabel('♥‿♥', self)
        blay6 = QHBoxLayout()
        blay6.setContentsMargins(0, 0, 0, 0)
        blay6.addStretch()
        blay6.addWidget(lbl4)
        blay6.addStretch()
        widg6.setLayout(blay6)

        widg7 = QWidget()
        lbl5 = QLabel('※\(^o^)/※', self)
        blay7 = QHBoxLayout()
        blay7.setContentsMargins(0, 0, 0, 0)
        blay7.addStretch()
        blay7.addWidget(lbl5)
        blay7.addStretch()
        widg7.setLayout(blay7)

        widg8 = QWidget()
        bt1 = QPushButton('The Author', self)
        bt1.setMaximumHeight(20)
        bt1.setMinimumWidth(100)
        bt1.clicked.connect(self.intro)
        bt2 = QPushButton('Github Page', self)
        bt2.setMaximumHeight(20)
        bt2.setMinimumWidth(100)
        bt2.clicked.connect(self.homepage)
        blay8 = QHBoxLayout()
        blay8.setContentsMargins(0, 0, 0, 0)
        blay8.addStretch()
        blay8.addWidget(bt1)
        blay8.addWidget(bt2)
        blay8.addStretch()
        widg8.setLayout(blay8)

        widg9 = QWidget()
        bt3 = QPushButton('🍪\n¥5', self)
        bt3.setMaximumHeight(50)
        bt3.setMinimumHeight(50)
        bt3.setMinimumWidth(50)
        bt3.clicked.connect(self.donate)
        bt4 = QPushButton('🥪\n¥10', self)
        bt4.setMaximumHeight(50)
        bt4.setMinimumHeight(50)
        bt4.setMinimumWidth(50)
        bt4.clicked.connect(self.donate2)
        bt5 = QPushButton('🍜\n¥20', self)
        bt5.setMaximumHeight(50)
        bt5.setMinimumHeight(50)
        bt5.setMinimumWidth(50)
        bt5.clicked.connect(self.donate3)
        bt6 = QPushButton('🍕\n¥50', self)
        bt6.setMaximumHeight(50)
        bt6.setMinimumHeight(50)
        bt6.setMinimumWidth(50)
        bt6.clicked.connect(self.donate4)
        blay9 = QHBoxLayout()
        blay9.setContentsMargins(0, 0, 0, 0)
        blay9.addStretch()
        blay9.addWidget(bt3)
        blay9.addWidget(bt4)
        blay9.addWidget(bt5)
        blay9.addWidget(bt6)
        blay9.addStretch()
        widg9.setLayout(blay9)

        widg10 = QWidget()
        lbl6 = QLabel('© 2023 Ryan-the-hito. All rights reserved.', self)
        blay10 = QHBoxLayout()
        blay10.setContentsMargins(0, 0, 0, 0)
        blay10.addStretch()
        blay10.addWidget(lbl6)
        blay10.addStretch()
        widg10.setLayout(blay10)

        main_h_box = QVBoxLayout()
        main_h_box.addWidget(widg1)
        main_h_box.addWidget(widg2)
        main_h_box.addWidget(widg3)
        main_h_box.addWidget(widg4)
        main_h_box.addWidget(widg5)
        main_h_box.addWidget(widg6)
        main_h_box.addWidget(widg7)
        main_h_box.addWidget(widg8)
        main_h_box.addWidget(widg9)
        main_h_box.addWidget(widg10)
        main_h_box.addStretch()
        self.setLayout(main_h_box)

    def intro(self):
        webbrowser.open('https://github.com/Ryan-the-hito/Ryan-the-hito')

    def homepage(self):
        webbrowser.open('https://github.com/Ryan-the-hito/Olive')

    def donate(self):
        dlg = CustomDialog()
        dlg.exec()

    def donate2(self):
        dlg = CustomDialog2()
        dlg.exec()

    def donate3(self):
        dlg = CustomDialog3()
        dlg.exec()

    def donate4(self):
        dlg = CustomDialog4()
        dlg.exec()

    def center(self):  # 设置窗口居中
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def activate(self):  # 设置窗口显示
        self.show()
        self.raise_()
        self.activateWindow()


class CustomDialog(QDialog):  # (About1)
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setUpMainWindow()
        self.setWindowTitle("Thank you for your support!")
        self.center()
        self.resize(400, 390)
        self.setFocus()
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

    def setUpMainWindow(self):
        widge_all = QWidget()
        l1 = QLabel(self)
        png = PyQt6.QtGui.QPixmap('wechat5.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
        l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        l1.setMaximumSize(160, 240)
        l1.setScaledContents(True)
        l2 = QLabel(self)
        png = PyQt6.QtGui.QPixmap('alipay5.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
        l2.setPixmap(png)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        l2.setMaximumSize(160, 240)
        l2.setScaledContents(True)
        bk = QHBoxLayout()
        bk.setContentsMargins(0, 0, 0, 0)
        bk.addWidget(l1)
        bk.addWidget(l2)
        widge_all.setLayout(bk)

        m1 = QLabel('Thank you for your kind support! 😊', self)
        m2 = QLabel('I will write more interesting apps! 🥳', self)

        widg_c = QWidget()
        bt1 = QPushButton('Thank you!', self)
        bt1.setMaximumHeight(20)
        bt1.setMinimumWidth(100)
        bt1.clicked.connect(self.cancel)
        bt2 = QPushButton('Donate later~', self)
        bt2.setMaximumHeight(20)
        bt2.setMinimumWidth(100)
        bt2.clicked.connect(self.cancel)
        blay8 = QHBoxLayout()
        blay8.setContentsMargins(0, 0, 0, 0)
        blay8.addStretch()
        blay8.addWidget(bt1)
        blay8.addWidget(bt2)
        blay8.addStretch()
        widg_c.setLayout(blay8)

        self.layout = QVBoxLayout()
        self.layout.addWidget(widge_all)
        self.layout.addWidget(m1)
        self.layout.addWidget(m2)
        self.layout.addStretch()
        self.layout.addWidget(widg_c)
        self.layout.addStretch()
        self.setLayout(self.layout)
        self.setStyleSheet('''
                QPushButton{
                border: 1px outset grey;
                background-color: #FFFFFF;
                border-radius: 4px;
                padding: 1px;
                color: #000000
        }
            QPushButton:pressed{
                border: 1px outset grey;
                background-color: #0085FF;
                border-radius: 4px;
                padding: 1px;
                color: #FFFFFF
        }''')

    def center(self):  # 设置窗口居中
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def cancel(self):  # 设置取消键的功能
        self.close()


class CustomDialog2(QDialog):  # (About2)
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setUpMainWindow()
        self.setWindowTitle("Thank you for your support!")
        self.center()
        self.resize(400, 390)
        self.setFocus()
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

    def setUpMainWindow(self):
        widge_all = QWidget()
        l1 = QLabel(self)
        png = PyQt6.QtGui.QPixmap('wechat10.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
        l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        l1.setMaximumSize(160, 240)
        l1.setScaledContents(True)
        l2 = QLabel(self)
        png = PyQt6.QtGui.QPixmap('alipay10.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
        l2.setPixmap(png)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        l2.setMaximumSize(160, 240)
        l2.setScaledContents(True)
        bk = QHBoxLayout()
        bk.setContentsMargins(0, 0, 0, 0)
        bk.addWidget(l1)
        bk.addWidget(l2)
        widge_all.setLayout(bk)

        m1 = QLabel('Thank you for your kind support! 😊', self)
        m2 = QLabel('I will write more interesting apps! 🥳', self)

        widg_c = QWidget()
        bt1 = QPushButton('Thank you!', self)
        bt1.setMaximumHeight(20)
        bt1.setMinimumWidth(100)
        bt1.clicked.connect(self.cancel)
        bt2 = QPushButton('Donate later~', self)
        bt2.setMaximumHeight(20)
        bt2.setMinimumWidth(100)
        bt2.clicked.connect(self.cancel)
        blay8 = QHBoxLayout()
        blay8.setContentsMargins(0, 0, 0, 0)
        blay8.addStretch()
        blay8.addWidget(bt1)
        blay8.addWidget(bt2)
        blay8.addStretch()
        widg_c.setLayout(blay8)

        self.layout = QVBoxLayout()
        self.layout.addWidget(widge_all)
        self.layout.addWidget(m1)
        self.layout.addWidget(m2)
        self.layout.addStretch()
        self.layout.addWidget(widg_c)
        self.layout.addStretch()
        self.setLayout(self.layout)
        self.setStyleSheet('''
                QPushButton{
                border: 1px outset grey;
                background-color: #FFFFFF;
                border-radius: 4px;
                padding: 1px;
                color: #000000
        }
            QPushButton:pressed{
                border: 1px outset grey;
                background-color: #0085FF;
                border-radius: 4px;
                padding: 1px;
                color: #FFFFFF
        }''')

    def center(self):  # 设置窗口居中
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def cancel(self):  # 设置取消键的功能
        self.close()


class CustomDialog3(QDialog):  # (About3)
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setUpMainWindow()
        self.setWindowTitle("Thank you for your support!")
        self.center()
        self.resize(400, 390)
        self.setFocus()
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

    def setUpMainWindow(self):
        widge_all = QWidget()
        l1 = QLabel(self)
        png = PyQt6.QtGui.QPixmap('wechat20.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
        l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        l1.setMaximumSize(160, 240)
        l1.setScaledContents(True)
        l2 = QLabel(self)
        png = PyQt6.QtGui.QPixmap('alipay20.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
        l2.setPixmap(png)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        l2.setMaximumSize(160, 240)
        l2.setScaledContents(True)
        bk = QHBoxLayout()
        bk.setContentsMargins(0, 0, 0, 0)
        bk.addWidget(l1)
        bk.addWidget(l2)
        widge_all.setLayout(bk)

        m1 = QLabel('Thank you for your kind support! 😊', self)
        m2 = QLabel('I will write more interesting apps! 🥳', self)

        widg_c = QWidget()
        bt1 = QPushButton('Thank you!', self)
        bt1.setMaximumHeight(20)
        bt1.setMinimumWidth(100)
        bt1.clicked.connect(self.cancel)
        bt2 = QPushButton('Donate later~', self)
        bt2.setMaximumHeight(20)
        bt2.setMinimumWidth(100)
        bt2.clicked.connect(self.cancel)
        blay8 = QHBoxLayout()
        blay8.setContentsMargins(0, 0, 0, 0)
        blay8.addStretch()
        blay8.addWidget(bt1)
        blay8.addWidget(bt2)
        blay8.addStretch()
        widg_c.setLayout(blay8)

        self.layout = QVBoxLayout()
        self.layout.addWidget(widge_all)
        self.layout.addWidget(m1)
        self.layout.addWidget(m2)
        self.layout.addStretch()
        self.layout.addWidget(widg_c)
        self.layout.addStretch()
        self.setLayout(self.layout)
        self.setStyleSheet('''
                QPushButton{
                border: 1px outset grey;
                background-color: #FFFFFF;
                border-radius: 4px;
                padding: 1px;
                color: #000000
        }
            QPushButton:pressed{
                border: 1px outset grey;
                background-color: #0085FF;
                border-radius: 4px;
                padding: 1px;
                color: #FFFFFF
        }''')

    def center(self):  # 设置窗口居中
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def cancel(self):  # 设置取消键的功能
        self.close()


class CustomDialog4(QDialog):  # (About4)
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setUpMainWindow()
        self.setWindowTitle("Thank you for your support!")
        self.center()
        self.resize(400, 390)
        self.setFocus()
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

    def setUpMainWindow(self):
        widge_all = QWidget()
        l1 = QLabel(self)
        png = PyQt6.QtGui.QPixmap('wechat50.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
        l1.setPixmap(png)  # 在l1里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        l1.setMaximumSize(160, 240)
        l1.setScaledContents(True)
        l2 = QLabel(self)
        png = PyQt6.QtGui.QPixmap('alipay50.png')  # 调用QtGui.QPixmap方法，打开一个图片，存放在变量png中
        l2.setPixmap(png)  # 在l2里面，调用setPixmap命令，建立一个图像存放框，并将之前的图像png存放在这个框框里。
        l2.setMaximumSize(160, 240)
        l2.setScaledContents(True)
        bk = QHBoxLayout()
        bk.setContentsMargins(0, 0, 0, 0)
        bk.addWidget(l1)
        bk.addWidget(l2)
        widge_all.setLayout(bk)

        m1 = QLabel('Thank you for your kind support! 😊', self)
        m2 = QLabel('I will write more interesting apps! 🥳', self)

        widg_c = QWidget()
        bt1 = QPushButton('Thank you!', self)
        bt1.setMaximumHeight(20)
        bt1.setMinimumWidth(100)
        bt1.clicked.connect(self.cancel)
        bt2 = QPushButton('Donate later~', self)
        bt2.setMaximumHeight(20)
        bt2.setMinimumWidth(100)
        bt2.clicked.connect(self.cancel)
        blay8 = QHBoxLayout()
        blay8.setContentsMargins(0, 0, 0, 0)
        blay8.addStretch()
        blay8.addWidget(bt1)
        blay8.addWidget(bt2)
        blay8.addStretch()
        widg_c.setLayout(blay8)

        self.layout = QVBoxLayout()
        self.layout.addWidget(widge_all)
        self.layout.addWidget(m1)
        self.layout.addWidget(m2)
        self.layout.addStretch()
        self.layout.addWidget(widg_c)
        self.layout.addStretch()
        self.setLayout(self.layout)
        self.setStyleSheet('''
                QPushButton{
                border: 1px outset grey;
                background-color: #FFFFFF;
                border-radius: 4px;
                padding: 1px;
                color: #000000
        }
            QPushButton:pressed{
                border: 1px outset grey;
                background-color: #0085FF;
                border-radius: 4px;
                padding: 1px;
                color: #FFFFFF
        }''')

    def center(self):  # 设置窗口居中
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def cancel(self):  # 设置取消键的功能
        self.close()


class window_update(QWidget):  # 增加更新页面（Check for Updates）
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):  # 说明页面内信息

        lbl = QLabel('Current Version: 0.1.9', self)
        lbl.move(110, 75)

        lbl0 = QLabel('Check Now:', self)
        lbl0.move(30, 20)

        bt1 = QPushButton('Check Github', self)
        bt1.clicked.connect(self.upd)
        bt1.move(110, 15)

        bt2 = QPushButton('Check Baidu Net Disk', self)
        bt2.clicked.connect(self.upd2)
        bt2.move(110, 45)

        self.resize(300, 110)
        self.center()
        self.setWindowTitle('Check for Updates')
        self.setFocus()
        self.setWindowFlags(Qt.WindowType.WindowStaysOnTopHint)

    def upd(self):
        webbrowser.open('https://github.com/Ryan-the-hito/Olive/releases')

    def upd2(self):
        webbrowser.open('https://pan.baidu.com/s/1trV85o0hfrzgnfGHXkgawQ?pwd=q5y5')

    def center(self):  # 设置窗口居中
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def activate(self):  # 设置窗口显示
        self.show()
        self.raise_()
        self.activateWindow()


class MyWidget(QWidget):  # 主窗口
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.trax = 2
        self.setUpMainWindow()
        self.center()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint | Qt.WindowType.WindowStaysOnTopHint)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground, True)
        self.clicktime = 0
        self.onlist = []
        home_dir = str(Path.home())
        tarname1 = "OliveAppPath"
        fulldir1 = os.path.join(home_dir, tarname1)
        if not os.path.exists(fulldir1):
            os.mkdir(fulldir1)
        tarname2 = "tarlist.txt"
        fulldir2 = os.path.join(fulldir1, tarname2)
        if not os.path.exists(fulldir2):
            cont = codecs.open('tarlist.txt', 'r', encoding='utf-8').read()
            with open(fulldir2, 'a', encoding='utf-8') as f0:
                f0.write(cont)
        self.ultraclick1 = 0
        self.ultraclick2 = 0
        self.ultraclick3 = 0
        self.ultraclick4 = 0
        self.ultraclick5 = 0
        self.ultraclick6 = 0
        self.ultraclick7 = 0
        self.ultraclick8 = 0
        self.ultraclick9 = 0
        self.ultraclick10 = 0
        self.ultraclick11 = 0
        self.ultraclick12 = 0
        self.ultraclick13 = 0
        self.ultraclick14 = 0
        self.ultraclick15 = 0
        self.ultraclick16 = 0
        self.ultraclick17 = 0
        self.ultraclick18 = 0
        self.ultraclick19 = 0
        self.ultraclick20 = 0

    def everytimefirst(self):
        cont = codecs.open('showlist.txt', 'r', encoding='utf-8').read()
        self.showlist = cont.split('☆')
        self.totalnum = len(self.showlist)
        if self.totalnum / 5 <= 1:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.setFixedHeight(190)
            if self.totalnum == 0:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.setFixedWidth(240)
                self.all_invisible()
                self.bt1.setVisible(True)
                self.bt1.setText('None')
            if self.totalnum == 1:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.setFixedWidth(240)
                self.all_invisible()
                self.bt1.setVisible(True)
                self.bt1.setText('None')
            if self.totalnum == 2:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.setFixedWidth(454)
                self.all_invisible()
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
            if self.totalnum == 3:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.setFixedWidth(668)
                self.all_invisible()
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
            if self.totalnum == 4:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.setFixedWidth(882)
                self.all_invisible()
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
            if self.totalnum == 5:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.setFixedWidth(1096)
                self.all_invisible()
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
        if 1 < self.totalnum / 5 <= 2:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.setFixedHeight(350)
            self.setFixedWidth(1096)
            if self.totalnum == 6:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
            if self.totalnum == 7:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
            if self.totalnum == 8:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
            if self.totalnum == 9:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt9.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
                self.bt9.setText(self.showlist[8])
            if self.totalnum == 10:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt9.setVisible(True)
                self.bt10.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
                self.bt9.setText(self.showlist[8])
                self.bt10.setText(self.showlist[9])
        if 2 < self.totalnum / 5 <= 3:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.setFixedHeight(510)
            self.setFixedWidth(1096)
            if self.totalnum == 11:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.widg3.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt9.setVisible(True)
                self.bt10.setVisible(True)
                self.bt11.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
                self.bt9.setText(self.showlist[8])
                self.bt10.setText(self.showlist[9])
                self.bt11.setText(self.showlist[10])
            if self.totalnum == 12:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.widg3.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt9.setVisible(True)
                self.bt10.setVisible(True)
                self.bt11.setVisible(True)
                self.bt12.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
                self.bt9.setText(self.showlist[8])
                self.bt10.setText(self.showlist[9])
                self.bt11.setText(self.showlist[10])
                self.bt12.setText(self.showlist[11])
            if self.totalnum == 13:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.widg3.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt9.setVisible(True)
                self.bt10.setVisible(True)
                self.bt11.setVisible(True)
                self.bt12.setVisible(True)
                self.bt13.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
                self.bt9.setText(self.showlist[8])
                self.bt10.setText(self.showlist[9])
                self.bt11.setText(self.showlist[10])
                self.bt12.setText(self.showlist[11])
                self.bt13.setText(self.showlist[12])
            if self.totalnum == 14:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.widg3.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt9.setVisible(True)
                self.bt10.setVisible(True)
                self.bt11.setVisible(True)
                self.bt12.setVisible(True)
                self.bt13.setVisible(True)
                self.bt14.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
                self.bt9.setText(self.showlist[8])
                self.bt10.setText(self.showlist[9])
                self.bt11.setText(self.showlist[10])
                self.bt12.setText(self.showlist[11])
                self.bt13.setText(self.showlist[12])
                self.bt14.setText(self.showlist[13])
            if self.totalnum == 15:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.widg3.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt9.setVisible(True)
                self.bt10.setVisible(True)
                self.bt11.setVisible(True)
                self.bt12.setVisible(True)
                self.bt13.setVisible(True)
                self.bt14.setVisible(True)
                self.bt15.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
                self.bt9.setText(self.showlist[8])
                self.bt10.setText(self.showlist[9])
                self.bt11.setText(self.showlist[10])
                self.bt12.setText(self.showlist[11])
                self.bt13.setText(self.showlist[12])
                self.bt14.setText(self.showlist[13])
                self.bt15.setText(self.showlist[14])
        if 3 < self.totalnum / 5 <= 4:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.setFixedHeight(670)
            self.setFixedWidth(1096)
            if self.totalnum == 16:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.widg3.setVisible(True)
                self.widg4.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt9.setVisible(True)
                self.bt10.setVisible(True)
                self.bt11.setVisible(True)
                self.bt12.setVisible(True)
                self.bt13.setVisible(True)
                self.bt14.setVisible(True)
                self.bt15.setVisible(True)
                self.bt16.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
                self.bt9.setText(self.showlist[8])
                self.bt10.setText(self.showlist[9])
                self.bt11.setText(self.showlist[10])
                self.bt12.setText(self.showlist[11])
                self.bt13.setText(self.showlist[12])
                self.bt14.setText(self.showlist[13])
                self.bt15.setText(self.showlist[14])
                self.bt16.setText(self.showlist[15])
            if self.totalnum == 17:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.widg3.setVisible(True)
                self.widg4.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt9.setVisible(True)
                self.bt10.setVisible(True)
                self.bt11.setVisible(True)
                self.bt12.setVisible(True)
                self.bt13.setVisible(True)
                self.bt14.setVisible(True)
                self.bt15.setVisible(True)
                self.bt16.setVisible(True)
                self.bt17.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
                self.bt9.setText(self.showlist[8])
                self.bt10.setText(self.showlist[9])
                self.bt11.setText(self.showlist[10])
                self.bt12.setText(self.showlist[11])
                self.bt13.setText(self.showlist[12])
                self.bt14.setText(self.showlist[13])
                self.bt15.setText(self.showlist[14])
                self.bt16.setText(self.showlist[15])
                self.bt17.setText(self.showlist[16])
            if self.totalnum == 18:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.widg3.setVisible(True)
                self.widg4.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt9.setVisible(True)
                self.bt10.setVisible(True)
                self.bt11.setVisible(True)
                self.bt12.setVisible(True)
                self.bt13.setVisible(True)
                self.bt14.setVisible(True)
                self.bt15.setVisible(True)
                self.bt16.setVisible(True)
                self.bt17.setVisible(True)
                self.bt18.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
                self.bt9.setText(self.showlist[8])
                self.bt10.setText(self.showlist[9])
                self.bt11.setText(self.showlist[10])
                self.bt12.setText(self.showlist[11])
                self.bt13.setText(self.showlist[12])
                self.bt14.setText(self.showlist[13])
                self.bt15.setText(self.showlist[14])
                self.bt16.setText(self.showlist[15])
                self.bt17.setText(self.showlist[16])
                self.bt18.setText(self.showlist[17])
            if self.totalnum == 19:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.widg3.setVisible(True)
                self.widg4.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt9.setVisible(True)
                self.bt10.setVisible(True)
                self.bt11.setVisible(True)
                self.bt12.setVisible(True)
                self.bt13.setVisible(True)
                self.bt14.setVisible(True)
                self.bt15.setVisible(True)
                self.bt16.setVisible(True)
                self.bt17.setVisible(True)
                self.bt18.setVisible(True)
                self.bt19.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
                self.bt9.setText(self.showlist[8])
                self.bt10.setText(self.showlist[9])
                self.bt11.setText(self.showlist[10])
                self.bt12.setText(self.showlist[11])
                self.bt13.setText(self.showlist[12])
                self.bt14.setText(self.showlist[13])
                self.bt15.setText(self.showlist[14])
                self.bt16.setText(self.showlist[15])
                self.bt17.setText(self.showlist[16])
                self.bt18.setText(self.showlist[17])
                self.bt19.setText(self.showlist[18])
            if self.totalnum == 20:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.all_invisible()
                self.widg2.setVisible(True)
                self.widg3.setVisible(True)
                self.widg4.setVisible(True)
                self.bt1.setVisible(True)
                self.bt2.setVisible(True)
                self.bt3.setVisible(True)
                self.bt4.setVisible(True)
                self.bt5.setVisible(True)
                self.bt6.setVisible(True)
                self.bt7.setVisible(True)
                self.bt8.setVisible(True)
                self.bt9.setVisible(True)
                self.bt10.setVisible(True)
                self.bt11.setVisible(True)
                self.bt12.setVisible(True)
                self.bt13.setVisible(True)
                self.bt14.setVisible(True)
                self.bt15.setVisible(True)
                self.bt16.setVisible(True)
                self.bt17.setVisible(True)
                self.bt18.setVisible(True)
                self.bt19.setVisible(True)
                self.bt20.setVisible(True)
                self.bt1.setText(self.showlist[0])
                self.bt2.setText(self.showlist[1])
                self.bt3.setText(self.showlist[2])
                self.bt4.setText(self.showlist[3])
                self.bt5.setText(self.showlist[4])
                self.bt6.setText(self.showlist[5])
                self.bt7.setText(self.showlist[6])
                self.bt8.setText(self.showlist[7])
                self.bt9.setText(self.showlist[8])
                self.bt10.setText(self.showlist[9])
                self.bt11.setText(self.showlist[10])
                self.bt12.setText(self.showlist[11])
                self.bt13.setText(self.showlist[12])
                self.bt14.setText(self.showlist[13])
                self.bt15.setText(self.showlist[14])
                self.bt16.setText(self.showlist[15])
                self.bt17.setText(self.showlist[16])
                self.bt18.setText(self.showlist[17])
                self.bt19.setText(self.showlist[18])
                self.bt20.setText(self.showlist[19])
        if self.totalnum / 5 > 4:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.setFixedHeight(690)
            self.setFixedWidth(1096)
            self.all_invisible()
            self.widg2.setVisible(True)
            self.widg3.setVisible(True)
            self.widg4.setVisible(True)
            self.bt1.setVisible(True)
            self.bt2.setVisible(True)
            self.bt3.setVisible(True)
            self.bt4.setVisible(True)
            self.bt5.setVisible(True)
            self.bt6.setVisible(True)
            self.bt7.setVisible(True)
            self.bt8.setVisible(True)
            self.bt9.setVisible(True)
            self.bt10.setVisible(True)
            self.bt11.setVisible(True)
            self.bt12.setVisible(True)
            self.bt13.setVisible(True)
            self.bt14.setVisible(True)
            self.bt15.setVisible(True)
            self.bt16.setVisible(True)
            self.bt17.setVisible(True)
            self.bt18.setVisible(True)
            self.bt19.setVisible(True)
            self.bt20.setVisible(True)
            self.bt1.setText(self.showlist[0])
            self.bt2.setText(self.showlist[1])
            self.bt3.setText(self.showlist[2])
            self.bt4.setText(self.showlist[3])
            self.bt5.setText(self.showlist[4])
            self.bt6.setText(self.showlist[5])
            self.bt7.setText(self.showlist[6])
            self.bt8.setText(self.showlist[7])
            self.bt9.setText(self.showlist[8])
            self.bt10.setText(self.showlist[9])
            self.bt11.setText(self.showlist[10])
            self.bt12.setText(self.showlist[11])
            self.bt13.setText(self.showlist[12])
            self.bt14.setText(self.showlist[13])
            self.bt15.setText(self.showlist[14])
            self.bt16.setText(self.showlist[15])
            self.bt17.setText(self.showlist[16])
            self.bt18.setText(self.showlist[17])
            self.bt19.setText(self.showlist[18])
            self.bt20.setText(self.showlist[19])
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.center()

    def setUpMainWindow(self):
        self.bt1 = QPushButton('', self)
        self.bt1.setFixedSize(200, 150)
        self.bt1.clicked.connect(self.clickplus1)
        self.bt1.setVisible(False)

        self.bt2 = QPushButton('', self)
        self.bt2.setFixedSize(200, 150)
        self.bt2.clicked.connect(self.clickplus2)
        self.bt2.setVisible(False)

        self.bt3 = QPushButton('', self)
        self.bt3.setFixedSize(200, 150)
        self.bt3.clicked.connect(self.clickplus3)
        self.bt3.setVisible(False)

        self.bt4 = QPushButton('', self)
        self.bt4.setFixedSize(200, 150)
        self.bt4.clicked.connect(self.clickplus4)
        self.bt4.setVisible(False)

        self.bt5 = QPushButton('', self)
        self.bt5.setFixedSize(200, 150)
        self.bt5.clicked.connect(self.clickplus5)
        self.bt5.setVisible(False)

        self.bt6 = QPushButton('', self)
        self.bt6.setFixedSize(200, 150)
        self.bt6.clicked.connect(self.clickplus6)
        self.bt6.setVisible(False)

        self.bt7 = QPushButton('', self)
        self.bt7.setFixedSize(200, 150)
        self.bt7.clicked.connect(self.clickplus7)
        self.bt7.setVisible(False)

        self.bt8 = QPushButton('', self)
        self.bt8.setFixedSize(200, 150)
        self.bt8.clicked.connect(self.clickplus8)
        self.bt8.setVisible(False)

        self.bt9 = QPushButton('', self)
        self.bt9.setFixedSize(200, 150)
        self.bt9.clicked.connect(self.clickplus9)
        self.bt9.setVisible(False)

        self.bt10 = QPushButton('', self)
        self.bt10.setFixedSize(200, 150)
        self.bt10.clicked.connect(self.clickplus10)
        self.bt10.setVisible(False)

        self.bt11 = QPushButton('', self)
        self.bt11.setFixedSize(200, 150)
        self.bt11.clicked.connect(self.clickplus11)
        self.bt11.setVisible(False)

        self.bt12 = QPushButton('', self)
        self.bt12.setFixedSize(200, 150)
        self.bt12.clicked.connect(self.clickplus12)
        self.bt12.setVisible(False)

        self.bt13 = QPushButton('', self)
        self.bt13.setFixedSize(200, 150)
        self.bt13.clicked.connect(self.clickplus13)
        self.bt13.setVisible(False)

        self.bt14 = QPushButton('', self)
        self.bt14.setFixedSize(200, 150)
        self.bt14.clicked.connect(self.clickplus14)
        self.bt14.setVisible(False)

        self.bt15 = QPushButton('', self)
        self.bt15.setFixedSize(200, 150)
        self.bt15.clicked.connect(self.clickplus15)
        self.bt15.setVisible(False)

        self.bt16 = QPushButton('', self)
        self.bt16.setFixedSize(200, 150)
        self.bt16.clicked.connect(self.clickplus16)
        self.bt16.setVisible(False)

        self.bt17 = QPushButton('', self)
        self.bt17.setFixedSize(200, 150)
        self.bt17.clicked.connect(self.clickplus17)
        self.bt17.setVisible(False)

        self.bt18 = QPushButton('', self)
        self.bt18.setFixedSize(200, 150)
        self.bt18.clicked.connect(self.clickplus18)
        self.bt18.setVisible(False)

        self.bt19 = QPushButton('', self)
        self.bt19.setFixedSize(200, 150)
        self.bt19.clicked.connect(self.clickplus19)
        self.bt19.setVisible(False)

        self.bt20 = QPushButton('', self)
        self.bt20.setFixedSize(200, 150)
        self.bt20.clicked.connect(self.clickplus20)
        self.bt20.setVisible(False)

        self.widg1 = QWidget()
        blay1 = QHBoxLayout()
        blay1.setContentsMargins(0, 0, 0, 0)
        blay1.addStretch()
        blay1.addWidget(self.bt1)
        blay1.addWidget(self.bt2)
        blay1.addWidget(self.bt3)
        blay1.addWidget(self.bt4)
        blay1.addWidget(self.bt5)
        blay1.addStretch()
        self.widg1.setLayout(blay1)

        self.widg2 = QWidget()
        blay2 = QHBoxLayout()
        blay2.setContentsMargins(0, 0, 0, 0)
        blay2.addStretch()
        blay2.addWidget(self.bt6)
        blay2.addWidget(self.bt7)
        blay2.addWidget(self.bt8)
        blay2.addWidget(self.bt9)
        blay2.addWidget(self.bt10)
        blay2.addStretch()
        self.widg2.setLayout(blay2)

        self.widg3 = QWidget()
        blay3 = QHBoxLayout()
        blay3.setContentsMargins(0, 0, 0, 0)
        blay3.addStretch()
        blay3.addWidget(self.bt11)
        blay3.addWidget(self.bt12)
        blay3.addWidget(self.bt13)
        blay3.addWidget(self.bt14)
        blay3.addWidget(self.bt15)
        blay3.addStretch()
        self.widg3.setLayout(blay3)

        self.widg4 = QWidget()
        blay4 = QHBoxLayout()
        blay4.setContentsMargins(0, 0, 0, 0)
        blay4.addStretch()
        blay4.addWidget(self.bt16)
        blay4.addWidget(self.bt17)
        blay4.addWidget(self.bt18)
        blay4.addWidget(self.bt19)
        blay4.addWidget(self.bt20)
        blay4.addStretch()
        self.widg4.setLayout(blay4)

        widg0 = QWidget()
        widg0.setObjectName("Main")
        blay0 = QVBoxLayout()
        blay0.setContentsMargins(20, 20, 20, 20)
        blay0.addStretch()
        blay0.addWidget(self.widg1)
        blay0.addWidget(self.widg2)
        blay0.addWidget(self.widg3)
        blay0.addWidget(self.widg4)
        blay0.addStretch()
        widg0.setLayout(blay0)

        blay = QHBoxLayout()
        blay.setContentsMargins(0, 0, 0, 0)
        blay.addStretch()
        blay.addWidget(widg0)
        blay.addStretch()
        self.setLayout(blay)

    def clickplus1(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt1.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        if ncount == 0:
            self.ultraclick1 += 1
            if self.ultraclick1 == 1:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                gettext = self.bt1.text()
                if gettext == 'None':
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    self.cancel()
                    button_action.setChecked(False)
                    action3.setChecked(False)
                if gettext != 'None':
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    self.onlist.append(gettext)
            if self.ultraclick1 == 2:
                self.bt1.setStyleSheet('''
                    border: 4px outset white;
                    background-color: #989896;
                    border-radius: 12px;
                    padding: 1px;
                    color: #000000''')
                self.bt1.setDisabled(True)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)
        if ncount != 0:
            self.bt1.setDisabled(True)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            if self.clicktime < ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.clicktime += 1
                gettext = self.bt1.text()
                if gettext == 'None':
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    self.cancel()
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    button_action.setChecked(False)
                    action3.setChecked(False)
                if gettext != 'None':
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    self.onlist.append(gettext)
            if self.clicktime == ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)

    def clickplus2(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt2.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        if ncount == 0:
            self.ultraclick2 += 1
            if self.ultraclick2 == 1:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                gettext = self.bt2.text()
                self.onlist.append(gettext)
            if self.ultraclick2 == 2:
                self.bt2.setStyleSheet('''
                    border: 4px outset white;
                    background-color: #989896;
                    border-radius: 12px;
                    padding: 1px;
                    color: #000000''')
                self.bt2.setDisabled(True)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)
        if ncount != 0:
            self.bt2.setDisabled(True)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            if self.clicktime < ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.clicktime += 1
                gettext = self.bt2.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.clicktime == ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)

    def clickplus3(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt3.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        if ncount == 0:
            self.ultraclick3 += 1
            if self.ultraclick3 == 1:
                gettext = self.bt3.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.ultraclick3 == 2:
                self.bt3.setStyleSheet('''
                    border: 4px outset white;
                    background-color: #989896;
                    border-radius: 12px;
                    padding: 1px;
                    color: #000000''')
                self.bt3.setDisabled(True)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)
        if ncount != 0:
            self.bt3.setDisabled(True)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            if self.clicktime < ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.clicktime += 1
                gettext = self.bt3.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.clicktime == ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)

    def clickplus4(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt4.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        if ncount == 0:
            self.ultraclick4 += 1
            if self.ultraclick4 == 1:
                gettext = self.bt4.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.ultraclick4 == 2:
                self.bt4.setStyleSheet('''
                    border: 4px outset white;
                    background-color: #989896;
                    border-radius: 12px;
                    padding: 1px;
                    color: #000000''')
                self.bt4.setDisabled(True)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)
        if ncount != 0:
            self.bt4.setDisabled(True)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            if self.clicktime < ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.clicktime += 1
                gettext = self.bt4.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.clicktime == ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)

    def clickplus5(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt5.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        if ncount == 0:
            self.ultraclick5 += 1
            if self.ultraclick5 == 1:
                gettext = self.bt5.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.ultraclick5 == 2:
                self.bt5.setStyleSheet('''
                    border: 4px outset white;
                    background-color: #989896;
                    border-radius: 12px;
                    padding: 1px;
                    color: #000000''')
                self.bt5.setDisabled(True)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)
        if ncount != 0:
            self.bt5.setDisabled(True)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            if self.clicktime < ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.clicktime += 1
                gettext = self.bt5.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.clicktime == ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)

    def clickplus6(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        
        self.bt6.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        if ncount == 0:
            self.ultraclick6 += 1
            if self.ultraclick6 == 1:
                gettext = self.bt6.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.ultraclick6 == 2:
                self.bt6.setStyleSheet('''
                    border: 4px outset white;
                    background-color: #989896;
                    border-radius: 12px;
                    padding: 1px;
                    color: #000000''')
                self.bt6.setDisabled(True)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)
        if ncount != 0:
            self.bt6.setDisabled(True)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            if self.clicktime < ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.clicktime += 1
                gettext = self.bt6.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.clicktime == ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)

    def clickplus7(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt7.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        if ncount == 0:
            self.ultraclick7 += 1
            if self.ultraclick7 == 1:
                gettext = self.bt7.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.ultraclick7 == 2:
                self.bt7.setStyleSheet('''
                    border: 4px outset white;
                    background-color: #989896;
                    border-radius: 12px;
                    padding: 1px;
                    color: #000000''')
                self.bt7.setDisabled(True)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)
        if ncount != 0:
            self.bt7.setDisabled(True)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            if self.clicktime < ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.clicktime += 1
                gettext = self.bt7.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.clicktime == ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)

    def clickplus8(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        
        self.bt8.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        if ncount == 0:
            self.ultraclick8 += 1
            if self.ultraclick8 == 1:
                gettext = self.bt8.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.ultraclick8 == 2:
                self.bt8.setStyleSheet('''
                    border: 4px outset white;
                    background-color: #989896;
                    border-radius: 12px;
                    padding: 1px;
                    color: #000000''')
                self.bt8.setDisabled(True)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)
        if ncount != 0:
            self.bt8.setDisabled(True)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            if self.clicktime < ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.clicktime += 1
                gettext = self.bt8.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.clicktime == ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)

    def clickplus9(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        
        self.bt9.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        if ncount == 0:
            self.ultraclick9 += 1
            if self.ultraclick9 == 1:
                gettext = self.bt9.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.ultraclick9 == 2:
                self.bt9.setStyleSheet('''
                    border: 4px outset white;
                    background-color: #989896;
                    border-radius: 12px;
                    padding: 1px;
                    color: #000000''')
                self.bt9.setDisabled(True)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)
        if ncount != 0:
            self.bt9.setDisabled(True)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            if self.clicktime < ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.clicktime += 1
                gettext = self.bt9.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.clicktime == ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)

    def clickplus10(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt10.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        if ncount == 0:
            self.ultraclick10 += 1
            if self.ultraclick10 == 1:
                gettext = self.bt10.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.ultraclick10 == 2:
                self.bt10.setStyleSheet('''
                    border: 4px outset white;
                    background-color: #989896;
                    border-radius: 12px;
                    padding: 1px;
                    color: #000000''')
                self.bt10.setDisabled(True)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)
        if ncount != 0:
            self.bt10.setDisabled(True)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            if self.clicktime < ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.clicktime += 1
                gettext = self.bt10.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.clicktime == ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)

    def clickplus11(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt11.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        if ncount == 0:
            self.ultraclick11 += 1
            if self.ultraclick11 == 1:
                gettext = self.bt11.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.ultraclick11 == 2:
                self.bt11.setStyleSheet('''
                    border: 4px outset white;
                    background-color: #989896;
                    border-radius: 12px;
                    padding: 1px;
                    color: #000000''')
                self.bt11.setDisabled(True)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)
        if ncount != 0:
            self.bt11.setDisabled(True)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            if self.clicktime < ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.clicktime += 1
                gettext = self.bt11.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.clicktime == ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)

    def clickplus12(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt12.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        if ncount == 0:
            self.ultraclick12 += 1
            if self.ultraclick12 == 1:
                gettext = self.bt12.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.ultraclick12 == 2:
                self.bt12.setStyleSheet('''
                    border: 4px outset white;
                    background-color: #989896;
                    border-radius: 12px;
                    padding: 1px;
                    color: #000000''')
                self.bt12.setDisabled(True)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)
        if ncount != 0:
            self.bt12.setDisabled(True)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            if self.clicktime < ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.clicktime += 1
                gettext = self.bt12.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.clicktime == ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)

    def clickplus13(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt13.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        if ncount == 0:
            self.ultraclick13 += 1
            if self.ultraclick13 == 1:
                gettext = self.bt13.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.ultraclick13 == 2:
                self.bt13.setStyleSheet('''
                    border: 4px outset white;
                    background-color: #989896;
                    border-radius: 12px;
                    padding: 1px;
                    color: #000000''')
                self.bt13.setDisabled(True)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)
        if ncount != 0:
            self.bt13.setDisabled(True)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            if self.clicktime < ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.clicktime += 1
                gettext = self.bt13.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.clicktime == ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)

    def clickplus14(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt14.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        if ncount == 0:
            self.ultraclick14 += 1
            if self.ultraclick14 == 1:
                gettext = self.bt14.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.ultraclick14 == 2:
                self.bt14.setStyleSheet('''
                    border: 4px outset white;
                    background-color: #989896;
                    border-radius: 12px;
                    padding: 1px;
                    color: #000000''')
                self.bt14.setDisabled(True)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)
        if ncount != 0:
            self.bt14.setDisabled(True)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            if self.clicktime < ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.clicktime += 1
                gettext = self.bt14.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.clicktime == ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)

    def clickplus15(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt15.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        if ncount == 0:
            self.ultraclick15 += 1
            if self.ultraclick15 == 1:
                gettext = self.bt15.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.ultraclick15 == 2:
                self.bt15.setStyleSheet('''
                    border: 4px outset white;
                    background-color: #989896;
                    border-radius: 12px;
                    padding: 1px;
                    color: #000000''')
                self.bt15.setDisabled(True)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)
        if ncount != 0:
            self.bt15.setDisabled(True)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            if self.clicktime < ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.clicktime += 1
                gettext = self.bt15.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.clicktime == ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)

    def clickplus16(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt16.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        if ncount == 0:
            self.ultraclick16 += 1
            if self.ultraclick16 == 1:
                gettext = self.bt16.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.ultraclick16 == 2:
                self.bt16.setStyleSheet('''
                    border: 4px outset white;
                    background-color: #989896;
                    border-radius: 12px;
                    padding: 1px;
                    color: #000000''')
                self.bt16.setDisabled(True)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)
        if ncount != 0:
            self.bt16.setDisabled(True)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            if self.clicktime < ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.clicktime += 1
                gettext = self.bt16.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.clicktime == ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)

    def clickplus17(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt17.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        if ncount == 0:
            self.ultraclick17 += 1
            if self.ultraclick17 == 1:
                gettext = self.bt17.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.ultraclick17 == 2:
                self.bt17.setStyleSheet('''
                    border: 4px outset white;
                    background-color: #989896;
                    border-radius: 12px;
                    padding: 1px;
                    color: #000000''')
                self.bt17.setDisabled(True)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)
        if ncount != 0:
            self.bt17.setDisabled(True)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            if self.clicktime < ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.clicktime += 1
                gettext = self.bt17.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.clicktime == ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)

    def clickplus18(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt18.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        if ncount == 0:
            self.ultraclick18 += 1
            if self.ultraclick18 == 1:
                gettext = self.bt18.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.ultraclick18 == 2:
                self.bt18.setStyleSheet('''
                    border: 4px outset white;
                    background-color: #989896;
                    border-radius: 12px;
                    padding: 1px;
                    color: #000000''')
                self.bt18.setDisabled(True)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)
        if ncount != 0:
            self.bt18.setDisabled(True)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            if self.clicktime < ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.clicktime += 1
                gettext = self.bt18.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.clicktime == ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)

    def clickplus19(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        
        self.bt19.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        if ncount == 0:
            self.ultraclick19 += 1
            if self.ultraclick19 == 1:
                gettext = self.bt19.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.ultraclick19 == 2:
                self.bt19.setStyleSheet('''
                    border: 4px outset white;
                    background-color: #989896;
                    border-radius: 12px;
                    padding: 1px;
                    color: #000000''')
                self.bt19.setDisabled(True)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)
        if ncount != 0:
            self.bt19.setDisabled(True)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            if self.clicktime < ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.clicktime += 1
                gettext = self.bt19.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.clicktime == ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)

    def clickplus20(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt20.setStyleSheet('''
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000''')
        ncount = int(codecs.open('multinum.txt', 'r', encoding='utf-8').read())
        if ncount == 0:
            self.ultraclick20 += 1
            if self.ultraclick20 == 1:
                gettext = self.bt20.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.ultraclick20 == 2:
                self.bt20.setStyleSheet('''
                    border: 4px outset white;
                    background-color: #989896;
                    border-radius: 12px;
                    padding: 1px;
                    color: #000000''')
                self.bt20.setDisabled(True)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)
        if ncount != 0:
            self.bt20.setDisabled(True)
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            if self.clicktime < ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.clicktime += 1
                gettext = self.bt20.text()
                self.onlist.append(gettext)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            if self.clicktime == ncount:
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.showhide()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                self.cancel()
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
                action3.setChecked(False)
                button_action.setChecked(False)

    def showhide(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.hidelist = list(set(self.showlist) - set(self.onlist))
        for t in range(len(self.hidelist)):
            result0 = ''
            result = 0

            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            pattern0 = re.compile(r'(.*?)\n~')
            resulta = pattern0.findall(self.hidelist[t])
            if resulta != []:
                result0 = ''.join(resulta)

            pattern = re.compile(r'~(.*?)~')
            resultb = pattern.findall(self.hidelist[t])
            if resultb != []:
                result = int(''.join(resultb))
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()

            if result0 != '' and result != 0:
                if result0 == 'Finder':
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    cmd = f"""osascript -e '''
                            tell application "Finder"
                                try
                                    set collapsed of window {result} to true
                                on error errorMessage
                                    tell application "Finder" to activate
                                    delay 0.1
                                    tell application "System Events" to tell process "Finder"
                                        keystroke "m" using command down
                                    end tell
                                end try
                            end tell
                            '''"""
                    os.system(cmd)
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                if result0 != 'Finder':
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    cmd = f"""osascript -e '''
                            tell application "System Events"
                                tell application "{result0}"
                                    try
                                        set miniaturized of window {result} to true
                                    end try
                                    try
                                        tell application "{result0}" to activate
                                        -- delay 0.1
                                        tell application "System Events" to tell process "{result0}"
                                            keystroke "m" using command down
                                        end tell
                                    end try
                                end tell
                            end tell'''"""
                    os.system(cmd)
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()

        for i in range(len(self.onlist)):
            result0 = ''
            result = 0
            
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            pattern0 = re.compile(r'(.*?)\n~')
            resulta = pattern0.findall(self.onlist[i])
            if resulta != []:
                result0 = ''.join(resulta)

            pattern = re.compile(r'~(.*?)~')
            resultb = pattern.findall(self.onlist[i])
            if resultb != []:
                result = ''.join(resultb)
                QApplication.processEvents()
                QApplication.restoreOverrideCursor()
            
            if result0 != '' and result != 0:
                first_name = result0 + '\n~' + result + '~\n'
                window_name = self.onlist[i].replace(first_name, '').replace('\n', '')
                if result0 == 'Finder':
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    cmd = f"""osascript -e '''
                    tell application "Finder"
                        try
                            tell application "System Events"
	                            tell process "Dock"
                                    set appIcon to UI element ("Finder") of list 1
                                    perform action "AXShowMenu" of appIcon
                                    delay 0.2
                                    click menu item "{window_name}" of menu 1 of appIcon
                                    delay 0.2
                                end tell
                            end tell
                        on error errorMessage
                            set collapsed of window {result} to false
                        end try
                    end tell
                    '''"""
                    os.system(cmd)
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                if result0 == 'Music' or result0 == 'Photos' or result0 == 'Messages' or result0 == 'Reminders' or \
                        result0 == 'Calendar' or result0 == 'Notes' or result0 == 'Podcasts' or result0 == 'Contacts' \
                        or result0 == 'Calculator' or result0 == 'Font Book':
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    cmd = f"""osascript -e '''
                    tell application "{result0}"
                        try
                            set miniaturized of window {result} to false
                            activate
                        on error errorMessage
                            reopen
                            activate
                        end try
                    end tell'''"""
                    os.system(cmd)
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                if result0 != 'Finder' and result0 != 'Music' and result0 != 'Photos' and result0 != 'Messages' \
                    and result0 != 'Reminders' and result0 != 'Calendar' and result0 != 'Notes' and result0 !='Podcasts' \
                    and result0 != 'Contacts' and result0 != 'Calculator' and result0 != 'Font Book':
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    cmd = f"""osascript -e '''
                    tell application "{result0}"
                        try
                            tell application "System Events"
                                tell process "Dock"
                                    set appIcon to UI element ("{result0}") of list 1
                                    perform action "AXShowMenu" of appIcon
                                    delay 0.2
                                    click menu item "{window_name}" of menu 1 of appIcon
                                    delay 0.2
                                end tell
                            end tell
                        end try
                    end tell'''"""
                    os.system(cmd)
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
        self.onlist = []
        self.hidelist = []

    def all_invisible(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt1.setVisible(False)
        self.bt2.setVisible(False)
        self.bt3.setVisible(False)
        self.bt4.setVisible(False)
        self.bt5.setVisible(False)
        self.bt6.setVisible(False)
        self.bt7.setVisible(False)
        self.bt8.setVisible(False)
        self.bt9.setVisible(False)
        self.bt10.setVisible(False)
        self.bt11.setVisible(False)
        self.bt12.setVisible(False)
        self.bt13.setVisible(False)
        self.bt14.setVisible(False)
        self.bt15.setVisible(False)
        self.bt16.setVisible(False)
        self.bt17.setVisible(False)
        self.bt18.setVisible(False)
        self.bt19.setVisible(False)
        self.bt20.setVisible(False)
        self.widg2.setVisible(False)
        self.widg3.setVisible(False)
        self.widg4.setVisible(False)
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.ultraclick1 = 0
        self.ultraclick2 = 0
        self.ultraclick3 = 0
        self.ultraclick4 = 0
        self.ultraclick5 = 0
        self.ultraclick6 = 0
        self.ultraclick7 = 0
        self.ultraclick8 = 0
        self.ultraclick9 = 0
        self.ultraclick10 = 0
        self.ultraclick11 = 0
        self.ultraclick12 = 0
        self.ultraclick13 = 0
        self.ultraclick14 = 0
        self.ultraclick15 = 0
        self.ultraclick16 = 0
        self.ultraclick17 = 0
        self.ultraclick18 = 0
        self.ultraclick19 = 0
        self.ultraclick20 = 0
        

    def restorebutton(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt1.setDisabled(False)
        self.bt2.setDisabled(False)
        self.bt3.setDisabled(False)
        self.bt4.setDisabled(False)
        self.bt5.setDisabled(False)
        self.bt6.setDisabled(False)
        self.bt7.setDisabled(False)
        self.bt8.setDisabled(False)
        self.bt9.setDisabled(False)
        self.bt10.setDisabled(False)
        self.bt11.setDisabled(False)
        self.bt12.setDisabled(False)
        self.bt13.setDisabled(False)
        self.bt14.setDisabled(False)
        self.bt15.setDisabled(False)
        self.bt16.setDisabled(False)
        self.bt17.setDisabled(False)
        self.bt18.setDisabled(False)
        self.bt19.setDisabled(False)
        self.bt20.setDisabled(False)
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt1.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt2.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt3.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt4.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt5.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt6.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt7.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt8.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt9.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt10.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt11.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt12.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt13.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt14.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt15.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt16.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt17.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt18.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt19.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.bt20.setStyleSheet('''
        QPushButton{
            border: 2px solid #989896;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:hover{
            border: 4px outset black;
            background-color: transparent;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }
        QPushButton:pressed{
            border: 4px outset black;
            background-color: #989896;
            border-radius: 12px;
            padding: 1px;
            color: #000000
        }''')

    def activate(self):  # 设置窗口显示
        if action3.isChecked():
            self.restorebutton()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.everytimefirst()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.show()
            self.center()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.setFocus()
            self.raise_()
            self.activateWindow()
            button_action.setChecked(True)
            self.trax += 1
            self.clicktime = 0
        if not action3.isChecked():
            self.cancel()
            button_action.setChecked(False)

    def key_activate(self):  # 设置窗口显示
        if button_action.isChecked():
            self.restorebutton()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.everytimefirst()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.show()
            self.center()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.setFocus()
            self.raise_()
            self.activateWindow()
            action3.setChecked(True)
            self.trax += 1
            self.clicktime = 0
        if not button_action.isChecked():
            self.cancel()
            action3.setChecked(False)
    
    def tray_activate(self):  # 设置窗口显示
        if self.trax % 2 == 0:
            self.restorebutton()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.everytimefirst()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.show()
            self.center()
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.setFocus()
            self.raise_()
            self.activateWindow()
            button_action.setChecked(True)
            action3.setChecked(True)
            self.clicktime = 0
        if self.trax % 2 == 1:
            QApplication.processEvents()
            QApplication.restoreOverrideCursor()
            self.close()
            self.restorebutton()
            button_action.setChecked(False)
            action3.setChecked(False)
        self.trax += 1

    def center(self):  # 设置窗口居中
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        qr.moveCenter(cp)
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        xy = str(qr.topLeft()).replace('PyQt6.QtCore.QPoint(', '').replace(')', '').split(', ')
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.move(int(xy[0]), int(xy[1]))
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()

    def cancel(self):  # 设置取消键的功能
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        self.close()
        self.restorebutton()
        self.trax += 1

    def keyPressEvent(self, e):  # 当页面显示的时候，按下esc键可关闭窗口
        if e.key() == Qt.Key.Key_Escape.value:
            self.close()


class window4(QWidget):  # Customization settings
    def __init__(self):
        super().__init__()
        self.initUI()
        w3 = MyWidget()

    def initUI(self):  # 设置窗口内布局
        self.setUpMainWindow()
        self.resize(839, 475)
        self.center()
        self.setWindowTitle('Customization settings')
        self.setFocus()

    def setUpMainWindow(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()

        lbl1 = QLabel('Number of side-by-side windows:', self)

        self.le1 = QLineEdit(self)
        ncount = codecs.open('multinum.txt', 'r', encoding='utf-8').read()
        self.le1.setText(ncount)

        QApplication.processEvents()
        QApplication.restoreOverrideCursor()

        lbl2 = QLabel('Apps at running (copy and paste the apps you want to control from this frame to the one below):', self)

        self.te1 = QTextEdit(self)
        resp = applescript.tell.app("System Events", '''
            tell application "System Events"
                set processName to name of processes
                set processDic to processName
                return processDic
            end tell''')
        assert resp.code == 0, resp.err
        runnin = resp.out.replace(', ', '\n')
        runninlist = runnin.split('\n')
        runninlist.sort()
        runnin2 = '\n'.join(runninlist)
        self.te1.setText(runnin2)

        QApplication.processEvents()
        QApplication.restoreOverrideCursor()

        lbl3 = QLabel('Apps to control (one app each line):', self)

        self.te2 = QTextEdit(self)
        home_dir = str(Path.home())
        tarname1 = "OliveAppPath"
        fulldir1 = os.path.join(home_dir, tarname1)
        if not os.path.exists(fulldir1):
            os.mkdir(fulldir1)
        tarname2 = "tarlist.txt"
        fulldir2 = os.path.join(fulldir1, tarname2)
        cont = codecs.open(fulldir2, 'r', encoding='utf-8').read()
        self.te2.setText(cont)

        btn4_1 = QPushButton('Save', self)
        btn4_1.setMaximumHeight(20)
        btn4_1.setMinimumWidth(80)
        btn4_1.clicked.connect(self.saveapps)

        widg1 = QWidget()
        blay1 = QHBoxLayout()
        blay1.setContentsMargins(0, 0, 0, 0)
        blay1.addWidget(lbl1)
        blay1.addWidget(self.le1)
        blay1.addStretch()
        widg1.setLayout(blay1)

        widg2 = QWidget()
        blay2 = QHBoxLayout()
        blay2.setContentsMargins(0, 0, 0, 0)
        blay2.addWidget(lbl2)
        blay2.addStretch()
        widg2.setLayout(blay2)

        widg3 = QWidget()
        blay3 = QVBoxLayout()
        blay3.setContentsMargins(0, 0, 0, 0)
        blay3.addWidget(widg2)
        blay3.addWidget(self.te1)
        widg3.setLayout(blay3)

        widg4 = QWidget()
        blay4 = QHBoxLayout()
        blay4.setContentsMargins(0, 0, 0, 0)
        blay4.addWidget(lbl3)
        blay4.addStretch()
        widg4.setLayout(blay4)

        widg5 = QWidget()
        blay5 = QVBoxLayout()
        blay5.setContentsMargins(0, 0, 0, 0)
        blay5.addWidget(widg4)
        blay5.addWidget(self.te2)
        widg5.setLayout(blay5)

        blay6 = QVBoxLayout()
        blay6.setContentsMargins(20, 20, 20, 20)
        blay6.addWidget(widg1)
        blay6.addWidget(widg3)
        blay6.addWidget(widg5)
        blay6.addWidget(btn4_1)
        self.setLayout(blay6)
        self.mytimer = QTimer(self)
        self.mytimer.timeout.connect(self.onTimer)
        self.last_active_name = None

    def saveapps(self):
        QApplication.processEvents()
        QApplication.restoreOverrideCursor()
        with open('multinum.txt', 'w', encoding='utf-8') as f0:
            f0.write(self.le1.text())

        home_dir = str(Path.home())
        tarname1 = "OliveAppPath"
        fulldir1 = os.path.join(home_dir, tarname1)
        if not os.path.exists(fulldir1):
            os.mkdir(fulldir1)
        tarname2 = "tarlist.txt"
        fulldir2 = os.path.join(fulldir1, tarname2)
        cont = self.te2.toPlainText()
        with open(fulldir2, 'w', encoding='utf-8') as f0:
            f0.write(cont)
        self.close()

    def onrunstart(self):
        if action5.isChecked():
            self.counter = 5
            self.mytimer.start(1000)
        if not action5.isChecked():
            with open('showlist.txt', 'w', encoding='utf-8') as f0:
                f0.write('')

    def onTimer(self):
        if action5.isChecked():
            self.counter -= 1
            #print(str(self.counter))
            active_app = NSWorkspace.sharedWorkspace().activeApplication()
            if active_app:
                if active_app['NSApplicationName'] != self.last_active_name and active_app['NSApplicationName'] == 'Olive':
                    # print('yyy')
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    self.last_active_name = active_app['NSApplicationName']
                    # print(self.last_active_name)
                    self.mytimer.stop()
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    self.onlist = []
                    self.showlist0 = []
                    resp = applescript.tell.app("System Events", '''
                                            tell application "System Events"
                                                set processName to name of processes
                                                set processDic to processName
                                                return processDic
                                            end tell''')
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    assert resp.code == 0, resp.err
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    runlist = resp.out.split(', ')

                    home_dir = str(Path.home())
                    tarname1 = "OliveAppPath"
                    fulldir1 = os.path.join(home_dir, tarname1)
                    if not os.path.exists(fulldir1):
                        os.mkdir(fulldir1)
                    tarname2 = "tarlist.txt"
                    fulldir2 = os.path.join(fulldir1, tarname2)
                    cont = codecs.open(fulldir2, 'r', encoding='utf-8').read()
                    tarlist = cont.split('\n')
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()

                    for i in range(len(tarlist)):
                        QApplication.processEvents()
                        QApplication.restoreOverrideCursor()
                        if tarlist[i] in runlist:
                            QApplication.processEvents()
                            QApplication.restoreOverrideCursor()
                            cmd = f'''
                                                on count_windows_on_current_space(process_name)
                                                    tell application "System Events"
                                                        tell process process_name
                                                            return count of windows
                                                        end tell
                                                    end tell
                                                end count_windows_on_current_space

                                                on name_windows_on_current_space(process_name)
                                                    tell application "System Events"
                                                        tell process process_name
                                                            #return name of windows
                                                            set names to name of windows
                                                            set AppleScript's text item delimiters to "///"
                                                            set strnam to names as text
                                                            return strnam
                                                        end tell
                                                    end tell
                                                end name_windows_on_current_space

                                                tell application "{tarlist[i]}"
                                                    if my count_windows_on_current_space("{tarlist[i]}") > 0 then
                                                        try
                                                            return my name_windows_on_current_space("{tarlist[i]}")
                                                        on error errorMessage
                                                            return "F"
                                                        end try
                                                    end if
                                                end tell'''
                            QApplication.processEvents()
                            QApplication.restoreOverrideCursor()
                            result = subprocess.run(['osascript', '-e', cmd], capture_output=True, encoding='UTF-8')
                            QApplication.processEvents()
                            QApplication.restoreOverrideCursor()
                            if result.stdout != '' and result.stdout != 'F':
                                QApplication.processEvents()
                                QApplication.restoreOverrideCursor()
                                multilist = result.stdout.replace('\n', '').split('///')
                                for n in range(len(multilist)):
                                    QApplication.processEvents()
                                    QApplication.restoreOverrideCursor()
                                    if len(multilist[n]) > 15:
                                        QApplication.processEvents()
                                        QApplication.restoreOverrideCursor()
                                        multilist[n] = multilist[n][0:12] + '\n' + multilist[n][12:]
                                for m in range(len(multilist)):
                                    QApplication.processEvents()
                                    QApplication.restoreOverrideCursor()
                                    multilist[m] = str(tarlist[i]) + '\n~' + str(m + 1) + '~\n' + multilist[m]
                                    self.showlist0.append(multilist[m])

                    showcont = '☆'.join(self.showlist0)
                    with open('showlist.txt', 'w', encoding='utf-8') as f0:
                        f0.write(showcont)
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    self.counter = 5
                    self.mytimer.start(1000)
                    w3.everytimefirst()
                if active_app['NSApplicationName'] != self.last_active_name and self.counter == 0:
                    #print('yyy')
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    self.last_active_name = active_app['NSApplicationName']
                    #print(self.last_active_name)
                    self.mytimer.stop()
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    self.onlist = []
                    self.showlist0 = []
                    resp = applescript.tell.app("System Events", '''
                        tell application "System Events"
                            set processName to name of processes
                            set processDic to processName
                            return processDic
                        end tell''')
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    assert resp.code == 0, resp.err
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    runlist = resp.out.split(', ')

                    home_dir = str(Path.home())
                    tarname1 = "OliveAppPath"
                    fulldir1 = os.path.join(home_dir, tarname1)
                    if not os.path.exists(fulldir1):
                        os.mkdir(fulldir1)
                    tarname2 = "tarlist.txt"
                    fulldir2 = os.path.join(fulldir1, tarname2)
                    cont = codecs.open(fulldir2, 'r', encoding='utf-8').read()
                    tarlist = cont.split('\n')
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()

                    for i in range(len(tarlist)):
                        QApplication.processEvents()
                        QApplication.restoreOverrideCursor()
                        if tarlist[i] in runlist:
                            QApplication.processEvents()
                            QApplication.restoreOverrideCursor()
                            cmd = f'''
                            on count_windows_on_current_space(process_name)
                                tell application "System Events"
                                    tell process process_name
                                        return count of windows
                                    end tell
                                end tell
                            end count_windows_on_current_space
        
                            on name_windows_on_current_space(process_name)
                                tell application "System Events"
                                    tell process process_name
                                        #return name of windows
                                        set names to name of windows
                                        set AppleScript's text item delimiters to "///"
                                        set strnam to names as text
                                        return strnam
                                    end tell
                                end tell
                            end name_windows_on_current_space
        
                            tell application "{tarlist[i]}"
                                if my count_windows_on_current_space("{tarlist[i]}") > 0 then
                                    try
                                        return my name_windows_on_current_space("{tarlist[i]}")
                                    on error errorMessage
                                        return "F"
                                    end try
                                end if
                            end tell'''
                            QApplication.processEvents()
                            QApplication.restoreOverrideCursor()
                            result = subprocess.run(['osascript', '-e', cmd], capture_output=True, encoding='UTF-8')
                            QApplication.processEvents()
                            QApplication.restoreOverrideCursor()
                            if result.stdout != '' and result.stdout != 'F':
                                QApplication.processEvents()
                                QApplication.restoreOverrideCursor()
                                multilist = result.stdout.replace('\n', '').split('///')
                                for n in range(len(multilist)):
                                    QApplication.processEvents()
                                    QApplication.restoreOverrideCursor()
                                    if len(multilist[n]) > 15:
                                        QApplication.processEvents()
                                        QApplication.restoreOverrideCursor()
                                        multilist[n] = multilist[n][0:12] + '\n' + multilist[n][12:]
                                for m in range(len(multilist)):
                                    QApplication.processEvents()
                                    QApplication.restoreOverrideCursor()
                                    multilist[m] = str(tarlist[i]) + '\n~' + str(m + 1) + '~\n' + multilist[m]
                                    self.showlist0.append(multilist[m])

                    showcont = '☆'.join(self.showlist0)
                    with open('showlist.txt', 'w', encoding='utf-8') as f0:
                        f0.write(showcont)
                    QApplication.processEvents()
                    QApplication.restoreOverrideCursor()
                    self.counter = 5
                    self.mytimer.start(1000)
                    w3.everytimefirst()
                if self.counter <= 0:
                    self.counter = 5
                    self.mytimer.start(1000)

    def totalquit(self):
        self.mytimer.stop()
        app.quit()

    def center(self):  # 设置窗口居中
        qr = self.frameGeometry()
        cp = self.screen().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

    def keyPressEvent(self, e):  # 当页面显示的时候，按下esc键可关闭窗口
        if e.key() == Qt.Key.Key_Escape.value:
            self.close()

    def activate(self):  # 设置窗口显示
        resp = applescript.tell.app("System Events", '''
        tell application "System Events"
            set processName to name of processes
            set processDic to processName
            return processDic
        end tell''')
        assert resp.code == 0, resp.err
        runnin = resp.out.replace(', ', '\n')
        runninlist = runnin.split('\n')
        runninlist.sort()
        runnin2 = '\n'.join(runninlist)
        self.te1.setText(runnin2)

        home_dir = str(Path.home())
        tarname1 = "OliveAppPath"
        fulldir1 = os.path.join(home_dir, tarname1)
        if not os.path.exists(fulldir1):
            os.mkdir(fulldir1)
        tarname2 = "tarlist.txt"
        fulldir2 = os.path.join(fulldir1, tarname2)
        cont = codecs.open(fulldir2, 'r', encoding='utf-8').read()
        self.te2.setText(cont)

        self.show()
        self.raise_()
        self.activateWindow()

style_sheet_cha = '''
    QTabWidget::pane {
        border: 1px solid #ECECEC;
        background: #ECECEC;
        border-radius: 9px;
}
    QWidget{
        border: transparent;
        background: transparent;
        border-radius: 20px;
}
    QWidget#Main {
        border: 1px solid #ECECEC;
        background-image:url(back4.png);
        border-radius: 20px;
}
    QWidget#Main:before {
        box-shadow: inset 0 0 2000px rgba(255, 255, 255, .5);
        filter: blur(10px);
}
    QPushButton{
        border: 2px solid #989896;
        background-color: transparent;
        border-radius: 12px;
        padding: 1px;
        color: #000000
}
    QPushButton:hover{
        border: 4px outset black;
        background-color: transparent;
        border-radius: 12px;
        padding: 1px;
        color: #000000
}
    QPushButton:pressed{
        border: 4px outset black;
        background-color: #989896;
        border-radius: 12px;
        padding: 1px;
        color: #000000
}
    QPlainTextEdit{
        border: 1px solid grey;  
        border-radius:4px;
        padding: 1px 5px 1px 3px; 
        background-clip: border;
        background-color: #F3F2EE;
        color: #000000;
        font: 14pt Times New Roman;
}
    QPlainTextEdit#edit{
        border: 1px solid grey;  
        border-radius:4px;
        padding: 1px 5px 1px 3px; 
        background-clip: border;
        background-color: #FFFFFF;
        color: rgb(113, 113, 113);
        font: 14pt Helvetica;
}
    QLineEdit{
        border-radius:4px;
        border: 1px solid gray;
        background-color: #FFFFFF;
}
    QTextEdit{
        border: 1px solid grey;  
        border-radius:4px;
        padding: 1px 5px 1px 3px; 
        background-clip: border;
        background-color: #F3F2EE;
        color: #000000;
        font: 14pt Times New Roman;
}
'''
style_sheet_ori = '''
    QTabWidget::pane {
        border: 1px solid #ECECEC;
        background: #ECECEC;
        border-radius: 9px;
}
    QPushButton{
        border: 1px outset grey;
        background-color: #FFFFFF;
        border-radius: 4px;
        padding: 1px;
        color: #000000
}
    QPushButton:pressed{
        border: 1px outset grey;
        background-color: #0085FF;
        border-radius: 4px;
        padding: 1px;
        color: #FFFFFF
}
    QPlainTextEdit{
        border: 1px solid grey;  
        border-radius:4px;
        padding: 1px 5px 1px 3px; 
        background-clip: border;
        background-color: #F3F2EE;
        color: #000000;
        font: 14pt Times New Roman;
}
    QPlainTextEdit#edit{
        border: 1px solid grey;  
        border-radius:4px;
        padding: 1px 5px 1px 3px; 
        background-clip: border;
        background-color: #FFFFFF;
        color: rgb(113, 113, 113);
        font: 14pt Helvetica;
}
    QLineEdit{
        border-radius:4px;
        border: 1px solid gray;
        background-color: #FFFFFF;
}
    QTextEdit{
        border: 1px solid grey;  
        border-radius:4px;
        padding: 1px 5px 1px 3px; 
        background-clip: border;
        background-color: #F3F2EE;
        color: #000000;
        font: 14pt Times New Roman;
}
'''


if __name__ == '__main__':
    w1 = window_about()  # about
    w2 = window_update()  # update
    w3 = MyWidget()
    w4 = window4()
    action1.triggered.connect(w1.activate)
    action2.triggered.connect(w2.activate)
    action3.triggered.connect(w3.activate)
    action4.triggered.connect(w4.activate)
    action5.triggered.connect(w4.onrunstart)
    button_action.triggered.connect(w3.key_activate)
    tray.activated.connect(w3.tray_activate)
    quit.triggered.connect(w4.totalquit)
    w1.setStyleSheet(style_sheet_ori)
    w2.setStyleSheet(style_sheet_ori)
    w4.setStyleSheet(style_sheet_ori)
    w3.setStyleSheet(style_sheet_cha)
    app.exec()
    