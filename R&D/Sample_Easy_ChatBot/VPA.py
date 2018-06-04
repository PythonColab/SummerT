import speech_recognition as sr
import pyttsx3
import os
from time import ctime
import time

def SpToTeMic():
    r = sr.Recognizer()
    mic = sr.Microphone()
    stn=""
    while(stn==""):
        with mic as source:
            r.adjust_for_ambient_noise(source)
            print("Say Something")
            audio = r.listen(source)
        try:
            stn=r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Could not understand audio")
        except sr.RequestError as e:
            print("Could not request results; {0}".format(e))
    return stn

def speak(stn):
    import pyttsx3
    engine = pyttsx3.init()
    engine.say(stn)
    engine.runAndWait()

stn=SpToTeMic()
print(stn)
speak(stn)
    
#Take Input From MIC
"""
import speech_recognition as sr
r = sr.Recognizer()
mic = sr.Microphone()
with mic as source:
    print("say Something")
    r.adjust_for_ambient_noise(source)
    audio = r.listen(source)
print(type(audio))   
try:
    print("You said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
"""

#Take Input From Audio File
"""
import speech_recognition as sr
from wave import open as waveOpen
s = sr.AudioFile('HelloBhanu.wav')                                                                       
r = sr.Recognizer()                                                                                   
with s as source:                                                                                   
    audio = r.record(source)
print(type(audio))   
try:
    print("You said " + r.recognize_google(audio))
except sr.UnknownValueError:
    print("Could not understand audio")
except sr.RequestError as e:
    print("Could not request results; {0}".format(e))
"""

#Text To Speech
"""
from gtts import gTTS
from pygame import mixer
tts = gTTS(text='Good morning Bhanu, Whats next?', lang='en')
tts.save("temp.mp3")
mixer.init()
mixer.music.load("temp.mp3")
mixer.music.play()
"""

#Text To Speech 2nd Method
"""
import pyttsx3
engine = pyttsx3.init()
engine.say('Good morning.')
engine.runAndWait()
print("Hello")
"""

#Run Command
"""
import os
os.system("explorer /root,")
os.system("explorer BhanuScrapyTry")
"""
