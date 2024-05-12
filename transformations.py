import cv2 as cv 
import numpy as np

img = cv.imread('Photos/boston.jpg')

cv.imshow('Boston', img)

## 1. Translation
"""
Translation is basically shifting an image along the 
x and y axis. So using translation, you can shift an image
up, down, left, right, or with any combination of the above.

x and y basically stands for the number of pixels, 
you want to shift along the x axis and the y axis respectively.

    -x --> Left
    -y --> Up
    x --> Right
    y --> Down
"""

def translate(img, x, y):
    transMat = np.float32([[1,0,x], [0,1,y]])
    #(width, height)
    dimensions = (img.shape[1], img.shape[0])
    return cv.warpAffine(img, transMat, dimensions)

translated = translate(img, 100, 100)
#translated = translate(img, -100, 100)
cv.imshow('Translated', translated)

## 2. Rotation
"""
Rotation is exactly what it sounds like rotating
an image by some angle. Open CV allows you to specify
any rotation point that you'd like to rotate the image around.
Usually the center but with open CV, you could
specify any arbitrary point it could be any corner, 
it could be 10 pixels to the right and 40 pixels down, 
and you can shift the image around that point. 
"""
def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]

    if rotPoint is None:
        #assume to rotate around center
        rotPoint = (width // 2, height // 2)
    
    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)

#rotated = rotate(img, 45) anticlockwise
rotated = rotate(img, -45) #clockwise
cv.imshow('Rotated', rotated)
#while rotating rotated image, we rotate black triangles too with the 
"""
when you took this rotated image and rotated it by 45 degrees, 
you essentially rotated the image, but introduce the black triangles too.
Now if you tried to rotate this image further by some angle, you are also
trying to rotate these black triangles alongwith it. So that's why you get these kind
of a skewed image. So the additional triangles are included over here. 
"""
rotated_rotated = rotate(rotated, -45)
cv.imshow('Rotated Rotated', rotated_rotated)

#Rather do:
rotated_rotated_right = rotate(img, -90)
cv.imshow('Rotated Rotated Right', rotated_rotated_right)

## 3. Resizing
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

## 4. Flipping 
"""
0 --> flipping image vertically that is over x axis
1 --> flipping image horizontally that is over y axis (mirror images)
-1 --> flipping both vertically and horizontally (reverse mirror images)
"""
flip = cv.flip(img, 0)
cv.imshow('Flip', flip)

## 5. Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
