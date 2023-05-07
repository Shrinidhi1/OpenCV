import cv2
import numpy as np
#img = cv2.imread("Resources/276575.jpg")
#cv2.imshow("Output", img)
#cv2.waitKey(0)

#cap = cv2.VideoCapture("Resources/sampleVideo.mp4")

#cap = cv2.VideoCapture(0)
#cap.set(3, 640) #Height
#cap.set(4, 480) #Width
#cap.set(10, 100) #Brightness

#while True:
#    success, img = cap.read()
#    cv2.imshow("Video", img)
#    if cv2.waitKey(1) & 0xFF == ord('q'):
#        break

img = cv2.imread("Resources/461506.jpg")
kernel = np.ones((5,5), np.uint8)

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (7, 7), 0) #Kernel size for blurriness, has to be odd numbers; Sigma(x) value
#Edge Detector
imgCanny = cv2.Canny(img, 150, 200) #Threshold values
imgDilation = cv2.dilate(imgCanny, kernel, iterations=2) #iterations=thickness
imgErode = cv2.erode(imgDilation, kernel, iterations=2)

cv2.imshow("Gray", imgGray)
cv2.imshow("Blur", imgBlur)
cv2.imshow("Canny", imgCanny)
cv2.imshow("Dilation", imgDilation)
cv2.imshow("Eroded", imgErode)
cv2.waitKey(0)

