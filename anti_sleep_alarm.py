import numpy as np
import playsound
import time
import cv2


fixed_length = 30
fixed_width = 14.5

alarm = r"C:\Users\91635\Downloads\emergency.mp3"

focal_length_measured = 400

cap = cv2.VideoCapture(0)
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')
count = 0


def play_alarm():
    playsound.playsound(r'C:\Users\91635\Downloads\emergency.mp3')

#  The width of the face w decides which face to capture
#  As width increases distance decreases
#  choose the frame which has less distance or more width


def face_(faces,gray):
    for(x,y,h,w) in faces:
        if len(faces)>1:
            vector1 = faces[:1,:]
            vector2 = faces[1:,:]
            distance1 = (vector1[0,3])   
            distance2 = (vector2[0,3])
            #print(distance1)
            #print(distance2)
            
            if(distance1 > distance2):
                face = vector1   
            else:
                face = vector2


while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray , 1.3, 5)
    face=faces[:1]
    #print(face)
    face_(faces , gray)
    if len(face)!=0 :
        for(x,y,h,w) in face:
            cv2.rectangle(frame , (x , y) , (x + w , y + h), (255,0,0) , 5)
            roi_gray = gray[y:y+h , x:x+w]
            roi_color = frame[y:y+h , x:x+w]
            eyes = eye_cascade.detectMultiScale(roi_gray , 1.3 , 5 )
            if len(eyes) >= 2 :

                for(x1 , y1 , h1 ,w1) in eyes:
                    cv2.rectangle(roi_color , (x1 , y1) , (x1 + w1 , y1 + h1), (0,255,0) , 5)
                    count=0
            else:
                ##begin = time.time()
                ##end  = time.time()
                ##elapsed_time = end - begin
                ##elapsed_time = int(elapsed_time)
                count = count + 1
                print(count)
                if count > 200 :
                    cv2.putText(frame,"person is sleeping",(50,50),cv2.FONT_HERSHEY_SIMPLEX , 1 ,(0,255,0),2)
                    play_alarm()

                 
                    

    cv2.imshow('frame',frame)

    if(cv2.waitKey(1) == ord('b')):
        break

cap.release()
cv2.destroyAllWindows()