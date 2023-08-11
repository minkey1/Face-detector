import cv2
from random import randrange
import numpy as np
trained_data = cv2.CascadeClassifier('face_data.xml')
webcam = cv2.VideoCapture(0)
text = ("Gay","Horny","Normie","Chutiya","Perfect"," ")
choice = randrange(6)
img = cv2.imread('clown1.png')
alpha = 0



while True:
    suc, frame = webcam.read()
    if choice == 0:
        color = (randrange(256),randrange(256),randrange(256))
    else:
        color = (0,0,255)
    grayframe = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    front_faces= trained_data.detectMultiScale(grayframe)

    if choice == 5:
        for (x,y,w,h) in front_faces:
                logo = cv2.resize(img, (w, w))
                rows,cols,channels = logo.shape
                added_image = cv2.addWeighted(frame[y:y+rows,x:x+cols],alpha,logo,1-alpha,0)
                # Change the region with the result
                frame[y:y+rows,x:x+cols] = added_image

    else:
            (x,y,w,h) = front_faces[0]
            cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)
            cv2.putText(frame,text[choice],(x+w,y),cv2.FONT_HERSHEY_SIMPLEX,1,color,3)
        



    cv2.imshow('Bencho',frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
webcam.release()