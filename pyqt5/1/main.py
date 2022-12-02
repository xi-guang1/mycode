import sys
import requests
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit

app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('单词查询')
w.setGeometry(0,0,600,450)

btn_1 = QPushButton('查询',w)
edit_1 = QLineEdit(w)

btn_1.setGeometry(0,25,50,20)

w.show()
app.exec()