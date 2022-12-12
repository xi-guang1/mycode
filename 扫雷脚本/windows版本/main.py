import win32
import win32ui
import win32gui
import win32api
import win32con
import numpy as np
from PIL import Image
import pyautogui
import ctypes
import cv2
import os


def get_img(window_name):
    
    path = './images/'
    if not os.path.exists(path):
        # 如果不存在，创建它
        os.makedirs(path)
    
    # 获取软件窗口的句柄
    hwnd = win32gui.FindWindow(None, window_name)

    # 获取软件窗口的设备上下文
    wDC = win32gui.GetWindowDC(hwnd)
    dcObj = win32ui.CreateDCFromHandle(wDC)
    cDC = dcObj.CreateCompatibleDC()

    # 获取软件窗口的位图对象
    dataBitMap = win32ui.CreateBitmap()
    dataBitMap.CreateCompatibleBitmap(dcObj, ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1))
    cDC.SelectObject(dataBitMap)
    cDC.BitBlt((0, 0), (ctypes.windll.user32.GetSystemMetrics(0), ctypes.windll.user32.GetSystemMetrics(1)), dcObj, (0, 0), win32con.SRCCOPY)

    # 保存软件窗口图像
    dataBitMap.SaveBitmapFile(cDC, path + "window_image.bmp")

    # 释放资源
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    
    img = Image.open(path + "window_image.bmp")
    img = img.crop((35,75,205,245))
    img.save(path + "window_image.bmp")

    # 计算每个正方形的尺寸
    square_size = 17

    # 遍历每行每列的正方形
    for row in range(10):
        for col in range(10):
            # 计算左上角和右下角坐标
            left = col * square_size
            top = row * square_size
            right = left + square_size
            bottom = top + square_size

            # 裁剪正方形
            square = img.crop((left, top, right, bottom))

            # 保存正方形
            square.save(path + f'image_{row}_{col}.png')
    
    return path + "window_image.bmp"
    
get_img('扫雷')
