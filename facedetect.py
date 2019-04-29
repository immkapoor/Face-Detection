# -*- coding: utf-8 -*-
"""

@author: Meghna
"""

import cv2
face_cascade = cv2.CascadeClassifier('C:\\Users\\Meghna\\AppData\\Local\\Programs\\Python\\Python37-32\\opencv\\sources\\data\\haarcascades\\haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('C:\\Users\\Meghna\\AppData\\Local\\Programs\\Python\\Python37-32\\opencv\\sources\\data\\haarcascades\\haarcascade_eye.xml')

imgo = cv2.imread('bb.jpg')
img  = cv2.resize(imgo,(1200,950))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

faces = face_cascade.detectMultiScale(gray, 1.32,3)
for (x,y,w,h) in faces:
    img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    eyes = eye_cascade.detectMultiScale(roi_gray,1.01,6)
    for (ex,ey,ew,eh) in eyes:
        cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)
print("No of faces found ", len(faces))
cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()