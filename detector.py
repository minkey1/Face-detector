import cv2


trained_data = cv2.CascadeClassifier('face_data.xml')
img = cv2.imread('abc.jpg')
grayed_img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
front_faces= trained_data.detectMultiScale(grayed_img)

for (x,y,w,h) in front_faces:
    cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2)
    print(front_faces)


cv2.imshow('ddd',vid)
cv2.waitKey()