import pynput
import pyautogui as pag
import cv2



res = []
def screenshot(x,y,a,b):
    global res
    # print(x,y,a,b)
    if b & (len(res) < 4):
        x,y = pag.position()
        res.append(x)
        res.append(y)


def get_pos():
    global res
    with pynput.mouse.Listener(on_click=screenshot) as lsn:
        while len(res) != 4:
            continue
        x1,y1,x2,y2 = res
        if x1 == x2 | y1 == y2:
            print('')
            return get_pos()
        if x1 < x2:
            if y1 < y2:
                res = [x1,y1,x2-x1,y2-y1]
            else:
                res = [x1,y2,x2-x1,y1-y2]
        else:
            if y1 < y2:
                res = [x2,y1,x1-x2,y2-y1]
            else:
                res = [x2,y2,x1-x2,y1-y2]
        return res
    


path = "扫雷脚本/1.png"
img = pag.screenshot(region=get_pos())
img.save(path)
img_read = cv2.imread(path)
