def answer(xs):
    xs = sorted(xs)
    
    boola = False
    negcount = 0
    allnegative = True
    notpositive = True
    for item in xs:
        if item > 0 :
            allnegative = False
            notpositive = False
            break
        if item > -1:
            allnegative = False
    
    if allnegative:
        for item in xs:
            negcount +=1
        if negcount % 2 == 0:
            try:
                xs = xs[:-1]
            except:
                pass
            try:
                xs = xs[:1]
            except:
                pass        
            
        else:
            xs = xs[:-1]
    elif notpositive:
        for item in xs:
            if item < 0:
                negcount += 1
        if negcount % 2 == 0:
            while True:
                try:
                    xs.remove(0)
                    boola = True
                except:
                    break
        if negcount % 2 == 1:
            xs = xs[1:]
    else:
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

    if len(xs) > 0:
        for val in xs:
            product *= val
        
        return(str(product))
    else:
        return 0

print(answer([-1]))

