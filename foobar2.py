def answer(n):
    primecount = 0
    string = "2357"
    primes = []

    for val in range(8,1000000):
         boo = True
         for item in range(2,val):
             if val % item == 0:
                 boo = False
                 break
         if boo == True:
             primes.append(val)
         if len(primes) > 10000:
             break
    for item in primes:
         string += str(item)

    
    return(string[n:n+5])
answer(7)
