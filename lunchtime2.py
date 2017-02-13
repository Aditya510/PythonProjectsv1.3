n = int(input())
from functools import reduce

def gcd(a, b):
    """Return greatest common divisor using Euclid's Algorithm."""
    while b:      
        a, b = b, a % b
    return a

def lcm(a, b):
    """Return lowest common multiple."""
    return a * b // gcd(a, b)


n = int(input())
for i in range(n):
      t = input()
      string = input()
      li = string.split()
      lis = []
      for item in li:
          lis.append(int(item))
      result = 0
      lis.sort()
      for i in range(len(lis)):
          if lis[i] < lis[-1]:
              result += 1
      print(result)
        

##    d = reduce(lcm,lis)
##    
##    
##    result = 0
##    for i in range(len(lis)):
##        if d/lis[i] > 1:
##            lis[i] *= d/lis[i]
##            result += 1
##    print(result)
    

