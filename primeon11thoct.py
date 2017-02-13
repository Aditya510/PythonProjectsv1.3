def collatz(x):
    count = 0
    while x != 1:
        if x % 2 == 0:
            x = x / 2
        else:
            x = 3*x + 1
        count += 1
    return count
import time
print(collatz(13))
start= time.time()
length = 1
for i in range(1,1000000,2):
    if i % 3 != 0:
        continue
    y = collatz(i)
    if y > length:
        length = y
        print(i)
print(length)
end  = time.time()
print(end-start)
