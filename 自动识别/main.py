# 1. 导入库：
import cv2
import time

# 2. 加载检测器：
dataPath = r"test\trainData\haarcascade_eye.xml"
face_cascade = cv2.CascadeClassifier(dataPath)
 # 打开摄像头
cap = cv2.VideoCapture(0) 

while True:
    startTime = time.time()
	# 开始用摄像头读数据，返回hx为true则表示读成功，frame为读的图像
    hx, frame = cap.read() 
    
    # 如果hx为Flase表示开启摄像头失败
    if not hx:
    	# 打印报错
        print('摄像头启动失败')
        # 退出程序
        exit(0)
    # 4. 转换为灰度图像：
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 5. 检测人脸：
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    # 6. 在图片上绘制矩形框：
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)

    # 7. 显示图片：
    # 显示摄像头图像，其中的video为窗口名称，frame为图像
    cv2.imshow('video', frame)
    
    # 监测键盘输入是否为q，为q则退出程序
    if cv2.waitKey(1) & 0xFF == ord('q'):       # 按q退出
        break

    print(f"FPS:{int(1//(time.time()-startTime))}")

# 释放摄像头
cap.release()

# 结束所有窗口
cv2.destroyAllWindows() 


'''
# 4. 转换为灰度图像：
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 5. 检测人脸：
faces = face_cascade.detectMultiScale(gray, 1.3, 5)

# 6. 在图片上绘制矩形框：
for (x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+h),(255,0,0),2)

# 7. 显示图片：
cv2.imshow("Faces found", image)
cv2.waitKey(0)
'''