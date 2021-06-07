# Import image

import cv2 as cv
print("Package Imported")


# img = cv.imread("original.jpg")
# cv.imshow("Original",img)
# cv.waitKey(0)

cap = cv.VideoCapture("Opencv 3original.mp4")
while True:
  success, img = cap.read()
  cv.imshow("Video",img)
  if cv.waitKey(1) & 0xFF ==ord('q'):
    break