from random import choice
#hangmanhangman
wordcol = """acres
adult
advice
arrangement
attempt
August
Autumn
border
breeze
brick
calm
canal
Casey
cast
chose
claws
coach
constantly
contrast
cookies
customs
damage
Danny
deeply
depth
discussion
doll
donkey
Egypt
Ellen
essential
exchange

exist
explanation
facing
film
finest
fireplace
floating
folks
fort
garage
grabbed
grandmother
habit
happily
Harry
heading
hunter
Illinois
image
independent
instant
January
kids
label
Lee
lungs
manufacturing
Martin
mathematics
melted
memory
mill

mission
monkey
Mount
mysterious
neighborhood
Norway
nuts
occasionally
official
ourselves
palace
Pennsylvania
Philadelphia
plates
poetry
policeman
positive
possibly
practical
pride
promised
recall
relationship
remarkable
require
rhyme
rocky
rubbed
rush
sale
satellites
satisfied

scared
selection
shake
shaking
shallow
shout
silly
simplest
slight
slip
slope
soap
solar
species
spin
stiff
swung
tales
thumb
tobacco
toy
trap
treated
tune
University
vapor
vessels
wealth
wolf
zoo
"""
wordlist = [item for item in wordcol.split() if len(item)>5]
wordselected = choice(wordlist)
blanklist = ["_" for char in range(len(wordselected))]
print("I have chosen a word.Guess it!")
print("It contains" + str(len(wordselected)) + "letters")
print(blanklist)
print(wordselected)
print("Please guess a number")
wordl = list(wordselected)
while "_" in blanklist:
    losecount = 0
    inp = input("Enter a single alphabet")
    charcount = 0
    for char in wordl:
        if inp == char :
            print("Congratulations, you have guessed a letter correctly.")
            index = wordl.index(char)
            blanklist[index] = inp        
            print(blanklist)
            checklist = []
            checklist.append(inp)
            print(checklist)
            continue
    else:
        losecount += 1
    if losecount > 5:
        print("You lose")
    print(charcount)

