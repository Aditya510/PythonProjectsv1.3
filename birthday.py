import random
count = 0
for j in range(1000):
     births = []
     for i in range(0,40):
        births.append(random.randint(1,365))
     
     if len(set(births)) != len(births):
        
        count += 1

print(count/10)


