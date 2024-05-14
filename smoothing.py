import cv2 as cv 

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

"""
We generally smooth an image when it tends to have a lot of noise,
maybe caused from camera sensors or problems in lighting when the image was taken.
We can reduce this noise or smooth out the image by applying some blurring method 
like gaussian blur method.
"""


## 1. Averaging
"""
Averaging is we define a kernel window over a specific portion of an image, this window
will essentially compute the pixel intensity of the middle pixel (of the true center) as
the average of the surrounding pixel intensities. 
Kernel size = rowNum x colNum (kind of tictactoe matrix)
higher the kernel size more will be the blur
"""
average = cv.blur(img, (3,3))
cv.imshow('Average Blur', average)

## 2. Gaussian Blur

"""
Gaussian basically does the same thing as averaging, except that 
instead of computing the average of all of the running pixel intensity, 
each running pixel is given a particular weight. And essentially, 
the average of the products of those weights gives you the value for the true center. 
Now using this method, you tend to get less blurring than compared to the averaging method. 
But the Gaussian Blur is more natural as compared to averaging.
"""
gauss = cv.GaussianBlur(img, (3,3), 0)
cv.imshow('Gaussian Blur', gauss)
#SigmaX (3rd parameter) - standard deviaton in the x direction

## 3. Median Blur
"""
Median blurring is basically the same thing as averaging, except that instead of 
finding the average of the surrounding pixels, it finds the median of the surrounding pixels. 
Generally, median blurring tends to be more effective in reducing noise in an image as compared to averaging
and even Gaussian Blur. And it's pretty good at removing some salt and pepper noise that
may exist in the image. In general, people tend to use this image in advanced computer
vision projects that tend to depend on the reduction of substantial amount of noise.
Generally not meant for high kernel sizes
"""
# here we pass 3 as a parameter instead of (3,3) because openCV itself assume that kernel size is 3x3 just based on given integer
median = cv.medianBlur(img, 3)
cv.imshow('Median Blurring', median)

## 4. Bilateral Blur
"""
Bilateral blurring is the most effective, and sometimes used in a lot of advanced 
computer vision projects, essentially because of how it blurs. Now traditional blurring methods 
basically blur the image without looking at whether you're reducing edges in the image or not.
Bilateral blurring applies blurring but retains the edges in the image. 
So you have a blurred image, but you get to retain the edges as well. 
"""
"""
d (2nd parameter) is not kernel size instead is a diameter
sigmaColor (3rd parameter) - larger values of this color sigma means that there are more colors
                            in the neighborhood, that will be considered when the blur is computed. 
sigmaSpace (4th parameter) - larger values of this space sigma means that pixels further out from 
                            the central pixel will influence the blurring calculation.
"""
bilateral = cv.bilateralFilter(img, 5, 15, 15)
cv.imshow('Bilateral Blurring', bilateral)

cv.waitKey(0)