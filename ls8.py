import cv2
import urllib
import numpy as np

url = "http://192.168.43.1:8080/videofeed"

cap = cv2.VideoCapture(url)

while True:
	_, frame = cap.read()
	frame = cv2.resize(frame, (360,240))
	hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

#	HUE SAT VALUE
	lower_yellow = np.array([150,150,50])
	upper_yellow = np.array([180,255,150])

	mask = cv2.inRange(hsv, lower_yellow, upper_yellow)
	res = cv2.bitwise_and(frame, frame, mask=mask)

	kernel = np.ones((5,5), np.uint8)
	erosion = cv2.erode(mask, kernel, iterations = 1)
	dilation = cv2.dilate(mask, kernel, iterations = 1)

	opening = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
	closing = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)



	cv2.imshow('frame', frame)
	cv2.imshow('res', res)
	cv2.imshow('erosion', erosion)
	cv2.imshow('dilation', dilation)

	if cv2.waitKey(1) & 0xFF == ord('c'):
		break

cv2.destroyAllWindows()
cap.release()