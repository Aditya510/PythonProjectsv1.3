import random
hangmanpics = ["die start","further dying","more","more1","more2","dead"]
word = "rhyythmh"
wordlist = list(word)
incorrectletters = 0
incorrectlist = []
correctletters = 0
correctlist = []
def printboard(incorrectletters, correctletters, wordlist):
    print(hangmanpics[incorrectletters-1])
    print("You have guessed " + str(correctletters) +" letters correctly.")
    print("And " + str(incorrectletters) + " incorrectly.")
    blanklist = ['_' for i in range(len(wordlist))]
    global correctlist
    for i in range(len(word)):
        if wordlist[i] in correctletters:
            print(wordlist[i])
    print(blanklist)


def inputforguess():
    checkcount = 0
    while checkcount == 0:
        inp = input("Enter a single letter").lower()
        if len(inp) > 1:
            print("Please enter a single value")            
        elif inp not in "abcdefghijklmnopqrstuvwxyz":
            print("Please enter a letter")
        elif inp in incorrectlist:
            print("You have already guessed that one.")
        elif inp in wordlist:
            correctlist.append(inp)
            global correctletters
            correctletters +=1
            checkcount += 1
        else:
            incorrectlist.append(inp)
            global incorrectletters
            incorrectletters+=1
            checkcount += 1
            

inputforguess()
printboard(incorrectletters,correctletters, wordlist)

    
