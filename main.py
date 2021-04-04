import webbrowser as wb
import speech_recognition as sr
import datetime
import system_shutdown_restart as ssr
import pyttsx3 as py
import requests as r
from englisttohindi.englisttohindi import EngtoHindi
import voice_assistant as vs
from gtts import gTTS
from playsound import playsound


def engtohin(english_text):
    print("hello kishan")
    eng_text = EngtoHindi(english_text)
    hin_text = eng_text.convert
    myobj = gTTS.hin_text
    myobj.save("hello.mp3")
    playsound('hello.mp3')


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


def VoiceRecognition(text):
    if 'translator' in text:
        A1 = sr.Recognizer()
        with sr.Microphone() as source:
            A1.adjust_for_ambient_noise(source, duration=2)
            offline_sound("speak your word")
            audio2 = A1.listen(source, timeout=5, phrase_time_limit=5)
            try:
                #query = A1.recognize_google(audio2)
                engtohin("cat")
                #print(query)
                print("kishan")
            except:
                print("lol")
                offline_sound("Speak Properly")

    elif 'YouTube' in text:
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

    elif 'Wikipedia' in text:
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
                offline_sound("Speak properly!!!!!")

    elif 'Python package' in text:
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

    elif 'Google' in text:
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

    elif text != "":
        A1 = sr.Recognizer()
        url = "https://www.google.com/search?q="
        try:
            offline_sound("searching" + text + "on google search")
            wb.get().open_new(url + text)
        except:
            pass
    else:
        offline_sound("I am not hearing your voice. please speak or speak louder")


if __name__ == "__main__":
    # setting up a recogniser for converting the voice into the text
    A = sr.Recognizer()
    A1 = sr.Recognizer()
    A2 = sr.Recognizer()
    audio = None
    text = ""

    # Checking the connectivity of the internet
    url = "http://www.google.com"
    timeout = 5

    try:
        request = r.get(url, timeout=timeout)
        offline_sound("Welcome sir. All the connection are online and secured")
    except(r.ConnectionError, r.Timeout) as exception:
        offline_sound("sir. you are not connected with the internet please check your internet connectivity")
        pass

    # while True:
    #     print("lol")
    #     with sr.Microphone() as source:
    #         A2.adjust_for_ambient_noise(source, duration=2)
    #         try:
    #             audio = A2.listen(source, timeout=5, phrase_time_limit=5)
    #         except (sr.WaitTimeoutError, sr.UnknownValueError):
    #             continue
    #         try:
    #             text = A.recognize_google(audio)
    #             lol = ["nobita", "sizuka"]
    #             print("hello")
    #             if "nobita" in lol:
    #                 offline_sound("welcome boss. how can i help you.")
    #                 break
    #             else:
    #                 continue
    #         except (sr.RequestError, sr.UnknownValueError):
    #             print("lol1")
    #             continue

    # Taking the audio from the user
    try:
        with sr.Microphone() as source:
            offline_sound("speak your command or searching platform")
            print(datetime.datetime.now())
            A.adjust_for_ambient_noise(source, duration=2)  # its recognise the background sound
            offline_sound("listening")
            audio = A.listen(source, timeout=5, phrase_time_limit=5)  # its taking the audio from the user and
            print(datetime.datetime.now())

    except (KeyboardInterrupt, sr.UnknownValueError, sr.WaitTimeoutError):  # it is basically cnt+c
        offline_sound("Exiting")

    try:
        text = A.recognize_google(audio)
        print(text)
    except (sr.RequestError, sr.UnknownValueError, sr.WaitTimeoutError, AssertionError):
        pass
    splited_text = text.split()

    if "shutdown" in splited_text and "abort" not in splited_text and "how" not in splited_text:
        offline_sound("your system is going to shutdown")
        ssr.shutdown(self=True)
    if "restart" in splited_text and "how" not in splited_text:
        offline_sound("your system is going to restart")
        ssr.restart(self=True)
    if "hibernate" in splited_text and "how" not in splited_text:
        offline_sound("your system is going to hibernate")
        ssr.hibernate(self=True)
    if "abort" in splited_text and "shutdown" in splited_text and "how" not in splited_text:
        offline_sound("your system is going to abort shutdown")
        ssr.abort_shutdown(self=True)

    VoiceRecognition(text)
