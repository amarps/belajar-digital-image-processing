import cv2
import numpy as np

# mengambil video dari webcam // 0 adalah jumlah kamera
cap = cv2.VideoCapture(0)

fourcc = cv2.VideoWriter_fourcc(*'XVID')
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while True:
# return sama frame // membaca file
	ret, frame = cap.read()
	
# menulis file yang akan disimpan
	out.write(frame)
# mengkonvert warna
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

# menampilkan file // nama file, file
	cv2.imshow("kontol", frame)
	cv2.imshow("gray", gray)

# break ketika menekan key c
	if cv2.waitKey(1) & 0xFF == ord('c'):
		break

# menyimmpan file
cap.release()
out.release()
# menutup semua window
cv2.destroyAllWindows()