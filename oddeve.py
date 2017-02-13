from random import randint as rint
i = 1
print("Let's play oddeve")
print("We'll begin with the toss")
while i > 0:
    print("Odd or eve?")
    tosscount = 0
    while tosscount<1:
        toss = input()
        lowertoss = toss.lower()
        if lowertoss != "odd" and lowertoss != "eve":
            print("Please enter a valid input")
        else :
            tosscount += 1
    compchoose = rint(1,11)

    numcount = 0
    while numcount < 1:
        numchoose = input("Please specify a number between 1 to 10")
        print("I am thinking of :" ,compchoose)
        if numchoose.isnumeric() and int(numchoose) < 11:2
            if (int(numchoose) + compchoose) % 2 == 0 and  lowertoss == "odd":
                print("You have lost the toss")
                tossresult = 0
            if (int(numchoose) + compchoose) % 2 == 0 and  lowertoss == "even":
                print("You have won the toss")
                tossresult = 1
            if (int(numchoose) + compchoose) % 2 == 1 and  lowertoss == "odd":
                print("You have won the toss")
                tossresult = 1
            if (int(numchoose) + compchoose) % 2 == 1 and  lowertoss == "even":
                print("You have loss the toss")
                tossresult = 0
            numcount +=1
        else :
            print("Please enter a valid input")
    batresult = 0
    while batresult < 1:
        if tossresult == 0:
            batchoose = rint(0,2)
            batresult += 1
            if batchoose == 0:
                print("I choose to bat")
                batdecision = 0
            else:
                print("I choose to bowl")
                batdecision = 1
        elif tossresult == 1:
            batchoose = input("Bat or bowl?")
            lowerbatchoose = batchoose.lower()
            if lowerbatchoose != "bat" and lowerbatchoose != "bowl":
                print("Please enter a valid input")
            elif lowerbatchoose == "bat":
                batdecision = 1
                print("You choose to bat.")
                batresult += 1
            elif lowerbatchoose == "bowl":
                batdecision = 0
                print("You choose to bowl.")
                batresult += 1
    if batdecision == 0:
        print("I am batting first.")
    else:
        print("You are batting first.")
    out = 0
    score = 0
    print("The match begins")
    while out < 2:
        playerinput = input("Enter a value")
        compnumber = rint(1,11)
        if playerinput.isnumeric() and int(playerinput) < 11:
            if int(playerinput) != compnumber:
                score += int(playerinput)
                if batdecision == 0:
                    print("My score is:")
                else:
                    print("Your score is:")
                print(score)
                print("For the loss of", out,"wickets")
            else :
                print("Clean bowled")
                out += 1
                if batdecision == 0:
                    print("My current score is:")
                else:
                    print("Your current score is:")
                print(score)
                print("For the loss of", out,"wickets")
        else:
            print("Please enter a valid input")
    firstinning= score
    if batdecision == 0:
        print("My final score is:", score)
    else:
        print("Your final score is:", score)
    out = 0
    score = 0
    while out < 2:
        playerinput = input("Enter a value")
        compnumber = rint(1,11)
        if playerinput.isnumeric() and int(playerinput) < 11:
            if int(playerinput) != compnumber:
                score = score + int(playerinput)
                if batdecision == 1:
                    print("My score is:")
                else:
                    print("Your score is:")
                print(score)
                print("For the loss of", out,"wickets")
            else :
                print("Clean bowled")
                out += 1
                if batdecision == 0:
                    print("My current score is:")
                else:
                    print("Your current score is:")
                print(score)
                print("For the loss of", out,"wickets")
        else:
            print("Please enter a valid input")
        if score > firstinning:
            if batdecision == 0:
                print("Badhai! You have won the game")
            else :
                print("Loser, you lost it.")


    if batdecision == 1:
        print("My final score is:", score)
    else:
        print("Your final score is:", score)
    secondinning = score
    if batdecision == 0:
        if secondinning > firstinning:
            print("Badhai! You have won the game")
        else :
            print("Loser, you lost it.")
    else :
        if secondinning < firstinning:
            print("Badhai! You have won the game")
        else :
            print("Loser, you lost it.")
    playchoosecount = 0
    while playchoosecount<1:
        playchoose = input("Play again? enter yes or no")
        print("Let's play again!")
        lowerplay = playchoose.lower()
        if lowerplay != "yes" and lowerplay != "no":
            print("Please enter a valid input")
        else :
            playchoosecount += 1
            if lowerplay == "no":
                i -= 1
