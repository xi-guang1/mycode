import cv2
import os


file_list = []

def eachFile(filepath):
    pathDir =  os.listdir(filepath)
    for allDir in pathDir:
        child = os.path.join(f'{filepath}\{allDir}')
        if not os.path.isdir(child):
            file_list.append(child)

eachFile(r"C:\Users\lxq860404\Desktop\picture")

face_cascade = cv2.CascadeClassifier("haarcascade_eye.xml")
for path in file_list:
# 加载图片及检测器：
    try:
        img = cv2.imread(path)
        dsize = (500, int(500*img.shape[0]/img.shape[1]))
        img = cv2.resize(img, dsize)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    except Exception as err:
        print(err)
        continue

    # 5. 检测人脸：
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # 在图片上绘制矩形框：
    if not len(faces):
        continue
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)

    # 显示图片：
    cv2.imshow('video', img)
    cv2.waitKey(0)