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
        listen()

def respond(text):
    tts = gTTS(text=text, lang='en')
    tts.save("output.mp3")

def speak():
    import webbrowser
    webbrowser.open("output.mp3")
