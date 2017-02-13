from core import *

text = listen()
print(text)
def matchstring(text,texttomatch):
    text = text.lower()
    for item in texttomatch:

        total = len(item.split())
        count = 0

        for subitem in item.split():

            if subitem.lower() in text.split():
                count += 1
            elif len(subitem) > 6:

                for word in text.split():
                    if (subitem.lower())[:6] in word:
                        count += 1

        if count >= 0.6*(total):

            return True
matchstring("Introducing yourself", ["Introduce yourself"])
def introduce():
    tomatch = "Who are you"
    tomatch1 = "what is your name"
    tomatch2 = "who r u"
    tomatch3 = "Introduce yourself"


    intro = [tomatch,tomatch1,tomatch2, tomatch3, "introduce your self"]
    if matchstring(text, intro):
        respond("Hello, I am a Assistant")
        speak()

def location():
    tomatch = "Where do you live"
    if matchstring(text,tomatch.lower()):
        respond("I live in Greater Noida")
        speak()

def age():
    tomatch = "What is your age"
    if matchstring(text,tomatch.lower()):
        respond("I am just a newborn.")
        speak()

def relax():
    tomatch = "When will you relax"
    if matchstring(text,tomatch.lower()):
        respond("You should relax right now!")
        speak()

introduce()
location()