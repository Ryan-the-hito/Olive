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