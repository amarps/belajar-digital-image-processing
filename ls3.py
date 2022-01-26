import cv2
import numpy as np

img = cv2.imread('aha.jpeg', cv2.IMREAD_COLOR)

img[100:150, 100:150] = [255,255,255]

# sumbu y - sumbu x
muka_spongebob = img[10:300, 300:500]
img[0:290,0:200] = muka_spongebob

cv2.imshow('imges', img)

cv2.waitKey(0)
cv2.destroyAllWindows()