import numpy as np
import cv2

# mengambil gambar
img = cv2.imread('aha.jpeg', cv2.IMREAD_COLOR)

# menggambar garis
cv2.line(img, (0,0), (200,55), (0, 255, 0), 10)
# menggambar persegi
cv2.rectangle(img, (200,200), (400,400), (250, 200, 200), 20)

# menambahkan teks
font = cv2.FONT_HERSHEY_DUPLEX
cv2.putText(img, "Gw Ganteng Banget", (20, 100), font, 1, (20,33,100), 5, cv2.LINE_AA)

cv2.imshow("winname", img)
cv2.waitKey(0)
cv2.destroyAllWindows()