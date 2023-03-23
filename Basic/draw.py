import cv2 as cv
import numpy as np

image = cv.imread('Photos/cat.jpg')
blank = np.zeros((500,500,3), dtype='uint8')

#cv.imshow('Cat', image)
cv.imshow('Blank', blank)

#1. Painting the blank
# Setting all pixels in the array to be green

blank[:, :, 0] = 0  # Set blue channel to 0
blank[:, :, 1] = 255  # Set green channel to 255
blank[:, :, 2] = 0  # Set red channel to 0

cv.imshow('Green', blank)


#2. Drawing a Rectangle

cv.rectangle(blank, (0,0),(250,250), (0,0,200),thickness= cv.FILLED)
cv.imshow('Rectangle', blank)


#3. Drawing a Circle
height = blank.shape[0]
width = blank.shape[1]

center_x = height//2
center_y = width//2

cv.circle(blank, (center_x,center_y), 125,(255,0,0),thickness=2 )
cv.imshow('Circle',blank)


cv.waitKey(0)