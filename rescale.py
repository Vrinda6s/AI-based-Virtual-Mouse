# we usually resize and rescale video files and images to prevent computational strain. 
#Large media files tend to store a
#lot of information in it and displaying it takes up a lot of processing needs that your
#computer needs to assign. So by resizing and rescaling, we're actually trying to get rid
#of some of that information. rescaling video implies modifying its height and width to
#a particular height and width. Generally,it's always best practice to downscale or
#change the width and height of your video files to a smaller value than the original
#dimensions. The reason for this is because while most cameras your webcam included, do
#not support going higher than its maximumcapability. So for example, if a camera shoots
#in 720 P, chances are it's not going to beable to shoot in 1080 P or higher. 

import cv2 as cv 

def rescaleFrame(frame, scale=0.75):
    # Work for all Images, Videos, Live Videos
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)

    dimensions = (width, height)

    return cv.resize(frame, dimensions, interpolation=cv.INTER_AREA)

capture = cv.VideoCapture('Videos/dog.mp4')

##resize image:
# img = cv.imread('Photos/cat.jpg')
# resized_image = rescaleFrame(img)
# cv.imshow('Cat', resized_image)

def changeRes(width, height):
    # Work only for Live Videos (does not work with already existing video file)
    capture.set(3, width)
    capture.set(4, height)

while True:
    isTrue, frame = capture.read()

    frame_resized = rescaleFrame(frame, scale=.2)

    cv.imshow('Video', frame)
    cv.imshow('Video', frame_resized)

    if cv.waitKey(20) & 0xff==ord('d'):
        break

capture.release()
cv.destroyAllWindows()