import cv2

try:
    from cv2 import cv2
except ImportError:
    pass

img = cv2.imread("source/cards.jpg") # 디렉토리에서 이미지를 읽음
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

## 일반적으로 아래 3개는 같이 사용
cv2.imshow("gray card", gray_img) #회색 이미지
cv2.imshow("card", img) #불러온 이미지를 보여주기 위한 창 설정, 제목
cv2.waitKey(0) # 창이 켜지고 유지되도록, 키입력이 있으면 끝
cv2.destroyAllWindows() # 이미지 윈도우 삭제
