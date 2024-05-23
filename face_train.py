import os
import cv2 as cv 
import numpy as np

# We need os for looping over directory

# M - 1
people = ['Ben Afflek', 'Elton John', 'Jerry Seinfield', 'Madonna', 'Mindy Kaling']
DIR = r'C:\Users\lenovo\OneDrive\Documents\OpenCV\train' # base folder which has folders containing images

haar_cascade = cv.CascadeClassifier('haar_face.xml')

# M - 2
# people = []
# for i in os.listdir(r'C:\Users\lenovo\OneDrive\Documents\OpenCV\train'):
#     people.append(i)

# print(people)

features = [] # image array of faces
labels = [] # which face belongs to whom
"""
create_train function will loop over every folder in the base folder. 
And inside that folder, it's going to loop over every image and 
grab the face in that image and add that to our training set.
"""
def create_train():
    for person in people:
        path = os.path.join(DIR, person)
        """
        the idea behind converting a label to numerical values is reducing the strain that our
        computer will have, by creating some sort of mapping between a string and the numerical label.
        """
        label = people.index(person)

        for img in os.listdir(path):
            img_path = os.path.join(path, img)

            img_array = cv.imread(img_path)
            gray = cv.cvtColor(img_array, cv.COLOR_BGR2GRAY)

            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=4)

            for (x,y,w,h) in faces_rect:
                # roi - region of interest
                faces_roi = gray[y:y+h, x:x+w]
                features.append(faces_roi)
                labels.append(label)
create_train()
print('Training Done!')

# print(f'Length of the features = {len(features)}')
# print(f'Length of the labels = {len(labels)}')

# Before using features and labels list for training we need to convert them to numpy array
features = np.array(features, dtype='object')
labels = np.array(labels)

# instantiate face recognizer
face_recognizer = cv.face.LBPHFaceRecognizer_create() 

# Train the Recognizer on the features list and the labels list
face_recognizer.train(features, labels)

"""
openCV allows us to save this trained model so that we can use it in another file or in another directory 
just by using that particular YML source file, rather than manually repeating this whole process of 
adding those images to a list and getting the corresponding labels, and then converting that to NumPy arrays, 
and then training all over again and again whenever we want to use the model.
"""
face_recognizer.save('face_trained.yml')

np.save('features.npy', features)
np.save('labels.npy', labels)