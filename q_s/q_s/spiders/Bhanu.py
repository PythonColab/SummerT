import speech_recognition as sr
from time import ctime
import time
import os
from pygame import mixer
import pyttsx3
import pygame
from tkinter import *

print("Hi I am Jarvis, Whats Your Name : ")
name=input("Enter The Name : ")

window = Tk()
window.title("JARVIS")
window.geometry('750x400')
filename = PhotoImage(file = "jar3.png")
background_label = Label(window, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
logo = PhotoImage(file="jar2.gif")
lb1 = Label(window, text="JARVIS",height=3,bg="Black",fg="RED",font=("Times",12))
lb1.grid(column=0, row=0,columnspan=4)
lb2 = Label(window,anchor="nw",text="Click Speak for Starting",height=15,width=65,borderwidth=4, relief="sunken",justify=LEFT,bg="Cyan",fg="GREEN")
lb2.configure(font=("Comic Sans MS",8))
lb2.grid(column=0, row=1)
lb3 = Label(window,height=2)
lb3.grid(row=2)
def p(res):
    text = lb2.cget("text") +"\n"+res
    lb2.configure(text=text)
def speak(audioString):
    p(audioString)
    time.sleep(6)
    engine = pyttsx3.init()
    engine.say(audioString)
    engine.runAndWait()
     
def recordAudio():
    r = sr.Recognizer()
    speak("Say something!")
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio)
        p("You said: " + data)
    except sr.UnknownValueError:
        lb2.configure(fg="RED")
        p("Speech Recognition could not understand audio")
    except sr.RequestError as e:
        lb2.configure(fg="RED")
        p("Could not request results from Speech Recognition service; {0}".format(e))
     
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
def clicked():
    lb2.configure(fg="GREEN")
    lb2.configure(text="")
    data = txt.get()
    jarvis(data,name)
def clicked1(name):
    lb2.configure(fg="GREEN")
    lb2.configure(text="")
    speak("Hi "+name+", what can I do for you?")
    data = recordAudio()
    jarvis(data,name)
btn = Button(window, text="SPEAK", command= lambda: clicked1(name),width=50,height=3,bg="BLUE",fg="WHITE")
btn.grid(column=0, row=3,rowspan=3)
lb4 = Label(window,image=logo)
lb4.grid(row=1,column=2,columnspan=2)
txt = Entry(window,width=40,bg="RED",fg="WHITE")
txt.grid(column=2,row=3)
btn1 = Button(window, text="Enter", command=clicked,width=30,bg="BLUE",fg="WHITE")
btn1.grid(column=2, row=5)
window.mainloop()
