import random
import sys
from MainWindow import MainWindow
import PyQt5.QtWidgets
import PySide6.QtWidgets


def poem_cloud(file = sys.stdout):
    b = int(input("生成多少首诗"))
    for j in range(b):
        # print(f"\n第{j+1}首：",file=file)
        for a in range(4):
            for i in range(5):
                u1 = random.randint(0x4e00, 0x9fbf)
                # print(chr(u1),end='',file=file)
            # print(file=file)


def word_cloud(file = sys.stdout):
    b = int(input("生成多少个词"))
    for j in range(b):
        for i in range(2):
            u1 = random.randint(0x4e00, 0x9fbf)
            print(chr(u1),end='',file=file)
        # print(file=file)
            
            
with open(r"test\test.txt","a+",encoding='utf-8') as f:
    word_cloud(f)

app = PySide6.QtWidgets.QApplication(sys.argv)
root = PySide6.QtWidgets.QMainWindow()

MainWindow = MainWindow(root)

root.show()
sys.exit(app.exec_())