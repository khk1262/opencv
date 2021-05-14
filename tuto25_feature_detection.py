import cv2
import numpy as np

img = cv2.imread("source/the_book_thief.jpeg", cv2.IMREAD_GRAYSCALE)

# sift = cv2.xfeatures2d.SIFT_create()

orb = cv2.ORB_create(nfeatures=1500)

kp, des = orb.detectAndCompute(img, None)

img = cv2.drawKeypoints(img, kp, None)

print(des)

cv2.imshow("Image", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
