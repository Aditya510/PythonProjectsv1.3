from gtts import gTTS
import speech_recognition as sr
r = sr.Recognizer()

def listen():
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        listen()
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition ")

def respond(text):
    tts = gTTS(text=c, lang='en')
    tts.save("output.mp3")

def speak():
    import webbrowser
    webbrowser.open("output.mp3")

c = listen()
print(c)
c = c.lower()
if ("name" in c):
    c = "My name is Jarvis."

if ("age" in c):
    c = "I am 17 years old"

if ("where" in c):
    c = "I live in greater noida"

if ("time" in c):
    import datetime
    now = datetime.datetime.now()
    c = now.strftime("%Y-%m-%d %H:%M")
    c = str(c)
import os
if ("shape" in c):

    c = "Playing as requested!"
    os.startfile("shape.webm")

from os import listdir
from os.path import isfile, join
mypath = "C:/Users/Aditya/PycharmProjects/Evoting/"
onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for item in onlyfiles:
    item = item.lower()
c = c.split()
for item in c:
    for file in onlyfiles:
        if item in file:
            if len(item)>3:
                os.startfile(mypath+file)
