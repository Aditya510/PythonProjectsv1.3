def googlejam(n):
    lis = []
    a = 1
    while len(lis) < 10:
        c = n*a
        a += 1
        for char in str(c):
            if char not in lis:
                lis.append(char)
                print(char)
        
        
    return(c)

print(googlejam(12))
        
