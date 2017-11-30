with open('result.txt') as f:
    lines = f.readlines()
count = 0
for item in lines:
    if len(item.split()) > 10:
        lis = item.split()
        try:
            if int(lis[-1]) > 275:
                print(int(lis[-1]))
                count += 1
        except:
            continue
print(count)
        
        
