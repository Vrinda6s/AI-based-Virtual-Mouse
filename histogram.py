import cv2 as cv 
import matplotlib.pyplot as plt
import numpy as np

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

"""
Histograms actually allow you to analyze the distribution of pixel
intensities, whether for a grayscale image or for a colored image. 
These are really helpful in a lot of advanced computer vision projects. 
When you actually trying to analyze the image that you get, 
and maybe try to equalize the image so that there's no peeking of pixel
values here and there.
It is like a graph or a plot which will give you 
a high level intuition of the pixel distribution in the image.
"""

blank = np.zeros(img.shape[:2], dtype='uint8')

"""
calHist - This method will compute the histogram for the image that we pass into.
1st parameter - list of images we want to compute histogram of
2nd parameter - index of the image in the list for which histogram has to be computed
3rd parameter - provide mask, if we want to compute histogram for particular part of image (if no masking set None)
4th parameter - histSize is number of bins that we want to use to compute histogram
5th parameter - range of all possible pixel values
"""

## 1. Grayscale Histogram

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

circle = cv.circle(blank, (img.shape[1] // 2, img.shape[0] // 2), 100, 255, -1)
cv.imshow('Circle', circle)

mask = cv.bitwise_and(gray, gray, mask=circle)
cv.imshow('Mask', mask)

gray_hist = cv.calcHist([gray], [0], mask, [256], [0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins') # represent the interval of pixel intensities
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0,256])
plt.show()

## 2. Colour Histogram

plt.figure()
plt.title('Color Histogram')
plt.xlabel('Bins') 
plt.ylabel('# of pixels')

colors = ('b', 'g', 'r')

for i, col in enumerate(colors):
    hist = cv.calcHist([img], [i], mask, [256], [0,256])
    plt.plot(hist, color=col)
    plt.xlim([0,256])

plt.show()

cv.waitKey(0)