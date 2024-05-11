import cv2 as cv 
import numpy as np

#Now there are two ways, we can draw on images by actually
#drawing on stand alone images like this image of a cat
#or we can create a dummy image or a blank image to work with.

#datatype of an image is 'uint8'
#(500,500,3) = (height, width, number of colour channel)
blank = np.zeros((500,500,3), dtype='uint8')
cv.imshow('Blank', blank)

# 1. Paint the image a certain colour
blank[200:300, 300:400] = 0,0,255
cv.imshow('Green', blank)

# 2. Draw a Rectangle
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness = 2)
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=cv.FILLED)
cv.rectangle(blank, (0,0), (250,250), (0,255,0), thickness=-1)
cv.rectangle(blank, (0,0), (blank.shape[1] // 2, blank.shape[0] // 2), (0,255,0), thickness=-1)
cv.imshow('Rectangle', blank)

# 3. Draw a circle
cv.circle(blank, (blank.shape[1] // 2, blank.shape[0] // 2), 40, (0,0,250), thickness=-1)
cv.imshow('Circle', blank)
# $. Draw a line
cv.line(blank, (0,0), (blank.shape[1] // 2, blank.shape[0] // 2), (255,255,250), thickness=3)
cv.imshow('Line', blank)

# 5. Write text
cv.putText(blank, 'Hello', (225, 225), cv.FONT_HERSHEY_TRIPLEX, 1.0, (255,255,255), 2)
cv.imshow('Text', blank)

cv.waitKey(0)