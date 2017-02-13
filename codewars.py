def whitespace_number(n):
    n = bin(n)
    if str(n)[0] == "-":
      sta = "[tab]" + str(n)[3:]
    else : 
      sta = "[space]" + str(n)[2:]
    sta = sta.replace("0","[space]")
    sta = sta.replace("1","[tab]")
    sta += "[LF]"
    return sta

def unbleach(ws):
    return ws.replace(' ', '[space]').replace('\t', '[tab]').replace('\n', '[LF]')

print(whitespace_number(0))
print(unbleach(     " \n"))
