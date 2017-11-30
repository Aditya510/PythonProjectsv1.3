def takeandverifyinput():
    global num
    num = input("Hello there!")
    try:
        int(num)
    except:
        print("Incorrect Input")
        takeandverifyinput()
        return num

def factorial():
    x = int(takeandverifyinput())
    if x == 1:
        return x
    else:
        print(x * factorial(x-1))
def tryagain():
    y = 0
    while y == 0:
        factorial()
        print("Wanna try again")
        i = input.lower
        if i == "n":
            y = 1

print(tryagain())
