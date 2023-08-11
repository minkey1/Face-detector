import cv2
trained_data = cv2.CascadeClassifier('face_data.xml')
webcam = cv2.VideoCapture(0)
color = (0,255,0)

while True:
    suc, frame = webcam.read()
    grayframe = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    front_faces= trained_data.detectMultiScale(grayframe)

    for (x,y,w,h) in front_faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)
        cv2.putText(frame,'Face Detected',(x,y-2),cv2.FONT_HERSHEY_SIMPLEX,1,color,2)


    cv2.imshow('ddd',frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
webcam.release()
