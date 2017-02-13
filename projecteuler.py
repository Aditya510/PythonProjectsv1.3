#problem 1
def multipleof3or5():
    suma = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            suma += i
    return suma
def fiboneven():
    fibonaccio = [0,1]
    while fibonaccio[-1] < 4000000:
        fibonaccio.append(fibonaccio[-1]+fibonaccio[-2])
    asum = [x for x in fibonaccio if x % 2 == 0]
    return sum(asum)

def checkforprimes(num):
    lis = []
    for i in range(1,int(num**0.5),2):
        if num % i == 0:
            lis.append(i)
    print(lis)
    print(lis[-1])
    if len(lis) <= 2:
        return lis[-1]
    else:
        checkforprimes(lis[-1])

def palindromeproduct():
    lis = []
    for i in range(900,1000):
        for j in range(900,1000):

            if str(i*j) == str(i*j)[::-1]:
                lis.append(i*j)
            print(lis)


def squaresum():
    sumof100 = sum(range(101))
    squareofsum = sumof100 ** 2
    sumofsquare = 0
    for i in range(101):
        sumofsquare += i**2
    return squareofsum - sumofsquare
print(squaresum())

def primechecker(n):
    if n%2 == 0:
        return False
    for i in range(2,int((3/2)*(n**0.5))):
        if n%i == 0:
            return False

    return True
print(primechecker(5))
lista = [x for x in range(0,50) if x % 6 == 5 or x%6 == 1]
print(lista)

def primegenerator(listgiven):
    lis = []

    for i in listgiven:
        if primechecker(i):
             print(str(i) + ": This is the" + str(len(lis)+1) + "nth number")
             lis.append(i)

    return sum(lis)
print(primegenerator(lista))



#sieve of erastothenes
def sieve(anylist):
    for item in anylist:
        s
