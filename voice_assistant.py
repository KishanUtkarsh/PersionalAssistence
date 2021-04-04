import pyttsx3 as py


def offline_sound(sound):
    engine = py.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)  # setting up speed of the voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # setting up girls voice for boys voice remove 1 and put 0.
    volume = engine.getProperty('volume')
    engine.setProperty('volume', 1.0)  # setting volume 0 to 1
    engine.say(sound)
    engine.runAndWait()
    engine.stop()


def assistant(text):
    if "hello" in text.split() and "how" in text.split() and "are" in text.split() and "you" in text:
        offline_sound("I am fine boss. i am very thankful for this")

