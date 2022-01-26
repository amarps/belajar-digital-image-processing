import cv2
import numpy as np

img = cv2.imread("kocheng1.jpg")
retval, threshold = cv2.threshold(img, 100, 255, cv2.THRESH_BINARY)

grayscale = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
retval2, threshold2 = cv2.threshold(grayscale, 100, 255, cv2.THRESH_BINARY)

gaus = cv2.adaptiveThreshold(grayscale, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)
retval3, otsu = cv2.threshold(grayscale, 125, 255, cv2.THRESH_BINARY+cv2.THRESH_OTSU)

cv2.imshow("img", img)
cv2.imshow("th2", threshold2)
cv2.imshow("gaus", gaus)
cv2.imshow("khon", threshold)
cv2.imshow("otsu", otsu)
cv2.waitKey(0)
cv2.destroyAllWindow()