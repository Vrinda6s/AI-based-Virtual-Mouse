import cv2 as cv 
import numpy as np 

"""
There are four basic bitwise operators AND, OR, XOR and NOT.
They are used a lot in image processing, especially when we're working with masks.
At a very high level bitwise operators operate in a binary manner. 
So a pixel is turned off if it has a value of zero,
and is turned on if it has a value of one. 
"""

blank = np.zeros((400,400), dtype = 'uint8')

rectangle = cv.rectangle(blank.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank.copy(), (200,200), 200, 255, -1)

cv.imshow('Rectangle', rectangle)
cv.imshow('Circle', circle)

## 1. bitwise AND --> intersecting regions
bitwise_and = cv.bitwise_and(rectangle, circle)
cv.imshow('Bitwise AND', bitwise_and)

## 2. bitwise OR --> non-intersecting and intersecting regions
bitwise_or = cv.bitwise_or(rectangle, circle)
cv.imshow('Bitwise OR', bitwise_or)

## 3. bitwise XOR --> non-intersecting regions
bitwise_xor = cv.bitwise_xor(rectangle, circle)
cv.imshow('Bitwise XOR', bitwise_xor)

## 4. bitwise NOT --> inverts the binary color
bitwise_not = cv.bitwise_not(rectangle)
cv.imshow('Rectangle NOT', bitwise_not)

bitwise_not = cv.bitwise_not(circle)
cv.imshow('Circle NOT', bitwise_not)

cv.waitKey(0)