import cv2 as cv 
import numpy as np

img = cv.imread('Photos/boston.jpg')
cv.imshow('Boston', img)

blank = np.zeros(img.shape[:2], dtype = 'uint8')

#BGR - three color channel blue, green, red merge together, openCV allows us to split image into its color channel
b,g,r = cv.split(img)

cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)


"""
Printing shapes and dimensions of the image, b, g, r.
These are depicted and displayed as grayscale images
that show the distribution of pixel intensities. 
Regions where it's lighter showed that there is a 
far more concentration of those pixel values and regions 
where it's darker, represented a little or even no pixels in that region.
"""
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

merged = cv.merge([b,g,r])
cv.imshow('Merged Image', merged)

"""
To see shape and dimension of b,g,r in b,g,r respectively 
instead of grayscale we use blank image created using numpy 
and then merge them as follows: (use either grayscale or this)
"""
blue = cv.merge([b,blank,blank])
green = cv.merge([blank, g, blank])
red = cv.merge([blank,blank,r])
cv.imshow('Blue', blue)
cv.imshow('Green', green)
cv.imshow('Red', red)

cv.waitKey(0)