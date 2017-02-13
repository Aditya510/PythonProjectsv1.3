def formpoly(lis,n):
   stra = ""
   for x in range(len(lis)):
       stra += (str(lis[x]) + "x^" + str(n - x)+"+")
   print(stra)
def differ(n):
   lis = []
   for x in range(n+1):
       lis.append(input("Please enter x^" + str(n-x) +" coefficient"))
   formpoly(lis,n)
   

differ(5)
