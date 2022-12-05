import sys
from requests import get
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QLineEdit, QMessageBox


headers={
 "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36 Edg/97.0.1072.55"
    }


def click():
    global headers
    res = get(f'http://api.tangdouz.com/fy.php?nr={edit_1.text()}',headers=headers)
    res.encoding = 'utf-8'
    QMessageBox.information(w,'查询结果',res.text)


app = QApplication(sys.argv)
w = QWidget()
w.setWindowTitle('查询单词')
w.setGeometry(0,0,600,450)

btn_1 = QPushButton('查询',w)
edit_1 = QLineEdit(w)

btn_1.setGeometry(0,25,50,20)
btn_1.clicked.connect(click)

w.show()
app.exec()