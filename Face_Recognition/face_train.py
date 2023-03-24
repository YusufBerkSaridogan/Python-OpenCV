import os
import numpy as np
import cv2 as cv

people = []

for i in os.listdir('Faces/train'):
    people.append(i)

DIR = r'Faces/train'

haar_cascade = cv.CascadeClassifier('Haar/haarcascade_face.xml')

features = []
labels = []

def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        label = people.index(person)

        for image in os.listdir(path):
            image_path = os.path.join(path, image)

            image_array = cv.imread(image_path)
            gray_image_array = cv.cvtColor(image_array,cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray_image_array,1.1,4)

            for (x,y,w,h) in faces_rect:
                faces_roi = gray_image_array[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)

create_train()
print("-------------------Training Completed--------------------------")

features = np.array(features,dtype='object')
labels = np.array(labels)

face_recognizer = cv.face.LBPHFaceRecognizer_create()

#Train the Face Recognizer on the features list and labels
face_recognizer.train(features, labels)

face_recognizer.save('face_trained.yml')
np.save('features.npy', features)
np.save('labels.npy', labels)