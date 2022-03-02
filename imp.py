import cv2 as cv

img = cv.imread("IMAGES/panda.jpg")
cv.imshow("panda", img)

bw = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("black n white", bw)

cv.waitKey(0)