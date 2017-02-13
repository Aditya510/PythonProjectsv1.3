n = input()
for i in range(int(n)):
    string = input()
    count= 0
    lis = [item for item in string]
    
    for i in range(len(lis)):
        if lis[i] == "<":
            lis[i] = ">"
        elif lis[i]== ">":
            lis[i] = "<"
    
    for i in range(len(lis)-1):
        if lis[i] == ">" and lis[i+1] == "<":
            count += 1
    print(count)
