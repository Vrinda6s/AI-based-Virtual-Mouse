import cv2 as cv 
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

## Laplacian 
lap = cv.Laplacian(gray, cv.CV_64F) # 2nd parameter - ddepth - data depth
"""
When you do transition from black to white and white to black, 
that's considered a positive and a negative slope. Now, images itself cannot
have negative pixel values. So what we do is we essentially compute the absolute value
of that image. So all the pixel values of the image are converted to the absolute values.
And then we convert that to a uint8 an image specific datatype.
"""
lap = np.uint8(np.absolute(lap))
cv.imshow('Laplacian', lap)

## Sobel - computes gradients in two direction x and y
sobelx = cv.Sobel(gray, cv.CV_64F, 1, 0)
sobely = cv.Sobel(gray, cv.CV_64F, 0, 1)
combined_sobel = cv.bitwise_or(sobelx, sobely)

cv.imshow('Sobel X', sobelx)
cv.imshow('Sobel Y', sobely)
cv.imshow('Combined Sobel', combined_sobel)

canny = cv.Canny(gray, 150, 175)
cv.imhow('Canny', canny)

# compare laplacian, combined sobel and canny method

cv.waitKey(0)