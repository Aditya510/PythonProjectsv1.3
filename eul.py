def factorial(i):
    r = 1
    for i in range(1,i+1):
        r *= i
    return r
stra = 0
for char in str(factorial(100)):
    stra += int(char)
print(stra)

