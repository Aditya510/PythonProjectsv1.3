for j in range(0,9):
    for k in range(0,9):
        for l in range(0,9):
            for m in range(0,9):
                for d in range(0,9):
                    for c in range(0,9):
                        if (j**5 + k**5 + l**5 + m**5 + d**5 + c**5) == 100000*j + 10000*k + 1000*l + 100*m + 10 *d + 1*c:
                            print(j,k,l,m,d,c)
