# import pyttsx3 as py
#
# engine = py.init()
# rate = engine.getProperty('rate')
# engine.setProperty('rate',150)
# voices = engine.getProperty('voices')
# engine.setProperty('voice', voices[1].id)
# engine.say("hello kishan you are my boss "+"how can i help you")
# engine.runAndWait()
import pyaudio
from gtts import gTTS
import os
tts = gTTS(text='welcome kishan how can i help you', lang='en')
tts.save("hello.mp3")
os.system("hello.mp3")
