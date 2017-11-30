import bisect
import random
random.seed(1)
print('New Element---Location---Contents of the list')
DATA_LIST = []
for i in range(1, 15):
 var = random.randint(1, 100)
 loc = bisect.bisect(DATA_LIST, var)
 bisect.insort(DATA_LIST, var)
 print ('%3d %3d') % (var, loc), DATA_LIST
