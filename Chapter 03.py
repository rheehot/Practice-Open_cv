# Resizing and cropping

import cv2 as cv

img = cv.imread("original.jpg")
print(img.shape)

imgResize = cv.resize(img, dsize=(768,432))
print(imgResize.shape)

cv.imshow("Image Resize",imgResize)
cv.waitKey(0)