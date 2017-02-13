def fibonacci(n):
    x = [0,1]
    for i in range(n):
        x.append(x[-1]+x[-2])
    print(x)
fibonacci(int(input()))