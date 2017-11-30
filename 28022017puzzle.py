i1 = 6210001000
def check(string):
    boole = True
    for i in range(0,10):
        if string[i] != string.count(str(i)):
            boole = False
    return boole
while i1 < 9999999999:
    i1 = str(i1)
    print(i1)
    if check(i1):
        print(i1)
        print("Yeahyeah")
        break
    i1 = int(i1)
    i1 += 1
    
