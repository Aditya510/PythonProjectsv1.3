compiledlist = [('The', 7258), ('said', 1943), ('an', 3542), ('of', 36080), ('no', 1781), ('that', 10237), ('any', 1301), ('place', 528), ('in', 19536), ('the', 62713), ('which', 3540), ('had', 5102), ('and', 27932), ('for', 8841), ('was', 9777), ('been', 2470), ('by', 5103), ('to', 25732), ('such', 1192), ('this', 3966), ('it', 6723), ('did', 994), ('many', 925), ('are', 4333), ('or', 4118), ('It', 2037), ('have', 3892), ('these', 1228), ('them', 1786), ('on', 6395), ('other', 1627), ('well', 757), ('both', 643), ('two', 1311), ('should', 865), ('be', 6344), ('is', 10011), ('as', 6706), ('take', 577), ('also', 999), ('so', 1755), ('may', 1292), ('at', 4963), ('This', 1179), ('one', 2873), ('but', 3007), ('has', 2425), ('through', 941), ('all', 2726), ('state', 544), ('with', 7012), ('they', 2773), ('might', 670), ('our', 1142), ('we', 1973), ('some', 1407), ('do', 1259), ('will', 2204), ('under', 648), ('its', 1780), ('found', 536), ('into', 1782), ('from', 4207), ('new', 1060), ('when', 1746), ('not', 4423), ('there', 1877), ('work', 755), ('his', 6466), ('His', 530), ('They', 847), ('man', 1151), ('more', 2130), ('than', 1788), ('year', 649), ('home', 526), ('back', 950), ('He', 2982), ('who', 2192), ('after', 823), ('he', 6566), ('would', 2677), ('up', 1874), ('In', 1801), ('out', 2058), ('When', 585), ('make', 768), ('were', 3279), ('before', 948), ('first', 1242), ('must', 1003), ('each', 759), ('time', 1556), ('three', 553), ('years', 943), ('where', 850), ('what', 1435), ('made', 1122), ('very', 772), ('being', 691), ('go', 605), ('then', 1025), ('most', 1055), ('old', 568), ('off', 634), ('against', 618), ('about', 1766), ('day', 623), ('can', 1738), ('As', 547), ('last', 636), ('like', 1237), ('see', 728), ('But', 1374), ('him', 2576), ('long', 713), ('just', 751), ('himself', 599), ('too', 801), ('good', 767), ('went', 506), ('There', 851), ('down', 888), ('little', 788), ('over', 1209), ('now', 1045), ('because', 811), ('their', 2562), ('If', 732), ('you', 2766), ('You', 520), ('only', 1646), ('between', 716), ('here', 607), ('get', 719), ('still', 731), ('if', 1466), ('people', 811), ('my', 1161), ('own', 772), ('right', 597), ('could', 1580), ('New', 575), ('We', 679), ('while', 560), ('your', 868), ('American', 569), ('much', 900), ('way', 892), ('even', 985), ('used', 610), ('another', 573), ('those', 782), ('use', 566), ('how', 623), ('For', 648), ('without', 541), ('never', 664), ('few', 583), ('came', 621), ('again', 534), ('around', 556), ('come', 589), ('world', 684), ('And', 938), ('great', 608), ('men', 736), ('know', 679), ('small', 518), ('me', 1165), ('us', 670), ('life', 676), ('She', 911), ('same', 679), ('she', 1949), ('thought', 515), ('her', 2885), ('Af', 995)]
compiledlist.remove(('The', 7258))
print(compiledlist[8][1])
compiledlist[8] = ('the', compiledlist[8][1] + 7258)

for item in compiledlist:
    if not item[0].islower():
        
        for aitem in compiledlist:
            if aitem[0] == item[0].lower():
                compiledlist[compiledlist.index(aitem)] = (aitem[0], aitem[1] + item[1])
                compiledlist.remove(item)

for item in compiledlist:
    if not item[0].islower():
        print(item)



wordlist = ['said']
emplist = [0]
countlist = [1943]
simulplot = [70000]
for i in range(1,162):
    print(70000/i+1)
    simulplot.append(70000/(i+1))

i = 1
import matplotlib.pyplot as plt
for item in compiledlist:
    bool1 = False
    for chota in countlist[::-1]:
        
        
        if item[1] > chota:
            countlist.insert(countlist.index(chota)+1,item[1])
            wordlist.insert(countlist.index(chota)+1, item[0])
            emplist.append(i)
            i += 1
            bool1 = True
            break
    if not bool1:
        if item[1] != 1943:
            print("yahoo!")
            countlist.insert(0,item[1])
            i += 1
            emplist.append(i)
print(len(emplist),len(countlist))
print(emplist,countlist)
import math
for i in range(len(emplist)):
    print(emplist[i])
    emplist[i] = math.log(emplist[i]+1)
    countlist[i] = math.log(countlist[i])

plt.plot(emplist, countlist[::-1])
plt.show()
