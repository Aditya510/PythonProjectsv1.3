import random
count = 0
for i in range(100000):
    a = random.randint(1,6)
    b = random.randint(1,6)
    c = random.randint(1,6)
    if (a,b,c) == (1,1,1) :
        count += 1

print(count/100000)
print(1/216)
