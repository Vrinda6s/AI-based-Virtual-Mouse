import cv2 as cv 
import numpy as np 

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

"""
Masking essentially allows us to focus on certain parts of an
image that we'd like to focus on. So for example, if you have an image of people in it, and
you're interested in focusing on the faces of those people, you could essentially apply
masking and mask over the people's faces and remove all the unwanted parts of the image. 
Using the bitwise operations, we can perform masking in openCV.
"""
#**The dimensions of the mask have to be the same size as that of the image.If it isn't, it will not work.**

# Example 1
blank1 = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank1 Image', blank1)

mask1 = cv.circle(blank1, (img.shape[1]//2,img.shape[0]//2), 100, 255, -1)
mask1 = cv.rectangle(blank1, (img.shape[1]//2-100,img.shape[0]//2+100), (img.shape[1]//2+100,img.shape[0]//2+200), 255, -1)
cv.imshow('Mask1', mask1)

masked_img1 = cv.bitwise_and(img,img,mask=mask1)
cv.imshow('Masked Image1', masked_img1)

# Example 2
blank2 = np.zeros(img.shape[:2], dtype='uint8')
cv.imshow('blank2 Image', blank2)

rectangle = cv.rectangle(blank2.copy(), (30,30), (370,370), 255, -1)
circle = cv.circle(blank2.copy(), (img.shape[1]//2 + 45,img.shape[0]//2), 100, 255, -1)
mask2 = cv.bitwise_and(circle, rectangle)
cv.imshow('Mask2', mask2)

masked_img2 = cv.bitwise_and(img,img,mask=mask2)
cv.imshow('Masked Image2', masked_img2)

cv.waitKey(0)