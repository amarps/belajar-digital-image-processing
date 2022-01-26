import cv2
import numpy as np

img1 = cv2.imread('kocheng1.jpg')
img2 = cv2.imread('kocheng2.jpg')

add = img1 + img2*2
add1 = cv2.addWeighted(img1, 0.6, img2, 0.4, 0)
add2 = cv2.add(img1, img2)

cv2.imshow("add", add)
cv2.imshow("add1", add1)
cv2.imshow("add2", add2)

cv2.waitKey(0)
cv2.destroyAllWindows()