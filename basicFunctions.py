import cv2 as cv 

img = cv.imread('Photos/boston.jpg')
# this is bgr image

cv.imshow('Boston', img)

# Converting an image to grayscale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray', gray)

## 1. Blur
"""
Now blurring an image essentially removes some of the noise that exists in an
image. For example, in an image, there maybe some extra elements that were there because
of bad lighting when the image was taken,or maybe some issues with the camera sensor
and so on. And some of the ways we can actually reduce this noise is by applying a slight
blur.
"""
blur = cv.GaussianBlur(img, (3,3), cv.BORDER_DEFAULT)
blur = cv.GaussianBlur(img, (7,7), cv.BORDER_DEFAULT)
"""
ksize (2nd parameter) - kernel size, which is actually a two by two 
tuple which is basically the window size that open cv
uses to compute the blown the image.(has be an odd number)
increasing this increases blur
"""
cv.imshow('Blur', blur)

## 2. Edge Cascade
"""
Here we're going to use the canny edge detector, 
which is pretty famous in the computer vision world. 
Essentially, it's a multi step process that involves 
a lot of blurring and then involves a lot of grading 
computations and stuff like that.
"""
canny = cv.Canny(img, 125, 175)
cv.imshow('Canny', canny)
#For less edges in canny img: passing blur instead of img
cannyBlur = cv.Canny(blur, 125, 175)
cv.imshow('CannyBlur', cannyBlur)

## 3. Dilating the image
dilated = cv.dilate(cannyBlur, (7,7), iterations=3)
cv.imshow('Dilated', dilated)

## 4. Eroding
eroded = cv.erode(dilated, (7,7), iterations=3)
#eroded = cv.erode(dilated, (3,3), iterations=1)
cv.imshow('Eroded', eroded)

## 5. Resize
# cubic is slowest among all, but the img quality is of much higher than other
resized = cv.resize(img, (500,500), interpolation=cv.INTER_AREA)
resized = cv.resize(img, (500,500), interpolation=cv.INTER_LINEAR)
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

## 6. Cropping 
"""
that's basically by utilizing the fact that images are arrays. 
And we can employ something called Array Slicing, we can select
a portion of the image on the basis of the pixel values.
"""
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)

cv.waitKey(0)
