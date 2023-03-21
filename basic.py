import cv2 as cv

image = cv.imread('Photos/park.jpg')
cv.imshow('Cat', image)
#Converting Graysclae
gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
cv.imshow('Gray Cat',gray_image)

#Adding Blur
blur = cv.GaussianBlur(image, (7,7), cv.BORDER_DEFAULT)
cv.imshow("Blur", blur)

#Edge Cascade
canny = cv.Canny(image,125,125)
canny2 =cv.Canny(blur,125,125)
cv.imshow("Edges",canny)
cv.imshow("Edges2",canny2)

#Dillatting Images
dillated = cv.dilate(canny2, (7,7),iterations=3)
cv.imshow("Dillated",dillated)

#Eroding Images
erodding = cv.erode(dillated, (7,7),iterations=3)
cv.imshow("Eroded",erodding)

#Resizing
resized = cv.resize(erodding, (125,125), interpolation=cv.INTER_AREA)
cv.imshow("Resized",resized)
#If you going to resize a smaller image "INTER_AREA" for larger "INTER_LINER" or "INTER_CUBIX"

#Cropping a Image
cropped = image[50:200,50:200]
cv.imshow("Cropped",cropped)

cv.waitKey(0)