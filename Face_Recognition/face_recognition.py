import numpy as np
import cv2 as cv
import os

haar_cascade = cv.CascadeClassifier('Haar/haarcascade_face.xml')
people = []
for i in os.listdir('Faces/train'):
    people.append(i)

#features = np.load('features.npy')
#labels = np.load('labels.npy')

face_recognizer = cv.face.LBPHFaceRecognizer_create()
face_recognizer.read('face_trained.yml')

image = cv.imread('Faces/val/madonna/1.jpg')
gray_image = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

#Detecting the person
face_rect = haar_cascade.detectMultiScale(gray_image,1.1,4)

for (x,y,w,h) in face_rect:
    faces_roi = gray_image[y:y+h, x:x+w]

    label, confidence = face_recognizer.predict(faces_roi)
    print(f"Label {people[label]}, of confidence {confidence}")
    cv.putText(image, str(people[label]), (20,20), cv.FONT_HERSHEY_COMPLEX,1.0, (0,255,0),2)
    cv.rectangle(image, (x,y), (x+w,y+h),(0,255,0),2)

cv.imshow("Detected Face",image)
cv.waitKey(0)
print("-----------------System closed---------------------")