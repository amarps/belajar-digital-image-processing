import cv2 
import numpy as np
import matplotlib.pyplot as plt 

url = "http://192.168.43.1:8080/videofeed"

cap = cv2.VideoCapture(url)

while True:
	_, frame = cap.read()
	frame = cv2.resize(frame, (360,240))

	laplacian = cv2.Laplacian(frame, cv2.CV_8U)
	sobelx = cv2.Sobel(frame, cv2.CV_8U, 1, 0, ksize=5)
	sobely = cv2.Sobel(frame, cv2.CV_8U, 0, 1, ksize=5)
	edges = cv2.Canny(frame, 90, 90)

	cv2.imshow("original", frame)
	cv2.imshow("laplacian", laplacian)
	cv2.imshow("sobelx", sobelx)
	cv2.imshow("sobely", sobely)
	cv2.imshow("edges", edges)

	if cv2.waitKey(1) & 0xFF == ord('c'):
		break

cv2.destroyAllWindows()
cv2.release()