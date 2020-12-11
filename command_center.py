#This piece of code aims to initiate the lift operation

#Importing all necessary packages : V1
import speech_recognition as sr
r = sr.Recognizer()
from time import sleep
import pyttsx3
engine = pyttsx3.init()

def say(r):      #This function based a TTS engine to convert a given text to speech  
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 125)
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[0].id)
    engine.say(r)
    engine.runAndWait()

