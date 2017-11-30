tictac = [["__","__","__"],["__","__","__"],["__","__","__",]] #grid defined

x = tictac[0]
y = tictac[1]
z = tictac[2]

def printtictac():    #function for printing defined
    print(x)
    print(y)
    print(z)
g = 0
printtictac()
print("I have a grid ready, let's play.")
print("How to enter value - If you need to place an X in 3rd row, 3rd column, enter 33")
while g < 10:

   i = (input("Enter your value"))
   b = i.split(",")
   r = int(b[0])
   c = int(b[1])
   c = c - 1
   g = g + 1
   if r == 1:
     x[c] = "X"
   if r == 2:
     y[c] = "X"
   if r == 3:
     z[c] = "X"
   if x[0] == x[1] and x[1] == x[2]
   printtictac()
   print("Player two chance")
   i = (input("Enter your value"))
   b = i.split(",")
   r = int(b[0])
   c = int(b[1])
   c = c - 1

   if r == 1:
     x[c] = "O"
   if r == 2:
     y[c] = "O"
   if r == 3:
     z[c] = "O"
   printtictac()
   
