import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('Photos/cats.jpg')

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow("Gray",gray)

#Graysclae Histogram

histogram = cv.calcHist([gray], [0], None, [256],[0,256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels ')
plt.plot(histogram)
plt.xlim([0,256])
plt.show()



cv.waitKey(0)