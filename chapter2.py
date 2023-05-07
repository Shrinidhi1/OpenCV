import cv2
import numpy as np

img = cv2.imread("Resources/461506.jpg")
print(img.shape) #(height, width, channels

imgResize = cv2.resize(img, (800, 450))
print(imgResize.shape)

imgCrop = img[100:300, 500:800] #[height,width]

cv2.imshow("Output", img)
cv2.imshow("Resized", imgResize)
cv2.imshow("Cropped", imgCrop)
cv2.waitKey(0)