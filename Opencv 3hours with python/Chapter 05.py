# Warp prespective

import cv2 as cv
import numpy as np

original_img = cv.imread("Chapter5_cards.jpg")

width,height = 250,350
pts1 = np.float32([[111,219],[287,188],[154,482],[352,440]])
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
matrix = cv.getPerspectiveTransform(pts1,pts2)
imgOutput = cv.warpPerspective(original_img,matrix,(width,height))


cv.imshow("Image",original_img)
cv.imshow("Output",imgOutput)
cv.waitKey(0)