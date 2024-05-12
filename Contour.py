import cv2 as cv 
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# a blank image which can be used to draw contours to know the kind of contours openCV finds
blank = np.zeros(img.shape, dtype='uint8')
cv.imshow('Blank', blank)

"""
Contours are basically the boundaries of objects.
The line or curve that joins the continuous points along the boundary of an object. 
But from a mathematical point of view, contours and edges are two different things. 
Contours are useful tools when you get into shape analysis and object detection
and recognition.
"""

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)


## Method - 1
blur = cv.GaussianBlur(gray, (5,5), cv.BORDER_DEFAULT)
cv.imshow('Blur', blur)

#Grabbing edges of image using canny edge detector
canny = cv.Canny(blur, 125, 175)
# canny = cv.Canny(img, 125, 175) 
cv.imshow('Canny', canny)

# finding contour using findContours method returning 2 parameters
# contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_NONE)
contours, hierarchies = cv.findContours(canny, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')
"""
contours - list
len(contours) - tells number of contours
"""

# To draw contours
"""
drawContours Method:
1st parameter - screen on which contour are to drawn
2nd parameter - list of contours
3rd parameter - number of contours you want to draw/see on blank screen, for all we pass -1
4th parameter - colour of which contour to be drawn
5th parameter - thickness of contour to be drawn on blank screen
"""
# cv.drawContours(blank, contours, -1, (0,0,255), 2)
# for better view of contour, thickness rather set to 1:
cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

## Method - 2
"""
Threshold essentially looks at an image and tries to binarize that image. 
example - if the density of a particular pixel is below 125,
it's going to be set to zero or blank. If it is above 125, it is set to white or 255
"""
ret, thresh = cv.threshold(gray, 125, 255, cv.THRESH_BINARY)
cv.imshow('Thresh', thresh)

contours, hierarchies = cv.findContours(thresh, cv.RETR_LIST, cv.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

cv.drawContours(blank, contours, -1, (0,0,255), 1)
cv.imshow('Contours Drawn', blank)

#findContours Method:
"""
Modes in which findContours method find and return contours:
RETR_TREE - if you want all hierarchical contours
RETR_EXTERNAL - if you want only external contours
RETR_LIST - if you want all the contours of the image
"""

"""
Contour approximation method - how we want to approximate contour
CHAIN_APPROX_NONE - does nothing, returns all of the contours
    example - coordinates of all points forming the line
CHAIN_APPROX_SIMPLE - compresses all the contours that are returned into simple one that make more sense
    example - coordiantes of start and end points (only 2 points)
"""

#canny method is recommended over threshold method as we binarizing the image (simplifying a lot)
#as binarizing is the simplest, so its most favourite type of threshold and it does job pretty well in most of the cases
cv.waitKey(0)