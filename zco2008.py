lis = [[12,-16,10,-12],[-16,13,-14,7],[7,-4,16,-15],[-7,16,-9,8]]
index = [0,0]
while index[0]< 3 and index[1] < 3:
    if lis[index[0]+1][index[1]] >  lis[index[0]][index[1]+1]:
        index[0] += 1
    else:
        index[1] += 1
    print(index)
print(lis)
print(index)
