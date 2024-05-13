import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/boston.jpg')
cv.imshow('Boston', img)

#using matplotlib library of python for RGB image
#in matplotlib RGB is default image format 
plt.imshow(img)
plt.show()

"""
Color spaces, basically a space of colors, 
a system of representing an array of pixel colors.
For example - RGB, grayscale, HSV, lamb, and manymore.
"""

## BGR to Grayscale
"""
BGR - openCV's default way of reading an image, but outside openCV RGB is used which is inverse of BGR format.
Grayscale images basically show you the distribution of 
pixel intensities at particular locations of your image. 
"""
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

## BGR to HSV
"""
HSV is also called hue saturation value and 
is kind of based on how humans think and conceive color. 
"""
hsv = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.imshow('HSV', hsv)

## BGR to LAB / L*A*B
"""
LAB looks like a washed down version of the BGR image.
LAB is more tuned to how humans perceive color.
"""
lab = cv.cvtColor(img, cv.COLOR_BGR2LAB)
cv.imshow('LAB', lab)

## BGR to RGB
rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
cv.imshow('RGB', rgb)
"""
do keep in mind the inversion of colors that tends to 
take place between these two libraries like here between openCV and matplotlib
"""
plt.imshow(rgb)
plt.show()

## HSV to BGR
hsv_bgr = cv.cvtColor(hsv, cv.COLOR_HSV2BGR)
cv.imshow('HSV-->BGR', hsv_bgr)

cv.waitKey(0)