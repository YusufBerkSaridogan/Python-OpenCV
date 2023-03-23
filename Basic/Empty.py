import cv2 as cv

image = cv.imread('Photos/lady.jpg')
image2 = cv.imread('Photos/lady.jpg',0)

resized = cv.resize(image,(500,500),(250,250))

gray = cv.cvtColor(resized,cv.COLOR_BGR2GRAY)

blurred = cv.blur(resized,(7,7),cv.BORDER_DEFAULT)

canny = cv.Canny(resized,100,100)

dilated = cv.dilate(canny,(7,7),iterations=2)

erodding = cv.erode(dilated, (7,7),iterations=3)

threshold, thresh = cv.threshold(gray, 150, 255, cv.THRESH_BINARY)

cv.imshow("Threshold",thresh)


#cv.imshow("Gray2",image2)
#cv.imshow("Normal",image)
#cv.imshow("Gray",gray)
#cv.imshow("Blur",blurred)
#cv.imshow("Resized",resized)
#cv.imshow("Canny",canny)
#cv.imshow("Dilated",dilated)
#cv.imshow("Eroded",erodding)



cv.waitKey(0)
