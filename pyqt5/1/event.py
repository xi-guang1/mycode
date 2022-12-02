from requests import get
from PyQt5.QtWidgets import QMessageBox
from main import w

def click(word):
    res = get(f'http://api.tangdouz.com/fy.php?nr={word}')
    QMessageBox.information(w,'asas',res)