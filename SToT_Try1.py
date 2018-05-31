# -*- coding: utf-8 -*-
"""
Created on Thu May 31 20:14:02 2018

@author: BHANU
"""

import speech_recognition as sr
r=sr.Recognizer()
harvard = sr.AudioFile('harvard.wav')
with harvard as source:
    audio = r.record(source)
type(audio)
r.recognize_google(audio)
print(r)