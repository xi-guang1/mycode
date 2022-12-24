# import win32
# import win32ui
import win32gui as gui
# import win32api
# import win32con
import numpy as np
# from PIL import Image
from check import getunknow,getaround
import pyautogui as pag
# import ctypes
import cv2
import os

unknow = np.array([255,255,255])
zero = np.array([192,192,192])
one = np.array([255,0,0])
two = np.array([0,128,0])
three = np.array([0,0,255])



board = [[],
         [],
         [],
         [],
         [],
         [],
         [],
         [],
         []]


class number():
    def __board__(self,num = 0,mine = 0,unknow = 0) -> None:
        self.num = num
        self.mine = mine
        self.unknow = unknow


def click_mine(board,unknow):
    global known,mine
    for row in range(9):
        for col in range(9):
            around = getaround(row,col)
            if board[row][col] == unknow[row][col] and board[row][col] != 0:
                for place in around:
                    if board[place[0]][place[1]] == 9 and known[place[1]][place[0]] == 0:
                        click(x,y,place[1],place[0],'right')
                        mine += 1
                        
                        
def click_other(board):
    global known
    for row in range(9):
        for col in range(9):
            around = getaround(row,col)
            around_mine = 0
            for place in around:
                if known[place[1]][place[0]] == 1:
                    around_mine += 1
            if around_mine == board[row][col]:
                for place in around:
                    if known[place[1]][place[0]] == 0 and board[place[0]][place[1]] == 9:
                        # print(board[place[1]][place[0]])
                        click(x,y,place[1],place[0],'left')
            # print(f'{row}-{col} {around_mine}')


def click(x,y,row,col,button):
    global known
    if known[row][col] == 0:
        pag.moveTo(x + row * 16,y + col * 16)
        pag.click(clicks = 1, button = button)
        if button == 'right':
            known[row][col] = 1
        elif button == 'left':
            known[row][col] = 0


def get_board(board):
    board = [[],
             [],
             [],
             [],
             [],
             [],
             [],
             [],
             []]
    path = './images/'
    if not os.path.exists(path):
        # 如果不存在，创建它
        os.makedirs(path)
    
    handle = gui.FindWindow(None, "扫雷")
    gui.SetForegroundWindow(handle)

    x0, y0, x1, y1 = gui.GetWindowRect(handle)
    x0, y0 = x0 + 15, y0 + 101
    x1, y1 = x1 - x0, y1 - y0 
    img = pag.screenshot(region=[x0,y0,x1,y1])
    
    img.save(path + "window_image.bmp")

    # 计算每个正方形的尺寸
    square_size = 16

    # 遍历每行每列的正方形
    
    for row in range(9):
        for col in range(9):
            board[row].append(0)
            # 计算左上角和右下角坐标
            left = col * square_size
            top = row * square_size
            right = left + square_size
            bottom = top + square_size

            # 裁剪正方形
            square = img.crop((left, top, right, bottom))
            # 保存正方形
            square.save(path + f'{row+1}-{col+1}.png')
            
            square = cv2.imread(path + f'{row+1}-{col+1}.png')
            if (square[7][7] == one).all():
                board[row][col] = 1
            elif (square[7][7] == two).all():
                board[row][col] = 2
            elif (square[7][7] == three).all():
                board[row][col] = 3
            elif (square[1][1] == zero).all():
                board[row][col] = 0
            else:
                board[row][col] = 9
                
            
    return board,x0+8,y0+8
 
mine = 0
known = [[0 for i in range(9)] for j in range(9)]

while mine < 10:
    board,x,y = get_board(board)
    unknow = getunknow(board,[9])
    click_mine(board,unknow)
    click_other(board)
    # print(mine)
# click_other(board)
# print(board)
# print(unknow)
# print(known)
# print(getunknow(board))
# input()