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

	kernel = np.ones((15,5), np.float) / 225
	# smothed = cv2.filter2D(res, -1, kernel)
	# median = cv2.medianBlur(res,15)
	# bilateral = cv2.bilateralFilter(res,15,75,75)

	blur = cv2.GaussianBlur(res, (15,15), 0)

	cv2.imshow('frame', frame)
#	cv2.imshow('mask', mask)
	# cv2.imshow('res', res)
	# cv2.imshow('blur', blur)
	# cv2.imshow('smothed', smothed)
	# cv2.imshow('median', median)
	# cv2.imshow('bilateral', bilateral)

	if cv2.waitKey(1) & 0xFF == ord('c'):
		break

cv2.destroyAllWindows()
cap.release()