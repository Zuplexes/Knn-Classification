import cv2
import os
cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
name = 'chirasak'
os.makedirs(name, exist_ok=True)
j=1
while True:
    ret, frame = cap.read()
    cv2.rectangle(frame,(250,120),(390,300),(255,0,0),2)
    face = cv2.cvtColor(frame[120:300,250:390,:], cv2.COLOR_BGR2GRAY)
    cv2.imshow('frame', frame)
    cv2.imshow('face', face)
    if cv2.waitKey(1) & 0xFF == ord('s'):
        cv2.imwrite(name+'/'+str(j)+'.jpg', face)
        j+=1