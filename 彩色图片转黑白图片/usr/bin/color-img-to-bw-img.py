#!/usr/bin/python3

import sys
from PySide6.QtWidgets import QApplication,QMainWindow
from ui_MainWindow import Ui_MainWindow

app = QApplication()
MainWindow = QMainWindow()
root = Ui_MainWindow()

root.setupUi(MainWindow)

MainWindow.show()
sys.exit(app.exec_())