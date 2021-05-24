import cv2
# 640 480
count = 0
cap = cv2.VideoCapture(1)                       # 1번 카메라 연결
print('width :%d, height : %d' % (cap.get(3), cap.get(4)))

if cap.isOpened():
    while True:
        ret, frame = cap.read()                 # 카메라 프레임 읽기
        frame = cv2.resize(frame, (640, 480))
        print(frame.shape)
        if ret:
            cv2.imshow('camera',frame)          # 프레임 화면에 표시
            if cv2.waitKey(1) != -1:            # 아무 키나 누르면
                cv2.imwrite(f'photo{count}.jpg', frame) # 프레임을 'photo.jpg'에 저장
                count += 1
                continue
        else:
            print('no frame!')
            break
else:
    print('no camera!')
cap.release()
cv2.destroyAllWindows()