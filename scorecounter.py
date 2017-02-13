def f(x):
    result = 1
    for i in range(1,x+1):
        result = result * i
    return result

def p(n,r) :
    return(factorial(n)/factorial(n-r))

def c(n,r) :
    return(permu(n,r)/factorial(r))
    
