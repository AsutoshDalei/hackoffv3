#This piece of code aims to initiate the lift operation

#Importing all necessary packages : V1
import speech_recognition as sr
r = sr.Recognizer()
from time import sleep
import pyttsx3
engine = pyttsx3.init()
import numpy as np
import cv2

def say(r):      #This function based a TTS engine to convert a given text to speech  
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 125)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(r)
    engine.runAndWait()

def listen():    #This function is to listen to a person talking. This function recognises the word or sentence told by the user.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Kindly tell your floor number now:")
        say("Kindly tell your floor number now:")
        audio_text = r.listen(source)
        sleep(3)
        print("Time over, thankyou")
        try:
            say("Floor is:"+r.recognize_google(audio_text))
            print(r.recognize_google(audio_text))
            return(r.recognize_google(audio_text))
        except:
            say("Sorry, I did not get that")
            return("sorry")

def see_people():
    classifier = cv2.CascadeClassifier(r'C:\Users\asuto\Desktop\hackoff_stuff\haarcascade_fullbody.xml')
    cam = cv2.VideoCapture(0)
    while True:
        ret , frame = cam.read()
        sleep(3)
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        m=[] 
        bodies = classifier.detectMultiScale(gray, 1.1, 3)
        m.append(bodies)
        for (x,y,w,h) in bodies:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 255), 3)
            cv2.putText(frame,len(m),(5,5),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,255,0),2)
            cv2.imshow('people', frame)
            
        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break

        cam.release()
        cv2.destroyAllWindows()

see_people()
