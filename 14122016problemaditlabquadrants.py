items = input().split()
x = []
y = []
for i in range(0,len(items),2):
    x.append(items[i])
    y.append(items[i+1])

def getmax(xcor,ycor):
    r = 0
    for i in range(len(x)):
        sx = int(x[i])
        sy = int(y[i])
        if (xcor < sx and ycor > sy) or (xcor > sx and ycor < sy):
            r += 1
    return(r)

def getmay(xcor,ycor):
    r = 0
    for i in range(len(x)):
        sx = int(x[i])
        sy = int(y[i])
        if (xcor > sx and ycor < sy) or (xcor < sx and ycor > sy):
            r += 1
    return(r)
highforx  = 0
for a in range(int(sorted(x)[-1])):
    highfory = 0
    valforhighy = 0
    for b in range(int(sorted(y)[-1])):
        if getmay(a,b) > highfory:
            valforhighy = b
    if getmax(a,valforhighy) > highforx:
        highforx = a
print(highforx)

        
