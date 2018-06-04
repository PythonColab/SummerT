from gtts import gTTS
from pygame import mixer
tts = gTTS(text='Good morning Bhanu, Whats next?', lang='en')
tts.save("temp.mp3")
mixer.init()
mixer.music.load("temp.mp3")
mixer.music.play()
