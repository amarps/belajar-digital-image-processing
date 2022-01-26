import cv2
import numpy as np

img_bgr = cv2.imread('fp.jpg')
img_bgr = cv2.resize(img_bgr, (1040, 780))
img_gray = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2GRAY)

template = cv2.imread('op.jpg', 0)
template = cv2.resize(template, (42, 43))
w, h = template.shape[::-1]

res = cv2.matchTemplate(img_gray, template, cv2.TM_CCOEFF_NORMED)
threshold = 0.70
loc = np.where(res >= threshold)

for pt in zip(*loc[::-1]):
	cv2.rectangle(img_bgr, pt, (pt[0]+w, pt[1]+h), (0,255,0), 1)

cv2.imshow('deteksi', img_bgr)

cv2.waitKey(0)