import tkinter
shell = tkinter.Tk()

word = "meghna"
word = word.lower()
wordlist = list(word)
t = wordlist[2]
emptylist = []
score = 0
blanklist = list("_" * len(wordlist))
while blanklist != wordlist:
    emptylist =[]
    e = tkinter.Entry(shell)
    e.pack()
    f = e.get()
    print(f)
    t = input("Please enter a letter")
    if t in wordlist:
        index = 0
        while index < len(wordlist):
            if t == wordlist[index]:
                emptylist.append(index)
                index += 1
            else:
                index += 1     
        for item in emptylist:
            blanklist[item] = t
        print(blanklist)
    elif len(t) != 1:
        print("Not found in the hidden word. Please ensure you use a single character.")
    else:
        score = score + 1
        print("That's a wrong guess!")
        print("You are " + str((10-score)) + " unsuccessful attemps away from losing")
    if score > 10:
        print("You lose!")               
print("You rock!, you win!")
shell.mainloop()
