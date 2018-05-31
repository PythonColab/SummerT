# -*- coding: utf-8 -*-
"""
Created on Thu May 31 20:14:02 2018

@author: BHANU
"""
"""
import speech_recognition as sr
r=sr.Recognizer()
harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.record(source)
print(audio)
r.recognize_google(audio,key='xxx', 'en-US', show_all=False)
print(r)


"""
import speech_recognition as sr

r = sr.Recognizer()

harvard = sr.AudioFile('harvard.wav')

# Read audio data
with harvard as source:
    audio_source = r.record(source)  # read the entire audio file

# Speech Recognition
text = r.recognize_google(audio_source,'xxx', 'en-US',False)