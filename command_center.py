#This piece of code aims to initiate the lift operation

#Importing all necessary packages : V1
import speech_recognition as sr
r = sr.Recognizer()
import time
import pyttsx3
engine = pyttsx3.init()
import numpy as np
import cv2
import pyzbar.pyzbar as pyzbar
import firebase_admin
from firebase_admin import credentials, firestore
from multiprocessing import Process


#We initiate the firebase project, through which we can transfer the floor input to the NodeMCU.
#Firebase is being added solely for the purpose of demonstration. Since we working from home.
cred = credentials.Certificate(r"C:\Users\asuto\Desktop\hackoff_stuff\hackoffv3-firebase-adminsdk-4jlgc-e63f6f9a28.json")
firebase_admin.initialize_app(cred)
firestore_db = firestore.client()

def say(r):      #This function based a TTS engine to convert a given text to speech  
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 140)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.say(r)
    engine.runAndWait()

def listen():    #This function is to listen to a person talking. This function recognises the word or sentence told by the user.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Kindly tell your floor number now:")
        say("Kindly tell your floor number now:")
        audio_text = r.listen(source)
        time.sleep(3)
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
    #init_time = time.time()
    t=0
    while cam.isOpened():
        _ , frame = cam.read()
        frame,text = qrcode(frame)
        cv2.imshow('LiftView', frame)
        print(text)
       
        if text != None :
            t+=1
            print(int(text))
            init_time = time.time()
            #if (time.time() - init_time > 10) and int(text) in range(10):
            if t > 35 and int(text) in range(10):
                push(int(text))
                print("sending")
                break
            
            elif t>60 :
                break

        k = cv2.waitKey(30) & 0xff
        if k == 27:
            break
       
    cam.release()
    cv2.destroyAllWindows()

def qrcode(op):  #This piece of code scans for a QR code being shown to it by the user.
    pic=op.copy()
    info = pyzbar.decode(pic)
    txt = None
    if(len(info)>0):
        for obj in info:
            txt=(obj.data).decode("utf-8")
            (x, y, w, h) = obj.rect
            cv2.rectangle(pic,(x,y),(x+w,y+h),(0,0,255),2)
            #cv2.circle(pic,(x+w//2,y+h//2),3,(255,255,0),-1)
        cv2.putText(pic,txt,(40,50),cv2.FONT_HERSHEY_SIMPLEX,2,(0,255,0),3)
    return(pic,txt)  


def push(floor):
    firestore_db.collection(u'floor_level').add({'floor': floor})
    say(f"going to floor {str(floor)}")

def get_data():
    snapshots = list(firestore_db.collection(u'floor_level').get())
    for snapshot in snapshots:
        print(snapshot.to_dict()["floor"])

def recheck():
    say("any other floor?")
    see_people()
#push(13)
#get_data()
#say("please tell or show your required floor number")
see_people()
