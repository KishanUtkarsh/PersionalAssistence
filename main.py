import webbrowser as wb
import speech_recognition as sr
import datetime
import system_shutdown_restart as ssr
import pyttsx3 as py
import requests as r


def offline_sound(text):
    engine = py.init()
    rate = engine.getProperty('rate')
    engine.setProperty('rate', 150)  # setting up speed of the voice
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # setting up girls voice for boys voice remove 1 and put 0.
    volume = engine.getProperty('volume')
    engine.setProperty('volume', 1.0)  # setting volume 0 to 1
    engine.say(text)
    engine.runAndWait()
    engine.stop()


def VoiceRecognition(x):
    if 'YouTube' in x:
        A1 = sr.Recognizer()
        url = "https://www.youtube.com/results?search_query="
        with sr.Microphone() as source:
            A1.adjust_for_ambient_noise(source, duration=2)
            offline_sound("speak video name you looking for")
            audio2 = A1.listen(source, timeout=5, phrase_time_limit=5)
            try:
                query = A1.recognize_google(audio2)
                offline_sound("searching your video" + query)
                wb.get().open_new(url + query)

            except:
                offline_sound("Speak properly")

    elif 'Wikipedia' in x:
        A1 = sr.Recognizer()
        url = "https://en.wikipedia.org/wiki/"
        with sr.Microphone() as source:
            A1.adjust_for_ambient_noise(source, duration=2)
            offline_sound("speak your query:")
            audio2 = A1.listen(source, timeout=5, phrase_time_limit=5)
            try:
                query = A1.recognize_google(audio2)
                offline_sound("searching " + query + "on wikipedia")
                wb.get().open_new(url + query)

            except:
                print("Speak properly!!!!!")

    elif 'Python package' in x:
        A1 = sr.Recognizer()
        url = "https://pypi.org/search/?q="
        with sr.Microphone() as source:
            A1.adjust_for_ambient_noise(source, duration=2)
            offline_sound("say your module name")
            audio2 = A1.listen(source, timeout=5, phrase_time_limit=5)
            try:
                query = A1.recognize_google(audio2)
                offline_sound("searching your module " + query)
                wb.get().open_new(url + query)

            except:
                offline_sound("Speak properly!!!!!")

    elif 'Google' in x:
        A1 = sr.Recognizer()
        url = "https://www.google.com/search?q="
        with sr.Microphone() as source:
            A1.adjust_for_ambient_noise(source, duration=2)
            offline_sound("speak your qurries:")
            audio2 = A1.listen(source, timeout=5, phrase_time_limit=5)
            try:
                query = A1.recognize_google(audio2)
                offline_sound("searching " + query)
                wb.get().open_new(url + query)

            except:
                offline_sound("Speak properly!!!!!")

    elif x != "":
        A1 = sr.Recognizer()
        url = "https://www.google.com/search?q="
        try:
            offline_sound("searching" + x + "on google search")
            wb.get().open_new(url + x)
        except:
            pass
    else:
        offline_sound("I am not hearing your voice. please speak or speak louder")


if __name__ == "__main__":
    # setting up a recogniser for converting the voice into the text
    A = sr.Recognizer()
    A1 = sr.Recognizer()
    audio = None
    x = ""

    # Checking the connectivity of the internet
    url = "http://www.google.com"
    timeout = 5
    try:
        request = r.get(url, timeout=timeout)
        offline_sound("sir. you are connected with the internet")
    except(r.ConnectionError, r.Timeout) as exception:
        offline_sound("sir. you are not connected with the internet please check your internet connectivity")
    # Taking the audio from the user
    try:
        with sr.Microphone() as source:
            offline_sound("speak your searching platform")
            print(datetime.datetime.now())
            A.adjust_for_ambient_noise(source, duration=2)  # its recognise the background sound
            offline_sound("listening")
            audio = A.listen(source, timeout=15, phrase_time_limit=20)  # its taking the audio from the user and
            print(datetime.datetime.now())

    except KeyboardInterrupt:  # it is basically cnt+c
        offline_sound("Exiting")

    try:
        x = A.recognize_google(audio)
        print(x)
    except sr.UnknownValueError:
        pass
    y = x.split()

    if x == "shutdown":
        offline_sound("your system is going to shutdown")
        ssr.shutdown(self=True)
    if x == "restart":
        ssr.restart(self=True)
    if x == "hibernate":
        ssr.hibernate(self=True)
    if "about" in y or "abort" in y:
        ssr.abort_shutdown(self=True)

    VoiceRecognition(x)
