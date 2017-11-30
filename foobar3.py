def answer(xs):
    
    xs = sorted(xs)
    
    boola = False
    negcount = 0
    for item in xs:
        if item < 0:
            negcount += 1
            i = item
            
    if negcount % 2 == 1:
        xs.remove(i)
        boola = True
        
    while True:
        try:
            xs.remove(0)
            boola = True
        except:
            break

    
    if boola == False :
        
        for pos in xs:
            if pos > 0:
                xs.remove(pos)
                break
        
    
    product = 1


    for val in xs:
        product *= val
    
    return(str(product))

print(answer([]))

