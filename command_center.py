#This piece of code aims to initiate the lift operation

#Importing all necessary packages : V1
import speech_recognition as sr
r = sr.Recognizer()
from time import sleep
import pyttsx3
engine = pyttsx3.init()
import numpy as np
import cv2
import pyzbar.pyzbar as pyzbar

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

def see_people():    #This piece of code is to see the number of people in the lift.
    cam = cv2.VideoCapture(0)
    #cam = cv2.VideoCapture(r'C:\Users\asuto\Desktop\hackoff_stuff\testingvideo3.mp4')
    #sleep(2)
    while cam.isOpened():
        _ , frame = cam.read()

        frame,text = qrcode(frame)
        cv2.imshow('LiftView', frame)

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
        
    cam.release()
    cv2.destroyAllWindows()

def qrcode(op):  #QR Code scanning part
    pic=op.copy()
    info = pyzbar.decode(pic)
    txt='Unreadable'
    if(len(info)>0):
        for obj in info:
            txt=(obj.data).decode("utf-8")
            (x, y, w, h) = obj.rect
            cv2.rectangle(pic,(x,y),(x+w,y+h),(0,0,255),2)
            #cv2.circle(pic,(x+w//2,y+h//2),3,(255,255,0),-1)
        cv2.putText(pic,txt,(40,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
    return(pic,txt)  

see_people()
