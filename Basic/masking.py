import cv2 as cv
import numpy as np

img = cv.imread('Photos/cat.jpg')

blank = np.zeros((img.shape[:2]),dtype='uint8')

mask = cv.circle(blank, ( (img.shape[0]//2),(img.shape[]//2) ),100,255,-1)

masked = cv.bitwise_and(img, mask, mask=mask)


cv.imshow("Blank",blank)
cv.imshow("Masked",mask)
cv.imshow("Masked Image",masked)


cv.waitKey(0)