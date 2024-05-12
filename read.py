import cv2 as cv 
##Photos:
#this method basically takes in a path to An image and returns that image as a matrix of pixels.
img = cv.imread('Photos/cat_large.jpg')
#this method displayes the image as new window
cv.imshow('Cat', img)
##Videos:
#Instance of video capture class
capture = cv.VideoCapture('Videos/dog.mp4')
#we read the video frame by frame
while True:
    isTrue, frame =  capture.read()
    cv.imshow('Video', frame)
    #to stop video playing indefinetely
    #if letter 'd' is pressed then break out of the loop and stop playing the video
    if cv.waitKey(20) & 0xff==ord('d'):
        break
capture.release()
cv.destroyAllWindows()
"""
keyboard binding function, it waits for a specific delay, or time in milliseconds for a key to be pressed. 
So if you pass in zero, it basically waits for an infinite amountof time for a keyboard key to be pressed.
"""
cv.waitKey(0)
