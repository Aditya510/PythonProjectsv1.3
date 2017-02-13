import time

def fib(n):
    if n <= 1:
        return 1
    return(fib(n-1) + fib(n-2))

def fib2(n):
    lis = [0,1]
    for i in range(n):
        lis.append(lis[-1]+lis[-2])
    return(lis[-1])




end = time.time()
print((str(fib2(4))))

end2 = time.time()

print(end2-end)
