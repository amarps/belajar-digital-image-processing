# ROI == region of image
# daerah dari gambar

import cv2 
import numpy as np

img1 = cv2.imread('aha.jpeg')
img2 = cv2.imread('aja.jpg')

# mengambil baris, kolom dan channels dari gambar ke 2
rows, cols, channels = img2.shape
# mendifine region of image
roi = img1[0:rows, 0:cols]

# mengkonvert gambar menjadi abu
img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
# membuat treshold gambar
ret, mask = cv2.threshold(img2gray, 170, 255, cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

# menggunakan operator bitwise pada gambar
img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)
img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

dst = cv2.add(img1_bg, img2_fg)
img1[0:rows,0:cols] = dst

cv2.imshow("img1", img1)
cv2.imshow("mask_inv", mask_inv)
cv2.imshow("img1_bg", img1_bg)
cv2.imshow("img2_fg", img2_fg)
cv2.imshow("dst", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()