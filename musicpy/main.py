#!/usr/bin/python3

import sys
import PyQt5.QtWidgets
import PySide6.QtWidgets
from ui_MainWindow import *
from typing import *
from event import *
from musicpy import *
from ui_messagebox import *
from lib import *


n = 1/4
nd = 1/4 + 1/8
_ = 1/8

# 
# note_lst = str_to_list('2 2 2 3 7.. 6.. 5.. 3.. 6.. 6.. 5.. 5.. 6.. 1 2 3 5 4 3 3 5 4 5 6 3 2 1 2 3 2')
# durlst = ([_,_,_,_,] + [n,n,n,n] + [nd+n] + [nd]) * 2 + [_,_+_,_+_,_,_] + [n,_,_+_,_+_] + [n]
# durlst_1 = ([_,_,_,_,] + [0,n,0,n] + [0] + [nd]) * 2 + [_,_+_,_+_,_,_] + [n,_,_+_,_+_] + [n]

# 两只老虎
# note_lst = str_to_list("1. 2. 3. 1. 1. 2. 3. 1. 3. 4. 5. 3. 4. 5. 5. 6. 5. 4. 3. 1. 5. 6. 5. 4. 3. 1. 2. 5 1. 2. 5 1.")
# durlst = [n,] * 8 + [n, n, nd + _,] *2 + [_,_,_,_,n,n,] * 2 + [n, n, nd + _,] *2

# 小星星
# note_lst = str_to_list("1 1 5 5 6 6 5 4 4 3 3 2 2 1 5 5 4 4 3 3 2 5 5 4 4 3 3 2 1 1 5 5 6 6 5 4 4 3 3 2 2 1")
# durlst = ([n,n,] * 3 + [nd + _]) * 6

# 义勇军进行曲
# note_lst = str_to_list("5.. 1 1 1 1 5.. 6.. 7.. 1 1")
# durlst = [_,] + [nd, _,] + [_, _, _, _ , _] + [n, n,]

# 国际歌
# note_lst = str_to_list("5 1. 7 2. 1. 5 3 6 6 4 6 2. 1. 7 6 5 4 3")
# durlst = [n] + [nd, _, _, _, _, _, ] + [nd , _, n + _, _] + [nd, _, _, _, _, _] + [n*3]

# print(len(note_lst),len(durlst))
# play(chord(note_lst, durlst, durlst_1), 120, name='musicpy/temp.mid')


app = PySide6.QtWidgets.QApplication(sys.argv)
main_window = PySide6.QtWidgets.QMainWindow()

root = Ui_MainWindow()
root.setupUi(main_window)

main_window.show()
app.exec()
