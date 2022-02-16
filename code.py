import cv2 as cv

img = cv.imread('IMAGES/tree.jpg')

cv.imshow('Tree', img)

def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height= int(frame.shape[0] * scale)
    dimensions=(width, height)
    
     return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)


# Reading videos

abc = cv.VideoCapture('videos/dog.mp4')

while True:
   isTrue, frame = abc.read()

   frame_resized = rescaleFrame(frame)

   cv.imshow('video', frame)
   cv.imshow('video resized',frame_resized)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

abc.release()
cv.destroyAllWindows

cv.waitKey()