# 一键扫雷
import win32gui
import win32process
import win32api
import ctypes
import win32con
import time
 
# 获取窗口句柄
window_handle = win32gui.FindWindow(None, "扫雷")
 
# 获取窗口坐标
left, top, right, bottom = win32gui.GetWindowRect(window_handle)
#print("窗口坐标：")
#print(str(left)+' '+str(right)+' '+str(top)+' '+str(bottom))
 
# 点击窗口函数
def click(x,y):
    win32api.SetCursorPos([x, y])
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)
    #time.sleep(0.5)
 
 
left = left + 6
top = top + 107
 
# 获取进程ID
process_id = win32process.GetWindowThreadProcessId(window_handle)[1]
 
# 获取进程句柄
process_handle = win32api.OpenProcess(0x1F0FFF, False, process_id)
 
# 调用系统内核
kernel32 = ctypes.windll.LoadLibrary("C:\Windows\System32\kernel32.dll")
 
# 读取内存
# 获取区域高度
height = ctypes.c_long()
kernel32.ReadProcessMemory(int(process_handle), 0x01005338, ctypes.byref(height), 4, None)
print(height)
 
# 获取区域宽度
width = ctypes.c_long()
kernel32.ReadProcessMemory(int(process_handle), 0x01005334, ctypes.byref(width), 4, None)
print(width)
 
# 打印每个格子的地址
def print_address(list):
    print('格子内存地址如下:')
    for i in list:
        print(i)
 
# 起始地址
s = 16798561 #Ox1005361
n = 0
lei = 0
list = []
 
for y in range(0,height.value):
    a = []
    for x in range(1,width.value+1):
        # 获取当前内存的值
        m = s + (x-1) + y*32
        n += 1
        #print("0x0%02x" % m)
        data = ctypes.c_long()
        kernel32.ReadProcessMemory(int(process_handle), m, ctypes.byref(data), 4, None)
        #print(hex(data.value))
        #print(hex(data.value)[-2:])
        a.append(hex(data.value))
 
        # 点击不是雷的
        if(hex(data.value)[-2:] != '8f' and hex(data.value)[-2:] != '8a' and hex(data.value)[-2:] != '71'):
            pass
            #print(hex(data.value))
            click(left + x*16, top + y*16)
            #print('点击了第{}行{}列'.format(y+1,x),hex(data.value))
        else:
            lei += 1
    list.append(a)
 
print_address(list)
print('扫雷结束')
print('共有{}个块,{}个雷'.format(n,lei))