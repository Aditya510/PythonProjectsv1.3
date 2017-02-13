import itertools
n = input()

lis = (input().split())
lis = list(map((lambda x: int(x)), lis))

results = []
for subitem in itertools.combinations(lis,3):
    if subitem[0] + subitem[1] > subitem[2] and subitem[1] + subitem[2] > subitem[0] and subitem[0] + subitem[2] > subitem[1]:
         results.append(subitem)
suma = 0
index = 0
try:
    for item in results:
        if sum(item) > suma:
            suma = sum(item)
            index = results.index(item)
    string = ""
    for item in results[index]:
        string += str(item)
        string += " "

    print(string[:-1])
except:
    print(-1)
