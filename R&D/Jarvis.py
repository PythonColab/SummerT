import speech_recognition as sr
from time import ctime
import time
import os
from pygame import mixer
import pyttsx3
import pygame
 
def speak(audioString):
    engine = pyttsx3.init()
    engine.say(audioString)
    print(audioString)
    engine.runAndWait()
 
def recordAudio():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        print("Say something!")
        audio = r.listen(source)
    print('Recognizing.....')
    data = ""
    try:
        data = r.recognize_google(audio)
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
 
    return data
 
def jarvis(data,name):
    if "how are you" in data:
        speak("I am fine")
 
    if "what time is it" in data:
        speak(ctime())
 
    if "where is" in data:
        data = data.split(" ")
        location = str(data[2])
        speak("Hold on "+name+", I will show you where " + location + " is.")
        os.system("start chrome \"www.google.nl/maps/place/" + location + "/&amp;\"")

    if "open Chrome" in data:
        speak("Hold on "+name+", Opening Chrome")
        os.system("start chrome \"www.google.com\"")

    if "search" in data:
        str1 = data.strip('search')
        speak("Hold on "+name+", Opening Chrome")
        os.system("start chrome \"https://www.google.co.in/search?q="+str1+"\"")

    if "play music" in data:
        speak("Hold on "+name+", Playing Music")
        pygame.init()
        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.play()

    

time.sleep(2)
speak("Hi I am Jarvis, Whats Your Name : ")
numa=input("Choose Input Method:\n1. Form MIC\n2. From Keyboard \n: ")
if(numa=='1'):
    name=recordAudio()
elif(numa=='2'):
    name=input("Enter The Name : ")
print("Initializing.../.")
speak("Hi "+name+", what can I do for you?")
while 1:
    data = recordAudio()
    jarvis(data,name)
