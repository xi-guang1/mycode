
from ui import *
import PyQt5.QtWidgets
import sys

app = PyQt5.QtWidgets.QApplication(sys.argv)
w = PyQt5.QtWidgets.QWidget()

root = Ui_Form()
root.setupUi(w)

w.show()
app.exec()
