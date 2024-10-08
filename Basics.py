import cv2
import numpy as np
import face_recognition

# Loading the images
imgRobert = face_recognition.load_image_file('ImagesBasic/Robert Pattinson.jpg')
imgRobert = cv2.cvtColor(imgRobert, cv2.COLOR_BGR2RGB)
imgTest = face_recognition.load_image_file('ImagesBasic/Robert Pattinson Test.jpg')
# Comment the line above and uncomment the one below to compare the results between 2 robert pattinson and owen wilson.
#imgTest = face_recognition.load_image_file('ImagesBasic/Owen Wilson.jpg')
imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)

# Finding the faces
faceLocation = face_recognition.face_locations(imgRobert)[0]
encodeRobert = face_recognition.face_encodings(imgRobert)[0]
cv2.rectangle(imgRobert, (faceLocation[3],faceLocation[0]), (faceLocation[1],faceLocation[2]), (255,0,255), 2)

faceLocationTest = face_recognition.face_locations(imgTest)[0]
encodeRobertTest = face_recognition.face_encodings(imgTest)[0]
cv2.rectangle(imgTest, (faceLocationTest[3],faceLocationTest[0]), (faceLocationTest[1],faceLocationTest[2]), (255,0,255), 2)

# Comparing the faces and finding the distance between them
results = face_recognition.compare_faces([encodeRobert],encodeRobertTest)
faceDistance = face_recognition.face_distance([encodeRobert],encodeRobertTest)
print(results,faceDistance)
cv2.putText(imgTest ,f'{results} {round(faceDistance[0],2)}' , (50,50) , cv2.FONT_HERSHEY_COMPLEX , 1 , (0,0,255) , 2)

cv2.imshow('Robert Pattinson', imgRobert)
cv2.imshow('Robert Pattinson Test', imgTest)
cv2.waitKey(0)