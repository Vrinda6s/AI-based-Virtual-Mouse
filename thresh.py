import cv2 as cv 

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

"""
Thresholding is a binarization of an image. In general, we want
to take an image and convert it to a binary image that is an image 
where pixels are either zero or black, or 255 or white. 
We compare each pixel of the image to the threshold of value. If that pixel
intensity is less than the threshold value,we set that pixel intensity to zero. And,
if it is above this threshold value, we set it to 255, or white. 
Therefore, we can create a binary image just from a regular standalone image.
"""

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

## Simple Thresholding
"""
1st parameter - grayscale image which is constant for thresholding
2nd parameter - threshold value
3rd parameter - maxValue at which pixel is be to set, if pixel is greater than threshold value
4th parameter - threshold type

this method return two value:
threshold - it denoted threshold value itself
thresh - thresholded or binarized image
"""
threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)
cv.imshow('Simple Thresholded', thresh)

# inverse of above thresh image (black and white parts of image interchanges)
threshold, thresh_inv = cv.threshold(gray, 150, 255, cv.THRESH_BINARY_INV)
cv.imshow('Simple Thresholded Inverse', thresh_inv)

## Adaptive Thresholding
"""
In advance cases, manually specifying a threshold value like in simple threshold might not work.
So in adaptive thresholding, open CV does that for us using a specific block size, c value etc,
computing the threshold of value on the basis of the mean, or on the basis of the Gaussian distribution.

adaptiveThreshold Method:
1st parameter - grayscale image 
2nd parameter - maxValue
3rd parameter - adaptiveMethod, it tells machine which method to use when computing the optimal threshold value
4th parameter - threshold type
5th parameter - blockSize - it is the neighborhood size of the kernel size, 
                            which openCV needs to use to compute mean to 
                            find the optimal threshold value.
6th parameter - C value - an integer that is subtracted from the mean, 
                        allowing us to fine tune our threshold value.
"""
adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY, 11, 3)
# adaptive_thresh = cv.adaptiveThreshold(gray, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 11, 3)
cv.imshow('Adaptive Thresholding', adaptive_thresh)

cv.waitKey(0)