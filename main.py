import webbrowser as wb
import speech_recognition as sr
import datetime
import system_shutdown_restart as ssr
import pyttsx3 as py


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


A = sr.Recognizer()
A1 = sr.Recognizer()


def VoiceRecognition(x):
    if 'YouTube' in x:
        A1 = sr.Recognizer()
        url = "https://www.youtube.com/results?search_query="
        with sr.Microphone() as source:
            offline_sound("speak video name you looking for")
            audio2 = A1.listen(source)
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
            print("speak your query:")
            audio2 = A1.listen(source)
            try:
                query = A1.recognize_google(audio2)
                print(query)
                wb.get().open_new(url + query)

            except:
                print("Speak properly!!!!!")

    elif 'Python package' in x:
        A1 = sr.Recognizer()
        url = "https://pypi.org/search/?q="
        with sr.Microphone() as source:
            offline_sound("say your module name")
            audio2 = A1.listen(source)
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
            offline_sound("speak your qurries:")
            audio2 = A1.listen(source)
            try:
                query = A1.recognize_google(audio2)
                offline_sound("searching " + query)
                wb.get().open_new(url + query)

            except:
                offline_sound("Speak properly!!!!!")

    else:
        A1 = sr.Recognizer()
        url = "https://www.google.com/search?q="
        try:
            offline_sound("searching"+ x + "on google search")
            wb.get().open_new(url + x)
        except:
            offline_sound("speak Correctly......")


if __name__ == "__main__":

    try:
        with sr.Microphone() as source:
            print("speak searching platform:")
            print("speak now:")
            print(datetime.datetime.now())
            audio = A.listen(source, timeout=10)
            print(datetime.datetime.now())
            x = A.recognize_google(audio)
            print(x)
    except KeyboardInterrupt:
        print("Exiting...")

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
