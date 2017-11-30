#Level 5 - Doding the Lasers
#https://math.stackexchange.com/questions/2052179/how-to-find-sum-i-1n-left-lfloor-i-sqrt2-right-rfloor-a001951-a-beatty-s

import math
#val of sqrt(2) - 1 - 
val =  4142135623730950488016887242096980785696718753769480731766797379907324784621070388503875343276415727

def n1(n):
    return (val*n)//(10**100)

def recurse(n):
    if n == 0 :
        return 0
    t = n1(n)
    return int((n*t) + n*(n+1)/2 - t*(t+1)/2 - recurse(t))

answer = lambda n: str(recurse(int(n)))


