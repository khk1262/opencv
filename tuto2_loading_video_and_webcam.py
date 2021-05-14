import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    # gray_scale = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # flip_frame = cv2.flip(frame, 0) # 0 : horizontal, 1 : vertical
    # cv2.imshow("gray scale", gray_scale)
    # cv2.imshow("flip" ,flip_frame)

    cv2.imshow("frame", frame)

    key = cv2.waitKey(1) # wait one milisecond
    if key == 27:
        break

cap.release() # 오픈한 cap 객체를 해제하는 것
cv2.destroyAllWindows() #생성한 모든 윈도우 제거