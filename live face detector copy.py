import cv2
trained_data = cv2.CascadeClassifier('face_data.xml')
webcam = cv2.VideoCapture(0)



while True:
    suc, frame = webcam.read()
    color = (0,255,0)
    grayframe = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    front_faces= trained_data.detectMultiScale(grayframe)


    for (x,y,w,h) in front_faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),color,2)
        cv2.putText(frame,'Face Detected',(x,y),cv2.FONT_HERSHEY_SIMPLEX,1,color,3)
        



    cv2.imshow('ddd',frame)
    key = cv2.waitKey(1)
    if key == 27:
        break
webcam.release()