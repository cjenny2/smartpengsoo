import numpy as np
import cv2
import speech_recognition as sr
import spsmusic
import spshi

music_start = '노래'
hi_start = '인사'
retry = '다시'
order = ['명령:','입력완료']
CapTure = '사진'
End='종료'

faceCascade = cv2.CascadeClassifier('ha/haarcascade_frontalface_default.xml')
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
            cv2.destroyAllWindows()
        k = cv2.waitKey(1) & 0xff
        if k == 27:
            break
    elif checkid==1:
        with sr.Microphone() as source:
            r.adjust_for_ambient_noise(source)
            print(order[0])
            audio_text = r.listen(source)
            try:
                print(order[1])
                r2=r.recognize_google(audio_text,language='ko-KR')
                print(r2)
                if r2==music_start:
                    music = spsmusic.music()
                elif r2==hi_start:
                    hi=spshi.hi()
                    hi.start()
                elif r2==CapTure:
                    cap = cv2.VideoCapture(0)
                    ret, frame = cap.read()
                    cv2.imshow('divx', frame)
                    cv2.imwrite("c.jpg",frame)
                    cap.release()
                elif r2==End:
                    break
            
            except:
                print(retry)



