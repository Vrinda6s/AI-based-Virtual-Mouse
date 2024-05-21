import cv2 as cv

# img = cv.imread('Photos/lady.jpg')
# cv.imshow('Person', img)

# img = cv.imread('Photos/group 2.jpg')
# cv.imshow('Group of 5 people', img)

img = cv.imread('Photos/group 1.jpg')
cv.imshow('Group of  people', img)

"""
Face Detection merely detects the presence of a face in an image, 
while face recognition involves identifying whose face it is.
Face detection is performed using classifiers.
A classifier is essentially an algorithm that decides whether a 
given image is positive or negative, whether a face is present or not.
Essentially,the two main classifiers that exist today
are haarcascades, and a more advanced classifier, local binary patterns.
Face detection does not involve skin tone or the colors that are present in the image. 
These haarcascades essentially look at an object in an image and 
using the edges tries to determine whether it's a face or not. 
"""

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Person', gray)
#CascadeClassifier method read in those 33000 lines present in haar_face.xml file and stores in a variable like here 'haar_cascade'
haar_cascade = cv.CascadeClassifier('haar_face.xml')

"""
detectMultiScale Method:
1st parameter - img in which face has to be detected
2nd parameter - scaleFactor
3rd parameter - minimum neighbors, that specifies the number of neighbors
                rectangle should have to be called a face.
"""
"""
This detectMultiscale is an instance of the cascade classifier class that will take the image, 
use these variables called scale factor and minNeighbours to detect a face and 
return the rectangular coordinates of that face as a list to faces_rect.
As haar cascade is very sensitive to noise in images it may give different count of faces than expected, 
to minimize this sensitivity to noise is by changing the parameters scaleFactor and minNeighbors.
By reducing these parameters we are making haar cascade more prone to noise.
"""
# faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3) # detect more faces
faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=6) # reduces sensitivity detect less faces

#to get number of faces detected in image, print length of faces_rect
print(f'Number of faces found = {len(faces_rect)}')
# print(faces_rect)
for (x,y,w,h) in faces_rect:
    #Here we are looping over this faces_rect list and grabbing the coordinates of the image then drawing a rectangle over the detected faces
    #x,y = top-left vertex coordinate, w,h are width and height of the rectangle
    #to form a rectangle we pass coordinates of two opposite vertices like top-left and bottom-right or other one
    cv.rectangle(img, (x,y), (x+w, y+h), (0,255,0), thickness=2)

# For video, we can detect faces in each frame

cv.imshow('Detected Faces', img)

cv.waitKey(0)