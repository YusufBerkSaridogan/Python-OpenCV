import cv2 as cv

img = cv.imread('Photos/basket.jpeg')
resized = cv.resize(img, (650,400))

gray = cv.cvtColor(resized, cv.COLOR_BGR2GRAY)
#cv.imshow("Gray",gray)

haar_cascade = cv.CascadeClassifier('Haar/haarcascade_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=3)

print(f'Number of Faces Found: , {len(faces_rect)}')

for x,y,w,h in faces_rect:
    cv.rectangle(resized,(x,y),(x+w,y+h),(0,255,0),thickness=1)

cv.imshow("Detected Faces",resized)
cv.waitKey(0)