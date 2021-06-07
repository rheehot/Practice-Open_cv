# Joining images

import cv2 as cv
import numpy as np

img_ori = cv.imread("original.jpg")
img = cv.resize(img_ori, dsize=(768,432))

imgHor = np.hstack((img,img))
imgVer = np.vstack((img,img))
cv.imshow('Horizontal',imgHor)
cv.imshow('Vertical',imgVer)

cv.waitKey(0)