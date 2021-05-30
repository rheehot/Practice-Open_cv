# Basic function

import cv2 as cv
import numpy as np

original_img = cv.imread("original.jpg")
img = cv.resize(original_img, dsize=(768,432))
kernel = np.ones((5,5),np.uint8)

imgGray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
imgBlur = cv.GaussianBlur(imgGray,(7,7),0)
imgCann = cv.Canny(img,150,200)
imgDial = cv.dilate(imgCann,kernel,iterations=1)
imgErod = cv.erode(imgDial,kernel,iterations=1)

cv.imshow("Gray Image",imgGray)
cv.imshow("Blur Image",imgBlur)
cv.imshow("Cann Image",imgCann)
cv.imshow("Dial Image",imgDial)
cv.imshow("Erod Image",imgErod)
cv.waitKey(0)