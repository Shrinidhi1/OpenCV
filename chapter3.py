import cv2
import numpy as np

img = np.zeros((512, 512, 3), np.uint8)
#print(img)
#img[:] = 255, 0, 0
#img[200:300, 100:300] = 255, 0, 0

#cv2.line(img, (0, 0), (300, 300), (0, 255, 0), 3) #Starting points; end points; color; thickness
cv2.line(img, (0, 0), (img.shape[1], img.shape[0]), (0, 255, 0), 3)
cv2.rectangle(img, (0,0), (250, 300), (0, 0, 255), 2)
#cv2.rectangle(img, (0,0), (250, 300), (0, 0, 255), cv2.FILLED)

cv2.circle(img, (250, 300), 100, (255, 255, 0), 4) #centre point; radius; color; thickness
cv2.putText(img, "OPENCV", (300, 100), cv2.FONT_HERSHEY_COMPLEX, 0.7, (0, 150, 0), 2) #origin; font; scale; color; thickness

cv2.imshow("Image", img)
cv2.waitKey(0)

