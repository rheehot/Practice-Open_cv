# Color detection

import cv2 as cv
import numpy as np

img_ori = cv.imread("original.jpg")
img = cv.resize(img_ori, dsize=(768,432))

cv.imshow('Original',img)
cv.waitKey(0)