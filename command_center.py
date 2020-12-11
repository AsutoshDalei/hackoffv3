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

def listen():    #This function is to listen to a person talking. This function recognises the word or sentence told by the user.
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Kindly speak now:")
        say("Kindly speak now")
        audio_text = r.listen(source)
        sleep(3)
        print("Time over, thanks")
        try:
            say("Did you say: "+r.recognize_google(audio_text))
            print(r.recognize_google(audio_text))
            return(r.recognize_google(audio_text))
        except:
            say("Sorry, I did not get that")
            return("sorry")

