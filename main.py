import numpy as np
import cv2
import speech_recognition as sr
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0) # 웹캠 설정
cap.set(3, 960) # 영상 가로길이 설정
cap.set(4, 480) # 영상 세로길이 설정
checkid=0
r = sr.Recognizer()
while True:
    if checkid==0 :
        ret, frame = cap.read() 
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray,1.2,5)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(255,0,0),2)
            roi_gray = gray[y:y+h, x:x+w]
            roi_color = frame[y:y+h, x:x+w]
            if w*h>=60000:
                checkid=1
        cv2.imshow('divx', frame)
        if checkid==1:
            print("접속")
            cv2.destroyAllWindows()
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break
    elif checkid==1:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print("명령입력")
            audio_text = r.listen(source)
            print("입력완료")
            try:
                print(r.recognize_google(audio_text,language='ko-KR'))
                #모든 명령은 여기서 결정합니다.
            except:
                print("제대로 말해주시죠?")
        
cap.release() 
cv2.destroyAllWindows()
