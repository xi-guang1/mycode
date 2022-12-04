#!/usr/bin/python3

import sys
import PyQt5.QtWidgets
from ui import *

app = PyQt5.QtWidgets.QApplication(sys.argv)
w = PyQt5.QtWidgets.QWidget()

root = Ui_Form()
root.setupUi(w)

w.show()
app.exec()
