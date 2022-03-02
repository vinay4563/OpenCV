import cv2 as cv
import numpy as np

#img = cv.imread('IMAGES/panda.jpg')
#cv.imshow('Panda', img)

blank = np.zeros((500,500,3), dtype = 'uint8')
cv.imshow('Blank', blank)

#img = cv.imread('blank') 
cv.rectangle(blank, (100,200), (500,500), (0,255,0), thickness=2)
cv.imshow("Rectangle", blank)


cv.circle(blank, (250,250), )
cv.waitKey(0)