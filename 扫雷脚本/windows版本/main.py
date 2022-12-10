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


def get_img(window_name):
    
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
    dataBitMap.SaveBitmapFile(cDC, "window_image.bmp")

    # 释放资源
    dcObj.DeleteDC()
    cDC.DeleteDC()
    win32gui.ReleaseDC(hwnd, wDC)
    win32gui.DeleteObject(dataBitMap.GetHandle())
    
    img = cv2.imread("window_image.bmp")
    print(img.shape)
    
    return "window_image.bmp"
    
img = get_img('扫雷')
print(img)